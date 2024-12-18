Available software
------------------

.. tags:: Julia, Mathematica, Conda, Slurm, VSCode, Containers, JupyterHub

This section briefly describes several options in which to set up your environment for working on subMIT. This section is not exhaustive but introduces several tools which can help you set up your code. 

You have several options available for either using installed software, or installing your own:

1. **Native system**: basic software is installed on SubMIT meachines by default, or easily installable via our suggested methods.
     - This includes: python, C++, Java, `MATLAB <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_1.html#matlab>`_, `Wolfram Mathematica <https://submit.mit.edu/submit-users-guide/program.html#wolfram-mathematica>`_, XRootD, gfal, gcc, hdf5.
2. **Package and Environment Managers**: 
     - **Conda** is a package and environment manager through which you can install software (not just python!).
     - **spack**
3. **Containers**:
     - **singularity** is an open source platform to create containers, which can be used to set up more complicated environments.
     - **podman** is an alternative to Docker (which can run in "rootless" mode), and gives more control, particularly for networking, than singularity.
4. **CVFMS** is provided by CERN, and has many environments.

Find below more details about each of your choices.
Feel free to reach out to us for how to best set up your software or environments on subMIT!

Native system
~~~~~~~~~~~~~

All of the subMIT machines come with several tools to help you get started with your work. Under `/usr/bin` you will find:

- python
- gcc
- XRootD
- gfal
- C++
- Java

The following software is also avaiable, but needs particular instructions, which are detailed below:

- Julia
- Mathematica
- Other versions of gcc

Julia
.....


As of right now, Julia is not available to download through dnf. As such, to install Julia, please do the following (instructions from the `Julia language website <https://julialang.org/downloads/platform/#linux_and_freebsd>`_):

.. code-block:: sh

     wget https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.4-linux-x86_64.tar.gz
     tar zxvf julia-1.10.4-linux-x86_64.tar.gz

Then open your bashrc and add:

.. code-block:: sh

     export PATH="$PATH:/path/to/<Julia directory>/bin"

Source your bashrc and then you should be able to use Julia from now on.

.. code-block:: sh

     source ~/.bashrc


Wolfram Mathematica
...................



Mathematica is easily accessible on ``submit00``. In order to use it for the first time, follow these simple steps:

#. ssh into submit00: ``ssh username@submit00.mit.edu``

#. type ``wolfram``. You should be prompted to enter an activation key, which you can get by requesting one from MIT, following the instructions on the MIT website here: `MIT_Wolfram <https://ist.mit.edu/wolfram/mathematica>`_. Once you have entered the activation key, after a few seconds you should see ``In[1]:=`` and be able to use Mathematica.

Then, anytime you want to use Mathematica, make sure to ssh into submit00 and type ``wolfram`` on the command prompt. When you are done, type ``Quit``, ``Quit[]``, ``Exit``, or ``Exit[]``.

You can easily run scripts (files with extension ``.wls`` and ``.m``) by using one of the following commands, directly into the terminal:

.. code-block:: sh

     wolfram -script scriptname.wls
     wolfram -run < scriptname.wls
     wolfram < scriptname.wls
     wolfram -noprompt -run "<<scriptname.wls"

When using scripts, you can use ``Print[]`` statements in your file that will directly appear in the terminal, or use ``Export[]`` to generate plots, for example.

Slurm for Mathematica
.....................



You can also submit batch jobs via slurm. In your batch file, make sure to include the line ``#SBATCH --nodelist=submit00``.


JupyterHub for Mathematica
..........................

If you wish to get an interface similar to a Mathematica notebook (.nb file), you can use WolframLanguageforJupyter. To install, follow these steps:

#. Download the most recent paclet available from `WolframLanguageForJupyter <https://github.com/WolframResearch/WolframLanguageForJupyter/releases>`_ in your home directory.

#. Make sure you are on submit00 and type ``wolfram`` on the command prompt, then

.. code-block:: mathematica

     (* replace x.y.z by the correct values, e.g. 0.9.3 *)
     PacletInstall["WolframLanguageForJupyter-x.y.z.paclet"] 
     Needs["WolframLanguageForJupyter`"]
     ConfigureJupyter["Add"]
     Quit

#. To test that the installation worked, check whether Wolfram has been added to your list of jupyter kernels by typing ``jupyter kernelspec list`` in the command prompt. You should see

.. code-block:: sh

     wolframlanguage13.2    /home/submit/username/.local/share/jupyter/kernels/wolframlanguage13.2

Now that the kernel is installed, you want to use jupyterhub on ``submit00``. Here's how to do this:

Go to the submit website and open jupyterhub. Choose the job profile to "Slurm for Wolfram Mathematica - submit00 - 1 CPU, 500 MB". The server should start. If you get the error message "Spawn failed: Timeout", it means the CPUs are already busy with other jobs and cannot be used at the moment. You can still use the method below.

You can make sure that you are on submit00 by opening a terminal within the webpage, which should show ``username@submit00.mit.edu``. You can now open a jupyter notebook (.ipynb file), make sure you are using the Wolfram kernel (choose the kernel in the top right of the screen), and use Wolfram syntax as you would in a Wolfram notebook. The outputs will even have the Wolfram fonts!

gcc and systemwide systems
..........................


The default gcc installed on the system is found in ``/usr/bin/gcc``, which is version 11.4.

If newer versions of gcc are needed, they are available through conda `conda gcc <https://anaconda.org/conda-forge/gcc>`_. 

Alternatively, you can also use a gcc version available through CVMFS. An example is shown below:

.. code-block:: sh

     #An example of using a newer version of gcc
 /cvmfs/cms.cern.ch/el9_amd64_gcc12/external/gcc/12.3.1-40d504be6370b5a30e3947a6e575ca28/bin/gcc

For systemwide tools such as gcc, these options should be considered first in order to solve the issues on the user side. If these options still do not work for your needs then please email <submit-help@mit.edu>.

Package and Environment Managers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conda
.....



Conda is an open source package management system and environment management system. We can use this to set up consistent environments and manage the package dependencies for various applications. Below is an example to set up a python environment as well as a different gcc compiler.

Important Notes for Using Conda on submit
.........................................

Please note that downloading many conda packages takes a large amount of space which can very quickly use up the quota in your home. If you plan to use conda heavily **it is suggested to download and configure it in your work directory** where there is much more space. 

Any new conda environment that you install in your ``/home/submit`` or ``/work/submit`` will be installed on your JupyterHub **only after your server is started up again**. If your server is already running, you can stop it by File -> Hub Control Panel -> Stop My Server and then restart it by clicking Start Server. 

Installing Conda
................

.. code-block:: sh

     wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
     # Run and follow instructions on screen
     bash Miniforge3-Linux-x86_64.sh

NOTE: always make sure that conda, python, and pip point to local Miniforge installation (``which conda`` etc.). Another thing to keep in mind is that you should avoid installing packages with ``pip`` using ``--user``. The coffea example below shows the correct way to use pip in conjunction with conda. 

See also https://hackmd.io/GkiNxag0TUmHnnCiqdND1Q#Local-or-remote

Quick commands to know
......................

.. code-block:: sh

     conda activate env_name # To activate the environment called env_name
     conda deactivate # To deactivate an environment
     conda info --envs # To list of your environments. You can also use "conda env list"
     conda install <package name> # To install packages, e.g. numpy, pandas, matplotlib
     conda list # To list the packages of an environment. Use after activating the environment or add "-n env_name"
     conda env export > environment.yml # To export your environment with its packages. Use after activating the environment
     conda remove --name env_name --all # To remove the environment env_name

Example: python environment installation
........................................

Always create a new environment, don't use the ``base`` one:

.. code-block:: sh

      # create new environment with python 3.7, e.g. environment of name "myenv"
      conda create --name myenv python=3.12
      # activate environment "myenv"
      conda activate myenv

To check that the right python version is there, run ``python --version``. This should show ``Python 3.12.XX``.

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

Example: gcc installation
.........................

You can find many compilers, and a lot of other software, conda channels. Here is an example for installing the latest gcc.

.. code-block:: sh

     # create new environment with python 3.7, e.g. environment of name "myenv"
     conda create --name myenv
     # activate environment "myenv"
     conda activate myenv
     # find your favorite version of gcc
     conda search gcc
     # ... and install it
     conda install gcc==14.2.0


Conda in Visual Studio Code
...........................



**Selecting and activating a conda environment in VSCode:** you need to inform VSCode which conda environment to use for your Python workspace. First, make sure you have the Python extension in VSCode, which you can install by searching for ''Python'' in the Extensions section of VSCode. Then, look at the bottom-left corner (macOS) or bottom-right corner (Windows) of the VSCode window to find the "Select Python Interpreter" button. Click on it and a list of available Python interpreters will appear. Choose the one that suits your needs (e.g., ``myenv``). You can also select the environment using the Command Palette (``Cmd+Shift+P`` in macOS or ``Ctrl+Shift+P`` in Windows) and searching for "Python: Select Interpreter". Note that it may take some time for VSCode to detect the available conda environments. Also, you may have to specifically install the Python extension for connections over SSH with submit.mit.edu.

Spack
.....

Docs coming soon...


Containers
~~~~~~~~~~



Containers are becoming commonplace in scientific workflows. SubMIT offers access to containers through Singularity and Podman (an alternative to Docker). This section will give a short example on how to enter into a singularity container to run your framework. For more information on dockers see the `docker engine site <https://docs.docker.com/engine/reference/commandline/build/>`_.

A comprehensive tutorial on how to set up containers and singularity images is presented `here <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_3.html>`_. Here, only general information and an overview are presented.


Podman
......



SubMIT uses Podman on all machines. For users who have been using or are familiar with Docker, you can run on Podman images created with Docker. You can also run familiar Docker commands, such as ``pull``, ``push``, ``build``, ``commit``, ``tag``, etc. with Podman.

All SubMIT users have access to build containers. You can start by finding instructions through your package's DockerHub or by downloading the code and building the image.

A tutorial for Podman is provided `here <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_3.html>`_.

Singularity and Singularity Image Format (SIF)
..............................................



Singularity can build containers in several different file formats. The default is to build a SIF (singularity image format) container. SIF files are compressed and immutable making them the best choice for reproducible, production-grade containers.

While Singularity doesn’t support running Docker images directly, it can convert them into a suitable format for running via Singularity. This opens up access to a huge number of existing container images available on DockerHub and other registries. When you pull a Docker image, Singularity pulls the slices or layers that make up the Docker image and converts them into a single-file Singularity SIF image. An example of this is shown below.

.. code-block:: sh

      singularity build docker_name.sif docker-daemon://local/docker_name:latest

And start the singularity

.. code-block:: sh

      singularity shell docker_name.sif

A tutorial for Singularity is provided `here <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_3.html>`_.


How to use your container in your jobs
......................................

There are a couple of options for this.

**If your jobs are running only on subMIT and you have a singularity image built**, your singularity image can be placed on some commonly-readable directory from any of the compute nodes (/ceph), so you can access it directly from any of your jobs.

**If your jobs are running on subMIT, MIT T3, MIT T2, OSG, or anywhere on the grid**, you can mirror your Docker container as a Singularity container to CVMFS. You can upload it to DockerHub with ``podman push`` and then add it to /cvmfs/singularity.opensciencegrid.org/.  This can be done by making a pull request to add the container to the following file which controls the sychrhonization
https://github.com/opensciencegrid/cvmfs-singularity-sync/blob/master/docker_images.txt. Your container will then appear as a singularity image in ``/cvmfs/singularity.opensciencegrid.org/``, which is mounted on all the machines of the aforementioned systems.

**If you need this available on worker nodes on the MIT T3 and T2**, you can add them to a space in your work directory. You will then need to email Max (Kerberos ID: maxi) or submit-help@mit.edu to create this CVMFs area for you.

.. code-block:: sh

    # Start singularity from your /work area (email Max with pathway EXAMPLE:/work/submit/freerc/cvmfs/):
    singularity shell /cvmfs/cvmfs.cmsaf.mit.edu/submit/work/submit/freerc/cvmfs/docker_name.sif


CVMFS
~~~~~


The CernVM File System (CVMFS) provides a scalable, reliable and low- maintenance software distribution service. It was developed to assist High Energy Physics (HEP) collaborations to deploy software on the worldwide-distributed computing infrastructure used to run data processing applications. CernVM-FS is implemented as a POSIX read-only file system in user space (a FUSE module). Files and directories are hosted on standard web servers and mounted in the universal namespace ``/cvmfs``.

More documentation on CVMFS can be found here: `CVMFS <https://cernvm.cern.ch/fs/>`_

A couple examples of using CVMFS are shown below.

ROOT
....



To set up ROOT:

.. code-block:: sh

     source /cvmfs/sft.cern.ch/lcg/views/LCG_105/x86_64-el9-gcc11-opt/setup.sh
     root

GEANT4
......



To set up GEANT4 (make sure to use one of the AlmaLinux9 machines):

.. code-block:: sh

     source /cvmfs/sft.cern.ch/lcg/releases/gcc/11.3.1/x86_64-centos9/setup.sh
     export GEANT4_DIR=/cvmfs/geant4.cern.ch/geant4/10.7.p01/x86_64-centos7-gcc8-optdeb-MT
     export QT5_HOME=/cvmfs/sft.cern.ch/lcg/releases/LCG_97/qt5/5.12.4/x86_64-centos7-gcc8-opt
     export Qt5_DIR=$QT5_HOME
     export QT_QPA_PLATFORM_PLUGIN_PATH=$QT5_HOME/plugins
     export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb
     cd ${GEANT4_DIR}/bin
     source ./geant4.sh
     
     # show the geant version:
     ./geant4-config --version

CMSSW
.....


To set up the CMS software (CMSSW) or other cms specific tools:

.. code-block:: sh

      source /cvmfs/cms.cern.ch/cmsset_default.sh

If you want to use ROOT or any other CMSSW specific tools you can also download CMSSW releases and work within a CMS environment. A simple example is shown below:

.. code-block:: sh

      cmsrel CMSSW_13_3_2
      cd CMSSW_13_3_2/src
      cmsenv

Once the CMS environment is set up, the CMS software version specific ROOT release is now available to you as well.

In addition to the typical CMVFS environments, MIT hosts its own version of CVMFS where additional software is placed. One such example is Matlab which is given through MIT. This can be accessed like below:

.. code-block:: sh
       
      /cvmfs/cvmfs.cmsaf.mit.edu/submit/work/submit/submit-software/matlab/Matlab_install/bin/matlab


Additional Operating Systems (CMS specific)
...........................................

For CMS users, there are additional options to operating systems through CMSSW. The following commands will set up CMSSW and then put you into a singularity for Scientific Linux CERN 6 (slc6), CentOS 7 (cc7), AlmaLinux 8 (el8) and AlmaLinux 9 (el9). 

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

>>>>>>> 129b44ec3365bf355c3aecd44e0dac40ef582c44
