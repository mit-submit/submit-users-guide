.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

Batch computing
---------------

.. tags:: Slurm, Condor, GPU

This section will give you a quick guide on how to submit batch jobs at submit. There will be a couple of simple examples to help get you started.

Running locally
~~~~~~~~~~~~~~~

The submit machines are powerful servers which can be used for local testing. This allows users to thoroughly test their code before expanding to batch submission. When you are ready to scale up your framework you can start with the examples below to start submitting to HTCondor or Slurm.

Note: The worker nodes that HTCondor uses does not have access to your home directory, This means that any input files that you need must be passed into the condor submission. Slurm is set up as a federation with all of the submit machines as clusters. This means that Slurm submissions will have access to the home directories. The submit home directories will also be exported to other clusters such as lqcd. 

Further documentation on `HTCondor <https://research.cs.wisc.edu/htcondor/>`_ and `Slurm <https://slurm.schedmd.com/documentation.html>`_ can be found in the links.

HTCondor
~~~~~~~~

HTCondor available clusters
===========================

The submit machines have access to several different clusters which can speed up the process of running large numbers of condor jobs. This section overviews which clusters are available to run on with a brief description. The following section will then describe what is needed in your condor submission file in order to send your condor jobs to each cluster. 

**MIT Tier-2 Computing Cluster**

The `MIT Tier-2 <http://www.cmsaf.mit.edu/>`_ computing cluster is hosted at Bates. 

**MIT Tier-3 Computing Cluster**

The `MIT Tier-3 <http://t3serv001.mit.edu/>`_ computing cluster is hosted at MIT in building 24.
   
**OSG**

The first external cluster to consider is the one supported by the Open Science Grid (`OSG <https://opensciencegrid.org/>`_). The OSG is a consortium of research collaborations, campuses, national laboratories and software providers dedicated to the advancement of all open science via the practice of distributed High Throughput Computing (dHTC). For `OSG support <https://support.opensciencegrid.org/support/home>`_ and `OSG requirements <https://support.opensciencegrid.org/support/solutions/articles/5000633467-steer-your-jobs-with-htcondor-job-requirements#requirements>`_ on submitting Condor jobs follow the links.

**EAPS Engaging HPC**

The next cluster is provided by the Earth, Atmospheric and Planetary Sciences (EAPS) department at MIT. For more information see their `Engaging home page <https://eapsweb.mit.edu/>`_.

   
**CMS Global Pool**

MIT has both a Tier-2 and Tier-3 computing cluster as discussed above which will support CERN users. In addition to this, CMS users have access to the global pool, allowing them to submit their jobs on clusters around the world. Links connecting you to these resources are shown in the following with a brief desctription of the `CERN Tier system <https://home.cern/science/computing/grid-system-tiers#:~:text=The%20Worldwide%20LHC%20Computing%20Grid,Large%20Hadron%20Collider%20(LHC).>`_.

The CMS global pool is hosted by various Tiers of computing clusters around the world. Jobs submitted by MIT users can be found in the link: `CMS <https://cms-gwmsmon.cern.ch/institutionalview>`_.

HTCondor examples
=================

This section will show you several ways to submit jobs through HTCondor. Here, you can see how to form your condor submission to control your jobs. A very simple example is shown below with several more complex examples afterwards.

#. `An example condor script <https://github.com/mit-submit/submit-examples/blob/main/test-all/base_sub>`_

.. code-block:: sh

      # Submit description file for test_all program
      #----------------------------------------------
      Executable            = run
      Requirements          = regexp("T2.*", MACHINE)
      Universe              = vanilla
      initialdir            = /tmp
      transfer_input_files  = input
      should_transfer_files = YES
      WhenToTransferOutput  = ON_EXIT_OR_EVICT
      Log                   = test-all.log

There are several more examples for different application types at

#. `submit-examples <https://github.com/mit-submit/submit-examples>`_

The different examples are below: `simple test <https://github.com/mit-submit/submit-examples/tree/main/test-all>`_, `testing julia <https://github.com/mit-submit/submit-examples/tree/main/julia>`_, `testing matlab <https://github.com/mit-submit/submit-examples/tree/main/matlab>`_.

If you know the gpu machines to run on you can try testing the following `condor_gpu <https://github.com/mit-submit/submit-examples/tree/main/condor_gpu>`_ by adding those machines in the requirements.

HTCondor on the different clusters
==================================

While using Condor you should be able to specify where you want your jobs to run at. Here we provide a couple of examples on modifying your requirements in order to run at different clusters. 

We have two main computing resources on MIT campus: tier2 and tier3 clusters. Users can submit condor jobs through glideinWMS or bosco.

Since condor jobs are running on external computing resources, your storage area (``/home``, ``/work``, ``/ceph``) is not accessible on the work nodes. You either need to transfer the files through condor script, or use xrootd to transfer the files. 

The xrootd transfers is enabled for ceph (``/ceph/submit/data``) storage, how to use it, see `details <https://submit.mit.edu/submit-users-guide/storage.html>`_ in "storage" section.

Glidein submission for T2/T3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:red:`The Glidein supports GPU and multi-CPU jobs.`

Submit jobs to tier2 clusters by adding following to condor script:

.. code-block:: sh

     Requirements = ( BOSCOCluster =!= "t3serv008.mit.edu" && BOSCOCluster =!= "ce03.cmsaf.mit.edu" && BOSCOCluster =!= "eofe8.mit.edu")
     +DESIRED_Sites = "mit_tier2"

If instead you want to run on the T3 machines you can replace the "DESIRED_Sites" to:

.. code-block:: sh

     +DESIRED_Sites = "mit_tier3"

If you want to submit to both tier2 and tier3, do:

.. code-block:: sh

     +DESIRED_Sites = "mit_tier2,mit_tier3"

To submit GPU jobs, you need to add:

.. code-block:: sh

     RequestGPus=1

To submit multi-core jobs, you need to add (4-core job for example, maximum 8):

.. code-block:: sh

     RequestCpus=4

Note: CMS users are recommended to submit jobs to T2 through CMS global pool, see "global pool section".

:red:`The Glidein will set a default X509_USER_KEY, which may affect the xrootd copy, therefore need to add command "unset X509_USER_KEY" before the xrootd copy .`

BOSCO submission for T2/T3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:red:`This will be deprecated eventually. It does not support GPU or multi-CPU jobs.`

.. code-block:: sh

     Requirements = (BOSCOGroup == "bosco_cms" && BOSCOCluster == "ce03.cmsaf.mit.edu")

If instead you want to run on the T3 machines you can change the requirements to the T3 BoscoCluster:

.. code-block:: sh

     Requirements = (BOSCOCluster == "t3serv008.mit.edu")

Jobs Submission to CMS global pool.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are a CMS member you can also go through the US CMS global pool:

.. code-block:: sh

     Requirements = ( BOSCOCluster =!= "t3serv008.mit.edu" && BOSCOCluster =!= "ce03.cmsaf.mit.edu" && BOSCOCluster =!= "eofe8.mit.edu")

     # you can also control what sites you want to run at. Here is a sample list to use:
     +DESIRED_Sites = "T2_AT_Vienna,T2_BE_IIHE,T2_BE_UCL,T2_BR_SPRACE,T2_BR_UERJ,T2_CH_CERN,T2_CH_CERN_AI,T2_CH_CERN_HLT,T2_CH_CERN_Wigner,T2_CH_CSCS,T2_CH_CSCS_HPC,T2_CN_Beijing,T2_DE_DESY,T2_DE_RWTH,T2_EE_Estonia,T2_ES_CIEMAT,T2_ES_IFCA,T2_FI_HIP,T2_FR_CCIN2P3,T2_FR_GRIF_IRFU,T2_FR_GRIF_LLR,T2_FR_IPHC,T2_GR_Ioannina,T2_HU_Budapest,T2_IN_TIFR,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome,T2_KR_KISTI,T2_MY_SIFIR,T2_MY_UPM_BIRUNI,T2_PK_NCP,T2_PL_Swierk,T2_PL_Warsaw,T2_PT_NCG_Lisbon,T2_RU_IHEP,T2_RU_INR,T2_RU_ITEP,T2_RU_JINR,T2_RU_PNPI,T2_RU_SINP,T2_TH_CUNSTDA,T2_TR_METU,T2_TW_NCHC,T2_UA_KIPT,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin,T3_CH_CERN_CAF,T3_CH_CERN_DOMA,T3_CH_CERN_HelixNebula,T3_CH_CERN_HelixNebula_REHA,T3_CH_CMSAtHome,T3_CH_Volunteer,T3_US_HEPCloud,T3_US_NERSC,T3_US_OSG,T3_US_PSC,T3_US_SDSC"

In order to use the CMS global pool, you will need to add a few additional lines to your condor submission. These lines below with the proper id and username (uid and id from submit) are necessary in order to get into the global pool:

.. code-block:: sh

     use_x509userproxy     = True
     x509userproxy         = /<path>/x509up_u<uid>
     +AccountingGroup = "analysis.<username>"

If you wish to submit jobs to GPU machines, you need to add additional line in the script:

.. code-block:: sh

     RequestGPus=1
     +RequiresGPU=1

There are resources available through MIT Earth, Atmospheric and Planetary Sciences (EAPS). These are accessed by adding the following requirements.

.. code-block:: sh

     Requirements =  (BOSCOCluster == "eofe8.mit.edu") 


And finally you can also use OSG:

.. code-block:: sh

      Requirements = (OSGVO_OS_STRING == "RHEL 7")
      +ProjectName            = "MIT_submit" 
 
Or depending on your workflow you may need RHEL 6 for OSG


.. code-block:: sh

      Requirements = (OSGVO_OS_STRING == "RHEL 6")      
      +ProjectName            = "MIT_submit" 


HTCondor example 1
==================

Lets look at a full example condor submission for downloading some ROOT file and transferring the output. In order to access files you will need to export your x509 proxy. The easiest way to do this on the submit machines is to first make this proxy available in your ``/home`` space and then add export lines in your condor submission. It is often easiest to add an alias command to your ``.bashrc`` like the following:

.. code-block:: sh

      alias proxy='voms-proxy-init -rfc -voms cms; cp /tmp/x509up_u'$(id -u)' ~/'


Once the x509 proxy is available, you can use xrootd freely. In this first example we will grab a ROOT file with xrootd and then transfer the file to hadoop scratch space using xrdcp. Lets run the following script in the condor job. Lets call it ``script.sh``. Make sure to update your uid and username before running the script.

.. code-block:: sh

      #!/bin/bash
      
      # if you need cvmfs or a given architecture
      source /cvmfs/cms.cern.ch/cmsset_default.sh
      export SCRAM_ARCH=slc7_amd64_gcc820
      export HOME=.
      export X509_USER_PROXY=x509up_u<uid>
      
      echo "hostname"
      hostname

      #download the file      
      xrdcp root://xrootd.cmsaf.mit.edu//store/user/paus/nanosu/A00/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8+RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1+MINIAODSIM/00A7C4D5-8881-5D47-8E1F-FADDC4B6FA96.root out.root
      
      # your Analyzer goes here

      # transfer the file
      xrdcp out.root root://submit50.mit.edu//<username>/

      echo "----- transferring output to scratch :"
      echo " ------ THE END (everyone dies !) ----- "

and the corresponding ``condor.sub`` file. Make sure to update the uid in the x509 proxy. This will run on the T3 but can be modified to run in other locations.

.. code-block:: sh

      universe              = vanilla
      request_disk          = 1024
      executable            = script.sh
      arguments             = $(ProcId)
      should_transfer_files = YES
      output                = $(ClusterId).$(ProcId).out
      error                 = $(ClusterId).$(ProcId).err
      log                   = $(ClusterId).$(ProcId).log
      use_x509userproxy     = True
      x509userproxy         = /home/submit/<username>/x509up_u<uid>
      when_to_transfer_output = ON_EXIT
      +DESIRED_Sites = "mit_tier3"
      queue 10

now you can submit your job:

.. code-block:: sh

      condor_submit condor.sub

HTCondor example 2
==================

If you have smaller output and you want to use the workspace rather than hadoop we can do something similar but instead transfer the output from the submit machines through remaps. Similar the above we will use a script.sh

.. code-block:: sh

      #!/bin/bash
      
      # if you need cvmfs or a given architecture
      source /cvmfs/cms.cern.ch/cmsset_default.sh
      export SCRAM_ARCH=slc7_amd64_gcc820
      export HOME=.
      export X509_USER_PROXY=x509up_u<uid>
      
      echo "hostname"
      hostname
      
      # download the file
      xrdcp root://xrootd.cmsaf.mit.edu//store/user/paus/nanosu/A00/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8+RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1+MINIAODSIM/00A7C4D5-8881-5D47-8E1F-FADDC4B6FA96.root out.root
      
      # your Analyzer goes here

      echo "----- transferring output to scratch :"
      echo " ------ THE END (everyone dies !) ----- "

Similar to above, we will also need a ``condor.sub``. However, this time we will transfer the file here rather than in the script. We will do this through a remap. Do not use this method to transfer any files through the fuse mount! 

.. code-block:: sh

      universe              = vanilla
      request_disk          = 1024
      executable            = script.sh
      arguments             = $(ProcId)
      should_transfer_files = YES
      output                = $(ClusterId).$(ProcId).out
      error                 = $(ClusterId).$(ProcId).err
      log                   = $(ClusterId).$(ProcId).log
      use_x509userproxy     = True
      x509userproxy         = /home/submit/<username>/x509up_u<uid>
      when_to_transfer_output = ON_EXIT
      transfer_output_remaps = "out.root = /work/submit/<username>/out.root"
      +DESIRED_Sites = "mit_tier3"
      queue 10

How to monitor and control your submitted HTCondor jobs
=======================================================

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

Useful condor set up
=====================

In the condor submission script, users are define the requirements of slots from the condor pool (conputing resources). 
The default memory requirement is 1024 MB per core.  If uses job uses more memory then 1024 MB, the job will get killed. To request more memories, users need to add this in the condor script:

.. code-block:: sh

       RequestMemory = 2000

Usually the maximum memory usage is 2000 MB for each core. But condor has a feature to adjust memory usage of a job requirement automatically even if users job requires more memory then 2000 MB, for example:

.. code-block:: sh

       RequestMemory = 4000

But keep in mind, the more memory user requires, the harder it is to find the slot. 

There is a hard limit on the size of input files that you can transfer with `transfer_input_files` at 250MB. In general, you should strive to have as few and small files as possible be transferred this way, in order to avoid overloading the condor scheduler. You can always read from `cvmfs` or with `xrootd` in case you need to get access to larger or more files.

Slurm
~~~~~

Slurm can also be used on the submit machines. There is a main slurm partition on the submit machines as well as GPUs available through ``submit-gpu`` and ``submit-gpu-a30`` partitions. Additionally slurm connects the lqcd cluster(TEMPORARILY OUT OF DATE).
The slurm partitions on SubMIT are fairly open but jobs are limited to 6 days of running time. In addition, each slurm node is limited to 80 GB of total memory to use.

Slurm example 1
===============

Below is a sample about how to submit a slurm job to the submit machines. Here we are doing similar to the condor samples above and copying a file with xrootd and then transferring the output to hadoop scratch space. Like Condor, you will need to export your x509 proxy in order to get access to certain files. Additional samples that utilize the GPUs on the submit cluster can be found in the GPU section of the guide: `submit GPU <http://submit.mit.edu/submit-users-guide/gpu.html>`_

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test
      #SBATCH --output=res_%j.txt
      #SBATCH --error=err_%j.txt
      #
      #SBATCH --time=10:00
      #SBATCH --mem-per-cpu=100
      
      export X509_USER_PROXY=~/x509up_u206148
      
      xrdcp root://xrootd.cmsaf.mit.edu//store/user/paus/nanosu/A00/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8+RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1+MINIAODSIM/00A7C4D5-8881-5D47-8E1F-FADDC4B6FA96.root out.root
      
      # Your Analyzer goes here

      xrdcp out.root root://submit50.mit.edu//freerc/SUEP/slurm.root
      
      srun hostname
      srun ls -hrlt

Slurm example lqcd
==================

An example for how to submit to the lqcd cluster from the submit machines. Here we need some extra set up and then test some simple srun commands like below (this example runs in the devel partition):

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
     srun sleep 60

How to see the available resources
====================================================

The `sinfo` command can give information about the Slurm partitions and nodes.  For detailed information about this command, view its manual page by typing `man sinfo`.

In particular, to view the resources in the subMIT Slurm cluster, the following command can be handy

.. code-block:: sh

     sinfo -Ne -O "PARTITION:.20,NodeHost:.10,StateLong:.11,NodeAIOT:.15,CPUsState:.15,Memory:.9,AllocMem:.9"

This will list each node on a separate line.  As described in `man sinfo`, the CPUS columns gives the count of the nodes CPUs in each state: "A/I/O/T" ("Allocated/Idle/Other/Total").  The MEMORY column gives the total memory for each node, while the ALLOCMEM gives the amount of memory which is currently allocated on that node.  Thus, with this command, you can see the total inventory of resources on each node, as well as what happens to be available at the moment.

Requesting memory
=================

On subMIT, Slurm treats both **CPUs** *and* **memory** as consumable resources.  This means that it is important to provide accurate requests of these resources in your slurm job submissions.  If you request more resources than you need (CPUs or memory), then you can unnecessarily block other users as well as your own jobs from running.  For example, a job which requests a single CPU and all the memory of a node will block any other job from running on that node even though the remaining CPUs will be sitting idle.  If, on the other hand, you request too little memory, you job will fail. This leads to the common question: how do I know how much memory to request?

In general it is recommended to request a bit more memory than you actually need so as to allow a "safety cushion" for variations in your jobs (so a job is not killed if your estimate was a little too low).  

One way to estimate your actual memory requirement is to run the command `seff <jobnumber>` to see memory usage information for a *completed* slurm job.  This can be either a batch job (e.g. submitted with `sbatch`) or an interactive session started with `salloc`.  

Another method is to use the `time` command.  Running `/usr/bin/time -v <command>` or `\\time -v <command>` will run `<command>` and print corresponding detailed memory and timing information.  Replace `<command>` with whatever you would type into the command prompt to run your calculation; this may be a script execution.  The "Maximum resident set size" output field will give an estimate of the memory to request (remember to add a safety cushion).  *Please note:* if `<command>` will use significant memory, then this should be done within a slurm job (either an interactive session requested with `salloc` or a batch job).

With respect to best-practices, as a general rule of thumb, if you run many or long jobs that request significantly more memory per cpu than the total memory of the node divided by the total number of CPUs on the node, it may be time to reexamine the efficinency of your memory usage or parallelization of your workflow to ensure fair/efficient usage of resources.

How to monitor and control your submitted slurm jobs
====================================================

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
