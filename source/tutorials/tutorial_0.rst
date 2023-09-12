Tutorial 0: Introduction to the terminal
----------------------------------------

This tutorial will show you some common commands for a terminal. Most commands have options, which you type as ``[command] [options] [file... | directory...]``. Multiple options can be combined together.

1. change directory (``cd``). You use this command to go into a specific folder or move out of it.

  .. code-block:: sh

    # go to your home directory from any directory
    cd /home/submit/username

    # move up one directory (e.g. from /home/submit/username to /home/submit)
    cd ..

    # move up two directories
    cd ../..

    # move down one directory (e.g. from /home/submit to /home/submit/username)
    cd username

2. check in which directory you are (``pwd``). This prints the full path of the directory where you are.

3. list the files and directories in alphabetical order (``ls``).

  .. code-block:: sh

    # list the files and sub-directories in the directory you are
    ls

    # list the files and sub-directories in a specific directory, e.g. your home directory
    ls /home/submit/username

Some common options are

  * Long format (``-l``): displays the file type, permissions, owner, size, last-modified date, and name.

  * All names (``-a``): includes the hidden files and sub-directories.

  * Sort by date modified (``-t``)

4. create a directory (``mkdir``).

  .. code-block:: sh

    # create a directory with the name mydir
    mkdir mydir

5. copy (``cp``) and safe copy (``scp``) files and directories.

  .. code-block:: sh

    # copy a file to a new location
    cp source_file destination_directory

    # copy a directory recursively (i.e., including its contents)
    cp -r source_directory destination_directory

    # copy a file to a remote server
    scp source_file username@remote_host:destination_directory

    # copy a file from a remote server
    scp username@remote_host:source_file destination_directory

6. move or rename files and directories (``mv``).

  .. code-block:: sh

    # move a file to a new location
    mv source_file destination_directory

    # rename a file
    mv old_filename new_filename

7. tape archive (``tar``), to create and extract archive files, which is common when installing packages or downloading datasets.

  .. code-block:: sh

    # create a tar archive
    tar -cvf archive_name.tar directory_name

    # extract a tar archive
    tar -xvf archive_name.tar

    # create a compressed tar archive using gzip
    tar -czvf archive_name.tar.gz directory_name

    # extract a compressed tar archive using gzip
    tar -xzvf archive_name.tar.gz

8. remove files or directories (``rm``).

  .. code-block:: sh

    # remove a file
    rm filename

    # remove a directory and its contents recursively
    rm -r directoryname

Understanding file permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each file and directory has a set of permissions that define what actions a user can perform on it. The permissions are divided into three groups: owner, group, and others. Each group has three permissions:

* **read** (``r``): allows the file to be opened and read.
* **write** (``w``): allows the file to be edited, deleted, or renamed.
* **execute** (``x``): allows the file to be executed as a program.

You can view the permissions of files and directories using the ``ls -l`` command, which will display a string of 10 characters representing the file type and permissions (e.g., ``-rwxr-xr-x``)

**Note:** online, you may see the command ``sudo`` which is added before another command. You can use it on your own device, but you cannot use it on subMIT.
