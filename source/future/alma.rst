Move to AlmaLinux
-----------------

In December 2020, Red Hat announced that development of CentOS, a free-of-cost downstream fork of the commercial Red Hat Enterprise Linux (RHEL), would be discontinued. As such, we will move to AlmaLinux, a community-supported, production-grade enterprise operating system that is binary-compatible with RHEL. This page covers the planned upgrade and testing of AlmaLinux on submit.

How we plan to upgrade submit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because it is hard to predict how an operating system upgrade will affect everyone's work, we will upgrade the system in stages and encourage users to test their workflows on AlmaLinux. For now, the submit system uses CentOS 7 with AlmaLinux machines available only through slurm using a test partition. For the future upgrades, the submit machines will get upgraded with anouncements in the submit-users email group.

Testing on Alma Linux
~~~~~~~~~~~~~~~~~~~~~

In order to start testing with AlmaLinux, we have set up a testing slurm partition which has machines with AlmaLinux. This partition is named "submit-alma9"

The easiest way to start working is to start an interactive session through slurm with salloc.

.. code-block:: sh

     salloc --partition=submit-alma9

You can also run a testing slurm job with the following submit script.

.. code-block:: sh

     #!/bin/bash
     #
     #SBATCH --job-name=test_alma9
     #SBATCH --output=res.txt
     #
     #SBATCH --time=10:00
     #SBATCH --mem-per-cpu=100
     #SBATCH --partition=submit-alma9

     <your script goes here>

Will CentOS still be available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your workflow is constrained to CentOS, submit will provide a cenbtrally available singularity of CentOS7.9. You can test this singularity below.

.. code-block:: sh

     singularity shell /cvmfs/cvmfs.cmsaf.mit.edu/submit/work/submit/submit-software/centos/centos7p9

If you need something specific besides this singularity, please email us at submit-help@mit.edu

Feedback on AlmaLinux
~~~~~~~~~~~~~~~~~~~~~

If you run into any issues while running on the AlmaLinux testing partition, please report them to the submit team at submit-help@mit.edu

Additionally, please report any differences that you see between the base CentOS system and the AlmaLinux testing partitions.

