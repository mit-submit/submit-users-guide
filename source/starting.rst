.. raw:: html

    <style> 
        .red {color:red;} 
        .black {color:black; text-shadow:none;} 
        .gold {color:#fecb2f;}
    </style>

.. role:: red

.. role:: black

.. role:: gold

Getting started
---------------

We allow login to the subMIT pool using ssh keys with authentication done through LDAP. Once, you have uploaded your ssh keys, you will also be given a home and work directory in which you can directly start working. This section will guide you on how to set up your ssh keys and upload them to the submit portal to allow login as well as describe the initial resources available to you.

How to get an account
~~~~~~~~~~~~~~~~~~~~~

If you already have a general MIT account then getting access to subMIT is easy. You only need to upload your ssh key to the `submit portal <https://submit-portal.mit.edu/>`_.

You might be prompted for not being authorized to access the portal. Please, follow the instructions on the screen.

If you are not familiar with ssh keys, generating keys is a straightforward process. 


.. tabs::

   .. group-tab:: :gold:`Mac OS`

      :black:`Open the Terminal application.`
      :black:`This can be done by clicking on Lanuchpad or hitting F4, and then typing "terminal" followed by the Return key.`

   .. group-tab:: :gold:`Windows`

      :black:`We recommend you install & use Windows Subsystem for Linux.  If you do not wish to at this time, you may follow these directions to generate keys natively in Windows...`

      :black:`Click in the Start Menu search bar (next to the Windows icon), then type "command prompt" followed by the Enter key.`



To generate keys on your machine use the following command (chose the defaults when being prompted):

.. code-block:: sh

   ssh-keygen -t rsa

This should create both a private and a public key (``id_rsa``, the private key, and ``id_rsa.pub``, the public key) in your ``.ssh`` directory. 

.. tabs::

   .. group-tab:: :gold:`Mac OS`

      :black:`In the output on your screen you will see a line specifying the path to your public key, such as "Your public key has been saved in /Users/[username]/.ssh/id_rsa.pub".`
      :black:`To copy your public key, run the following command using the path to your public key`

      .. code-block:: console

         cat /Users/[username]/.ssh/id_rsa.pub | pbcopy
      
      :black:`Or simply open the public key file in your favorite text editor and highlight & copy the text.`

   .. group-tab:: :gold:`Windows`

      :black:`In the output on your screen you will see a line specifying the path to your public key, such as "Your public key has been saved in C:\\Users\\[username]/.ssh/id_rsa.pub"`
      :black:`To copy your public key, run the following command using the path to your public key`
      
      .. code-block:: console

         clip < C:\Users\[username]/.ssh/id_rsa.pub
      
      :black:`Or simply open the public key file in your favorite text editor and highlight & copy the text.`


Simply paste the contents of the public key (``id_rsa.pub``) into the submit portal link above and you are ready. The private key is like your password and should never be exposed to anybody. Please do not paste this into the subMIT website; if you do you should re-create your keys by running the ``ssh-keygen`` command again.

We recommend that you use the standard name (as prompted by ``ssh-keygen``) for the keys, as this will make the process easier. Some advanced users may want to create differently named keys within their ``.ssh`` directory, as they may wish to keep separate keys for separate machines. If you do this, please remember to either create the appropriate configuration within ``.ssh/config``, or log in with ``ssh -i /path/to/identity/file``.

Login and basic areas
~~~~~~~~~~~~~~~~~~~~~

Now that you can login you can simply ssh into the submit machines like below:

.. code-block:: sh

   ssh <username>@submit.mit.edu

You should now be logged into one of our main submit server machines. By default you will get several areas automatically created for you. The starting quotas are 5 GB for the home directory and 50 GB for the work directory. If you need more space than the foreseen  please make your case to out help desk at <submit-help@mit.edu>.

.. code-block:: sh

   # You will start from home which has a quota of 5 GB of space
   /home/submit/<username>

   # You will also get a workspace in which has a quota of 50 GB of space
   /work/submit/<username>

   # For larger files, you will get a data storage space with a quoata of 1 TB of space
   /data/submit/<username>

Note that storing and editing code located in /data is discouraged.

Common issues with keys
~~~~~~~~~~~~~~~~~~~~~~~

A common issue with keys is when you already have a key in your .ssh directory and ssh defaults to a different key than the one uploaded to the submit-portal. For example, GitHub commonly uses id_ed25519 keys which can interfere when you try to login.

There are a few ways to handle this issue. If you prefer, you can simply upload the other key to the submit-portal. If you would like to use the rsa key, log in with a command like ``ssh -i <path>/.ssh/id_rsa <username>@submit.mit.edu`` or create the appropriate configuration within ``.ssh/config`` like below.


.. code-block:: sh

   Host submit
     HostName submit.mit.edu
     User <username>
     IdentitiesOnly=yes
     PreferredAuthentications publickey
     PasswordAuthentication no
     IdentityFile <path>/id_rsa

One thing to note, is that if you have already tried this ssh command once and it broke, you will need to modify your known_hosts file in the .ssh directory. In order to fix this you will need to remove lines with ``submit`` in them from the known_hosts. Please note that it is safe to remove the lines from this file. 

Creating a personal webpage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the areas above, you have the ability to create a personal webpage in order to store and share your files. In order to create this site you will need a directory named ``public_html`` in your home directory:

.. code-block:: sh

  mkdir $HOME/public_html

Once that is created, you can now access your personal webpage after inserting your username in \http://submit08.mit.edu/~<username>/.

The rules for an account
~~~~~~~~~~~~~~~~~~~~~~~~

Remember that these machines are shared. As such, do not max out resources on interactive jobs. As a guideline: If your job takes langer than 15 minutes it makes sense to dispatch it to a batch system. The machines in this login pool are connected to large computing clusters which are accessed by batch programs like `HTCondor <https://submit.mit.edu/submit-users-guide/running.html#id1>`_ or `Slurm <https://submit.mit.edu/submit-users-guide/running.html#id2>`_.
