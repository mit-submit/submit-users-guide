GPU resources
-------------

SubMIT also has access to several GPUs. In this section we will review how to access these machines and add them to your workflow.

submit-gpu login
~~~~~~~~~~~~~~~~

Submit allows interactive login access to GPUs through slurm. From submit, you have access to the submit-gpu server pool which contains four servers, each fitted with 2 GPUs as well as the submit-gpu1080 server pool which has several machines each fitted with 4 1080 GPUs.. This allows users to interactively test their GPU applications by simply logging into these machines through slurm using the salloc command shown below:

.. code-block:: sh

      salloc --partition=submit-gpu --cpus-per-gpu=1 --gres=gpu:1

or to the submit-gpu1080 partition:

.. code-block:: sh

      salloc --partition=submit-gpu1080 --cpus-per-gpu=1 --gres=gpu:1

If you want more than one gpu for an interactive session, you can request more with the following:

.. code-block:: sh

      salloc --partition=submit-gpu1080 --cpus-per-gpu=1 --gres=gpu:4


CUDA
~~~~

Compute Unified Device Architecture (CUDA) is a parallel computing platform and application programming interface (API) that allows software to use certain types of graphics processing unit (GPU) for general purpose processing. CUDA is available on the submit-gpu machines inherently. In order to check which CUDA version is installed you can use the command below. Make sure this version fits your workflow.

.. code-block:: sh

      nvcc --version

Slurm with GPUs
~~~~~~~~~~~~~~~

The submit-gpu machines are connected to the submit slurm cluster as the "submit-gpu" partition. This means that you can also scale up GPU applications through the use of slurm in order to access all of the GPUs available. Keep in mind that these are shared resources so use these machines responsibly. A sample slurm job designed to run on the submit-gpu machines is shown below. Notice the specifications in the beginning and make sure you tailor them to your use in order to optimize your jobs.

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test
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


A cuda example with slurm can be found here:
`slurm cuda <https://github.com/mit-submit/submit-examples/gpu/slurm_gpu>`_

In addition to the submit-gpu partition, there are additional GPUs available through submit-gpu1080. An example submit file is shown below.

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test
      #SBATCH --output=res_%j-%a.txt
      #SBATCH --error=err_%j-%a.txt
      #
      #SBATCH --ntasks=1
      #SBATCH --time=06:50:00
      #SBATCH --mem-per-cpu=2GB
      #SBATCH --partition=submit-gpu1080
      #SBATCH --gres=gpu:1
      #SBATCH --cpus-per-gpu=1

More info is here:
`slurm 1080 <https://github.com/mit-submit/submit-examples/tree/main/gpu/slurm_gpu1080>`_


Condor with GPUs
~~~~~~~~~~~~~~~~

The MIT T2 and T3 both have access to GPU machines through Condor. An example of how to access these resources through Condor is shown below

If you wish to submit jobs to GPU machines in T3/T2, you need to add additonal line in the script (only through glidein submission):

.. code-block:: sh

       RequestGPus=1

If you wish to submit jobs to GPU machines in CMS global pool, you need to add additional line in the script:

.. code-block:: sh

       RequestGPus=1
       +RequiresGPU=1

Some example scripts to run GPUs with condor can be found here:
`condor gpu <https://github.com/mit-submit/submit-examples/tree/main/gpu/condor_gpu>`_
