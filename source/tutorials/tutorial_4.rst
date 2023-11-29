Tutorial 4: Source Control (Git/Github) with Visual Studio Code (VSCode)
------------------------------------------------------------------------

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

* Set up source control (a.k.a. version control) from scratch in VSCode (with Git)
* Record your code versions/history using 'commits'.
* Switch between multiple versions of your code using branches
* Incorporate new changes to your code by merging branches 
* Publish your code / source control to GigHub for collaboration

In Git terminology (for those familiar), you will learn how to do the following Git actions in VSCode: ``init``, ``stage``, ``commit``, ``branch``, ``checkout``, ``push``

Prerequisites
~~~~~~~~~~~~~

You need to have Git installed.  You can `download Git here <https://git-scm.com/downloads>`_ or follow the directions in the Source Control sidebar in VSCode.

The Scenario
~~~~~~~~~~~~

You set up source control to keep track of the current stable version of your code.  Then you start working on a new feature, but are interrupted by someone who wants you to run a calculation using the orignal version of your code.  You switch to that code version to fulfill the request and the switch back to pick up where you left off developing your new feature.  Once you are happy with this new feature, you incorporate it into your main ('stable') version of your code.  Then you publish your code (and history) to GitHub to collaborate with others.

Setting up Source Control (with Git)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Follow the directions outlined `here <https://submit.mit.edu/submit-users-guide/program.html#getting-started-with-vscode-on-submit>`_ to open a session connecting Visual Studio Code on your laptop (or desktop) to subMIT.  (But do not open a folder yet once connected to subMIT).

2.  From the top menu, select "File" -> "New Text File ..."

    A new python-editor tab titled "Untitled-1" will appear (it may take a moment).

    .. image:: img/Untitled.png
       :width: 30 %
       :alt: Image of "Untitled-1" python editor tab in VSCode

3.  Copy & paste the following code into that editor window.

    .. code-block:: sh
        :linenos:

        x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
        y = []
        
        for xval in x:
            y.append(xval**2)
        
        print("The values squared from for loop are:{}".format(y))

    .. admonition:: |ShowMore|
       :class: dropdown
       
       a. Click and drag in your browser to highlight the code above, then right-click and select "Copy".
       
       b. Click in the "Untitled-1" editor tab in VSCode. (You should see a vertical text cursor bar blinking next to the number "1", indicating that the focus is set to line number 1).
       
       c. From the menu, select "Edit" -> "Paste".  The code should now appear within your "Untitled-1" editor tab within VSCode.

4.  From the menu, select "File" -> "Save".

    A drop-down menu will appear at the top of your screen suggesting a filename in your home directory on submit.  It will look something like: /home/submit/username/x = [1.py, where "username" is your subMIT (kerberos) username.  

    Change this to "/home/submit/username/tutorial_vscode_source/small_script.py", but replace "username" with your subMIT (kerberos) username.  Then hit OK.

    .. image:: img/WantToCreate.png
        :width: 100%

5.  VSCode will now prompt you, "The folder tutorial_vscode_source does not exist.  Would you like to create it?".  Hit the "OK" button.  
    
    .. admonition:: |ShowMore|
        :class: dropdown

        This is because we included a directory that does not exist yet in the path we just entered, at the top of the screen.  
        
        This created a directory (folder) and a file in your subMIT home directory (on the subMIT servers).

6.  Open the Source Control sidebar by clicking the "Source Control" icon or via the top menu: "View"->"Source Control".

    .. image:: img/SourceControl.png
       :width: 10 %

7.  Click the "Open Folder" button in the Source Control sidebar.

    .. image:: img/SourceControlOpen.png
       :width: 40 % 

    .. admonition:: |ShowMore|
        :class: dropdown

        We choose this option since we are making a repository from scratch in this example.

8.  In the bar that appears on the top of your screen, type in "/home/submit/username/tutorial_vscode_source" but change "username" to your subMIT (kerberos) username to select the folder we just created that contains our code.  Then click "Ok" or hit "Enter".
    
    .. note:: 

        This will re-establish your connection to subMIT so may take a moment.

        Now if you click on the File Explorer icon on the left, you will see our file "small_script.py" listed under this tutorial folder.  (Remember, this file is on the subMIT servers).

        .. image:: img/FileExplorer.png
           :width: 50%

9.  In the "Source Control" sidebar ("View"->"Source Control"), click the "Initialize Repository" button.

     .. image:: img/SourceControlInitialize.png
         :width: 40%

    .. note:: 

        At the bottom left of your VSCode window, you can see that you are now on the "main" branch.

        .. image:: img/MainBranch.png
            :width: 40 %

        The Source Control icon now has a blue circle with a "1" in it to indicate that 1 file has changes that are not in the repository.

        .. image:: img/PreStage.png
            :width: 40 %

        In the Source Control sidebar window, our file "small_script.py" appears under the "Changes" tree item to indicate that this file has changes which are not in the repository.

10. In the Source Control sidebar, click the "Stage Changes" icon (the "+") for "small_script.py" 

    .. image:: img/PreStage_Click.png
        :width: 40 %

    .. note:: 

        Now "small_script.py" is listed under "Staged Changes"

        .. image:: img/Staged.png
            :width: 40 %

    .. admonition:: |ShowMore|
       :class: dropdown

       VSCode has a "Smart Commit" feature which can eliminate this step of staging changes.

       To enable it, select the menu item "Code" -> "Preferences" -> "Settings" and then search for (and enable) "Git: Enable Smart Commit".  Also look at and configure the setting "Git: Smart Commit Changes", which defines the behavior of this feature.


11. Click in the "Message" box above the "Commit" button and type "First working version", then click the "Commit" button.
    
    You now have version control set up to track changes to our code in "small_script.py"!

    .. admonition:: |ShowMore|
       :class: dropdown

        .. note::
            The source control is performed by the program Git.  With this setup, Git and your code both run on the subMIT machines.
        
        .. tip::
            At this point, you *could* click the "Publish this Branch" button in order to put this code into a GitHub repository (repo) as well.  In this tutorial, we will wait until later to do this in order to illustrate that Git and GitHub are separate entities.


Simulating Code Editing (Adding a new feature)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now let's simulate creating a new experimental feature.  

First we create a *new branch* so we can work on this new feature while maintaining a perfect copy of our working code.  

12. Click on the current branch ("main") on the bottom of the window, and then select "+ Create new branch ..." from the dropdown that appears at the top of the screen.
        
    .. image:: img/MainBranch.png
        :width: 40 %

    .. admonition:: |ShowMore|
       :class: dropdown

        Alternatively, in the Source Control sidebar, you could click the "..." next to "Source Control", then select "Branch" -> "Create Branch ...".

        .. image:: img/CreateBranch.png
            :width: 50 %
        
        Yet another alternative is to click the "..." next to "Source Control", then select "Checkout to ..." and then select "+ Create new branch ..." from the dropdown that appears.


    Type "cubed" in the text box and then Enter (Return).  

    .. note::
        The bottom of the window now indicates that we are on the branch "cubed"

        .. image:: img/CubedBranch.png
            :width: 40 %

13. Click on the Explorer icon and then "small_script.py" to bring up the editor with our file.

    .. image:: img/Edit.png
        :width: 80 %

14. Let's add computing the cube of the number as well.  Make the following changes to the code:

    * add "``; z = []``" to the end of line 2
    * put your cursor at the end of line 5, then hit Enter, then type "``z.append(xval**3)``"

    Your code should now look like this:

    .. code-block:: sh
        :linenos:
        :emphasize-lines: 2,6

        x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
        y = []; z = []

        for xval in x:
            y.append(xval**2)
            z.append(xval**3)

        print("The values squared from for loop are:{}".format(y))

    Then "File" -> "Save". 

    .. hint:: 

        Instead of manually making the above changes, you can simply delete all the code in the editor, then copy & paste the entire above code block into the editor, then save.
            

    .. admonition:: |ShowMore|
        :class: dropdown

        * If you copy & paste, it will not fool the version control.  Instead, VSCode (via Git) will still only flag the actual meaningful changes in the code, rather than every line, even though you "rewrote" every line by pasting.  This is because Git does a ``diff`` comparison.  Try it. 
        * Note that the source control icon once again has a blue "1", indicating a pending change.  
        * The blue mark next to line 2 and green by line 6 indicate that those lines have been changed/added, respectively. 
        * A deletion will show up as a red arrow to the left of the line.
        
        If you click on those blue/green/red marks, VSCode will show the changes!

15. Now commit this change to record it with source control: as before, 
    
    * go to the Source Control sidebar ("View"->"Source Control")
    * click the "+" to stage the changes
    * type "calculates cube" in the Message box above the Commit button
    * click the Commit button

    .. admonition:: |ShowMore|
       :class: dropdown

        If you had forgotten to stage your changes and tried to commit an empty commit (no changes), then VSCode would have warned you and asked if you simply want to stage all changes for the commit.


Simulating Switching Back to Your Main (Stable) Version of the Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We're still in the middle of adding this new feature, but let's pretend you need to switch back to your main (stable) version of the code right now.  Perhaps someone urgently needs to know what 3 squared is, so you need to immediately switch back to your working version of the code!
  
Recall that we have the current stable version of your code on the "main" branch.

16. To switch to the "main" branch, simply click on the current branch ("cubed") at the bottom of the window.

    .. image:: img/CubedBranch.png
        :width: 40 %

    And then select "main" from the drop-down that appears at the top of your screen.

    .. note::
    
        Now the bottom of your window should indicate that you are back on the main branch:
        
        .. image:: img/MainBranch.png
            :width: 40 %

        And the code in the editor should reflect the 'old' version of your code which just squares numbers.

    Now you can run your code if you want from the menu: "Run" -> "Run Without Debugging" (or hitting the 'Play' button at the upper right of your editor) ... or just pretend that you did.

    You now switched back to the stable version of your code in the middle of working on a new feature!

Finish & Incorporate your new changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ok, so that fire has been put out.  Let's get back to our new feature...

The version of the code where we are adding the 'cubing functionality' is on the "cubed" branch.

17.  To switch to the "cubed" branch, simply click on "main" (the current branch) in the lower bar of your screen

    .. image:: img/MainBranch.png
        :width: 40 %
    
    Then click on "cubed" from the drop-down menu which appears at the top of your screen.

    .. note:: 

        The lower bar of your screen should indicate that you are on the "cubed" branch and the editor should reflect our new code which also cubes numbers.

18. To finish our work, we still need to print out our new results.  To do that, place your cursor (click) at the end of line 8, hit Enter, then type (or paste) "``print("The values cubed from for loop are:{}".format(z))``"

    Your code should now look like this:

    .. code-block:: sh
        :linenos:
        :emphasize-lines: 9

        x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
        y = []; z = []

        for xval in x:
            y.append(xval**2)
            z.append(xval**3)

        print("The values squared from for loop are:{}".format(y))
        print("The values cubed from for loop are:{}".format(z))

    Then hit "File"->"Save"

19. Now commit this change to record it with source control: as before, 
    
    * go to the Source Control sidebar ("View"->"Source Control")
    * click the "+" to stage the changes
    * type "prints cube" in the Message box above the Commit button
    * click the Commit button

Merging your changes into the main branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now lets say you have meticulously checked your new code and you are ready to incorporate these changes into your main (stable) version of the code.  
    
20.  To do this, go back to the 'main' branch of your code as before:

    * click "cubed" (the current branch) at the bottom of the screen
    * click "main" (the branch you want) from the drop-down that appears at the top of the screen
    * check that the bottom of the screen now says "main" and your code reflects your 'old' code

21. On the Source Control sidebar, click the "..." then "Branch" -> "Merge Branch ..."

    .. image:: img/MergeBranch.png
        :width: 60 %
    
22. Select "cubed" from the drop-down which appears at the top of your screen.
    
    Now your code contains your new cubed code and you are still on the main branch.  
    
    You have sucessfully merged these changes to the main branch!

.. admonition:: |ShowMore|
    :class: dropdown

    If you want to view the history of your code, one way is to view the "Timeline" portion of the "Explorer" sidebar ("View"->"Explorer").  By default, this contains both changes recorded in source control ("Git History") and other intermedaite file saves ("Local History").  You can filter (funnel icon) the Timeline window to only show "Git history".  Then you can see that our main branch has aquired the history of our "cubed" branch.

    Alternatively, you can always pull up a terminal within VSCode (menu "Terminal" -> "New Terminal") and run ordinary git commands such as ``git log``.

Publishing this to GitHub (remote repository)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What we have done so far has used git (behind the scenes within VSCode) and not GitHub.  GitHub is a web service which hosts the source control for your code and provides functionality to facilitate code sharing/collaboration.

Let's say now that you want to collaborate with others using GitHub, so you want to publish this to a GitHub repository. 

.. note:: 

    The standard terms 'remote' and 'local' can be confusing in this use case, since everything we have done so far was actually done on 'remote' machines (the subMIT servers).  *None* of the code actually lives or is tracked on your laptop (what we would typically call your 'local' machine).

    However, for the purposes of Github: 
    
    * 'local' means the repository located on subMIT.  (This is what we have been using so far.)

    * 'remote' means a repository hosted on GitHub.

23. In the Source Control sidebar, click "Publish Branch".

    A pop-up window will notify you that the 'GitHub' extension want to sign into GitHub.  Click Allow.

    Then you will be guided through an authentication process with GitHub.

    Once that is finished, a drop-down menu will appear at the top of your screen asking whether to make it a public or private repository.

    For this tutorial, choose (click) a public repository.

    Now you should be able to see this repo on your GitHub page!

    .. admonition:: |ShowMore|
        :class: dropdown

        When connected to a GitHub repo like this, after each commit, the Commit button will turn into a "Sync Changes" button to allow you to easily syncronize your changes with the GitHub repository.

More Resources
~~~~~~~~~~~~~~

* `VSCode Source Control page <https://code.visualstudio.com/docs/sourcecontrol/overview>`_ (has videos)
* `VSCode Git FAQs <https://code.visualstudio.com/docs/sourcecontrol/faq>`_ 
* `more about Git    in VSCode <https://code.visualstudio.com/docs/sourcecontrol/intro-to-git>`_
* `more about GitHub in VSCode <https://code.visualstudio.com/docs/sourcecontrol/github>`_ 
* `download Git <https://git-scm.com/downloads>`_ 
* `tools to help merge conflics in VSCode <https://code.visualstudio.com/docs/sourcecontrol/overview#_3way-merge-editor>`_ (see also `this video <https://code.visualstudio.com/docs/sourcecontrol/overview#_understanding-conflicts>`_)

More source control Extensions

* `GitHub Pull Requests and Issues <https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github>`_ 
* `GitHub Repositories <https://marketplace.visualstudio.com/items?itemName=github.remotehub>`_ 




.. Cloning a repository
.. ~~~~~~~~~~~~~~~~~~~~


.. Other Helpful Tips
.. ~~~~~~~~~~~~~~~~~~

.. Please see the "|ShowMore|" boxes above, as tips are hidden within those as well.

.. .. tip::
..    VSCode has a "Smart Commit" feature which can eliminate the step of staging changes.

..    To enable it, select the menu item "Code" -> "Preferences" -> "Settings" and then search for (and enable) "Git: Enable Smart Commit".  Also look at and configure the setting "Git: Smart Commit Changes", which defines the behavior of this feature.

.. .. tip:: 
..     VSCode has several different "``diff``" view for viewing changes to code.

..     For instance, see the tip in step 17 above.




