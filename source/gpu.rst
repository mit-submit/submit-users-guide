GPU resources
-------------

.. tags:: Slurm, Condor, JupyterHub, GPU

SubMIT provides access to several GPUs. This section outlines how to utilize these GPUs in your workflow. Access to GPUs is available via the ``submit-gpu`` and ``submit-gpu-a30`` partitions through slurm, Jupyterhub, and HTCondor. Direct SSH access is not permitted to ``submit-gpu`` or ``submit-gpu-a30``. This ensures a controlled and secure environment for utilizing GPU capabilities. Keep in mind that these are shared resources so use these machines responsibly.

There are two server pools available:

#. **submit-gpu server pool:** machines submit60 through submit 74, each with 4 NVIDIA GeForce GTX 1080 GPUs.
#. **submit-gpu-a30 server pool:** machines submit20 through submit 23, each equipped with 2 NVIDIA A30 GPUs.

Slurm with GPUs
~~~~~~~~~~~~~~~

Interactive access (salloc)
...........................

Submit allows interactive login access to GPUs through the ``salloc`` command. This allows users to interactively test their GPU applications. 

Accessing the ``submit-gpu`` partition:

.. code-block:: sh

      salloc --partition=submit-gpu --cpus-per-gpu=1 --gres=gpu:1

Accessing the ``submit-gpu-a30`` partition:

.. code-block:: sh

      salloc --partition=submit-gpu-a30 --cpus-per-gpu=1 --gres=gpu:1

To request more than one GPU, adjust the ``--gres=gpu:<number>`` option.

.. code-block:: sh

      salloc --partition=submit-gpu --cpus-per-gpu=1 --gres=gpu:4

Batch jobs and script execution
...............................

The GPUs resources are also available through batch scripts.

Example with the ``submit-gpu`` partition, using GTX 1080 GPUs:

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test_gpu
      #SBATCH --output=res_%j.txt
      #SBATCH --error=err_%j.txt
      #
      #SBATCH --time=10:00
      #SBATCH --mem-per-cpu=100
      #SBATCH --partition=submit-gpu
      #SBATCH --gres=gpu:2  
      #SBATCH --cpus-per-gpu=4
      
      srun hostname
      nvidia-smi

More info is available in the `slurm 1080 <https://github.com/mit-submit/submit-examples/tree/main/gpu/slurm_gpu1080>`_ Github repository.

Example with the ``submit-gpu-a30`` partition, using NVIDIA A30 GPUs:


.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test_gpu_a30
      #SBATCH --output=res_%j-%a.txt
      #SBATCH --error=err_%j-%a.txt
      #
      #SBATCH --ntasks=1
      #SBATCH --time=06:50:00
      #SBATCH --mem-per-cpu=2GB
      #SBATCH --partition=submit-gpu-a30
      #SBATCH --gres=gpu:1
      #SBATCH --cpus-per-gpu=1

For a CUDA example with Slurm, visit `slurm cuda <https://github.com/mit-submit/submit-examples/tree/main/gpu/slurm_gpu>`_.


CUDA
~~~~

Compute Unified Device Architecture (CUDA) is a parallel computing platform and application programming interface (API) that allows software to use certain types of graphics processing unit (GPU) for general purpose processing. CUDA is available on the submit-gpu machines inherently, but you need to properly set the path. Open your ``.bashrc`` file in your /home directory and add:

.. code-block:: sh

      export CUDA_ROOT=/usr/local/cuda
      export LD_LIBRARY_PATH=/usr/local/cuda/lib:/usr/local/cuda/lib:/usr/local/cuda/lib:
      export DYLD_LIBRARY_PATH=/usr/local/cuda/lib:

Once you source your bashrc file, you should be able to use CUDA.

.. code-block:: sh

      source ~/.bashrc

In order to check which CUDA version is installed you can use the command below; note that this command will not work if you are not on a GPU (e.g. access a GPU through `salloc <https://submit.mit.edu/submit-users-guide/gpu.html#interactive-access-salloc>`_). Make sure this version fits your workflow.

.. code-block:: sh

      nvcc --version


Jupyterhub
~~~~~~~~~~

You can also get to the submit-gpu machines through Jupyterhub. On the main `JupyterHub <http://submit.mit.edu/jupyter>`_ page, select submit-gpu in the dropdown menu.


Condor with GPUs
~~~~~~~~~~~~~~~~

The MIT T2 and T3 both have access to GPU machines through Condor. An example of how to access these resources through Condor is shown below.

If you wish to submit jobs to GPU machines in T3/T2, you need to add additional line in the script (only through glidein submission):

.. code-block:: sh

       RequestGPus=1

If you wish to submit jobs to GPU machines in CMS global pool, you need to add additional line in the script:

.. code-block:: sh

       RequestGPus=1
       +RequiresGPU=1

Some example scripts to run GPUs with condor can be found here:
`condor gpu <https://github.com/mit-submit/submit-examples/tree/main/gpu/condor_gpu>`_.


pytorch example
...............

Lets create a simple python code to test pytorch and name it condor_torch.py:

.. code-block:: sh

       #!/usr/bin/python

       import torch
       print(torch.cuda.device_count())

       # Your pytorch code
       # ...

In order to execute this we will make an executable that calls a cvmfs setup and then run the python file above. Name the file exec.sh

.. code-block:: sh

       echo `hostname`
       whoami
       id
       source /cvmfs/sft-nightlies.cern.ch/lcg/views/dev4cuda/latest/x86_64-centos7-gcc8-opt/setup.sh
       python condor_torch.py
       echo ">>>>>>>>>>\n"
       echo ""
       ls -a
       echo "<<<<<<<<<<\n"
       echo ""

We can then make a condor submission file to run this. As usual, name this condor.sub:

.. code-block:: sh

       universe              = vanilla
       request_disk          = 1024
       executable            = exec.sh
       arguments             = $(ProcId)
       should_transfer_files = YES
       output                = $(ClusterId).$(ProcId).out
       error                 = $(ClusterId).$(ProcId).err
       log                   = $(ClusterId).$(ProcId).log
       when_to_transfer_output = ON_EXIT
       RequestGPus=1
       +DESIRED_Sites = "mit_tier3,mit_tier2"
       queue 1

You can then submit this test with the following similar to what was shown in the Batch tutorial:

.. code-block:: sh

       condor_submit condor.sub
