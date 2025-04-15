.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

Batch computing
---------------

.. tags:: Slurm, Condor, GPU

This section will give you a quick guide on how to submit batch jobs at subMIT.
There will be a couple of simple examples to help get you started.
You have three options:

1. **Running locally**: limited to the interactive usage of CPUs in the login nodes. Ideal for developing, not for running jobs.
2. **HTCondor**: large pools of CPUs and some GPUs are available in clusters at MIT and around the world. Ideal for large scale processing. Worker nodes in HTCondor do not have access to your subMIT directories: this means that any input files and software that you need must be passed into the submission, or already be on the worker node. Several tools are available to achieve this, read below.
3. **Slurm**: medium-sized pool of CPUs and some GPUs available on subMIT worker-nodes. Slurm is set up as a federation with all of the subMIT machines as clusters. This means that Slurm submissions will have access to the /home, /work, and /ceph directories.

Running locally
~~~~~~~~~~~~~~~

The subMIT login machines are powerful servers which can be used for local testing.
This allows users to thoroughly test their code before expanding to batch submission.
When you are ready to scale up your framework, you can study the guide below to start submitting to HTCondor or Slurm.

HTCondor
~~~~~~~~

The subMIT machines have access to several clusters with thousands of available cores via HTCondor.
This  following sections describe which clusters are available to run on, a brief description of what is available on each sltuer, and what is needed in your submission script in order to send your HTCondor jobs to each cluster. 

Available clusters
==================

MIT Tier-2 Computing Cluster
****************************

The `MIT Tier-2 <http://www.cmsaf.mit.edu/>`_ computing cluster is hosted at Bates. 
This is part of the Worldwide LHC Computing Grid, and processes jobs for the CMS experiment.
Depending on the traffic, several hundred to a couple of thousand cores are available to subMIT users.

MIT Tier-3 Computing Cluster
****************************

The `MIT Tier-3 <http://t3serv001.mit.edu/>`_ computing cluster is hosted at MIT in building 24.
This is part of the Worldwide LHC Computing Grid, and processes jobs for the CMS experiment.
Depending on the traffic, a couple of hundred cores are available to subMIT users.
The T3 tends to have much less traffic from CMS than the T2.

OSG
***

The first external cluster to consider is the one supported by the Open Science Grid (`OSG <https://opensciencegrid.org/>`_).
The OSG is a consortium of research collaborations, campuses, national laboratories and software providers dedicated to the advancement of all open science via the practice of distributed High Throughput Computing (dHTC).
For `OSG support <https://support.opensciencegrid.org/support/home>`_ and `OSG requirements <https://portal.osg-htc.org/documentation/htc_workloads/workload_planning/htcondor_job_submission/>`_ on submitting HTCondor jobs follow the links.
   
CMS Global Pool
***************

MIT has both a Tier-2 and Tier-3 computing cluster as discussed above which will support CERN users.
In addition to this, CMS users have access to the global pool, allowing them to submit their jobs on clusters around the world.
Links connecting you to these resources are shown in the following with a brief desctription of the `CERN Tier system <https://home.cern/science/computing/grid-system-tiers#:~:text=The%20Worldwide%20LHC%20Computing%20Grid,Large%20Hadron%20Collider%20(LHC).>`_.

The CMS global pool is hosted by various Tiers of computing clusters around the world.
Jobs submitted by MIT users can be found in the link: `CMS <https://cms-gwmsmon.cern.ch/institutionalview>`_.

Submitting to the different clusters
====================================

Here we provide the recipes to run at different clusters. 

Glidein submission to T2/T3
***************************

Submit jobs to the T2 cluster by adding following to the HTCondor submission script:

.. code-block:: sh

     +DESIRED_Sites = "mit_tier2"

If instead you want to run on the T3 machines you can replace the "+DESIRED_Sites" to:

.. code-block:: sh

     +DESIRED_Sites = "mit_tier3"

If you want to submit to both T2 and T3, do:

.. code-block:: sh

     +DESIRED_Sites = "mit_tier2,mit_tier3"

To submit GPU jobs, you need to add:

.. code-block:: sh

     RequestGPus=1

To submit multi-core jobs, you need to add (4-core job for example, maximum 8):

.. code-block:: sh

     RequestCpus=4

Note: CMS users are recommended to submit jobs to T2 through CMS global pool, see the relevant section of this guide.

:red:`The Glidein supports GPU and multi-CPU jobs.`

:red:`The Glidein will set a default X509_USER_KEY, which may affect the xrootd copy, therefore need to add command "unset X509_USER_KEY" before the xrootd copy .`

Jobs submission to CMS global pool
**********************************

If you are a CMS member you can also go through the US CMS global pool.
Here is an example sample list of sites you can use,

.. code-block:: sh

     +DESIRED_Sites = "T2_AT_Vienna,T2_BE_IIHE,T2_BE_UCL,T2_BR_SPRACE,T2_BR_UERJ,T2_CH_CERN,T2_CH_CERN_AI,T2_CH_CERN_HLT,T2_CH_CERN_Wigner,T2_CH_CSCS,T2_CH_CSCS_HPC,T2_CN_Beijing,T2_DE_DESY,T2_DE_RWTH,T2_EE_Estonia,T2_ES_CIEMAT,T2_ES_IFCA,T2_FI_HIP,T2_FR_CCIN2P3,T2_FR_GRIF_IRFU,T2_FR_GRIF_LLR,T2_FR_IPHC,T2_GR_Ioannina,T2_HU_Budapest,T2_IN_TIFR,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome,T2_KR_KISTI,T2_MY_SIFIR,T2_MY_UPM_BIRUNI,T2_PK_NCP,T2_PL_Swierk,T2_PL_Warsaw,T2_PT_NCG_Lisbon,T2_RU_IHEP,T2_RU_INR,T2_RU_ITEP,T2_RU_JINR,T2_RU_PNPI,T2_RU_SINP,T2_TH_CUNSTDA,T2_TR_METU,T2_TW_NCHC,T2_UA_KIPT,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin,T3_CH_CERN_CAF,T3_CH_CERN_DOMA,T3_CH_CERN_HelixNebula,T3_CH_CERN_HelixNebula_REHA,T3_CH_CMSAtHome,T3_CH_Volunteer,T3_US_HEPCloud,T3_US_NERSC,T3_US_OSG,T3_US_PSC,T3_US_SDSC"

In order to use the CMS global pool, you will need to add a few additional lines to your submission script.
The lines below with the proper ID and username (uid and id from subMIT) are necessary in order to get into the global pool:

.. code-block:: sh

     use_x509userproxy     = True
     x509userproxy         = /<path>/x509up_u<uid>
     +AccountingGroup      = "analysis.<username>"

If you wish to submit jobs to GPU machines, you need to add additional lines in the script:

.. code-block:: sh

     RequestGPus=1
     +RequiresGPU=1

Jobs submission to OSG pool
***************************

Finally, you can also use OSG,

.. code-block:: sh

    +ProjectName            = "MIT_submit" 
 
You can specify the required OS of the node via the requirements; for example for RHEL 6,

.. code-block:: sh

      Requirements = (OSGVO_OS_STRING == "RHEL 6")      

or to use RHEL 7,

.. code-block:: sh

      Requirements = (OSGVO_OS_STRING == "RHEL 7")

You can also use the singularity images that they distribute through CVMFS.
These are managed `here <https://github.com/opensciencegrid/cvmfs-singularity-sync>`_, and can be found under the following CVMFS path, which is mounted also on subMIT, and the MIT T2 and T3,

.. code-block:: sh

    /cvmfs/singularity.opensciencegrid.org/

You can also add your container to this list by pushing it DockerHub and making a PR to that repository, and the container will be made available everywhere that this CVMFS is mounted.

In order to land on Singularity-enabled worker nodes in the OSG pool, you have to specify,

.. code-block:: sh

      Requirements = HAS_SINGULARITY == TRUE

You can find some examples of submission scripts for OSG on `our submit-examples GitHub repo <https://github.com/mit-submit/submit-examples/tree/main/htcondor>`_. 

General Tips for HTCondor Jobs
==============================

Transferring Input Scripts and Data
***********************************

Since HTCondor jobs are running on external computing resources, your subMIT storage areas (``/home``, ``/work``, ``/ceph``) are not accessible on the worker nodes.
Thus, you either need to transfer your input and output files through your submission script, or use XRootD to transfer files via the network. 

via the submission script
*************************

To transfer input files via the submission script,

.. code-block:: sh

    transfer_input_files    = <your comma-separated list of files>

N.B.: is a hard limit on the size of input files that you can transfer with ``transfer_input_files`` at 250MB.
In general, you should strive to have as few and small files as possible be transferred this way, in order to avoid overloading the HTCondor scheduler.

via XRootD
**********

For larger input files, you can use XRootD.
The XRootD transfers is enabled for ceph (``/ceph/submit/data``) storage, meaning you can read from ceph from anywhere in the world.
For instructions on how to set this up, see `details <https://submit.mit.edu/submit-users-guide/storage.html>`_ in "storage" section.
Once that is set up, in your bash script that is executed in the worker-node, you can have a line like the following to copy a file remotely,

.. code-block:: sh

    xrdcp root://submit50.mit.edu//data/user/w/wangzqe/test.txt .

Transferring Outputs
********************

If your code produces an output you want to bring back to subMIT, you have the same two options as for the input files.
You can either let the job copy it back, or transfer the output via XRootD.
The same considerations apply here: for larger files and more control, use XRootD.

via the submission script
*************************

Adding the following to your submission script will copy the outputs of your job back to subMIT automatically.

.. code-block:: sh

    should_transfer_files   = YES
    when_to_transfer_output = ON_EXIT

You can also control where the output files are transferred to via the ``transfer_output_remaps`` parameter.
Here is a simple example that writes the ``out.out`` file produced in the HTCondor job to your ``/work`` space.

.. code-block:: sh

    transfer_output_remaps = "out.out = /work/submit/$USER/out.out"

via XRootD
**********

You can add something like the following in your script that gets executed on the worker-node to copy your output back to the subMIT ceph space,

.. code-block:: sh

    xrdcp <your output> root://submit50.mit.edu//data/user/w/wangzqe/

Distributing Software to Worker Nodes
*************************************

Again since the HTCondor nodes don't have access to the subMIT storage areas, you need to distribute your software to the worker-node.
This is further complicated that the OS on each worker-node or cluster may be different.
Your best options are either to make your software available as a singularity image on CVMFS, or transfer it by hand.

via CVMFS
*********

`CVMFS <https://submit.mit.edu/submit-users-guide/program.html#cvmfs>`_ is mounted on subMIT and all clusters connected to subMIT via HTCondor, and supports the distribution of containers.

Several pre-built containers are available already that may meet your needs. Check our the ``/cvmfs`` space on subMIT.

Please see the relevant `Available Software <https://hep-fcc.github.io/FCCAnalyses/>`_ section of the User's Guide for how to distribute your custom container.

In order to use a container in your jobs, you can specify which image you want via the ``+SingularityImage`` parameter. For example, 

.. code-block:: sh

    +SingularityImage       = "/cvmfs/singularity.opensciencegrid.org/htc/rocky:9"

Note that some clusters may have nodes without singularity installed, so you may need to specify some particular requirement.
See the section on each cluster if that is the case.

Once the job starts, it will operate entirely inside the singularity container.

via transfer
************

If you don't need a lot of software, and you can package it (perhaps by compiling it in a way that is self-contained), you can transfer it via the methods outlines in the previous section: either through the submission script or HTCondor.

Operating Systems
*****************

It may be useful for you to impose on the HTCondor job some specific OS and set of libraries that is compatible with your code, so that each job is operating in an homogeneous environment.

For some clusters, you can do this via the ``requirements`` in the submission script: see sections pertaining to each cluster for more information on this, and check their documentation.

For all clusters supported by subMIT, as well as subMIT itself, you can also use CVMFS, which has many pre-built images of OSs that can be accessed: see `this section <https://submit.mit.edu/submit-users-guide/program.html#cvmfs>`_ of the guide for more information. See the above section for how to use singularity in your jobs. For example, to use rocky9, you can add the following to your submission script,

.. code-block:: sh

    +SingularityImage       = "/cvmfs/singularity.opensciencegrid.org/htc/rocky:9"

Requesting Resources
********************

In the HTCondor submission script, users define the requirements of their jobs, which will be used by HTCondor to assign worker-nodes.

The default memory requirement is 1024 MB per core. 
If uses job uses more memory than what is requested, the job will get killed.
To request more memory, users need to add this in the HTCondor script:

.. code-block:: sh

       RequestMemory = 2000

Usually the maximum memory usage is 2000 MB for each core.
But HTCondor has a feature to adjust memory usage of a job requirement automatically even if users job requires more memory then 2000 MB, for example:

.. code-block:: sh

       RequestMemory = 4000

But keep in mind, the more memory user requires, the harder it is to find the slot. 

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

HTCondor examples
=================

There are several more examples for different application types at

- `submit-examples <https://github.com/mit-submit/submit-examples/blob/main/htcondor/>`_ for a collection HTCondor examples
- `testing julia <https://github.com/mit-submit/submit-examples/tree/main/julia>`_ for use of Julia on HTCondor
- `testing matlab <https://github.com/mit-submit/submit-examples/tree/main/matlab>`_ for use of Matlab on HTCondor
- `condor_gpu <https://github.com/mit-submit/submit-examples/tree/main/gpu/condor_gpu>`_ for use of GPUs on HTCondor

Some worked-out examples are also provided in `Tutorial 2 <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_2.html>`_.

Slurm
~~~~~

Slurm can be used on the submit machines. There is a main slurm partition on the submit machines ``submit`` and a smaller partition for machines that are only connected via 1Gbit/s links ``submit-1gbs`` for jobs that are not I/O limited. GPUs are available through the ``submit-gpu`` and ``submit-gpu-a30`` partitions. Additionally slurm connects the lqcd cluster(TEMPORARILY OUT OF DATE).
The slurm partitions on SubMIT are fairly open but jobs are limited to 6 days of running time. In addition, each slurm node is limited to 160 GB of total memory to use.

Slurm example
=============

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

.. Slurm example lqcd
.. ==================

.. An example for how to submit to the lqcd cluster from the submit machines. Here we need some extra set up and then test some simple srun commands like below (this example runs in the devel partition):

.. .. code-block:: sh

..      #!/bin/bash
..      #
..      #SBATCH --job-name=test
..      #SBATCH --output=res_%j.txt
..      #SBATCH --error=err_%j.txt
..      #
..      #SBATCH --ntasks=1
..      #SBATCH --time=10:00
..      #SBATCH --mem-per-cpu=100
..      #SBATCH --cluster=lqcd
..      #SBATCH --partition=devel
     
..      unset MODULEPATH
..      unset MODULESHOME
..      export SLURM_CONF=/opt/lqcd/etc/slurm.conf
..      . /opt/software/modules-4.4.0/init/bash
..      module add slurm
     
..      srun hostname
..      srun ls -hrlt
..      srun sleep 60

How to see the available resources
====================================================

The ``sinfo`` command can give information about the Slurm partitions and nodes.  For detailed information about this command, view its manual page by typing ``man sinfo``.

In particular, to view the resources in the subMIT Slurm cluster, the following command can be handy

.. code-block:: sh

     sinfo -Ne -O "PARTITION:.20,NodeHost:.10,StateLong:.11,NodeAIOT:.15,CPUsState:.15,Memory:.9,AllocMem:.9"

This will list each node on a separate line.  As described in ``man sinfo``, the CPUS columns gives the count of the nodes CPUs in each state: "A/I/O/T" ("Allocated/Idle/Other/Total").  The MEMORY column gives the total memory for each node, while the ALLOCMEM gives the amount of memory which is currently allocated on that node.  Thus, with this command, you can see the total inventory of resources on each node, as well as what happens to be available at the moment.

Requesting memory
=================

On subMIT, Slurm treats both **CPUs** *and* **memory** as consumable resources.  This means that it is important to provide accurate requests of these resources in your slurm job submissions.  If you request more resources than you need (CPUs or memory), then you can unnecessarily block other users as well as your own jobs from running.  For example, a job which requests a single CPU and all the memory of a node will block any other job from running on that node even though the remaining CPUs will be sitting idle.  If, on the other hand, you request too little memory, you job will fail. This leads to the common question: how do I know how much memory to request?

In general it is recommended to request a bit more memory than you actually need so as to allow a "safety cushion" for variations in your jobs (so a job is not killed if your estimate was a little too low).  

One way to estimate your actual memory requirement is to run the command ``seff <jobnumber>`` to see memory usage information for a *completed* slurm job.  This can be either a batch job (e.g. submitted with ``sbatch``) or an interactive session started with ``salloc``.  

Another method is to use the ``time`` command.  Running ``/usr/bin/time -v <command>`` or ``\\time -v <command>`` will run ``<command>`` and print corresponding detailed memory and timing information.  Replace ``<command>`` with whatever you would type into the command prompt to run your calculation; this may be a script execution.  The "Maximum resident set size" output field will give an estimate of the memory to request (remember to add a safety cushion).  *Please note:* if ``<command>`` will use significant memory, then this should be done within a slurm job (either an interactive session requested with ``salloc`` or a batch job).

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
