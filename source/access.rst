Access to subMIT
----------------

.. tags:: JupyterHub, VSCode, GPU

You have several options to connect to subMIT, view and edit your files, and do your work.

1. **ssh** is the simplest way to connect to the login nodes, see `the starting guide <https://submit.mit.edu/submit-users-guide/starting.html>`_.
2. **`JupyterHub <https://submit.mit.edu/jupyter/hub/spawn>_`**  provides another easy alternative to connect to the cluster. You can log in using your Kerberos ID, and get access to an interactive graphical interface, terminal, text editor, and more.
3. **VS Code** is a powerful code editor that supports remote access through SSH, as well as many languages and extensions. 
4. **X2GO** is a remote desktop software. 
5. **XWin32** is a remote desktop software under Window system. 

You can find details and suggestions for these options below.

Jupyterhub
~~~~~~~~~~

SubMIT has a `custom installation of JupyterHub <http://submit.mit.edu/jupyter>`_.

This is set up through the subMIT machines meaning that you have access to all of your files and data. You will have access to basic python3 configurations. In addition, if you need a more complex environment, you can run your notebooks in any conda environment that you have set up. You can check the name and location of your environments using the command ``jupyter kernelspec list``. This allows you to create the exact environment you need for your projects. An example on how to set up a conda environment is shown above, and how it is implemented in jupyter is described below.

A few examples of simple Jupyter notebooks can be found in the `Github jupyter examples <https://github.com/mit-submit/submit-examples/tree/main/jupyter>`_. Several other intro notebooks can be found in the link below:
`JupyterHub_examples <https://github.com/CpResearch/PythonDataAnalysisTutorial/tree/main/jupyter>`_

You have access to a few job profiles. Make sure to use the one that fits your needs. Here are some of the available options:

* **Slurm - Submit - 1/2/4 CPU(s), 2 GB/4 GB/8 GB:** spawns a server on the submit slurm partition, requesting 1, 2, or 4 CPU(s) with 2, 4, or 8 GB of memory.

* **Slurm - Submit-GPU - 1 GPU:** spawns a server on a submit-gpu slurm partition, requesting 1 GPU.

* **Slurm - Submit-GPU-A30 - 1 GPU:** spawns a server on a submit-gpu slurm partition, requesting 1 GPU and specifically, a NVIDIA A30 GPU.

By default, Jupyterhub shows the files located in ``/home/submit/<username>``. If you store jupyter notebooks in ``/work`` and they are small, consider moving them to your ``/home`` directory. Otherwise, you should be able to access a notebook in ``/work`` by selecting "``File > Open from Path...``" in the top menu of Jupyter, then type the full path to your notebook. You can also set up a symlink in your ``/home`` to your ``/work`` space.

When you are finished using Jupyter, please select ``File -> Hub Control Panel -> Stop My Server`` from the top menu to stop your server.

.. admonition:: If your session repeatedly terminates unexpectedly ... (click here to show/hide)
   :class: dropdown

   A common reason for a session terminating unexpectedly (besides an unstable internet connection) is overrunning memory.  If this happens, please apply the following memory best practices first and then if still necessary, use a spawn option with a larger memory allocation.

   Memory best practices: *all* open notebooks/kernels contribute towards your memory budget.  If you have multiple notebooks open only to read (not to run), please set their kernel to "``No Kernel``".  Please close unused notebooks by selecting ``File --> Close and Shutdown Notebook`` from the top menu.  (When you close a tab, the kernel generally remains open, but closing it this way shuts down the kernel as well, freeing memory).

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
              
    * If you have a different version of conda, or it is located in a different place, or some other problem has come up, please contact us for help.
    * Alternatively, a manual installation can be performed:
    
    
        1. Switch to the python you want to make available
        2. ``pip install --user ipykernel``
        3. ``python -m ipykernel install --user --name <name>``; where ``<name>`` is what you want it to show up as on jupyter
        
     
    * What the manual and automatic installations do is to create a kernel folder in your ``/home/submit/<user>/.local/share/jupyter/kernels/``. These are then found by jupyterhub, and can be used as kernels for notebooks.
    * You can list all currently installed kernels with ``jupyter kernelspec list``. Individual kernels can be removed with ``jupyter kernelspec remove <name>``.
    * N.B.: if relying on the automatic installation, the first time you log in after having created some environment(s), the spawning will be slower than usual, since it has to install them.
     
#. Singularity

    Because singularity environments are not located in standardized locations like anaconda tends to be, there is no automatic installation for these environments to jupyterhub. However, we can create a kernel environment by hand, which we can then use in jupyter, just like any other python environment:
    
    
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

    GPUs are available on submit-gpu machines. The GPUs are not used or reserved by jupyterhub by itself. Rather, just like when you log in those machines through ssh, the GPUs can be used by a notebook or the jupyterhub terminal only if they are available (you can check this with ``nvidia-smi``).
     
#. SlurmSpawner

    This spawner relies on Slurm to run your server. You can monitor your job just like any other Slurm job, as described in this guide, with commands such as ``squeue``.

#. ROOT on python, on jupyter: pyROOT and jupyROOT

    If you are trying to use ROOT in an ipython notebook over jupyter, you might have issues, which are related to missing paths, in particular the path to ``x86_64-conda-linux-gnu-c++``. To fix this, try adding to the PATH of your kernel the ``bin`` directory of the environment. i.e. modify  ``~/.local/share/jupyter/kernel/<YOUR ENVIRONMENT>/kernel.json`` to include:
    
    .. code-block:: sh
    
         "env": {
           "PATH": "/work/submit/<USER>/miniforge3/envs/<YOUR ENVIRONMENT>/bin:${PATH}" 
          }
    
    * N.B.: if you have conda installed elsewhere, your path might be different.

#. IJulia

    IJulia is a Julia-language backend combined with the Jupyter interactive environment. Once installed, you can open Jupyterhub and select the Julia 1.6.5 kernel. To install it, in a terminal window, type ``julia``, then

    .. code-block:: julia

        ] # this enters pkg mode
        add IJulia # it will take a few minutes to install the required packages

    Now, if you type ``jupyter kernelspec list`` in a terminal window, you will see

    .. code-block:: sh

        julia-1.6     /home/submit/username/.local/share/jupyter/kernels/julia-1.6

    if it doesn't work, in Julia type ``using Pkg``, then ``Pkg.build("IJulia")``. You should now have the Julia kernel for Jupyterhub.


VSCode
~~~~~~

Please note: Not all of the following features are supported for all programming languages.

Visual Studio Code (VSCode) is a free, versatile source-code editor that supports a wide range of programming languages, including Python, C/C++, Java, Julia, Fortran, and others. It also supports various markup languages like HTML/CSS, Markdown, reStructuredText, LaTeX, and JSON. Key features of VSCode include:

* **Debugging:** `simplify your troubleshooting process <https://code.visualstudio.com/docs/editor/debugging>`_.

* **Source control:** `manage your code with git/GitHub <https://code.visualstudio.com/docs/sourcecontrol/overview>`_.

* **Integrated file browser:** easily navigate and manage your files within the editor.

One of the capabilities of VSCode is its client-server mode for `remote development <https://code.visualstudio.com/docs/remote/ssh>`_ on subMIT. This functionality allows you to edit, run, and debug code on the subMIT servers directly from your personal computer. This setup provides the ease of a GUI-based development environment on your local machine while executing the code on subMIT's infrastructure.

For `most languages <https://code.visualstudio.com/docs/languages/overview>`_, VScode enhances your coding experience with features like:

* **Edit code:** including code highlighting and easy `code navigation <https://code.visualstudio.com/docs/editor/editingevolved>`_. `More about code basics <https://code.visualstudio.com/docs/editor/codebasics>`_.

* **Advanced debugging:** use breakpoints, inspect variables, stack navigation. `Debugging guide <https://code.visualstudio.com/docs/editor/debugging>`_.

* **IntelliSense:** code completion, parameter info, quick info, and more. `Discover IntelliSense <https://code.visualstudio.com/docs/editor/intellisense>`_.

* **Time-saving features:** benefit from `AI-assisted code development <https://code.visualstudio.com/docs/editor/artificial-intelligence>`_, `user-defined snippets <https://code.visualstudio.com/docs/editor/userdefinedsnippets>`_, and `task automation <https://code.visualstudio.com/docs/editor/tasks>`_.

* **Accessibility features:** `learn about accessibility in VSCode <https://code.visualstudio.com/docs/editor/accessibility>`_.


Getting Started with VSCode on subMIT
.....................................

Microsoft provides some handy `videos <https://code.visualstudio.com/docs/getstarted/introvideos>`_ for getting started with VSCode, as well as detailed information on `remote connection <https://code.visualstudio.com/docs/remote/ssh>`_.

#. **Install VSCode:** `download and install instructions <https://code.visualstudio.com/docs/setup/setup-overview>`_

#. **SSH Configuration:** Follow the `general configuration guide <https://submit.mit.edu/submit-users-guide/starting.html#common-issues-with-keys>`_ in the subMIT User's Guide. Also have a look at the `VSCode configuration guide <https://submit.mit.edu/submit-users-guide/starting.html#connecting-to-submit-through-VSCode>`_ due to a recent VSCode upgrade which removed the compatibility with CentOS 7.

#. **Remote-SSH Extension:** Available in the VSCode Extensions tab or on the `VSCode website <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`_.

#. **Connect to subMIT:** Click the green "Open a Remote Window" button in the lower-left of the VSCode window. Select "submit" from the menu (VSCode automatically reads your ssh config file). Then, simply "open" a folder or workspace. Opening a folder is typically more convenient than opening a single code file.  Remember: VSCode is now connected to subMIT, so you are looking at and navigating your files on the subMIT servers, not on your laptop/desktop.

#. **Note:** Only run *light* calculations in VSCode; VSCode is intended for editing/debugging, not production runs.  If the execution of your code will consume significant resources (time, memory, processors, ...) then please run it outside VSCode using `Slurm or HTCondor <https://submit.mit.edu/submit-users-guide/running.html>`_.  For example, you can debug using a smaller subset of data than a production run.

Handy Resources
...............

* `Intro videos <https://code.visualstudio.com/docs/getstarted/introvideos>`_ (external)

* `Keyboard cheat sheet <https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_keyboard-reference-sheets>`_ (external)

* `Local Python environment tutorial <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_1.html#types-of-python-environments>`_ (internal)

* `Activating a Python environment tutorial <https://submit.mit.edu/submit-users-guide/program.html#conda-in-visual-studio-code>`_ (internal) 

X2GO
~~~~

X2Go is open source remote desktop software for Linux and is available on submit07. You will need to download the x2goclient on your local machine and then start a session to connect to submit07.mit.edu. 

`x2goclient <https://wiki.x2go.org/doku.php/doc:installation:x2goclient>`_

Remember to point to the correct ssh key that you have uploaded to the submit-portal. There is currently a bug in either XFCE or X2Go causing rendering issues with the compositor when using X2Go. To disable the compositor, you can go to Settings > Window Manager Tweaks > Compositor.

XWin32
~~~~~~
X-Win32 is an X11 server for Windows that allows remote graphical applications (GUIs) to be displayed from a Linux server.

#. **Install XWin32:** Download and install X-Win32 from googling.

#. **SSH Configuration:** In the X-config (ssh configuration), define connection, host and login accordingly. For the command bracket, set "xterm -ls". 

#. **Login Key Conversion:** In the advance option, you need use your private key to login. The key, unlike the private key you generated, should be in the "putty key" format. 

For this you need to download puttygen: https://www.puttygen.com/#google_vignette 
Then open puttygen, click "Conversions" in the top tag -> "Import Key" then select your private key
Then click "Save private key" button, give it a new name.  The new key is in the format of `*`.ppk, you then select this key in your x-win32 set up to login to SubMIT.

