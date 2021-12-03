Getting started:
----------------

We allow login to the subMIT pool using ssh keys with authentication done through LDAP. Once, you have uploaded your ssh keys, you will also be given a home and work directory in which you can directly start working. This section will guide you on how to set up your ssh keys and upload them to the submit portal to allow login as well as describe the initial resources available to you.

How to get an account:
~~~~~~~~~~~~~~~~~~~~~~

If you already have an MIT account then getting access to subMIT is easy! You only need to upload your ssh key to the submit portal below:

#. `submit-portal <https://submit-portal.mit.edu/>`_

If you are not familiar with ssh keys, no worries! Generating keys is an easy process. Let's start by generating keys on your machine:

.. code-block:: sh

   ssh-keygen

This should create both a private and a public key in your .ssh directory. Simply paste the contents of the public key into the link below and you are ready.

Login and basic areas:
~~~~~~~~~~~~~~~~~~~~~~

Now that you can login we can simply ssh into the submit machines like below:

.. code-block:: sh

   ssh <username>@submit.mit.edu

You should now be logged into one of our main submit server machines. By default you will get areas created for you:

.. code-block:: sh

   #You will start from home which has 5 GB of space
   /home/submit/<username>

   #You will also get a workspace in which to store up to 50 GB of files
   /work/submit/<username>

   #Some users will also get access to hadoop scratch storage amounting to 1 TB
   /mnt/T3_US_MIT/hadoop/scratch/<username>

The rules for an account:
~~~~~~~~~~~~~~~~~~~~~~~~~

Remember that these machines are shared. As such, do not max out resources on local jobs. These machines are connected to large computing clusters which can be accessed through batch submission programs like HTCondor or Slurm. There are tutorials for these tools later in this guide.  
