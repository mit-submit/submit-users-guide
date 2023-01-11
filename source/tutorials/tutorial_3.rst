Tutorial 3: Containers (Docker and Singularity)
-----------------------------------------------

This section briefly describes several options in which to set up your environment for working on submit. This section is not exhaustive but introduces several tools which can help you set up your code. 

Docker:
~~~~~~~

All SubMIT users have access to build dockers. This tutorial will guide you through creating a docker image from a dockerfile or through dockerhub. It will also introduce singularity and give an example of cvms.

We will start by downloading a Dockerfile and creating a docker image.

.. code-block:: sh

    wget https://raw.githubusercontent.com/docker-library/python/master/3.11/bullseye/Dockerfile 
    docker build -t docker_python . 

You can check that the new python is avaiable with:

.. code-block:: sh

      docker run --rm -i -t docker_python:latest python --version

or enter python through the docker image

.. code-block:: sh

      docker run --rm -i -t docker_python:latest

Dockerhub:
..........

For this example, we will do a docker build directly from a a repository on dockerhub. In the following sections we will use that example to run in docker and Singularity

Running:
........

We can grab the basic python distribution from dockerhub `dockerhub python <https://hub.docker.com/_/python>`_.

.. code-block:: sh

      docker pull python

After this is done downloading we can then enter into a python environment:

.. code-block:: sh

      docker run --rm -i -t python

You can run python commands through the docker as well. For example you can see the new python version from the docker:

.. code-block:: sh

      docker run --rm -i -t python python --version


Singularity:
~~~~~~~~~~~~

In high-performance computing (HPC) it is often convenient to create singularity images from containers. This section will guide you on how to create a Singularity Image Format (SIF) file to access your container.

Creating a Singularity:
.......................

We can create a .SIF file from the python docker we made above from dockerhub (you can also create from the Dockerfile instead if you would like):

.. code-block:: sh

      singularity build docker_name.sif docker://python

And start the singularity

.. code-block:: sh

      singularity shell docker_name.sif

You can also execute directly with singularity exec:

.. code-block:: sh

      singularity exec docker_name.sif python --version


CVMFS:
......

The CernVM File System (CVMFS) provides a scalable, reliable and low- maintenance software distribution service. It was developed to assist High Energy Physics (HEP) collaborations to deploy software on the worldwide- distributed computing infrastructure used to run data processing applications. CernVM-FS is implemented as a POSIX read-only file system in user space (a FUSE module). Files and directories are hosted on standard web servers and mounted in the universal namespace /cvmfs.

More documentation on CVMFS can be found here: `CVMFS <https://cernvm.cern.ch/fs/>`_

We can access python on any machine through CVMFS. Lets checkt a python out through CVMFS:

.. code-block:: sh

      singularity exec /cvmfs/unpacked.cern.ch/registry.hub.docker.com/library/python:3.9/ python --version

We can also enter the singularity:

.. code-block:: sh

      singularity shell -B ${PWD}:/work /cvmfs/unpacked.cern.ch/registry.hub.docker.com/library/python:3.9/

Once in the singularity, you can run code with the python of that singularity. In the command above, the current directory is binded so that you can write a python script and run it here.
