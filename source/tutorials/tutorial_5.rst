Tutorial 5: GPU Example (submit-gpu and GPU batch options)
----------------------------------------------------------

This section briefly describes several options in which to set up your environment for working on submit. This section is not exhaustive but introduces several tools which can help you set up your code. 

GPUs at submit:
~~~~~~~~~~~~~~~

SubMIT also has access to several GPUs. In this section we will review how to access these machines and add them to your workflow.

At SubMIT, you can access GPUs either through logging into submit-gpu, through slurm using the submit-gpu or submit-gpu1080 partitions and  through HTCondor.

submit-gpu:
...........

Submit allows access to several GPUs in different ways. In addition to the submit server pool, you also have access to the submit-gpu server pool which contains four servers, each fitted with 2 GPUs. This allows users to interactively test their GPU applications by simply logging into these machines through ssh

.. code-block:: sh

      salloc --partition=submit-gpu --cpus-per-gpu=1 --gres=gpu:1

Similar to submit, these machines use the ssh keys that you have already uploaded to the submit-portal and are connected to the same mounted directories meaning that your /home and /work directories can be accessed in the same way. Additionally, these machines have the same applications available on them as the submit machines.

Jupyterhub:
...........

You can also get to the submit-gpu machines through Jupyterhub. On the main page select submit-gpu in the dropdown menu. `JupyterHub <https://submit.mit.edu/jupyter>`_.

GPUs with Slurm:
~~~~~~~~~~~~~~~~

Slurm has options to access GPU machines on slurm through the submit-gpu and submit-gpu1080 partitions.

submit-gpu:
...........

The submit-gpu machines are connected to the submit slurm cluster as the "submit-gpu" partition. A sample slurm job designed to run on the submit-gpu machines is shown below. Notice the specifications in the beginning and make sure you tailor them to your use in order to optimize your jobs.

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test_gpu
      #SBATCH --output=res_gpu_%j.txt
      #SBATCH --error=err_gpu_%j.txt
      #
      #SBATCH --time=10:00
      #SBATCH --mem-per-cpu=100
      #SBATCH --partition=submit-gpu
      #SBATCH --gres=gpu:1  
      #SBATCH --cpus-per-gpu=2
      
      srun hostname
      nvidia-smi

submit-gpu1080:
...............

In addition to the submit-gpu partition, there are additional GPUs available through submit-gpu1080. An example submit file is shown below.

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test_gpu1080
      #SBATCH --output=res_gpu1080_%j.txt
      #SBATCH --error=err_gpu1080_%j.txt
      #
      #SBATCH --ntasks=1
      #SBATCH --time=10:00
      #SBATCH --mem-per-cpu=100
      #SBATCH --partition=submit-gpu1080
      #SBATCH --gres=gpu:1
      #SBATCH --cpus-per-gpu=2

      srun hostname
      nvidia-smi

Condor pytorch example:
~~~~~~~~~~~~~~~~~~~~~~~

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

You can then submit this test with the followinf similar to what was shown in the Batch tutorial:

.. code-block:: sh

       condor_submit condor.sub
