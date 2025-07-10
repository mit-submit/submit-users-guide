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

OpenMPI in containers when using HTCondor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This part walks you through running OpenMPI applications on an HTCondor-managed external cluster. 
Unfortunately, in this case, we cannot use the centralized OpenMPI installation, since that is only available on SubMIT clusters. We will here show how to run some testing scripts as an example.
We need to first create a container image that includes OpenMPI and the necessary libraries. Our ``mpi.def`` contains:

.. code-block:: none

    Bootstrap: docker
    From: centos:7

    %post
        # Redirect repos to vault.centos.org
        sed -i 's|^mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-Base.repo
        sed -i 's|^#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Base.repo
        yum clean all

        yum install -y openmpi openmpi-devel hwloc numactl

        export CFLAGS="-march=core2 -mtune=generic -mno-avx -mno-avx2 -mno-sse4"
        /usr/lib64/openmpi/bin/mpicc $CFLAGS -o /usr/local/bin/hello_c /hello_c.c
        /usr/lib64/openmpi/bin/mpicc $CFLAGS -o /usr/local/bin/ring_c  /ring_c.c

    %files
        hello_c.c /hello_c.c
        ring_c.c  /ring_c.c

    %environment
        export PATH=/usr/lib64/openmpi/bin:$PATH
        export LD_LIBRARY_PATH=/usr/lib64/openmpi/lib:$LD_LIBRARY_PATH

where you can find the `hello_c.c` and `ring_c.c` files in the "More Testing Scripts" section above and copy them to your current directory. Here we use the `centos:7` to ensure compatibility with the HTCondor-managed external cluster. 
We then build the container image via:

.. code-block:: bash

    singularity build mpi.sif mpi.def

Then we create a sample HTCondor submit file (``condor.sub``):

.. code-block:: bash

    universe              = vanilla
    request_disk          = 1024
    executable            = job.sh
    transfer_input_files  = mpi.sif, job.sh
    should_transfer_files = YES
    when_to_transfer_output = ON_EXIT
    request_cpus = 2
    output                = test.out
    error                 = test.err
    log                   = test.log
    +DESIRED_Sites        = "mit_tier3"
    queue 1

And a corresponding ``job.sh``:

.. code-block:: bash

    # Create a per-job temporary directory
    export TMPDIR=$(mktemp -d /tmp/openmpi.XXXXXX)

    # use container
    singularity exec mpi.sif /usr/lib64/openmpi/bin/mpirun -n 2 /usr/local/bin/hello_c
    singularity exec mpi.sif /usr/lib64/openmpi/bin/mpirun -n 2 /usr/local/bin/ring_c

    rm -rf "$TMPDIR"

We can then submit the job via:

.. code-block:: bash

    condor_submit condor.sub

The output in ``test.out`` should look like:

.. code-block:: none

    Hello, world, I am 0 of 2, (Open MPI v1.10.7, package: Open MPI mockbuild@x86-02.bsys.centos.org Distribution, ident: 1.10.7, repo rev: v1.10.6-48-g5e373bf, May 16, 2017, 142)
    Hello, world, I am 1 of 2, (Open MPI v1.10.7, package: Open MPI mockbuild@x86-02.bsys.centos.org Distribution, ident: 1.10.7, repo rev: v1.10.6-48-g5e373bf, May 16, 2017, 142)

    Process 0 sending 10 to 1, tag 201 (2 processes in ring)
    Process 0 sent to 1
    Process 0 decremented value: 9
    Process 0 decremented value: 8
    Process 0 decremented value: 7
    Process 0 decremented value: 6
    Process 0 decremented value: 5
    Process 0 decremented value: 4
    Process 0 decremented value: 3
    Process 0 decremented value: 2
    Process 0 decremented value: 1
    Process 0 decremented value: 0
    Process 0 exiting
    Process 1 exiting

Note that warnings are expected in general as the OpenMPI installed in the container is usually not optimized for the hardware of the external cluster. The most common one is complaining about the lack of OpenFabrics support.
You can try suppress that by adding ``--mca btl ^openib,ofi`` to the ``mpirun`` command in the ``job.sh`` file, but it is not absolutely necessary.