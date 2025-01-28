Tutorial 3: Containers (Podman and Singularity)
-----------------------------------------------

.. tags:: Containers

This tutorial will guide you through:

1. Basic Podman commands
2. Creating a Dockerfile
3. Creating a Docker image from a Dockerfile
4. Manage and run containers
5. Using DockerHub to download and use an existing container
6. Basic Singularity commands
7. Converting your Docker/Pdoman container to a Singularity image

Note: unsure whether containers are the right option for you? See other options for how to install software and environments on `our docs <https://submit.mit.edu/submit-users-guide/program.html>`_.

Podman: a Basic Introduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All the scripts in this tutorial are available in the `submit-examples GitHub <https://github.com/mit-submit/submit-examples/>`_ under the ``containers/podman/`` folder.
You should find the following files, which will be used in this tutorial,

.. code-block:: bash

    Dockerfile
    script.py
    run.sh

Creating a Dockerfile
.....................

**Dockerfiles** are text documents that provide a set of instructions to Docker/Podman (the terms are used interchangably in this tutorial) to create an **image**.

In this file, you specify which software you want to download, the environment you want to be in, and even the operating system you want to use.

... if you know what you want
.............................

If you know the software you want, you can set up your Dockerfile to install exactly what you need.

Suppose, for example, you want to install a simple stack consisting of: your favorite version of python with some packages, sitting on an Alma Linux 9 distribution.
The Dockerfile might look something this.

.. code-block:: sh

    # Dockerfile

    # specify the base image that we're building the image on top of
    # from https://hub.docker.com/_/almalinux
    FROM almalinux:9
    
    # set some variables
    USER $USER
    WORKDIR $PWD
    ENV TERM=xterm-256color
    
    # install the software we want
    RUN yum install -y python3.12 && yum install -y pip && yum install -y ncurses
    RUN python3 -m pip install --upgrade pip
    RUN python3 -m pip install \
        numpy \
        matplotlib \
        seaborn \
        scikit-learn
    
    # copy everything in the current directory into /home inside the container
    COPY . /home
    
    # run the command
    CMD ["/bin/bash"]

Let's break this down.

The ``FROM`` commands specifies that we want to build our image starting from an existing image; in this case, the base is an operating system we like, Alma Linux 9.
There is a large library of existing images that you can use; `DockerHub <https://hub.docker.com/>`_ provides a service to host and distribute images: see the later Section to learn more about this.

.. code-block:: sh

    # specify the base image that we're building the image on top of
    # from https://hub.docker.com/_/almalinux
    FROM almalinux:9

The ``ENV``, ``USER``, and ``WORKDIR`` set some environment variables.
Here we just set the terminal (``TERM``) and 

.. code-block:: sh

    # set some variables
    USER $USER
    WORKDIR $PWD
    ENV TERM=xterm-256color

The ``RUN`` commands then ... run certain commands, as you would on a command line, to install desired software.
In this case, we install python and some basic python packages.
This is simple stuff, but you have a huge freedom here to set up whatever software you want.

.. code-block:: sh

    # install the software we want
    RUN yum install -y python3.12 && yum install -y pip && yum install -y ncurses
    RUN python3.12 -m pip install --upgrade pip
    RUN python3.12 -m pip install \
        numpy \
        matplotlib \
        seaborn \
        scikit-learn

The copy command will create a copy of local scripts into the container.
Note that this is not a reference, but a copy, so if you these files inside the container, they will not affect the files outside the container.
Once the container is bulit, these files will be stored inside it.
We will talk later how to get data out of the container.

.. code-block:: sh

    # copy everything in the current directory into /home inside the container
    COPY . /home

Finally, the ``CMD``.
This is what is executed by the container when you run it.
In particular, when our container is created, it will execute ``\bin\bash``, i.e., it will just open up a bash shell.

.. code-block:: sh

    # run the command
    CMD ["/bin/bash"]

You could instead instruct the container to run some application or script by changing this to,

.. code-block:: sh

    # run the command
    CMD ["python3", "/home/script.py"]

... if you don't know what you want
...................................

If you don't know exactly the software you need, want to debug your configuration, or just could use to play around, you can run an existing image -- be it a prototype of your final product or the base image you are building your image from -- and work with it interactively, to then use as a testbed for writing your Dockerfile.

Suppose, for example, you want AlmaLinux9 as your OS.
You can then open a "blank" container,

.. code-block:: sh

      podman run -it --rm almalinux:9 /bin/bash

Now, you should be in a command line operating as "root" inside your container.
You can install things via ``yum install``, and figure out what you software you need to run your code.

Building and Running a Container from a Dockerfile
..................................................

Once you have a Dockerfile specifying your container’s setup, you can use Podman to first **build an image**, and then **run the container**.

To build an image from your Dockerfile, the general syntax is,

.. code-block:: bash

    podman build -t <image_name> .

- ``-t <image_name>`` assigns a name to your container image for easier reference.
- ``.`` specifies the current directory, where Podman expects to find the Dockerfile.

In our example, you can run,

.. code-block:: sh

    podman build -t tutorial .

Once your image is built, you can run a container from it.
You can spawn multiple containers from a single image, they are just instances of the same image.
The general syntax is,

.. code-block:: bash

    podman run -it --rm <image_name>

- ``-i`` keeps stdin open, allowing interaction.
- ``-t`` allocates a terminal.
- ``--rm`` automatically removes the container after it stops.

In our example, you can run,

.. code-block:: sh

    podman run -it tutorial

We provide a ``run.sh`` that you can run instead of typing our these commands, which will build the image and run the container.
It's good practice to put these commands in an executable script.

.. code-block:: sh

    ./run.sh

Once you run the container, because your ``CMD`` opens up a bash shell, you should see something like,

.. code-block:: sh

    [root@9f9ef97b19a9 home]#

We are inside the container!

You can look around, and you should see that in ``/home`` we have the scripts that we copied in,

.. code-block:: sh

    [root@9f9ef97b19a9 /]# ls
    afs  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    [root@9f9ef97b19a9 /]# cd /home
    [root@9f9ef97b19a9 home]# ls
    Dockerfile  run.sh  script.py

You can then run the script with the ``python3`` we have installed,

.. code-block:: sh

    python3 script.py

Enjoy the dance!

Basic Podman Commands 
.....................

This section covers some essential Podman commands to help you manage and interact with containers on the cluster.

To view all running containers, use:

.. code-block:: bash

    podman ps

This command shows an overview of running containers, displaying useful information such as container ID, image, status, and command. To see all containers (including stopped ones), add the `-a` flag:

.. code-block:: bash

    podman ps -a

If you ran your command with ``--rm``, you will not see anything running.
Else, you can see something like,

.. code-block:: sh

    $ podman ps
    CONTAINER ID  IMAGE                      COMMAND     CREATED         STATUS         PORTS       NAMES
    e3f3a82080c0  localhost/tutorial:latest  /bin/bash   16 minutes ago  Up 16 minutes              elegant_nash

Since it's running, we can always get back inside the container using either the name or the container ID,

.. code-block:: sh

    $ docker exec -it e3f3a82080c0 /bin/bash
    [root@e3f3a82080c0 /]#

To start or stop a container, use:

.. code-block:: bash

    podman start <container_id_or_name>
    podman stop <container_id_or_name>

To delete a stopped container:

.. code-block:: bash

    podman rm <container_id_or_name>

If you need to forcefully remove a running container, add the ``-f`` flag:

.. code-block:: bash

    podman rm -f <container_id_or_name>

To check the logs for a specific container:

.. code-block:: bash

    podman logs <container_id_or_name>

This command helps in troubleshooting or checking the output of a containerized application.

Podman: More Advanced Concepts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are all the basics you need to create and run containers! What follows are more advanced but important concepts that may help going from this simple tutorial to a more realistic use-case.

Accessing Local Data Inside a Container
.......................................

The ``-v`` option in Podman allows you to mount a host directory or file inside the container.
This is especially useful for sharing data between your host system and the container, or for persisting data generated by the container.

Basic syntax:

.. code-block:: bash

    podman run -v /host/path:/container/path <image_name>

- ``/host/path`` is the directory or file path on your local machine.
- ``/container/path`` is where you want it to appear inside the container.

For example:

.. code-block:: bash

    podman run -it -v /work/submit/$USER/:/data tutorial

This mounts the ``/work/submit/$USER/`` folder from your host machine at ``/data`` inside the container, allowing both the container and host to read and write to it.

.. code-block:: bash

    $ podman run -it -v /work/submit/$USER/:/data tutorial
    [root@b9d4e93b029a /]# ls
    afs  bin  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    [root@b9d4e93b029a /]# ls /data
    <whatever is in your /work/submit/$USER/ will appear here>

The ``-v`` option can also include additional flags to control access:

- ``:ro`` for read-only access.
- ``:rw`` (default) for read and write access.

Example with read-only:

.. code-block:: bash

    podman run -it -v /work/submit/$USER/:/data:ro tutorial

Cache
.....

As you may have noticed, building images isn't the fastest thing in the world.
Podman automatically caches any steps (called 'layers') that are unchanged in the Dockerfile.

You can be explicit about setting your cache when building an image,

.. code-block:: sh

    podman build --cache-to type=local,dest=/work/submit/$USER/ \
             --cache-from type=local,src=/work/submit/$USER/ \
             --layers -t tutorial .

DockerHub
.........

`DockerHub <https://hub.docker.com/>`_ is an extensive platform that allows you to host and distribute images.
Think of it as the GitHub for container images.
These are built images, so they contain already all the specified software and files that their creator configured.

Go on `their website <https://hub.docker.com/>`_, create an account, and create a new repository.
I will be calling mine ``submit-test``.

You can log in from the command line with,

.. code-block:: sh

    podman login docker.io

You can then create a tag, and push it to DockerHub,

.. code-block:: sh

    podman tag localhost/tutorial docker.io/<DOCKERHUB_USERNAME>/submit-test:latest
    podman push  docker.io/<DOCKERHUB_USERNAME>/submit-test:latest

You should see on the website that your image appeared.
Your friends can now pull your image,

.. code-block:: sh 

    podman pull docker.io/<DOCKERHUB_USERNAME>/submit-test:latest

Pretty neat!

Singularity
~~~~~~~~~~~

In high-performance computing (HPC) it is often convenient to create **singularity images** from Docker/Podman containers.
These are better served for executing your scripts on batch computing clusters serviced by Slurm and HTCondor.
In particular, they are more portable, and don't need a Docker deamon to run on the machine.
This section will guide you on how to create a Singularity Image Format (SIF) file to access your container.

**We strongly reccomend using Singularity for your Slurm jobs on subMIT.**

For HTCondor, the best solution for distributing your container will depend on the cluster, please see our User's Guide for more information.

Creating a Singularity from a Container
.......................................

We can create a ``.SIF`` file from any container.
It's best to first compress your container.
The general syntax is,

.. code-block:: sh

      podman save -o <your_compressed_container>.tar <your_container>

For example,

.. code-block:: sh

      podman save -o tutorial.tar tutorial

We can then use the compressed container to build the singularity image.
The general syntax is,

.. code-block:: sh

      singularity build <singularity_image_name>.sif docker-archive://<your_compressed_container>

For example,

.. code-block:: sh

      singularity build tutorial.sif docker-archive://tutorial.tar

The singularity image is now built!
It is just a file that will be created in the directory you are working in.

We can start a shell using the singularity image,

.. code-block:: sh

      singularity shell tutorial.sif

Inside of this shell, you will have access to the same software you have set up in the container.

You can also execute code directly with ``singularity exec``,

.. code-block:: sh

      singularity exec tutorial.sif python script.py

This is usually how you want to run your code using containers!

Accessing Mounts Inside Singularity
...................................

To mount host files and directories into a Singularity container, you can use the ``--bind`` option.
This allows you to specify paths on the host that should be accessible within the container, and is similiar to the ``-v`` option in podman.

Basic syntax:

.. code-block:: bash

    singularity exec --bind /host/path:/container/path <image_name>.sif /bin/bash

In this example, ``/host/path`` is the directory or file on the host, while ``/container/path`` is where it will be accessible inside the container. 

For example, to mount a data directory:

.. code-block:: bash

    singularity exec --bind /home/submit/$USER:/home tutorial.sif /bin/bash

This command mounts the ``/home/submit/$USER/`` directory from the host into the container at ``/home``, allowing both the host and the container to read and write to it. 

Conclusion
~~~~~~~~~~

We hope this tutorial gave you some practical examples for working with containers.
See our User's Guide for more information on podman and singularity, and feel free to reach out to us for any questions about containers.
