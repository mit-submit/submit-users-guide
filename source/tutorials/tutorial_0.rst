Tutorial 0: Introduction to using the terminal
----------------------------------------------

This tutorial will show you some common commands for a terminal.

#. change directory (``cd``). You use this command to go into a specific folder or move out of it.

  .. code-block:: sh

    # go to your home directory from any directory
    cd /home/submit/username
    # move up one directory (e.g. from /home/submit/username to /home/submit)
    cd ..
    # move down one directory (e.g. from /home/submit to /home/submit/username)
    cd username

#. check in which directory you are (``pwd``). This prints the full path of the directory where you are.

#. list the files and directories (``ls``).

  .. code-block:: sh

    # list the files and sub-directories in the directory you are
    ls
    # list the files and sub-directories in a specific directory, e.g. your home directory
    ls /home/submit/username

#. create a directory (``mkdir``).

  .. code-block:: sh

    # create a directory with the name mydir
    mkdir mydir

**Note:** online, you may see the command ``sudo`` which is added before another command. You can use it on your own device, but you cannot use it on subMIT.
