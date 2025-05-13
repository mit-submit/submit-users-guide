Using Globus on SubMIT
----------------------

.. tags:: Globus

Globus is a powerful platform for **fast, secure, and reliable data transfer** between research computing systems. On the SubMIT cluster, we have set up a Globus endpoint, allowing you to move data between your local machine, cloud storage, and SubMIT with ease.

.. note::

   You will need a Globus account to get started. You can register and log in using your MIT credential.

What is Globus?
~~~~~~~~~~~~~~~

Globus is a web-based service designed for transferring and sharing large datasets. It supports:

- High-speed, fault-tolerant transfers
- Direct transfers between endpoints (e.g., SubMIT ⇄ personal computer)
- Sharing data with collaborators
- Managing access permissions securely

The documentation of Globus is at https://docs.globus.org/

Setting up Globus
~~~~~~~~~~~~~~~~~

1. **Log in to Globus**:

   Go to https://www.globus.org/ and click "Log In" using your MIT credential.

2. **Search for the SubMIT Endpoint**:

   After logging in, go to the **File Manager** tab. In one of the search boxes, type ``SubMIT`` to find the endpoint for our cluster.

   .. image:: img/globus1.png
      :alt: Searching SubMIT endpoint
      :scale: 30%

3. **Authenticate to the SubMIT Endpoint**:

   Click on the SubMIT endpoint and authenticate with your MIT credential when prompted.

Transferring Files
~~~~~~~~~~~~~~~~~~

1. **Select Source and Destination**:

   In the File Manager, open two panels:
   - One for your **local machine** (via Globus Connect Personal or another endpoint)
   - One for **SubMIT**

   .. image:: img/globus2.png
      :alt: Dual panel view in Globus
      :scale: 30%

2. **Browse and Select Files**:

   Navigate to the desired directories and select files or folders to transfer.

3. **Click "Start" to Begin the Transfer**:

   Globus will handle the rest. It ensures reliability even if the connection drops, and you can monitor transfer progress in the **Activity** tab.

   .. image:: img/globus3.png
      :alt: Monitor activity
      :scale: 30%

Using Globus Connect Personal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To transfer data to/from your **personal laptop or workstation**, you need to install *Globus Connect Personal*:

1. Download it from: https://www.globus.org/globus-connect-personal
2. Install and log in with your Globus ID (linked with your MIT credential)
3. Set up a local endpoint and give it a name (e.g., "My Laptop")
4. Once running, your machine will appear as an endpoint in the File Manager.

Tips and Best Practices
~~~~~~~~~~~~~~~~~~~~~~~

- Use Globus for transferring **large datasets**, rather than scp or rsync.
- If a transfer fails, you can restart it from where it left off.
- Transfers happen **asynchronously** - you do not need to stay logged in.
- You can receive email notifications for completed or failed transfers.
