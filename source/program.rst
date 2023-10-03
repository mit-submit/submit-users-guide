Available software
------------------

This section briefly describes several options in which to set up your environment for working on submit. This section is not exhaustive but introduces several tools which can help you set up your code. 

Native system
~~~~~~~~~~~~~

All of the submit machines come with several tools to help you get started with your work. A few examples are shown below:

1. Languages: python, c++, Java, etc.

2. Tools: XRootd, gfal, etc.

For more complicated workflows, there are several options on how to proceed. Many environments can be set up through CVFMS provided by CERN. If you need more control of the environment, either conda or dockers are commonly used and well supported. For more information see the sections below.

X2GO
~~~~

X2Go is open source remote desktop software for Linux and is available on submit01. You will need to download the x2goclient on your local machine and then start a session to connect to submit01.mit.edu. 

`x2goclient <https://wiki.x2go.org/doku.php/doc:installation:x2goclient>`_

Remember to point to the correct ssh key that you have uploaded to the submit-portal. Use XFCE in the drop down once the x2goclient has started. 

VSCode
~~~~~~

Please note: Not all of the following features are supported for all programming languages.

Visual Studio Code (VSCode) is a free, versatile and user-friendly source-code editor which supports a variety of programming languages (Python, C/C++, Java, Julia, Fortran, ...) as well as markup languages and beyond (HTML/CSS, Markdown, reStructuredText, LaTex, JSON, ...).  It contains `debugging <https://code.visualstudio.com/docs/editor/debugging>`_ and `source control <https://code.visualstudio.com/docs/sourcecontrol/overview>`_ (e.g. git/GitHub) features as well as an integrated file browser.  VSCode can be easily run in a client-server mode for `remote development <https://code.visualstudio.com/docs/remote/ssh>`_ on subMIT.  This means that, in most cases, you can open VSCode on your own laptop/desktop computer to edit, run, & debug code on the subMIT servers.  This way you work in the convenience & comfort of a GUI-based integrated development environement in your native OS on your laptop, while behind the scenes, your code is actually being run on the subMIT machines using the software & environments on subMIT.

In other words, for `most languages <https://code.visualstudio.com/docs/languages/overview>`_, you can `edit <https://code.visualstudio.com/docs/editor/codebasics>`_ (including code highlighting, easy `code navigation <https://code.visualstudio.com/docs/editor/editingevolved>`_, code completion, parameter info, quick info and other `IntelliSense <https://code.visualstudio.com/docs/editor/intellisense>`_ features) and `debug <https://code.visualstudio.com/docs/editor/debugging>`_ (breakpoints, variable inspection, stack navigation, etc.) code easily on subMIT, as well as use advanced time-saving features like `AI-assisted code development <https://code.visualstudio.com/docs/editor/artificial-intelligence>`_, `snippets <https://code.visualstudio.com/docs/editor/userdefinedsnippets>`_, and `tasks <https://code.visualstudio.com/docs/editor/tasks>`_.  VSCode also supports many `accessibility features <https://code.visualstudio.com/docs/editor/accessibility>`_.

Getting Started with VSCode on subMIT
.....................................

We plan to provide more detailed instructions and tutorials in the near future, so please check back again later for more info!

Microsoft provides some handy `videos <https://code.visualstudio.com/docs/getstarted/introvideos>`_ for getting started with VSCode.  (As well as a detailed information `vsCode <https://code.visualstudio.com/docs/remote/ssh>`_).

First `download and install <https://code.visualstudio.com/docs/setup/setup-overview>`_ VSCode on your laptop/desktop.  

Then, a convenient way to set up VSCode for remote development is to set up an ssh config file as detailed `vs_config <https://submit.mit.edu/submit-users-guide/starting.html#common-issues-with-keys>`_ in the subMIT User's Guide.  

Then install the `VSCode Remote-SSH extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`_.  

Open VSCode on your laptop/desktop and click the green "Open a Remote Window" button in the extreme lower-left of the VSCode window.  (Alternatively, open the Command Palette by hitting F1 or Shift+Command+P and type "Remote-SSH: Connect to Host...".  A "Connect to" link also appears on the VSCode Welcome Page.)

Select "submit" from the menu (VSCode automatically reads your ssh config file).

Then, after VSCode establishes the connection, simply "Open" a folder or workspace.  Opening a folder is typically more convenient than opening a single code file.  Remember: VSCode is now connected to subMIT, so you are looking at and navigating your files on the subMIT servers, not your laptop/desktop.

Handy Resources
...............

* `intro videos <https://code.visualstudio.com/docs/getstarted/introvideos>`_

* `keyboard cheat sheet <https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_keyboard-reference-sheets>`_

* `Creating a local Python environment in VSCode <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_1.html#types-of-python-environments>`_

* `Choosing and activating a Python environment in VSCode <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_4.html#conda-in-visual-studio-code>`_

CVMFS
~~~~~

The CernVM File System (CVMFS) provides a scalable, reliable and low- maintenance software distribution service. It was developed to assist High Energy Physics (HEP) collaborations to deploy software on the worldwide- distributed computing infrastructure used to run data processing applications. CernVM-FS is implemented as a POSIX read-only file system in user space (a FUSE module). Files and directories are hosted on standard web servers and mounted in the universal namespace ``/cvmfs``.

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

In addition to the typical CMVFS environments, MIT hosts its own version of CVMFS where additional software is placed. One such example is Matlab which is given through MIT. This can be accessed like below:

.. code-block:: sh
       
      /cvmfs/cvmfs.cmsaf.mit.edu/submit/work/submit/submit-software/matlab/Matlab_install/bin/matlab


Conda
~~~~~

Conda is an open source package management system and environment management system. We can use this to set up consistent environments and manage the package dependencies for various applications. Below is an example to set up a python environment for working with `coffea <https://coffeateam.github.io/coffea/>`_ and `dask <https://docs.dask.org/en/stable/>`_. 

Important Note for Using Conda on submit
........................................

Please note that downloading many conda packages takes a large amount of space which can very quickly use up the quota in your home. If you plan to use conda heavily it is suggested to download and configure it in your work directory where there is much more space. Any new conda environment that you install in your ``/home/submit`` or ``/work/submit`` will be installed on your jupyterhub only after your server is started up again. If your server is already running, you can stop it by File -> Hub Control Panel -> Stop My Server and then restart it by clicking Start Server. 

Coffea installation with Miniforge
..................................

For installing Miniconda (see also https://hackmd.io/GkiNxag0TUmHnnCiqdND1Q#Local-or-remote)

.. code-block:: sh

      wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
      # Run and follow instructions on screen
      bash Miniforge3-Linux-x86_64.sh

NOTE: always make sure that conda, python, and pip point to local Miniforge installation (``which conda`` etc.). Another thing to keep in mind is that you should avoid installing packages with ``pip`` using ``--user``. The example below shows the correct way to use pip in conjunction with conda. 

You can either use the default environment (``base``) or create a new one:

.. code-block:: sh

      # create new environment with python 3.7, e.g. environment of name "coffea"
      conda create --name coffea python=3.7
      # activate environment "coffea"
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

Docker
......

All SubMIT users have access to build dockers. You can start by finidng instructions through your packages dockerhub or by downloading the code and building the docker image.

.. code-block:: sh

     docker build -t local/docker_name .

You can then run the docker like below.

.. code-block:: sh

     docker run --rm -i -t local/docker_name

Dockerhub:
..........

Code can be pulled directly from Dockerhub:  `dockerhub <https://hub.docker.com/>`_.

If there is a container that you would like to use on Dockerhub, you can pull the container directly.

.. code-block:: sh

      docker pull <Dockerhub_container>

After this is done downloading we can then enter into the container:

.. code-block:: sh

      docker run --rm -i -t <Dockerhub_container>


Singularity and Singularity Image Format (SIF)
..............................................

Singularity can build containers in several different file formats. The default is to build a SIF (singularity image format) container. SIF files are compressed and immutable making them the best choice for reproducible, production-grade containers. If you are going to be running your singularity through one of the batch systems provided by submit, it is suggested that you create a SIF file. For Slurm, this SIF file can be accessed through any of your mounted directories, while for HTCondor, the best practice is to make this file avialble through CVMFS. This singularity image could then be accessed through both the T2 and T3 resources via MIT's hosted CVMFS.

While Singularity doesn’t support running Docker images directly, it can pull them from Docker Hub and convert them into a suitable format for running via Singularity. This opens up access to a huge number of existing container images available on Docker Hub and other registries. When you pull a Docker image, Singularity pulls the slices or layers that make up the Docker image and converts them into a single-file Singularity SIF image. An example of this was shown below.

.. code-block:: sh

      singularity build docker_name.sif docker-daemon://local/docker_name:latest

And start the singularity

.. code-block:: sh

      singularity shell docker_name.sif

If you need this available on worker nodes through HTCondor you can add them to a CVMFS space in your work directory. You will then need to email Max (maxi@mit.edu) to create this CVMFs area for you.

.. code-block:: sh

    #Start singularity from your /work area (email Max with pathway EXAMPLE:/work/submit/freerc/cvmfs/):
    singularity shell /cvmfs/cvmfs.cmsaf.mit.edu/submit/work/submit/freerc/cvmfs/docker_name.sif

Singularity container
.....................

For this example, we will use the coffea-base singularity image based on the following `docker coffea image <https://github.com/CoffeaTeam/docker-coffea-base>`_.

Entering into the singularity container. You can simply do the following command:

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

Additional Operating Systems (CMS specific)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For CMS users, there are additional options to operating systems through CMSSW. The following commands will set up CMSSW and then put you into a singularity for Scientific Linux CERN 6 (slc6), CentOS 7(cc7), AlmaLinux 8 (el8) and AlmaLinux 9 (el9). 

.. code-block:: sh

     source /cvmfs/cms.cern.ch/cmsset_default.sh

You can then do any of the following depending on your desired OS.

.. code-block:: sh

     cmssw-slc6
     cmssw-cc7
     cmssw-el8
     cmssw-el9

If you want to check the OS, you caan do the following.

.. code-block:: sh

     cat /etc/os-release

Jupyterhub
~~~~~~~~~~

In addition to the tools above, you have access to Jupyter Notebooks through a `JupyterHub <https://submit.mit.edu/jupyter>`_ set up at submit.

This is set up through the submit machines meaning that you have access to all of your data through jupyter notebooks. You will have access to basic python2 and python3 configurations. In addition, if you need a more complex environment, you can run your notebooks in any conda environment that you have set up. This allows you to create the exact environement you need for your projects. An example on how to set up a conda environment is shown above, and how it is implemented in jupyter is described below.

A few examples of simple Jupyter noteooks can be found in the submit-examples `jupyter examples <https://github.com/mit-submit/submit-examples/tree/main/jupyter>`_.

Here is how jupyter interacts with: conda, singularity, GPUs, Slurm, and ROOT.

#. Conda

    * jupyterhub is set up to automatically load all conda and python environments which are found in the following directories
              
    .. code-block:: sh
    
         '/usr/bin/',
        '/home/submit/<username>/miniforge3/',
        '/home/submit/<username>/anaconda3/',
        '/home/submit/<username>/miniconda3/', 
        '/home/submit/<username>/.conda/',
        '/work/submit/<username>/anaconda3/',
        '/work/submit/<username>/miniconda3/', 
        '/work/submit/<username>/miniforge3/',
        '/data/submit/<username>/anaconda3/', 
        '/data/submit/<username>/miniconda3/',
        '/data/submit/<username>/miniforge3/',
        ]
              
    * If you have a different version of conda, or it is located in a different place, or some other problem has come up, please contact us for help.
    * Alternatively, a manual installation can be performed:
    
    
        1. Switch to the python you want to make available
        2. ``pip install --user ipykernel``
        3. ``python -m ipykernel install --user --name <name>``; where ``<name>`` is what you want it to show up as on jupyter
        
     
    * What the manual and automatic installations do is to create a kernel folder in your ``/home/submit/<user>/.local/share/jupyter/kernels/``. These are then found by jupyterhub, and can be used as kernels for notebooks.
    * N.B.: if relying on the automatic installation, the first time you log in after having created some environment(s), the spawning will be slower than usual, since it has to install them.
     
#. Singularity

    * Because singularity environments are not located in standardized locations like anaconda tends to be, there is no automatic installation for these environments to jupyterhub.
    * However, we can create a kernel environment by hand, which we can then use in jupyter, just like any other python environment:
    
    
        1. ``mkdir /home/submit/$USER/.local/share/jupyter/kernels/<name>/``
        2. ``touch /home/submit/$USER/.local/share/jupyter/kernels/<name>/kernel.json``
        3. And finally, place the following in the json file
    
        .. code-block:: sh
        
             {
               "argv": [
                "singularity",
                "exec",
                "-e",
                "</path/to/singularity/image/>",
                "python",
                "-m",
                "ipykernel_launcher",
                "-f",
                "{connection_file}"
               ],
               "display_name": "test",
               "language": "python",
               "metadata": {
                "debugger": true
               }
              }
        
        4. You can personalize this ``singularity exec`` command, e.g. if you want to bind a directory, you can just add two lines to the ``argv``, "--bind", "<directory>". You can test out this command by something like:
              
              ``singularity exec -e /path/to/image/ -m python``
          
#. GPUs

    * GPUs are available on submit-gpu machines. The GPUs are not used or  reserved by jupyterhub by itself. Rather, just like when you log in those machines through ssh, the GPUs can be used by a notebook or the jupyterhub terminal only if they are available (you can check this with ``nvidia-smi``).
     
#. SlurmSpawner

    * This spawner relies on Slurm to run your server. You can monitor your job just like any other Slurm job, as described in this guide, with commands such as ``squeue``.

#. ROOT on python, on jupyter: pyROOT and jupyROOT

    * If you are trying to use ROOT in an ipython notebook over jupyter, you might have issues, which are related to missing paths, in particular the path to ``x86_64-conda-linux-gnu-c++``.
    * To fix this, try adding to the PATH of your kernel the ``bin`` directory of the environment. i.e. modify  ``~/.local/share/jupyter/kernel/<YOUR ENVIRONMENT>/kernel.json`` to include:
    
    .. code-block:: python
    
         "env": {
           "PATH": "/work/submit/<USER>/miniforge3/envs/<YOUR ENVIRONMENT>/bin:${PATH}" 
          }
    
    * N.B.: if you have conda installed elsewhere, your path might be different.

Wolfram Mathematica
~~~~~~~~~~~~~~~~~~~

Mathematica is easily accessible on ``submit00``. In order to use it for the first time, follow these simple steps:

#. ssh into submit00: ``ssh username@submit00.mit.edu``

#. type ``wolfram``. You should be prompted to enter an activation key, which you can get by requesting one from MIT, following the instructions `here <https://ist.mit.edu/wolfram/mathematica>`_. Once you have entered the activation key, after a few seconds you should see ``In[1]:=`` and be able to use Mathematica.

Then, anytime you want to use Mathematica, make sure to ssh into submit00 and type ``wolfram``. 

You can easily run scripts (files with extension ``.wls`` and ``.m``) by using one of the following commands:

.. code-block:: python

     wolfram -script scriptname.wls
     wolfram -run < scriptname.wls
     wolfram < scriptname.wls
     wolfram -noprompt -run "<<scriptname.wls"

When using scripts, you can use ``Print[]`` statements in your file that will directly appear in the terminal, or use ``Export[]`` to generate plots, for example.
