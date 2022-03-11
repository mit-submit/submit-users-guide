Getting started
---------------

We allow login to the subMIT pool using ssh keys with authentication done through LDAP. Once, you have uploaded your ssh keys, you will also be given a home and work directory in which you can directly start working. This section will guide you on how to set up your ssh keys and upload them to the submit portal to allow login as well as describe the initial resources available to you.

How to get an account
~~~~~~~~~~~~~~~~~~~~~

If you already have a general MIT account then getting access to subMIT is easy. You only need to upload your ssh key to the `submit portal <https://submit-portal.mit.edu/>`_.

You might be prompted for not being authorized to access the portal. Please, follow the instructions on the screen.

If you are not familiar with ssh keys, generating keys is a straightforward process. To generate keys on your machine use the following command (chose the defaults when being prompted):

.. code-block:: sh

   ssh-keygen

This should create both a private and a public key in your .ssh directory. Simply paste the contents of the public key into the submit portal link above and you are ready. The private key is like your password and should never be exposed to anybody.

Login and basic areas
~~~~~~~~~~~~~~~~~~~~~

Now that you can login you can simply ssh into the submit machines like below:

.. code-block:: sh

   ssh <username>@submit.mit.edu

You should now be logged into one of our main submit server machines. By default you will get several areas automatically created for you. The starting quotas are 5 GB for the home directory and 50 GB for the work directory. If you need more space than the foreseen  please make your case to out help desk at <submit-help@mit.edu>.

.. code-block:: sh

   # You will start from home which has a quota of 5 GB of space
   /home/submit/<username>

   # You will also get a workspace in which has a qupta of 50 GB of space
   /work/submit/<username>



Creating a personal webpage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the areas above, you have the ability to create a personal webpage in order to store and share your files. In order to create this site you will need a directory named public_html in your home directory:

.. code-block:: sh

  mkdir $HOME/public_html

Once that is created, you can now access your personal webpage after inserting your username in \http://submit08.mit.edu/~<username>/.

The rules for an account
~~~~~~~~~~~~~~~~~~~~~~~~

Remember that these machines are shared. As such, do not max out resources on interactive jobs. As a guideline: If your job takes langer than 15 minutes it makes sense to dispatch it to a batch system. The machines in this login pool are connected to large computing clusters which are accessed by batch programs like HTCondor or Slurm. There are tutorials for these tools later in this guide.  
