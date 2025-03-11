.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

User quota and storage at submit
--------------------------------
This section describes the quota and storage for a user and where the storage areas are located. For the large storage area, submit also allows user to use xrootd to make the remote transfer.

Due to the recent updates on the xrootd worldwide, the copy will fail if X509_USER_KEY is not set up correctly. In the x509proxy authentication mentioned below, X509_USER_KEY value can be null, it is recommended to run command "unset X509_USER_KEY" if user encounters the problem about "couldn't find hostkey.pem". 

The quota of home and work area
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For a typical user, the home directory is located at /home/submit/<USER> with quota 5GB. The work directory is located at /work/submit/<USER> with quota 50 GB. 

It is recommended to keep larger files or software in work directory. If there are special requirements to increase the quota, please send request via email submit-help@mit.edu. 


The storage filesystem
~~~~~~~~~~~~~~~~~~~~~~
Users also have a larger quota in storage filesystem, under the directory /ceph/submit/data/user/<first letter>/<USER> with quota 1TB.

Submit uses the ceph to form the filesystem. Currently users could use xrootd to transfer the files to/from ceph through the GSI authentication (with x509 proxy). If users have demands to upload/download files to their personal filesystem (/ceph/submit/data/user/<first letter>/<USER>) remotely, you can send request to submit-help@mit.edu together with your DN. DN is the subject of your certificate.

:red:`Users need x509 certificate to use xrootd transfer.`

For CERN users, they can use their CERN Grid Certificates. For non-CERN users, they can request user certificates from OSG, see `link <https://osg-htc.org/docs/security/certificate-management/>`_.

The way to extract your DN from your certificate usercert.pem: 

.. code-block:: sh

     openssl x509 -in usercert.pem -noout -subject

Once the admin add your DN to the xrootd mapping, you could download or upload your file remotely using xrootd command:

.. code-block:: sh

     Download: xrdcp root://submit50.mit.edu//data/<PATH-TO-FILE> .
     Upload: xrdcp <FILE> root://submit50.mit.edu//data/<PATH-TO-SAVE> 
     <PATH-TO-FILE> and <PATH-TO-SAVE> corresponds to the path under /ceph/submit/data/<PATH-TO-SAVE>
     For example: root://submit50.mit.edu//data/user/w/wangzqe/test.txt refers to /ceph/submit/data/user/w/wangzqe/test.txt 
  
The xrootd request by default tries both IPV6 and IPV4 protocol. It tries IPV6 first, then tries IPV4. If the xrootd server has IPV6 but not enabled, it may affect the transfer speed. To resolve this, users can just enable IPV4 only by typing command:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPv4

To change is back to default, type:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPAuto

To just enable IPV6, type:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPv6

Keep in mind that filesystem is in favor of large files, therefore it is not recommended to save large numbers of small files in the filesystem, for example, 100k+ small log files. 


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

Upon request, we can create user group storage spaces on /ceph at ``/ceph/submit/data/<group name>`` to easily share files. Unless specified otherwise, this group space has between 1 and 10 TB of storage, although we are flexible to create larger spaces if necessary. By default, all members of the group, and only them, can access, modify, and execute the contents of the group storage space. To create this group space, please email submit-help@mit.edu with the requested amount of storage, group name, and email address or Kerberos ID of the users who should have access to the storage space.
