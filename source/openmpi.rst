OpenMPI on SubMIT
-----------------

.. tags:: OpenMPI

The Message Passing Interface (MPI) is a standardized and widely used communication protocol designed for parallel computing in distributed-memory systems. 
It enables processes running on different nodes of a cluster to exchange data efficiently, making it essential for high-performance computing (HPC) applications. 
OpenMPI is a popular open-source implementation of the MPI standard, offering high flexibility, scalability, and performance optimizations. 
Developed collaboratively by the HPC community, OpenMPI supports multiple network interfaces and integrates seamlessly with modern supercomputing environments. 
Its modular architecture allows users to tailor configurations for specific hardware, making it a preferred choice for researchers and engineers running large-scale simulations, numerical computations, and machine learning workloads.

Here we briefly introduce the OpenMPI installation on SubMIT and provide some examples of running your program with it. 

Centralized installation of OpenMPI on SubMIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We provide a centralized OpenMPI installation through the ``module`` system. One can load the OpenMPI module using:

.. code-block:: sh

    module load mpi

you can check if it is successfully loaded by running:

.. code-block:: sh

    module list
    mpirun --version

Running MPI Programs in C/C++ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a simple example of an MPI program in C (`mpi_hello.c`):

.. code-block:: c

    #include <mpi.h>
    #include <stdio.h>

    int main(int argc, char** argv) {
        MPI_Init(&argc, &argv);
        int rank, size;
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);
        printf("Hello from process %d out of %d\n", rank, size);
        MPI_Finalize();
        return 0;
    }

Compile the code using:

.. code-block:: bash

    mpicc -o mpi_hello mpi_hello.c  # For C
    mpicxx -o mpi_hello mpi_hello.cpp  # For C++

Run the program with:

.. code-block:: bash

    mpirun -np 4 ./mpi_hello

Running MPI Programs in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use OpenMPI with Python, one can install ``mpi4py`` or equivalent python packages. We recommended you to install it with ``conda`` using the following command:

.. code-block:: bash

    conda install -c conda-forge mpi4py openmpi=4.1.*=external_*

The last part of the command specifies that the system-provided OpenMPI libraries will be used. Otherwise, ``conda`` will try to install its own version of OpenMPI or other MPI distributions (which usually will work as well, but there is no guarantee that they are optimized as the system-provide one).

Please also install the ``ucx`` libary (as the necessary point-to-point messaging layer):

.. code-block:: bash

    conda install -c conda-forge ucx

Here is a simple Python MPI example (`mpi_example.py`):

.. code-block:: python

    from mpi4py import MPI

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print(f"Hello from process {rank} out of {size}")

Run the script using:

.. code-block:: bash

    mpirun -np 4 python mpi_example.py

Submitting Jobs to the Slurm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An example submission script to Slurm is:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=test
    #SBATCH --nodes=3
    #SBATCH --ntasks=12
    #SBATCH --cpus-per-task=1
    #SBATCH --time=00:20:00
    #SBATCH --mem-per-cpu=100

    module load mpi  
    mpirun -np $SLURM_NTASKS ./my_program

Here we request 3 nodes with 12 tasks in total. Each task has 1 CPU, so we are only doing multi-processing here and no multi-threading.

More Testing scripts for OpenMPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More testing scripts for OpenMPI can be found at:

https://github.com/mit-submit/submit-examples/blob/main/openmpi/

To use them, load the OpenMPI module on SubMIT and run the make file to compile the codes.
