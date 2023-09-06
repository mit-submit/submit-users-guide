Tutorial 0: Introduction to using the terminal
----------------------------------------------

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

5. copy (``cp``). There's also safe copy (``scp``)

6. move (``mv``)

7. tape archive (``tar``). Create and extract archive files. This is especially common when installing packages or downloading datasets.

permissions: write, read, delete

**Note:** online, you may see the command ``sudo`` which is added before another command. You can use it on your own device, but you cannot use it on subMIT.
