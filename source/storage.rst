.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

User quota and storage at SubMIT
--------------------------------
This section describes the quota and storage for a user and where the storage areas are located.
For the large storage area, SubMIT also allows user to use XRootD to make the remote transfer.

Due to the recent updates on the xrootd worldwide, the copy will fail if X509_USER_KEY is not set up correctly. In the x509proxy authentication mentioned below, X509_USER_KEY value can be null, it is recommended to run command "unset X509_USER_KEY" if user encounters the problem about "couldn't find hostkey.pem". 

The home and work areas
~~~~~~~~~~~~~~~~~~~~~~~
For a typical user, the home directory is located at ``/home/submit/<USER>`` with quota 5GB. The work directory is located at ``/work/submit/<USER>`` with quota 50 GB. 

It is recommended to keep larger files or software in work directory. If there are special requirements to increase the quota, please send request via email submit-help@mit.edu. 

The storage filesystem
~~~~~~~~~~~~~~~~~~~~~~

Users also have a larger quota in storage filesystem, under the directory ``/ceph/submit/data/user/<first letter>/<USER>`` with quota 1TB.
SubMIT uses ceph to form the filesystem.
The filesystem is accessible from all subMIT nodes (e.g. any node you can log in to, and any node connected via Slurm) directly via the ``/ceph`` mount.

:red: Keep in mind that filesystem is optimized for large files, therefore it is not recommended to save large numbers of small files in the filesystem, for example, 100k+ small log files. This will seriously hinder the performance of the filesystem for all users.

Remote reading via XRootD
~~~~~~~~~~~~~~~~~~~~~~~~~

Users can use XRootD to transfer the files *remotely* to/from ceph through the GSI authentication with a x509 proxy.
This is useful, for example, if you are running jobs using HTCondor on other clusters, and want to copy data from or to SubMIT.

1. **Users need x509 certificates to use XRootD transfer:** for CERN users, they can use their CERN Grid Certificates. For non-CERN users, they can request user certificates from CILogon, see `link <https://cilogon.org/>`_.

2. **Install your certificates:** with the .p12 you have downloaded, you need to install the certificates. On the SubMIT command line, exectute,

.. code-block:: sh

    openssl pkcs12 -in [your-cert-file] -clcerts -nokeys -out ~/.globus/usercert.pem
    openssl pkcs12 -in [your-cert-file] -nocerts -out ~/.globus/userkey.pem
    chmod 0444 ~/.globus/usercert.pem
    chmod 0400 ~/.globus/userkey.pem

3. **Extract DN from your certificate and send it to the admin team**: Run the following, and send it via email to submit-help@mit.edu, asking the team to add you to the list of allowed users,

.. code-block:: sh

     openssl x509 -in usercert.pem -noout -subject

Once the admin team adds your DN to the XRootD mapping, you're good to go.
The redirector is,

.. code-block:: sh

    root://submit50.mit.edu/

For example, to download a file form SubMIT,

.. code-block:: sh

     xrdcp root://submit50.mit.edu//data/user/a/attila/file.txt .

And to upload a file to SubMIT,

..code-block:: sh

     xrdcp file.txt root://submit50.mit.edu//data/user/a/attila/

Note that the path on XRootD omits the ``/ceph/submit``, starting only with ``/data``; i.e., the local path ``/ceph/submit/data/user/a/attila`` is accessed via XRootD as ``/data/user/a/attila``.

**IP v4 vs v6**

The xrootd request by default tries both IPV6 and IPV4 protocol. It tries IPV6 first, then tries IPV4. If the xrootd server has IPV6 but not enabled, it may affect the transfer speed. To resolve this, users can just enable IPV4 only by typing command:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPv4

To change is back to default, type:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPAuto

To just enable IPV6, type:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPv6


The storage at fast mount space (/scratch/)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is a fast mount space mounted as /scratch/ which provides high speed I/O. This speeds up the physics researches which have large input files and require fast accessing speed. The files under /scratch is for short term analyzing and not meant for long term storage. The data under /scratch should have a backup under the storage system if it is important.

The files under /scratch can be accessed both through the mounting point /scratch and xrootd. To use xrootd, the accessing point is 

.. code-block:: sh

     root://submit30.mit.edu//scratch/

It shares the same x509 authentication as the xrootd for the main storage space. We will soon add kerberos authentication (in progress).

The storage on Tier2
~~~~~~~~~~~~~~~~~~~~
Upon request, users may also have some storage on MIT Tier2 sites. Note that tier2 is external computing resources and users can only use xrootd to transfer the files. In other words, to use storage in tier2, users must have x509 certificate. The details of how to get such certificates are above. 

Group storage at submit
~~~~~~~~~~~~~~~~~~~~~~~

Upon request, we can create user group storage spaces on /ceph at ``/ceph/submit/data/<group name>`` to easily share files. Unless specified otherwise, this group space has between 1 and 10 TB of storage, although we are flexible to create larger spaces if necessary. Upon request we can also create backed up group storage space in ``/home/submit/<group name>`` with a 5GB quota that can be extended if needed. By default, all members of the group, and only them, can access, modify, and execute the contents of the group storage space. A ``public_html`` can be added in ``/home/submit/<group name>`` to create a group webpage in order to view or share your files in the same way as possible for users (see `<https://submit.mit.edu/submit-users-guide/starting.html#creating-a-personal-webpage>`_). To create this group space, please email submit-help@mit.edu with the requested group name, amount of storage, if a ``/home/submit`` space is needed, and email address or Kerberos ID of the users who should have access to the resources.
