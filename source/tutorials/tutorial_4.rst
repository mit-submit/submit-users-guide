Tutorial 4: Package Manager (Conda and Jupyterhub)
--------------------------------------------------

This section briefly describes several options in which to set up your environment for working on submit. This section is not exhaustive but introduces several tools which can help you set up your code. 


Conda:
~~~~~~


Install Miniconda:
.......

For installing Miniconda (see also https://hackmd.io/GkiNxag0TUmHnnCiqdND1Q#Local-or-remote)

.. code-block:: sh

      wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
      # Run and follow instructions on screen
      bash Miniforge3-Linux-x86_64.sh

NOTE: always make sure that conda, python, and pip point to local Miniforge installation (``which conda`` etc.). Another thing to keep in mind is that you should avoid installing packages with ``pip`` using ``--user``. The example below shows the correct way to use pip in conjunction with conda. 

You can either use the default environment (``base``) or create a new one:

.. code-block:: sh

      # create new environment with python 3.9, e.g. environment of name "pyenv"
      conda create --name pyenv python=3.9
      # activate environment "pyenv"
      conda activate pyenv

In this environment, let's check that the right python version is there:

.. code-block:: sh

      python --version

Lets download numpy now and see if its there:

.. code-block:: sh

      conda install -c conda-forge numpy

Let's check to make sure it finds numpy in the new environment:

.. code-block:: sh

      python -c "import numpy; print(numpy.__file__)"

This should print a path with your conda path.

Python Example:
...............

We can now run the example from `tutorial 1 <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_1.html>`_ in our new conda environment:

.. code-block:: sh

     x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
     y = []
     
     for xval in x:
         y.append(xval**2)
     
     print("The values squared from for loop are:{}".format(y))
     
     import numpy as np
     
     x_np = np.linspace(1,10,10)
     y_np = x_np**2
     
     print("The values squared from numpy are:{}".format(y_np))

Conda in Visual Studio Code:
............................

**Selecting and activating a conda environment in VSCode:** you need to inform VSCode which conda environment to use for your Python workspace. Look at the bottom-left corner (macOS) or bottom-right corner (Windows) of the VSCode window to find the "Select Python Interpreter" button. Click on it and a list of available Python interpreters will appear. Choose the one that suits your needs (e.g., ``myenv``). You can also select the environment using the Command Palette (``Cmd+Shift+P`` in macOS or ``Ctrl+Shift+P`` in Windows) and searching for "Python: Select Interpreter". Note that it may take some time for VSCode to detect the available conda environments.

Jupyterhub:
~~~~~~~~~~~

On submit, you have access to Jupyter Notebooks through a `JupyterHub <https://submit.mit.edu/jupyter>`_ set up at submit.

This is set up through the submit machines meaning that you have access to all of your data through jupyter notebooks. 
You will have access to basic python2 and python3 configurations. 
In addition, if you need a more complex environment, you can run your notebooks in any conda environment that you have set up. 
This allows you to create the exact environement you need for your projects. 

Getting your Conda Environment:
...............................

jupyterhub is set up to automatically load all conda and python environments which are found in the following directories

.. code-block:: sh          

      /usr/bin/
      /home/user/<user>/miniforge3/
      /home/user/<user>/anaconda3/
      /home/user/<user>/miniconda3/ 
      /home/user/<user>/.conda/
      /work/submit/<user>/anaconda3/
      /work/submit/<user>/miniconda3/
      /work/submit/<user>/miniforge3/
      /data/submit/<user>/anaconda3/
      /data/submit/<user>/miniconda3/
      /data/submit/<user>/miniforge3/


Example Notebook:
.................

Several intro notebooks can be found in the link below:
`JupyterHub_examples <https://github.com/CpResearch/PythonDataAnalysisTutorial/tree/main/jupyter>`_
