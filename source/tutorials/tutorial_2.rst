.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

Tutorial 2: Batch Job (HTCondor and Slurm)
------------------------------------------

This section briefly describes several options in which to set up your environment for working on submit. This section is not exhaustive but introduces several tools which can help you set up your code. 

HTCondor:
~~~~~~~~~

This section will show you several ways to submit jobs through HTCondor. Here, you can see how to form your condor submission to control your jobs. A very simple example is shown below with several more complex examples afterwards.

.. code-block:: sh

      universe              = vanilla
      request_disk          = 1024
      executable            = script.sh
      arguments             = $(ProcId)
      should_transfer_files = YES
      output                = $(ClusterId).$(ProcId).out
      error                 = $(ClusterId).$(ProcId).err
      log                   = $(ClusterId).$(ProcId).log
      when_to_transfer_output = ON_EXIT
      queue 1

The submit machines have access to several different clusters which can speed up the process of running large numbers of condor jobs. This section overviews which clusters are available to run on with a brief description. The following section will then describe what is needed in your condor submission file in order to send your condor jobs to each cluster. 

**MIT Tier-2 Computing Cluster**

The `MIT Tier-2 <http://www.cmsaf.mit.edu/>`_ computing cluster is hosted at Bates. 

**MIT Tier-3 Computing Cluster**

The `MIT Tier-3 <http://t3serv001.mit.edu/>`_ computing cluster is hosted at MIT in building 24.
   
**OSG**

The OSG is a consortium of research collaborations, campuses, national laboratories and software providers dedicated to the advancement of all open science via the practice of distributed High Throughput Computing (dHTC). 

**EAPS Engaging HPC**

The next cluster is provided by the Earth, Atmospheric and Planetary Sciences (EAPS) department at MIT. For more information see their `Engaging home page <https://eapsweb.mit.edu/>`_.

   
**CMS Global Pool**

The CMS global pool is hosted by various Tiers of computing clusters around the world. Jobs submitted by MIT users can be found in the link: `CMS <https://cms-gwmsmon.cern.ch/institutionalview>`_.


An example job:
...............

Lets start with a very simple script. Lets run the following script in the condor job. Lets call it script.sh. 

.. code-block:: sh

      #!/bin/bash
      
      echo "hostname"
      hostname

      echo "----- transferring output to scratch :"
      echo " ------ THE END (everyone dies !) ----- "

and the corresponding condor.sub file to run it on the T3. 

.. code-block:: sh

      universe              = vanilla
      request_disk          = 1024
      executable            = script.sh
      arguments             = $(ProcId)
      should_transfer_files = YES
      output                = $(ClusterId).$(ProcId).out
      error                 = $(ClusterId).$(ProcId).err
      log                   = $(ClusterId).$(ProcId).log
      when_to_transfer_output = ON_EXIT
      +DESIRED_Sites = "mit_tier3"

now you can submit your job:

.. code-block:: sh

      condor_submit condor.sub

If you ran the previous tutorial, you can run the code you created in addition to hostname. I
n scipt.sh you can add the line to execute the code. In the condor.sun you can add the following line adding in the script Condor will execute.

.. code-block:: sh

      transfer_input_files  = <example_script.py>


Controlling/Analyzing Jobs:
...........................

After you have submitted your jobs, it is important to be able to monitor their progress. This section gives a couple of simple examples on how to check on the status of your jobs directly from the submit machines.

The first step in monitoring jobs is to check which jobs are running. This can be done with the command below:

.. code-block:: sh

       # This will show the number of jobs in the Done, Running and Idle states
       condor_q

       # If you want more information about a job you can look into it here
       condor_q -l <jobid> 

       # If you are interested in knowing which machines your jobs are running on you can examine that as well
       condor_q -r <jobid>

Jobs can often stay in the Idle state or be moved into a Hold state. In order to analyze this you can use the analyze of condor.

.. code-block:: sh

       # Check on the status of a job if it is stuck in Idle or moved to Hold
       condor_q -analyze <jobid>

       # If more information is needed
       condor_q -better-analyze <jobid> 

If you made a mistake during submission, you can also cancel your jobs. This should be done if any mistakes were made in order to free up the queue.

.. code-block:: sh

       # You can remove a broken job
       condor_rm <jobid>

       # If you want to remove all of your jobs
       condor_rm <username>

MIT T2:
.......

If you would like to run at the T2, add the following to the condor.sub

.. code-block:: sh

     Requirements = ( BOSCOCluster =!= "t3serv008.mit.edu" && BOSCOCluster =!= "ce03.cmsaf.mit.edu" && BOSCOCluster =!= "eofe8.mit.edu")
     +DESIRED_Sites = "mit_tier2"

MIT T3:
.......

If you would like to run at the T3, add the following to the condor.sub

.. code-block:: sh

     +DESIRED_Sites = "mit_tier3"

EAPS:
.....

If you would like to run at EAPS, add the following to the condor.sub

.. code-block:: sh

     Requirements =  (BOSCOCluster == "eofe8.mit.edu") 

GPU:
....

If you require GPUs, add the following to the condor.sub

.. code-block:: sh

     RequestGPus=1
     +RequiresGPU=1

Mulit-core:
...........

.. code-block:: sh

     RequestCpus=4

OSG:
....

.. code-block:: sh

      Requirements = (OSGVO_OS_STRING == "RHEL 7")
      +ProjectName            = "MIT_submit" 

Slurm:
~~~~~~

Slurm works on the Submit machines themselves, or on LQCD machines at MIT. Unlike HTCondor, ``/home/submit``, ``/work/submit``, and ``/data/submit`` are all mounted across all machines available to you on slurm. 

Below is a sample about how to submit a slurm job to the submit machines. Save the following into a file named ``submit.sh``.

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test
      #SBATCH --output=res_%j.txt
      #SBATCH --error=err_%j.txt
      #
      #SBATCH --time=10:00
      #SBATCH --mem-per-cpu=100
      
      srun hostname
      srun ls -hrlt

The following can then be run below

.. code-block:: sh

       sbatch submit.sh

Controlling/Analyzing Jobs:
...........................

Similar to HTCondor, Slurm has command line options to monitor and control your jobs. This section gives a couple of simple examples on how to monitor your slurm jobs on submit.

The first step in monitoring jobs is to check which jobs are running. This can be done with the command below:

.. code-block:: sh

       # This will show the number of jobs and their states.
       squeue -u <username>

       # You can also ask for the jobs on the different clusters with the -M option. You can also use a specific cluster (e.g. submit, lqcd).
       squeue -M all -u <username>

In order to analyze your jobs you can use the scontrol feature of slurm.

.. code-block:: sh

       # Check on the status of a job
       scontrol show jobid -dd <jobid>

       # If more information is needed
       sstat --jobs=<jobid> 

       # A more organized way to look at this information is through the format option. In order to see all options use --helpformat. An example is below
       sstat --jobs=<jobid> --format=jobid,maxrss,ntasks

If you made a mistake during submission, you can also cancel your jobs. This should be done if any mistakes were made in order to free up the queue.

.. code-block:: sh

       # You can remove a broken job
       scancel <jobid>

       # If you want to remove all of your jobs
       scancel -u <username>

       # If need be you can also change the state of the job with scontrol to suspend, remove, hold or release
       scontrol suspend <jobid>

Slurm also has the sacct command to help you to look at information from past jobs. These commands are similar to the sstat commands but are used for jobs that have finished rather than jobs currently running.

.. code-block:: sh

       # Look at information from your hobs after they have finished running. You can use the --long to get the non-abbreviated version
       sacct --jobs=<jobid> --long

       # Look at all of your recent jobs
       sacct --user=<username>

       # You can also use the format options to get specific information in the same way that sstat was used above
       sacct --jobs=<jobid> --format=jobid,maxrss,ntasks

       # A nice summary of a job is available through the seff command
       seff <jobid>

Submit:
.......

The default is to run on submit. If you would like to specifiy, you can add the following to the submit.sh

.. code-block:: sh

     #SBATCH --partition=submit

submit-gpu:
...........

If you would like to use GPUs, you can use the GPU partition on submit by adding the following:

.. code-block:: sh

     #SBATCH --partition=submit-gpu

Soe older 1080 GPUs are available. These are kept separate from submit-gpu but if 1080s are ok for your workflow, you can use the 1080 partition. The advantage of this partition is that there are approximately 50 GPUs available. In order to use the submit-gpu1080 partition add the following to the submission script:

.. code-block:: sh

     #SBATCH --partition=submit-gpu1080

LQCD:
.....

If you have access to the LQCD clusters, you can run the following script to set up and use slurm on those machines:

.. code-block:: sh

     #!/bin/bash
     #
     #SBATCH --job-name=test
     #SBATCH --output=res_%j.txt
     #SBATCH --error=err_%j.txt
     #
     #SBATCH --ntasks=1
     #SBATCH --time=10:00
     #SBATCH --mem-per-cpu=100
     #SBATCH --cluster=lqcd
     #SBATCH --partition=devel
     
     unset MODULEPATH
     unset MODULESHOME
     export SLURM_CONF=/opt/lqcd/etc/slurm.conf
     . /opt/software/modules-4.4.0/init/bash
     module add slurm
     
     srun hostname
     srun ls -hrlt
