Things that work and things that do not
---------------------------------------

Submit is a shared tool. As such, you are responsible for setting up your work to properly use the resources available to you through submit. This section covers a few examples of avoidable problems. 

Use batch submission systems to scale up your workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The submit machines are powerful servers. However, if your jobs will take longer than approximately 15 minutes, then it is better to submit them through a batch system. Additionally, if you want to analyze many files, batch systems should be used. On submit, we provide use for both `HTCondor <https://research.cs.wisc.edu/htcondor/>`_ and `Slurm <https://slurm.schedmd.com/documentation.html>`_. Setting up these tools will allow you to scale out your tools and will also prevent clutter on the submit machines. There are simple examples on how to use these batch submission systems later in this guide.

Avoid massive parallel access of a single file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you try to access a single file from multiple processes at the same time, there will be issues on the machine hosting that file. Design your workflow to spread your requests over several files or simply make the access sequential for each file.

To increase the possible bandwidth to a single file use the mass storage (hadoop) that has some file spreading mechanisms built in.

Do not directly write to hadoop spaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users will have a significant amount of scratch space available to them through hadoop. Users should store large files here rather than in the /home or /work spaces. However, users need to be careful how to transfer files to this space as they should be transferred through gfal or xrootd rather than being transferred directly using the standard linux *cp* command and the fuxe mount point at */mnt/T3_US_MIT/hadoop/scratch*. Good use examples are shown below.

.. code-block:: sh

     # Use xrootd directly for fast IO
     xrdcp out.root root://t3serv017.mit.edu://scratch/username/out.root

     # Or through gfal
     gfal-copy file://`pwd`/out.root davs://t3serv017.mit.edu:1094//scratch/username/out.root

If you are using xrootd for the first time, you will need to be added to the mapping. Please, contact submit-help via email (submit-help@mit.edu) to be added.

Be aware of your own data
~~~~~~~~~~~~~~~~~~~~~~~~~

You are given storage spaces on submit that you are in charge of. Make sure to keep these areas clean and remove data that is no longer needed. Keep in mind that the hadoop storage is scratch for submit users.

Software environments
~~~~~~~~~~~~~~~~~~~~~

Submit provides several tools in order to help you set up and configure your software environments to suit your needs. If possible, it is better to set up your environments through these tools rather than installing things on your own. There is a section later in this guide describing some of these tools.
