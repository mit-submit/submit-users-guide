User quota and storage at submit
--------------------------------
This section describes the quota and storage for a user and where the storage areas are located. For the large storage area, submit also allows user to use xrootd to make the remote transfer.

The quota of home and work area
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For a typical user, the home directory is located at /home/submit/<USER> with quota 5GB. The work directory is located at /work/submit/<USER> with quota 50 GB. 

It is recommanded to keep larger files or softwares in work directory. If there are special requirements to increase the quota, please send request via email submit-help@mit.edu. 


The storage filesystem
~~~~~~~~~~~~~~~~~~~~~~
Users also have a larger quota in storage filesystem, under the directory /data/submit/<USER> with quota 1TB.

Submit uses the gluster to form the filesystem. Currently users could use xrootd to transfer the files to/from the gluster through the GSI authentication (with x509 proxy). If users have demands to upload/download files to their personal filesystem (/data/submit/<USER>) remotely, you can send request to submit-help@mit.edu togethor with your DN. DN is the subject of your certificate.

:red:`Users need x509 certificate to use xrootd transfer.`

For CERN users, they can use their CERN Grid Certificates. For non-CERN users, they can request user certificates from OSG, see `link ye==test <https://osg-htc.org/docs/security/certificate-management/>`_.

The way to extract your DN from your certificate usercert.pem: 

.. code-block:: sh

     openssl x509 -in usercert.pem -noout -subject

Once the admin add your DN to the xrootd mapping, you could download or upload your file remotely using xrootd command:

.. code-block:: sh

     Download: xrdcp root://submit50.mit.edu//<USER>/<PATH-TO-FILE> .
     Upload: xrdcp <FILE> root://submit50.mit.edu//<USER>/<PATH-TO-SAVE> 
     <PATH-TO-FILE> and <PATH-TO-SAVE> corresponds to the path under /data/submit/<USER>

The xrootd request by default trys both IPV6 and IPV4 protocol. It tries IPV6 first, then tries IPV4. If the xrootd server has IPV6 but not enabled, it may affect the transfer speed. To resolve this, users can just enable IPV4 only by typing command:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPv4

To change is back to default, type:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPAuto

To just enable IPV6, type:

.. code-block:: sh

     export XRD_NETWORKSTACK=IPv6

Keep in mind that filesystem is in favor of large files, therefore it is not recommanded to save large numbers of small files in the filesystem, for example, 100k+ small log files. The gluster system may unmount your directory if you transfer too many small files in a short time. 

The storage on Tier2
~~~~~~~~~~~~~~~~~~~~
Upon request, users may also have some storage on MIT Tier2 sites. Note that tier2 is external computing resources and users can only use xrootd to transfer the files. If other words, to use storage in tier2, users must have x509 certificate. The details of how to get such certificates are above. 
 
