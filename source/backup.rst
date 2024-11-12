Data backup
-----------

In this section we will to discuss the backup policy of subMIT. In short, the only space that has a conventional backup is the home directory for users (/home/submit). The directories under work (/work/submit) and data (/ceph/submit/data) have intrinsic resilience by raiding and erasure coding but are not backed up. The subMIT team is making its best effort to keep data safe but due to the size a full backup is not feasible.

If there is a particular emergency situation involving backups please contact submit-help@mit.edu.


Home directory backup
~~~~~~~~~~~~~~~~~~~~~

The home directories are completely backed up every Sunday early morning (~3am).

Every other day than Sunday an incremental backup of only files newer than the last backup will be stored. This means you can always recover files within the last 24 hours and up to one week ago.

There is also one more complete backup from longer ago which is occasionally reset.

The backup is stored on submit07.mit.edu and thus best retrieved from that machine. Users can access the files normally because they are created with the permissions based on the users permission.

Restoring files
~~~~~~~~~~~~~~~
	  
**WARNING**

Generally speaking if you have a major issue of accidental file deletions or such we would be glad to support you to best retrieve those files. Touching the backup yourself might cause more issues because in principle you have permissions to delete your backup files. Once those are broken we cannot help you anymore.

**WARNING**

Use the following syntax to restore the latest version of the given file from the backup after you have logged in to **submit07.mit.edu**:

   retrieve_backup.sh <user>/<myFile>

If <myFile> is a directory the complete directory is restored. Be careful that there is enough space in /tmp because the backup is restored into /tmp/....
