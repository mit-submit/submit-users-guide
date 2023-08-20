Tutorial 7: Debugging Fortran code with Visual Studio Code (VSCode)
-------------------------------------------------------------------

This takes a bit more initial configuration (that may be less than obvious) than some other languages, so we'll walk you through this.

.. |ShowMore| replace:: More Detail (click here to show/hide)

.. tip:: 
    Click on the boxes throughout this tutorial labeled "|ShowMore|" in order to see more detailed information and/or helpful hints.  Click again to hide the info again.

.. admonition:: |ShowMore|
    :class: dropdown

    The instructions below make use of the menus to run commands, but you could alternatively run the commands using keyboard shortcuts, or by pulling up the Command Palette (Command+Shift+P on Mac, or Ctrl+Shift+P on Windows or Linux) and simply typing the command (e.g. Command+Shift+P then type "connect to host").

    .. tip:: 
    
        Click any picture to enlarge it.  (Then use your browser's 'Back' button to return to the tutorial).

You will learn to ...
~~~~~~~~~~~~~~~~~~~~~

* Configure VSCode for debugging Fortran code
* Perform basic debugging of Fortrancode in VSCode

In Git terminology (for those familiar), you will learn how to do the following Git actions in VSCode: ``init``, ``stage``, ``commit``, ``branch``, ``checkout``, ``push``

Prerequisites
~~~~~~~~~~~~~

* The `Modern Fortran extension <https://marketplace.visualstudio.com/items?itemName=fortran-lang.linter-gfortran>`_ for VSCode (This requires and will automatically install the `C/C++ extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools>`_ as well)
* (As an alternative to the above, we have successfully used the `Fortran Breakpoint Support extension <https://marketplace.visualstudio.com/items?itemName=ekibun.fortranbreaker>`_ with the `C/C++ extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools>`_)
* subMIT already has both ``gfortran`` and ``gdb`` already installed natively, so you don't need to worry about those.  However, if you wish to use a custom version of ``gfortran`` in a conda environment, make sure you install ``gdb`` in that conda environment as well, as these are both necessary (e.g. ``conda create --name gfort_dbg -c conda-forge gfortran gdb``).

.. conda install -c conda-forge fortls

Configuring VSCode to debug Fortran
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Follow the directions outlined `here <https://submit.mit.edu/submit-users-guide/program.html#getting-started-with-vscode-on-submit>`_ to open a session connecting Visual Studio Code on your laptop (or desktop) to subMIT.  (But do not open a folder yet once connected to subMIT).

2.  From the top menu, select "File" -> "New Text File ..."  

    A new editor tab titled "Untitled-1" will appear (it may take a moment).

    .. image:: img/Untitled.png
       :width: 30 %
       :alt: Image of "Untitled-1" editor tab in VSCode

3.  Copy & paste the following code into that editor window.

    .. code-block:: sh
        :linenos:

        program hello
          print *, 'Hello, World!'
          print *, 'Hi again'
        end program hello

    .. admonition:: |ShowMore|
       :class: dropdown
       
       a. Click and drag in your browser to highlight the code above, then right-click and select "Copy".
       
       b. Click in the "Untitled-1" editor tab in VSCode. (You should see a vertical text cursor bar blinking next to the number "1", indicating that the focus is set to line number 1).
       
       c. From the menu, select "Edit" -> "Paste".  The code should now appear within your "Untitled-1" editor tab within VSCode.

4.  From the menu, select "File" -> "Save".

    A drop-down menu will appear at the top of your screen suggesting a filename in your home directory on submit.  It will look something like: /home/submit/username/program hello.md, where "username" is your subMIT (kerberos) username.  

    Change this to "/home/submit/username/tutorial_dbg_fort/hello.f90", but replace "username" with your subMIT (kerberos) username.  Then hit OK.

    .. image:: img/ConfirmFort.png
        :width: 100%

5.  VSCode will now prompt you, "The folder tutorial_dbg_fort does not exist.  Would you like to create it?".  Hit the "OK" button.  
    
    .. admonition:: |ShowMore|
        :class: dropdown

        This is because we included a directory that does not exist yet in the path we just entered, at the top of the screen.  
        
        This created a directory (folder) and a file in your subMIT home directory (on the subMIT servers).

6.  In the menu (top of screen), selct "File" -> "Open Folder..."

    In the text box that appears at the top of your screen, type "/home/submit/username/tutorial_vscode_dbgfort/" but replace "username" with your subMIT (kerberose) username.  (It is likely already pre-filled).

    Hit OK.

    VSCode will re-establish your connection to subMIT and may take a moment.

7.  Open the Command Pallete

    .. todo: add in how for all OS

    Type "tasks: Configure Task" in the text box that appears at the top of your screen.  Then hit Enter/Return.

    Then select "Create tasks.json file from template" from the drop-down menu that appears at the top of your screen.

    Then select "Others" from the drop-down menue that appears.

    This will bring up an editor with a json file pre-filled.

8.  Replace the contents of that editor with the lines below

    .. code-block:: json
        
        {
            "version": "2.0.0",
            "tasks": [
                {
                    "type": "shell",
                    "label": "gfbuild",
                    "command": "gfortran hello.f90 -g -Wall -Wextra -Warray-temporaries -Wconversion -fimplicit-none -fbacktrace -ffree-line-length-0 -fcheck=all -ffpe-trap=zero,overflow,underflow -finit-real=nan",
                }
            ]
        }

    Click "File" -> "Save" from the menu

    .. admonition:: |ShowMore|
       :class: dropdown
       
        Delete all the lines that were pre-filled in the editor, then copy the above lines and paste them into the editor.  Then click "File" -> "Save" from the menu.



.. come back to
.. ``fortls`` (see notes app)
.. references?
.. in conda environment
