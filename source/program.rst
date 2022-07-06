Available Software
------------------

This section briefly describes several options in which to set up your environment for working on submit. This section is not exhaustive but introduces several tools which can help you set up your code. 

Native system
~~~~~~~~~~~~~

All of the submit machines come with several tools to help you get started with your work. A few examples are shown below:

1. Languages: python, c++, Java, etc.

2. Tools: XRootd, gfal, etc.

For more complicated workflows, there are several options on how to proceed. Many environments can be set up through CVFMS provided by CERN. If you need more control of the environment, either conda or dockers are commonly used and well supported. For more information see the sections below.

CVMFS
~~~~~

The CernVM File System (CVMFS) provides a scalable, reliable and low- maintenance software distribution service. It was developed to assist High Energy Physics (HEP) collaborations to deploy software on the worldwide- distributed computing infrastructure used to run data processing applications. CernVM-FS is implemented as a POSIX read-only file system in user space (a FUSE module). Files and directories are hosted on standard web servers and mounted in the universal namespace /cvmfs.

More documentation on CVMFS can be found here: `CVMFS <https://cernvm.cern.ch/fs/>`_

A couple examples of using CVMFS are shown below:

To set up ROOT:

.. code-block:: sh

     source /cvmfs/sft.cern.ch/lcg/views/LCG_101/x86_64-centos7-gcc11-opt/setup.sh
     root

To set up GEANT4:

.. code-block:: sh

     source /cvmfs/sft.cern.ch/lcg/releases/gcc/11.1.0/x86_64-centos7/setup.sh
     export GEANT4_DIR=/cvmfs/geant4.cern.ch/geant4/10.7.p01/x86_64-centos7-gcc8-optdeb-MT
     export QT5_HOME=/cvmfs/sft.cern.ch/lcg/releases/LCG_97/qt5/5.12.4/x86_64-centos7-gcc8-opt
     export Qt5_DIR=$QT5_HOME
     export QT_QPA_PLATFORM_PLUGIN_PATH=$QT5_HOME/plugins
     export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb
     cd ${GEANT4_DIR}/bin
     source ./geant4.sh
     
     # show the geant version:
     ./geant4-config --version

To set up the CMS software (CMSSW) or other cms specific tools:

.. code-block:: sh

      source /cvmfs/cms.cern.ch/cmsset_default.sh

If you want to use ROOT or any other CMSSW specific tools you can also download CMSSW releases and work within a CMS environment. A simple example is shown below:

.. code-block:: sh

      cmsrel CMSSW_10_2_13
      cd CMSSW_10_2_13/src
      cmsenv

Once the CMS environment is set up, the CMS software version specific ROOT release is now available to you as well.

Conda
~~~~~

Conda is an open source package management system and environment management system. We can use this to set up consistent environments and manage the package dependencies for various applications. Below is an example to set up a python environment for working with `coffea <https://coffeateam.github.io/coffea/>`_ and `dask <https://docs.dask.org/en/stable/>`_. 

Important Note for Using Conda on submit
........................................

Please note that downloading many conda packages takes a large amount of space which can very quickly use up the quota in your home. If you plan to use conda heavily it is suggested to download and configure it in your work directory where there is much more space. Any new conda environment that you install in your /home/submit or /work/submit will be installed on your jupyterhub only after your server is started up again. If your server is already running, you can stop it by File -> Hub Control Panel -> Stop My Server and then restart it by clicking Start Server. 

Coffea installation with Miniforge
..................................

For installing Miniconda (see also https://hackmd.io/GkiNxag0TUmHnnCiqdND1Q#Local-or-remote)

.. code-block:: sh

      wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
      # Run and follow instructions on screen
      bash Miniforge3-Linux-x86_64.sh

NOTE: always make sure that conda, python, and pip point to local Miniforge installation (`which conda` etc.). Another thing to keep in mind is that you should avoid installing packages with pip using --user. The example below shows the correct way to use pip in conjunction with conda. 

You can either use the default environment`base` or create a new one:

.. code-block:: sh

      # create new environment with python 3.7, e.g. environment of name `coffea`
      conda create --name coffea python=3.7
      # activate environment `coffea`
      conda activate coffea

An example of how to install a mix of packages through conda and pip:


.. code-block:: sh

      pip install git+https://github.com/CoffeaTeam/coffea.git #latest published release with `pip install coffea`
      conda install -c conda-forge xrootd
      conda install -c conda-forge ca-certificates
      conda install -c conda-forge ca-policy-lcg
      conda install -c conda-forge dask-jobqueue
      conda install -c anaconda bokeh 
      conda install -c conda-forge 'fsspec>=0.3.3'
      conda install dask
      conda install pytables
      pip install --pre fastjet
      pip install vector


Containers
~~~~~~~~~~

Containers are becoming commonplace in scientific workflows. Submit offers access to containers through Singularity images provided through CVMFS. This section will give a short example on how to enter into a singularity container to run your framework. For more information on dockers see the `docker engine site <https://docs.docker.com/engine/reference/commandline/build/>`_.

For this example, we will use the coffea-base singularity image based on the following `docker coffea image <https://github.com/CoffeaTeam/docker-coffea-base>`_.

Entering into the singularity environment is easy once you have sourced CVMFS. You can simply do the following command:

.. code-block:: sh

     singularity shell -B ${PWD}:/work /cvmfs/unpacked.cern.ch/registry.hub.docker.com/coffeateam/coffea-dask:latest

Now you should be in a singularity environment. To test you try to import a non-native package like coffea in python:

.. code-block:: sh

     python3 -c "import coffea"

The command above naturally binds the PWD and work directory. If you need to specify another area to bind you can do the following:

.. code-block:: sh

     export SINGULARITY_BIND="/mnt"

Now you can run in many different environments that are available in singularity images through CVMFS.

gcc and systemwide systems
~~~~~~~~~~~~~~~~~~~~~~~~~~

SubMIT is a CentOS07 system and as such will have old versions for some compilers and tools. For example, the gcc compiler for CentOS07 is quite old. Rather than trying to install many versions throughout SubMIT it is suggested for users to try and control the versions themselves. The tools listed above can often help with this. A couple of examples of using a newer version of gcc are shown below. 

If newer versions of gcc are needed, they are available through conda `conda gcc <https://anaconda.org/conda-forge/gcc>`_. 

Alternatively, you can also use a gcc version available through CVMFS. An example is shown below:

.. code-block:: sh

     #An example of using a newer version of gcc
     /cvmfs/cms.cern.ch/el8_amd64_gcc12/external/gcc/12.1.1-bf4aef5069fdf6bb6f77f897bcc8a6ae/bin/gcc

For systemwide tools such as gcc, these options should be considered first in order to solve the issues on the user side. If these options still do not work for your needs then please email <submit-help@mit.edu>.

JupyterHub
~~~~~~~~~~

In addition to the tools above, you have access to Jupyter Notebooks through a `JupyterHub <https://submit00.mit.edu/jupyter>`_ set up at submit.

This JupyterHub is set up through the submit machines meaning that you have access to all of your data through jupyter notebooks. You will have access to basic python2 and python3 configurations. In addition, if you need a more complex environment, you can run your notebooks in any conda environment that you have set up. This allows you to create the exact environement you need for your projects. An example on how to set up a conda environment is shown above. 

A few examples of simple Jupyter noteooks can be found in the submit-examples `jupyter examples <https://github.com/mit-submit/submit-examples/tree/main/jupyter>`_.


If you have any questions about JupyterHub you can email us (submit-jupyter@mit.edu).
