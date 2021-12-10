Running and Batch jobs
----------------------

This section will give you a quick guide on how to submit batch jobs at submit. There will be a couple of simple examples to help get you started.

Running locally
~~~~~~~~~~~~~~~

The submit machines are powerful servers which can be used for local testing. This allows users to thoroughly test their code before expanding to batch submission. When you are ready to scale up your framework you can start with the examples below to start submitting to HTCondor or Slurm.

HTCondor examples
~~~~~~~~~~~~~~~~~

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

The different examples are below: `simple test <https://github.com/mit-submit/submit-examples/tree/main/test-all>`_, `testing julia <https://github.com/mit-submit/submit-examples/tree/main/julia>`_, `testing matlab <https://github.com/mit-submit/submit-examples/tree/main/matlab>`.

Submissions can also be done through DAGMan: `DAGMan simple <https://github.com/mit-submit/submit-examples/tree/main/DAGMan>`_, `DAGMan with child process <https://github.com/mit-submit/submit-examples/tree/main/DAGMan2>`_.

If you know the gpu machines to run on you can try testing the following `condor_gpu ye==test <https://github.com/mit-submit/submit-examples/tree/main/condor_gpu>`_ by adding those machines in the requirements.


Using batch systems
~~~~~~~~~~~~~~~~~~~

While using Condor you should be able to specify where you want your jobs to run at. Here we provide a couple of examples on modifying your requirements in order to run at different clusters. For more info see `our tips <http://submit04.mit.edu/tips.html>`_.

The condor examople above ran on T2 machines using a regular expression but lets run on the different clusters by modifying the requirements in different ways. Lets start with requirements to run on the T2 machines:

.. code-block:: sh

     Requirements = (BOSCOGroup == "bosco_cms" && BOSCOCluster == "ce03.cmsaf.mit.edu")

If instead you want to run on the T3 machines you can change the requirements to the T3 BoscoCluster:

.. code-block:: sh

     Requirements = (BOSCOCluster == "t3serv008.mit.edu")

If you are a CMS member you can also go through the US CMS global pool:

.. code-block:: sh

     Requirements = ( BOSCOCluster =!= "t3serv008.mit.edu" && BOSCOCluster =!= "ce03.cmsaf.mit.edu" )

     #You can also control what sites you want to run at. Here is a sample list to use:
     +DESIRED_Sites = "T2_AT_Vienna,T2_BE_IIHE,T2_BE_UCL,T2_BR_SPRACE,T2_BR_UERJ,T2_CH_CERN,T2_CH_CERN_AI,T2_CH_CERN_HLT,T2_CH_CERN_Wigner,T2_CH_CSCS,T2_CH_CSCS_HPC,T2_CN_Beijing,T2_DE_DESY,T2_DE_RWTH,T2_EE_Estonia,T2_ES_CIEMAT,T2_ES_IFCA,T2_FI_HIP,T2_FR_CCIN2P3,T2_FR_GRIF_IRFU,T2_FR_GRIF_LLR,T2_FR_IPHC,T2_GR_Ioannina,T2_HU_Budapest,T2_IN_TIFR,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome,T2_KR_KISTI,T2_MY_SIFIR,T2_MY_UPM_BIRUNI,T2_PK_NCP,T2_PL_Swierk,T2_PL_Warsaw,T2_PT_NCG_Lisbon,T2_RU_IHEP,T2_RU_INR,T2_RU_ITEP,T2_RU_JINR,T2_RU_PNPI,T2_RU_SINP,T2_TH_CUNSTDA,T2_TR_METU,T2_TW_NCHC,T2_UA_KIPT,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin,T3_CH_CERN_CAF,T3_CH_CERN_DOMA,T3_CH_CERN_HelixNebula,T3_CH_CERN_HelixNebula_REHA,T3_CH_CMSAtHome,T3_CH_Volunteer,T3_US_HEPCloud,T3_US_NERSC,T3_US_OSG,T3_US_PSC,T3_US_SDSC"



And finally you can also use OSG:

.. code-block:: sh

      #Coming soon

Condor example 1
~~~~~~~~~~~~~~~~

Lets look at a full example condor submission for downloading some ROOT file and transfering the output. In order to access files you will need to export your x509 proxy. The easiest way to do this on the submit machines is to first make this proxy available in your /home space and then add export lines in your condor submission. It is often easiest to add an alias commad to your .bashrc like the following:

.. code-block:: sh

      alias proxy='voms-proxy-init -rfc -voms cms; cp /tmp/x509up_u'$(id -u)' ~/'


Once the x509 proxy is available, you can use xrootd freely. In this first example we will grab a ROOT file with xrootd and then transfer the file to hadoop scratch space using xrdcp. Lets run the following script in the condor job. Lets call it script.sh. Make sure to update your uid and username before running the script.

.. code-block:: sh

      #!/bin/bash
      
      #if you need cvmfs or a given architecture
      source /cvmfs/cms.cern.ch/cmsset_default.sh
      export SCRAM_ARCH=slc7_amd64_gcc820
      export HOME=.
      export X509_USER_PROXY=x509up_u<uid>
      
      echo "hostname"
      hostname

      #download the file      
      xrdcp root://xrootd.cmsaf.mit.edu//store/user/paus/nanosu/A00/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8+RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1+MINIAODSIM/00A7C4D5-8881-5D47-8E1F-FADDC4B6FA96.root out.root
      
      #Your Analyzer goes here

      #transfer the file
      xrdcp out.root root://t3serv017.mit.edu//scratch/<username>/

      echo "----- transferring output to scratch :"
      echo " ------ THE END (everyone dies !) ----- "

and the corresponding condor.sub file. Make sure to update the uid in the x509 proxy. This will run on the T3 but can be modified to run in other locations.

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
      requirements          = (BOSCOCluster == "t3serv008.mit.edu")
      queue 10

now you can submit your job:

.. code-block:: sh

      condor_submit condor.sub

Condor example 2
~~~~~~~~~~~~~~~~

If you have smaller output and you want to use the workspace rather than hadoop we can do something similar but instead trasnfer the output from the submit machines through remaps. Similar the above we will use a script.sh

.. code-block:: sh

      #!/bin/bash
      
      #if you need cvmfs or a given architecture
      source /cvmfs/cms.cern.ch/cmsset_default.sh
      export SCRAM_ARCH=slc7_amd64_gcc820
      export HOME=.
      export X509_USER_PROXY=x509up_u<uid>
      
      echo "hostname"
      hostname
      
      #download the file
      xrdcp root://xrootd.cmsaf.mit.edu//store/user/paus/nanosu/A00/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8+RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1+MINIAODSIM/00A7C4D5-8881-5D47-8E1F-FADDC4B6FA96.root out.root
      
      #Your Analyzer goes here

      echo "----- transferring output to scratch :"
      echo " ------ THE END (everyone dies !) ----- "

Similar to above, we will also need a condor.sub. However, this time we will transfer the file here rather than in the script. We will do this through a remap. Do not use this method to transer any files through the fuse mount! 

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
      requirements          = (BOSCOCluster == "t3serv008.mit.edu")
      queue 10


Slurm example 1
~~~~~~~~~~~~~~~

Slurm can also be used on the submit machines. There is a slurm federation on the submit machines as well as slurm clusters connected through lqcd. Below is a sample about how to submit a slurm job to the submit machines. Here we are doing similar to the condor samples above and copying a file with xrootd and then transferring the output to hadoop scratch space. Like Condor, you will need to export your x509 proxy in order to get access to certain files.


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
      
      #Your Analyzer goes here

      xrdcp out.root root://t3serv017.mit.edu//scratch/freerc/SUEP/slurm.root
      
      srun hostname
      srun ls -hrlt

Slurm example lqcd
~~~~~~~~~~~~~~~~~~

THIS SECTION IS UNDER CONSTRUCTION AS THE LQCD CLUSTER IS NOT AVAILABLE TO SUBMIT USERS

And now an example for how to submit to the lqcd cluster from the submit machines. Here we need some extra set up and then test some simple srun commands like below:

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
