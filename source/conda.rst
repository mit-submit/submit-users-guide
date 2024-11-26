Conda and its benefits beyond python
------------------------------------

.. tags:: Conda

Conda is a powerful, open-source package and environment management system that allows you to manage compilers and packages for various programming languages. Although commonly associated with Python, Conda supports many more languages, making it versatile for diverse computational tasks. Here’s a guide to briefly introduce Conda for a few programming languages. Feel free to jump to the section on the language of your interest!

**Summary of programming languages**

:ref:`Python<Conda for Python>`, :ref:`Julia<Conda for Julia>`, :ref:`C++ (gcc)<Conda for C++>`, :ref:`FORTRAN (gfortran)<Conda for FORTRAN>`, :ref:`R<Conda for R>`, :ref:`Java<Conda for Java>`, :ref:`Perl<Conda for Perl>`, :ref:`Ruby<Conda for Ruby>`


What is Conda and Why Use It?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conda is useful for:

**Managing dependencies:** Avoid version conflicts between libraries or packages. One of Conda's most powerful features is its ability to resolve dependencies automatically when installing multiple packages. When you specify multiple packages in a single conda install command, Conda determines compatible versions of each package to ensure they work together without conflicts. This avoids version mismatch errors, which can occur when packages are installed separately, as they may depend on incompatible versions of shared libraries.

**Creating isolated environments:** Work on multiple projects with different setups without interference. This also avoids problems when our operating system updates, and with it, the native version of a few programming languages and compilers.

**Cross-language compatibility:** Manage tools and packages not only for Python, but also for R, Julia, C++, and others.

Dependencies and version conflicts
==================================


By separately installing packages, i.e. running ``conda install <package1>`` then ``conda install <package2>``, you miss the features of Conda where it can resolve the dependencies, e.g. package2 needs a specific version of package1. Instead, it is recommended to use ``conda install <package1> <package2>``, such that you don't have th manually resolve the version conflicts.

Installing Conda
~~~~~~~~~~~~~~~~

If you don’t have Conda installed, please see our `Available software page <https://submit.mit.edu/submit-users-guide/program.html#installing-conda>`_.

Conda for Python
~~~~~~~~~~~~~~~~

Create a Python environment:

.. code-block:: sh
    
    conda create -n python_env python

You can check the version using ``python --version`` and the location with ``which python``.


Beyond Python
~~~~~~~~~~~~~

Conda for Julia
===============

You can install Julia through Conda, instead of installing directly as presented in the `User's Guide <https://submit.mit.edu/submit-users-guide/program.html#julia>`_, using the command 

.. code-block:: sh

    conda install -c conda-forge julia

You can then check which version is installed with ``julia --version`` and where using ``which julia``.

Create a Julia environment:

.. code-block:: sh

    conda create -n julia_env julia



Conda for C++
=============

While Conda doesn’t directly install C++ as a standalone compiler, it can install related tools (like GCC [GNU Compiler Collection] or Clang) and libraries for building C++ projects, e.g.

.. code-block:: sh

    conda install -c conda-forge gcc

To check the version you have install, use ``g++ --version`` and to get its location, use ``which g++``.

You can then write your code, let's say in a file called ``example.cpp``, and compile it using ``g++ example.cpp -o example``. Finally, you can run it with the command ``./example``.

Conda for FORTRAN
=================

Similarly to C++, Conda can install FORTRAN compilers, such as ``gfortran``, through the command:

.. code-block:: sh

    conda install -c conda-forge gfortran

You can check the version of ``gfortran`` through the command ``gfortran --version``, and where it is installed with ``which gfortran``. Install Fortran libraries, e.g.

.. code-block:: sh

	conda install -c conda-forge lapack blas fftw

Create an environment:

.. code-block:: sh

    conda create -n fortran_env gfortran

Compile your code with ``gfortran example.f90 -o example``, and run with ``./example``.


Conda for R
===========

Conda can also install R

.. code-block:: sh

    conda install -c r r-base

Use ``R --version`` to determine the version of the language, and ``which R`` for its location.


To create an environment for R, use 

.. code-block:: sh

    conda create -n r_env r-base

To run a script called ``example.R`` in R, use ``Rscript example.R``.

Conda for Java
==============

install using

.. code-block:: sh

    conda install -c conda-forge openjdk

``java --version``, ``which java``

Some, but not all, Java-related libraries are available via Conda, e.g.

.. code-block:: sh

    conda install -c conda-forge java-jline

Conda for Perl
==============

.. code-block:: sh

    conda install -c conda-forge perl

``perl --version`` will give the version you have installed, and ``which perl``, its location.

Import Perl libraries, such as ``perl-dbi``, with

.. code-block:: sh

    conda install -c conda-forge perl-dbi

Conda for Ruby
==============

.. code-block:: sh

    conda install -c conda-forge ruby

``ruby --version``, ``which ruby``

Conda's ability to import Ruby packages is limited. You can manage Ruby gems indirectly or use Ruby libraries available through Conda, e.g.

.. code-block:: sh

    conda install -c conda-forge ruby-rails

Ruby environments can be created with Conda.

How about pip?
~~~~~~~~~~~~~~

pip and Conda are package management tools commonly used for Python. The main features of pip are:

* **Python-focused** pip is a package manager specifically for Python

* **Dependencies** pip does not perform dependency resolution like Conda. pip will install the latest version of each package, without checking if some packages require an earlier version to be compatible.

* **Environments** pip's virtual environments, ``venv``, can be created and activated using

    .. code-block:: sh

        python -m venv my_env

* **Exporting environment** with both Conda and pip, we can export an environment to share it with other users. The commands are

    .. code-block:: sh

        conda env export > environment.yml
        pip freeze > requirements.txt

    These environments can then be recreated by other users by running

    .. code-block:: sh

        conda env create -f environments.yml
        pip install -r requirements.txt