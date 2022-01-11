Getting started
---------------

We allow login to the subMIT pool using ssh keys with authentication done through LDAP. Once, you have uploaded your ssh keys, you will also be given a home and work directory in which you can directly start working. This section will guide you on how to set up your ssh keys and upload them to the submit portal to allow login as well as describe the initial resources available to you.

How to get an account
~~~~~~~~~~~~~~~~~~~~~

If you already have a general MIT account then getting access to subMIT is easy. You only need to upload your ssh key to the submit portal below:

#. `submit-portal <https://submit-portal.mit.edu/>`_

You might be prompted for not being authorized to access the portal. Please, follow the instructions on the screen.

If you are not familiar with ssh keys, generating keys is an easy process. To generate keys on your machine use the following command:

.. code-block:: sh

   ssh-keygen

This should create both a private and a public key in your .ssh directory. Simply paste the contents of the public key into the submit portal link above and you are ready.


Login and basic areas
~~~~~~~~~~~~~~~~~~~~~

Now that you can login you can simply ssh into the submit machines like below:

.. code-block:: sh

   ssh <username>@submit.mit.edu

You should now be logged into one of our main submit server machines. By default you will get several areas automatically created for you:

.. code-block:: sh

   # You will start from home which has 5 GB of space
   /home/submit/<username>

   # You will also get a workspace in which to store up to 50 GB of files
   /work/submit/<username>

   # Some users will also get access to hadoop scratch storage amounting to 1 TB
   /mnt/T3_US_MIT/hadoop/scratch/<username>

Creating a personal webpage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the areas above, you have the ability to create a personal webpage in order to store and share your files. In order to create this site you will need a directory named public_html in your home directory:

.. code-block:: sh

  mkdir $HOME/public_html

..
   You then need to out an index.php file in that directory. The index.php can be found below. Make sure you change the username for the includeUrl as well as the directoryUrl.

..
   .. collapse:: A long code block
      
       .. code-block:: php
   
             <?php
             session_start();
             class DirectoryListing {
                     /*
                     ====================================================================================================
                     Evoluted Directory Listing Script - Version 4
                     www.evoluted.net / info@evoluted.net
                     ====================================================================================================
             
                     SYSTEM REQUIREMENTS
                     ====================================================================================================
                     This script requires a PHP version 5.3 or above (5.6 is the recommended minimum) along with the GD
                     library if you wish to use the thumbnail/image preview functionality. For (optional) unzip
                     functionality, you'll need the ZipArchive php extension.
             
                     HOW TO USE
                     ====================================================================================================
                     1) Unzip the provided files.
                     2) Upload the index.php file to the directory you wish to use the script on
                     3) Browse to the directory to see the script in action
                     4) Optionally change any of the settings below
             
                     CONFIGURATION
                     ====================================================================================================
                     You may edit any of the variables in this section to alter how the directory listing script will
                     function. Please read the notes above each variable for details on what they change.
                     */
             
                     // The top level directory where this script is located, or alternatively one of it's sub-directories
                     public $startDirectory = '.';
             
                     // An optional title to show in the address bar and at the top of your page (set to null to leave blank)
                     public $pageTitle = null;
             
                     // The URL of this script. Optionally set if your server is unable to detect the paths of files
                     public $includeUrl = 'http://submit08.mit.edu/~<username>/index.php';
             
                     // If you've enabled the includeUrl parameter above, enter the full url to the directory the index.php file
                     // is located in here, followed by a forward slash.
                     public $directoryUrl = 'http://submit08.mit.edu/~<username>/';
             
                     // Set to true to list all sub-directories and allow them to be browsed
                     public $showSubDirectories = true;
             
                     // Set to true to open all file links in a new browser tab
                     public $openLinksInNewTab = true;
             
                     // Set to true to show thumbnail previews of any images
                     public $showThumbnails = false;
             
                     // Set to true to allow new directories to be created.
                     public $enableDirectoryCreation = false;
             
                     // Set to true to allow file uploads (NOTE: you should set a password if you enable this!)
                     public $enableUploads = false;
             
                     // Enable multi-file uploads (NOTE: This makes use of javascript libraries hosted by Google so an internet connection is required.)
                     public $enableMultiFileUploads = false;
             
                     // Set to true to overwrite files on the server if they have the same name as a file being uploaded
                     public $overwriteOnUpload = false;
             
                     // Set to true to enable file deletion options
                     public $enableFileDeletion = false;
             
                     // Set to true to enable directory deletion options (only available when the directory is empty)
                     public $enableDirectoryDeletion = false;
             
                     // List of all mime types that can be uploaded. Full list of mime types: http://www.iana.org/assignments/media-types/media-types.xhtml
                     public $allowedUploadMimeTypes = array(
                             'image/jpeg',
                             'image/gif',
                             'image/png',
                             'image/bmp',
                             'audio/mpeg',
                             'audio/mp3',
                             'audio/mp4',
                             'audio/x-aac',
                             'audio/x-aiff',
                             'audio/x-ms-wma',
                             'audio/midi',
                             'audio/ogg',
                             'video/ogg',
                             'video/webm',
                             'video/quicktime',
                             'video/x-msvideo',
                             'video/x-flv',
                             'video/h261',
                             'video/h263',
                             'video/h264',
                             'video/jpeg',
                             'text/plain',
                             'text/html',
                             'text/css',
                             'text/csv',
                             'text/calendar',
                             'application/pdf',
                             'application/x-pdf',
                             'application/vnd.openxmlformats-officedocument.wordprocessingml.document', // MS Word (modern)
                             'application/msword',
                             'application/vnd.ms-excel',
                             'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', // MS Excel (modern)
                             'application/zip',
                             'application/x-tar'
                     );
             
                     // Set to true to unzip any zip files that are uploaded (note - will overwrite files of the same name!)
                     public $enableUnzipping = false;
             
                     // If you've enabled unzipping, you can optionally delete the original zip file after its uploaded by setting this to true.
                     public $deleteZipAfterUploading = false;
             
                     // The Evoluted Directory Listing Script uses Bootstrap. By setting this value to true, a nicer theme will be loaded remotely.
                     // Setting this to false will make the directory listing script use the default bootstrap style, loaded locally.
                     public $enableTheme = true;
             
                     // Set to true to require a password be entered before being able to use the script
                     public $passwordProtect = false;
             
                     // The password to require to use this script (only used if $passwordProtect is set to true)
                     public $password = 'CMS';
             
                     // Optional. Allow restricted access only to whitelisted IP addresses
                     public $enableIpWhitelist = false;
             
                     // List of IP's to allow access to the script (only used if $enableIpWhitelist is true)
                     public $ipWhitelist = array(
                             '127.0.0.1'
                     );
             
                     // File extensions to block from showing in the directory listing
                     public $ignoredFileExtensions = array(
                             'php',
                             'ini',
                     );
             
                     // File names to block from showing in the directory listing
                     public $ignoredFileNames = array(
                             '.htaccess',
                             '.DS_Store',
                 'Thumbs.db',
                 '.dropbox',
                     );
             
                     // Directories to block from showing in the directory listing
                     public $ignoredDirectories = array(
             
                     );
             
                     // Files that begin with a dot are usually hidden files. Set this to false if you wish to show these hiden files.
                     public $ignoreDotFiles = true;
             
                     // Works the same way as $ignoreDotFiles but with directories.
                     public $ignoreDotDirectories = true;
             
                     /*
                     ====================================================================================================
                     You shouldn't need to edit anything below this line unless you wish to add functionality to the
                     script. You should only edit this area if you know what you are doing!
                     ====================================================================================================
                     */
                     private $__previewMimeTypes = array(
                             'image/gif',
                             'image/jpeg',
                             'image/png',
                             'image/bmp'
                     );
             
                     private $__currentDirectory = null;
             
                     private $__fileList = array();
             
                     private $__directoryList = array();
             
                     private $__debug = true;
             
                     public $sortBy = 'name';
             
                     public $sortableFields = array(
                             'name',
                             'size',
                             'modified'
                     );
             
                     private $__sortOrder = 'asc';
             
                     public function __construct() {
                             define('DS', '/');
                     }
             
                     public function run() {
                             if ($this->enableIpWhitelist) {
                                     $this->__ipWhitelistCheck();
                             }
             
                             $this->__currentDirectory = $this->startDirectory;
             
                             // Sorting
                             if (isset($_GET['order']) && in_array($_GET['order'], $this->sortableFields)) {
                                     $this->sortBy = $_GET['order'];
                             }
             
                             if (isset($_GET['sort']) && ($_GET['sort'] == 'asc' || $_GET['sort'] == 'desc')) {
                                     $this->__sortOrder = $_GET['sort'];
                             }
             
                             if (isset($_GET['dir']) || isset($_POST['download_dirpath'])) {
                                     if (isset($_GET['delete']) && $this->enableDirectoryDeletion) {
                                             $this->deleteDirectory();
                                     }
             
                   if (isset($_POST['download_dirpath'])) {
                     $this->__currentDirectory = $_POST['download_dirpath'];
                   } else {
                     $this->__currentDirectory = $_GET['dir'];
                   }
                                     return $this->__display();
                             } elseif (isset($_GET['preview'])) {
                                     $this->__generatePreview($_GET['preview']);
                             } else {
                                     return $this->__display();
                             }
                     }
             
                     public function login() {
                             $password = filter_var($_POST['password'], FILTER_SANITIZE_STRING);
             
                             if ($password === $this->password) {
                                     $_SESSION['evdir_loggedin'] = true;
                                     unset($_SESSION['evdir_loginfail']);
                             } else {
                                     $_SESSION['evdir_loginfail'] = true;
                                     unset($_SESSION['evdir_loggedin']);
             
                             }
                     }
             
                     public function upload() {
                             $files = $this->__formatUploadArray($_FILES['upload']);
             
                             if ($this->enableUploads) {
                                     if ($this->enableMultiFileUploads) {
                                             foreach ($files as $file) {
                                                     $status = $this->__processUpload($file);
                                             }
                                     } else {
                                             $file = $files[0];
                                             $status = $this->__processUpload($file);
                                     }
             
                                     return $status;
                             }
                             return false;
                     }
             
                     private function __formatUploadArray($files) {
                             $fileAry = array();
                             $fileCount = count($files['name']);
                             $fileKeys = array_keys($files);
             
                             for ($i = 0; $i < $fileCount; $i++) {
                                     foreach ($fileKeys as $key) {
                                             $fileAry[$i][$key] = $files[$key][$i];
                                     }
                             }
             
                             return $fileAry;
                     }
             
                     private function __processUpload($file) {
                             if (isset($_GET['dir'])) {
                                     $this->__currentDirectory = $_GET['dir'];
                             }
             
                             if (! $this->__currentDirectory) {
                                     $filePath = realpath($this->startDirectory);
                             } else {
                                     $this->__currentDirectory = str_replace('..', '', $this->__currentDirectory);
                                     $this->__currentDirectory = ltrim($this->__currentDirectory, "/");
                                     $filePath = realpath($this->__currentDirectory);
                             }
             
                             $filePath = $filePath . DS . $file['name'];
             
                             if (! empty($file)) {
             
                                     if (! $this->overwriteOnUpload) {
                                             if (file_exists($filePath)) {
                                                     return 2;
                                             }
                                     }
             
                                     if (! in_array($file['type'], $this->allowedUploadMimeTypes)) {
                                             return 3;
                                     }
             
                                     move_uploaded_file($file['tmp_name'], $filePath);
             
                                     if ($file['type'] == 'application/zip' && $this->enableUnzipping && class_exists('ZipArchive')) {
             
                                             $zip = new ZipArchive;
                                             $result = $zip->open($filePath);
                                             $zip->extractTo(realpath($this->__currentDirectory));
                                             $zip->close();
             
                                             if ($this->deleteZipAfterUploading) {
                                                     // Delete the zip file
                                                     unlink($filePath);
                                             }
             
             
                                     }
             
                                     return true;
                             }
                     }
             
                     public function deleteFile() {
                             if (isset($_GET['deleteFile'])) {
                                     $file = $_GET['deleteFile'];
             
                                     // Clean file path
                                     $file = str_replace('..', '', $file);
                                     $file = ltrim($file, "/");
             
                                     // Work out full file path
                                     $filePath = __DIR__ . $this->__currentDirectory . '/' . $file;
             
                                     if (file_exists($filePath) && is_file($filePath)) {
                                             return unlink($filePath);
                                     }
                                     return false;
                             }
                     }
             
                     public function deleteDirectory() {
                             if (isset($_GET['dir'])) {
                                     $dir = $_GET['dir'];
                                     // Clean dir path
                                     $dir = str_replace('..', '', $dir);
                                     $dir = ltrim($dir, "/");
             
                                     // Work out full directory path
                                     $dirPath = __DIR__ . '/' . $dir;
             
                                     if (file_exists($dirPath) && is_dir($dirPath)) {
             
                                             $iterator = new RecursiveDirectoryIterator($dir, RecursiveDirectoryIterator::SKIP_DOTS);
                                             $files = new RecursiveIteratorIterator($iterator, RecursiveIteratorIterator::CHILD_FIRST);
             
                                             foreach ($files as $file) {
                                                     if ($file->isDir()) {
                                                             rmdir($file->getRealPath());
                                                     } else {
                                                             unlink($file->getRealPath());
                                                     }
                                             }
                                             return rmdir($dir);
                                     }
                             }
                             return false;
                     }
             
                     public function createDirectory() {
                             if ($this->enableDirectoryCreation) {
                                     $directoryName = $_POST['directory'];
             
                                     // Convert spaces
                                     $directoryName = str_replace(' ', '_', $directoryName);
             
                                     // Clean up formatting
                                     $directoryName = preg_replace('/[^\w-_]/', '', $directoryName);
             
                                     if (isset($_GET['dir'])) {
                                             $this->__currentDirectory = $_GET['dir'];
                                     }
             
                                     if (! $this->__currentDirectory) {
                                             $filePath = realpath($this->startDirectory);
                                     } else {
                                             $this->__currentDirectory = str_replace('..', '', $this->__currentDirectory);
                                             $filePath = realpath($this->__currentDirectory);
                                     }
             
                                     $filePath = $filePath . DS . strtolower($directoryName);
             
                                     if (file_exists($filePath)) {
                                             return false;
                                     }
             
                                     return mkdir($filePath, 0755);
             
                             }
                             return false;
                     }
             
                     public function sortUrl($sort) {
             
                             // Get current URL parts
                             $urlParts = parse_url($_SERVER['REQUEST_URI']);
             
                             $url = '';
             
                             if (isset($urlParts['scheme'])) {
                                     $url = $urlParts['scheme'] . '://';
                             }
             
                             if (isset($urlParts['host'])) {
                                     $url .= $urlParts['host'];
                             }
             
                             if (isset($urlParts['path'])) {
                                     $url .= $urlParts['path'];
                             }
             
             
                             // Extract query string
                             if (isset($urlParts['query'])) {
                                     $queryString = $urlParts['query'];
             
                                     parse_str($queryString, $queryParts);
             
                                     // work out if we're already sorting by the current heading
                                     if (isset($queryParts['order']) && $queryParts['order'] == $sort) {
                                             // Yes we are, just switch the sort option!
                                             if (isset($queryParts['sort'])) {
                                                     if ($queryParts['sort'] == 'asc') {
                                                             $queryParts['sort'] = 'desc';
                                                     } else {
                                                             $queryParts['sort'] = 'asc';
                                                     }
                                             }
                                     } else {
                                             $queryParts['order'] = $sort;
                                             $queryParts['sort'] = 'asc';
                                     }
             
                                     // Now convert back to a string
                                     $queryString = http_build_query($queryParts);
             
                                     $url .= '?' . $queryString;
                             } else {
                                     $order = 'asc';
                                     if ($sort == $this->sortBy) {
                                             $order = 'desc';
                                     }
                                     $queryString = 'order=' . $sort . '&sort=' . $order;
                                     $url .= '?' . $queryString;
                             }
             
                             return $url;
                     }
             
                     public function sortClass($sort) {
                             $class = $sort . '_';
             
                             if ($this->sortBy == $sort) {
                                     if ($this->__sortOrder == 'desc') {
                                             $class .= 'desc sort_desc';
                                     } else {
                                             $class .= 'asc sort_asc';
                                     }
                             } else {
                                     $class = '';
                             }
                             return $class;
                     }
             
                     private function __ipWhitelistCheck() {
                             // Get the users ip
                             $userIp = $_SERVER['REMOTE_ADDR'];
             
                             if (! in_array($userIp, $this->ipWhitelist)) {
                                     header('HTTP/1.0 403 Forbidden');
                                     die('Your IP address (' . $userIp . ') is not authorized to access this file.');
                             }
                     }
             
                     private function __display() {
                             if ($this->__currentDirectory != '.' && !$this->__endsWith($this->__currentDirectory, DS)) {
                                     $this->__currentDirectory = $this->__currentDirectory . DS;
                             }
             
                             return $this->__loadDirectory($this->__currentDirectory);
                     }
             
                     private function __loadDirectory($path) {
                             $files = $this->__scanDir($path);
             
                             if (! empty($files)) {
                                     // Strip excludes files, directories and filetypes
                                     $files = $this->__cleanFileList($files);
             
                                     foreach ($files as $file) {
                                             $filePath = realpath($this->__currentDirectory . DS . $file);
             
                                             if ($this->__isDirectory($filePath)) {
             
                                                     if (! $this->includeUrl) {
                                                             $urlParts = parse_url($_SERVER['REQUEST_URI']);
             
                                                             $dirUrl = '';
             
                                                             if (isset($urlParts['scheme'])) {
                                                                     $dirUrl = $urlParts['scheme'] . '://';
                                                             }
             
                                                             if (isset($urlParts['host'])) {
                                                                     $dirUrl .= $urlParts['host'];
                                                             }
             
                                                             if (isset($urlParts['path'])) {
                                                                     $dirUrl .= $urlParts['path'];
                                                             }
                                                     } else {
                                                             $dirUrl = $this->directoryUrl;
                                                     }
             
                                                     if ($this->__currentDirectory != '' && $this->__currentDirectory != '.') {
                                                             $dirUrl .= '?dir=' . $this->__currentDirectory . $file;
                                                     } else {
                                                             $dirUrl .= '?dir=' . $file;
                                                     }
             
                                                     $this->__directoryList[$file] = array(
                                                             'name' => $file,
                                                             'path' => $filePath,
                                                             'type' => 'dir',
                                                             'url' => $dirUrl
                                                     );
                                             } else {
                                                     $this->__fileList[$file] = $this->__getFileType($filePath, $this->__currentDirectory . DS . $file);
                                             }
                                     }
                             }
             
                             if (! $this->showSubDirectories) {
                                     $this->__directoryList = null;
                             }
             
                             $data = array(
                                     'currentPath' => $this->__currentDirectory,
                                     'directoryTree' => $this->__getDirectoryTree(),
                                     'files' => $this->__setSorting($this->__fileList),
                                     'directories' => $this->__directoryList,
                                     'requirePassword' => $this->passwordProtect,
                                     'enableUploads' => $this->enableUploads
                             );
             
                             return $data;
                     }
             
                     private function __setSorting($data) {
                             $sortOrder = '';
                             $sortBy = '';
             
                             // Sort the files
                             if ($this->sortBy == 'name') {
                                     function compareByName($a, $b) {
                                             return strnatcasecmp($a['name'], $b['name']);
                                     }
             
                                     usort($data, 'compareByName');
                                     $this->soryBy = 'name';
                             } elseif ($this->sortBy == 'size') {
                                     function compareBySize($a, $b) {
                                             return strnatcasecmp($a['size_bytes'], $b['size_bytes']);
                                     }
             
                                     usort($data, 'compareBySize');
                                     $this->soryBy = 'size';
                             } elseif ($this->sortBy == 'modified') {
                                     function compareByModified($a, $b) {
                                             return strnatcasecmp($a['modified'], $b['modified']);
                                     }
             
                                     usort($data, 'compareByModified');
                                     $this->soryBy = 'modified';
                             }
             
                             if ($this->__sortOrder == 'desc') {
                                     $data = array_reverse($data);
                             }
                             return $data;
                     }
             
                     private function __scanDir($dir) {
                             // Prevent browsing up the directory path.
                             if (strstr($dir, '../')) {
                                     return false;
                             }
             
                             if ($dir == '/') {
                                     $dir = $this->startDirectory;
                                     $this->__currentDirectory = $dir;
                             }
             
                             $strippedDir = str_replace('/', '', $dir);
             
                             $dir = ltrim($dir, "/");
             
                             // Prevent listing blacklisted directories
                             if (in_array($strippedDir, $this->ignoredDirectories)) {
                                     return false;
                             }
             
                             if (! file_exists($dir) || !is_dir($dir)) {
                                     return false;
                             }
             
                             return scandir($dir);
                     }
             
                     private function __cleanFileList($files) {
                             $this->ignoredDirectories[] = '.';
                             $this->ignoredDirectories[] = '..';
             
                             foreach ($files as $key => $file) {
             
                                     // Remove unwanted directories
                                     if ($this->__isDirectory(realpath($file)) && in_array($file, $this->ignoredDirectories)) {
                                             unset($files[$key]);
                                     }
             
                                     // Remove dot directories (if enables)
                                     if ($this->ignoreDotDirectories && substr($file, 0, 1) === '.') {
                                             unset($files[$key]);
                                     }
             
                                     // Remove unwanted files
                                     if (! $this->__isDirectory(realpath($file)) && in_array($file, $this->ignoredFileNames)) {
                                             unset($files[$key]);
                                     }
             
                                     // Remove unwanted file extensions
                                     if (realpath($file) != '' && ! $this->__isDirectory(realpath($file))) {
             
                                             $info = pathinfo($file);
                                             $extension = $info['extension'];
             
                                             if (in_array($extension, $this->ignoredFileExtensions)) {
                                                     unset($files[$key]);
                                             }
             
                                             // If dot files want ignoring, do that next
                                             if ($this->ignoreDotFiles) {
             
                                                     if (substr($file, 0, 1) == '.') {
                                                             unset($files[$key]);
                                                     }
                                             }
                                     }
                             }
                             return $files;
                     }
             
                     private function __isDirectory($file) {
                             if ($file == $this->__currentDirectory . DS . '.' || $file == $this->__currentDirectory . DS . '..') {
                                     return true;
                             }
                             if (filetype($file) == 'dir') {
                                     return true;
                             }
             
                             return false;
                     }
             
                     /**
                      * __getFileType
                      *
                      * Returns the formatted array of file data used for thre directory listing.
                      *
                      * @param  string $filePath Full path to the file
                      * @return array   Array of data for the file
                      */
                     private function __getFileType($filePath, $relativePath = null) {
                             $fi = new finfo(FILEINFO_MIME_TYPE);
             
                             if (! file_exists($filePath)) {
                                     return false;
                             }
             
                             $type = $fi->file($filePath);
             
                             $filePathInfo = pathinfo($filePath);
             
                             $fileSize = filesize($filePath);
             
                             $fileModified = filemtime($filePath);
             
                             $filePreview = false;
             
                             // Check if the file type supports previews
                             if ($this->__supportsPreviews($type) && $this->showThumbnails) {
                                     $filePreview = true;
                             }
             
                             return array(
                                     'name' => $filePathInfo['basename'],
                                     'extension' => $filePathInfo['extension'],
                                     'dir' => $filePathInfo['dirname'],
                                     'path' => $filePath,
                                     'relativePath' => $relativePath,
                                     'size' => $this->__formatSize($fileSize),
                                     'size_bytes' => $fileSize,
                                     'modified' => $fileModified,
                                     'type' => 'file',
                                     'mime' => $type,
                                     'url' => $this->__getUrl($filePathInfo['basename']),
                                     'preview' => $filePreview,
                                     'target' => ($this->openLinksInNewTab ? '_blank' : '_parent')
                             );
                     }
             
                     private function __supportsPreviews($type) {
                             if (in_array($type, $this->__previewMimeTypes)) {
                                     return true;
                             }
                             return false;
                     }
             
                     /**
                      * __getUrl
                      *
                      * Returns the url to the file.
                      *
                      * @param  string $file filename
                      * @return string   url of the file
                      */
                     private function __getUrl($file) {
                             if (! $this->includeUrl) {
                                     $dirUrl = $_SERVER['REQUEST_URI'];
             
                                     $urlParts = parse_url($_SERVER['REQUEST_URI']);
             
                                     $dirUrl = '';
             
                                     if (isset($urlParts['scheme'])) {
                                             $dirUrl = $urlParts['scheme'] . '://';
                                     }
             
                                     if (isset($urlParts['host'])) {
                                             $dirUrl .= $urlParts['host'];
                                     }
             
                                     if (isset($urlParts['path'])) {
                                             $dirUrl .= $urlParts['path'];
                                     }
                             } else {
                                     $dirUrl = $this->directoryUrl;
                             }
             
                             if ($this->__currentDirectory != '.') {
                                     $dirUrl = $dirUrl . $this->__currentDirectory;
                             }
                             return $dirUrl . $file;
                     }
             
                     private function __getDirectoryTree() {
                             $dirString = $this->__currentDirectory;
                             $directoryTree = array();
             
                             $directoryTree['./'] = 'Index';
             
                             if (substr_count($dirString, '/') >= 0) {
                                     $items = explode("/", $dirString);
                                     $items = array_filter($items);
                                     $path = '';
                                     foreach ($items as $item) {
                                             if ($item == '.' || $item == '..') {
                                                     continue;
                                             }
                                             $path .= $item . '/';
                                             $directoryTree[$path] = $item;
             
                                     }
                             }
             
                             $directoryTree = array_filter($directoryTree);
             
                             return $directoryTree;
                     }
             
                     private function __endsWith($haystack, $needle) {
                             return $needle === "" || (($temp = strlen($haystack) - strlen($needle)) >= 0 && strpos($haystack, $needle, $temp) !== false);
                     }
             
                     private function __generatePreview($filePath) {
                             $file = $this->__getFileType($filePath);
             
                             if ($file['mime'] == 'image/jpeg') {
                                     $image = imagecreatefromjpeg($file['path']);
                             } elseif ($file['mime'] == 'image/png') {
                                     $image = imagecreatefrompng($file['path']);
                             } elseif ($file['mime'] == 'image/gif') {
                                     $image = imagecreatefromgif($file['path']);
                             } else {
                                     die();
                             }
             
                             $oldX = imageSX($image);
                             $oldY = imageSY($image);
             
                             $newW = 250;
                             $newH = 250;
             
                             if ($oldX > $oldY) {
                                     $thumbW = $newW;
                                     $thumbH = $oldY * ($newH / $oldX);
                             }
                             if ($oldX < $oldY) {
                                     $thumbW = $oldX * ($newW / $oldY);
                                     $thumbH = $newH;
                             }
                             if ($oldX == $oldY) {
                                     $thumbW = $newW;
                                     $thumbH = $newW;
                             }
             
                             header('Content-Type: ' . $file['mime']);
             
                             $newImg = ImageCreateTrueColor($thumbW, $thumbH);
             
                             imagecopyresampled($newImg, $image, 0, 0, 0, 0, $thumbW, $thumbH, $oldX, $oldY);
             
                             if ($file['mime'] == 'image/jpeg') {
                                     imagejpeg($newImg);
                             } elseif ($file['mime'] == 'image/png') {
                                     imagepng($newImg);
                             } elseif ($file['mime'] == 'image/gif') {
                                     imagegif($newImg);
                             }
                             imagedestroy($newImg);
                             die();
                     }
             
                     private function __formatSize($bytes) {
                             $units = array('B', 'KB', 'MB', 'GB', 'TB');
             
                             $bytes = max($bytes, 0);
                             $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
                             $pow = min($pow, count($units) - 1);
             
                             $bytes /= pow(1024, $pow);
             
                             return round($bytes, 2) . ' ' . $units[$pow];
                     }
             
             }
             
             $listing = new DirectoryListing();
             
             $successMsg = null;
             $errorMsg = null;
             
             if (isset($_POST['password'])) {
                     $listing->login();
             
                     if (isset($_SESSION['evdir_loginfail'])) {
                             $errorMsg = 'Login Failed! Please check you entered the correct password an try again.';
                             unset($_SESSION['evdir_loginfail']);
                     }
             
             } elseif (isset($_FILES['upload'])) {
                     $uploadStatus = $listing->upload();
                     if ($uploadStatus == 1) {
                             $successMsg = 'Your file was successfully uploaded!';
                     } elseif ($uploadStatus == 2) {
                             $errorMsg = 'Your file could not be uploaded. A file with that name already exists.';
                     } elseif ($uploadStatus == 3) {
                             $errorMsg = 'Your file could not be uploaded as the file type is blocked.';
                     }
             } elseif (isset($_POST['directory'])) {
                     if ($listing->createDirectory()) {
                             $successMsg = 'Directory Created!';
                     } else {
                             $errorMsg = 'There was a problem creating your directory.';
                     }
             } elseif (isset($_GET['deleteFile']) && $listing->enableFileDeletion) {
                     if ($listing->deleteFile()) {
                             $successMsg = 'The file was successfully deleted!';
                     } else {
                             $errorMsg = 'The selected file could not be deleted. Please check your file permissions and try again.';
                     }
             } elseif (isset($_GET['dir']) && isset($_GET['delete']) && $listing->enableDirectoryDeletion) {
                     if ($listing->deleteDirectory()) {
                             $successMsg = 'The directory was successfully deleted!';
                             unset($_GET['dir']);
                     } else {
                             $errorMsg = 'The selected directory could not be deleted. Please check your file permissions and try again.';
                     }
             }
             
             $data = $listing->run();
             
             function pr($data, $die = false) {
                     echo '<pre>';
                     print_r($data);
                     echo '</pre>';
             
                     if ($die) {
                             die();
                     }
             }
             ?>
             <html>
             <head>
                     <title><?php echo $data['currentPath'] . (!empty($listing->pageTitle) ? ' (' . $listing->pageTitle . ')' : null); ?> | Benedikt Maier</title>
                     <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; minimum-scale=1.0; user-scalable=no; target-densityDpi=device-dpi" />
                     <style>
                     </style>
                     <?php if($listing->enableTheme): ?>
                     <link href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.5/yeti/bootstrap.min.css" rel="stylesheet" integrity="sha256-gJ9rCvTS5xodBImuaUYf1WfbdDKq54HCPz9wk8spvGs= sha512-weqt+X3kGDDAW9V32W7bWc6aSNCMGNQsdOpfJJz/qD/Yhp+kNeR+YyvvWojJ+afETB31L0C4eO0pcygxfTgjgw==" crossorigin="anonymous">
                     <?php endif; ?>
             </head>
             <body>
                     <div class="container-fluid">
                             <?php if (! empty($listing->pageTitle)): ?>
                                     <div class="row">
                                             <div class="col-xs-12">
                                                     <h1 class="text-center"><?php echo $listing->pageTitle; ?></h1>
                                             </div>
                                     </div>
                             <?php endif; ?>
             
                             <?php if (! empty($successMsg)): ?>
                                     <div class="alert alert-success"><?php echo $successMsg; ?></div>
                             <?php endif; ?>
             
                             <?php if (! empty($errorMsg)): ?>
                                     <div class="alert alert-danger"><?php echo $errorMsg; ?></div>
                             <?php endif; ?>
             
             
                             <?php if ($data['requirePassword'] && !isset($_SESSION['evdir_loggedin'])): ?>
             
                                     <div class="row">
                                             <div class="col-xs-12">
                                             <hr>
                                                     <form action="" method="post" class="text-center form-inline">
                                                             <div class="form-group">
                                                                     <label for="password">What experiment do you work for? </label>
                                                                     <input type="password" name="password" class="form-control">
                                                                     <button type="submit" class="btn btn-primary">Login</button>
                                                             </div>
                                                     </form>
                                             </div>
                                     </div>
             
                             <?php else: ?>
             
                                     <?php if(! empty($data['directoryTree'])): ?>
                                             <div class="row">
                                                     <div class="col-xs-12">
                                                             <ul class="breadcrumb">
                                                             <?php foreach ($data['directoryTree'] as $url => $name): ?>
                                                                     <li>
                                                                             <?php
                                                                             $lastItem = end($data['directoryTree']);
                                                                             if($name === $lastItem):
                                                                                     echo $name;
                                                                             else:
                                                                             ?>
                                                                                     <a href="?dir=<?php echo $url; ?>">
                                                                                             <?php echo $name; ?>
                                                                                     </a>
                                                                             <?php
                                                                             endif;
                                                                             ?>
                                                                     </li>
                         <?php endforeach; ?>
                           <li>
                             <a href=<?php echo str_replace('/?','/view.php?',str_replace('index','view',"http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]"));?> >
                               [browse gallery]
                             </a>
                           </li>
                                                             </ul>
                                                     </div>
                                             </div>
                                     <?php endif; ?>
             
                   <?php 
                             $regex = ".*"; 
                             if (!empty($_GET["regex"])) {
                               $regex = $_GET["regex"];
                             }
             
                             $download_regex = $regex; 
                             if (!empty($_POST["download_regex"])) {
                               $download_regex = $_POST["download_regex"];
                               $base_regex = $_POST["base_regex"];
                             }
                             if (isset($_POST["download_files"]) && $_POST["download_files"] == "Download files") {
                               $rootPath = realpath($_POST["download_dirpath"]);
                               $tarPath = sys_get_temp_dir(). DS . $_POST["download_name"] . '.tar';
                               $gzPath = $tarPath . '.gz';
                               unlink($tarPath); unlink($gzPath);
                               $phar = new PharData($tarPath);
                               foreach ($data['files'] as $file) {
                                 if (preg_match("/" . $download_regex . "/",$file['name'])) 
                                 {
                                   $filePath = realpath($_POST["download_dirpath"] . DS . $file['name']);
                                   $relativePath = $_POST["download_name"] . DS . substr($filePath,strlen($rootPath)+1);
                                   $ret = $phar->addFile($filePath,$relativePath);
                                   $ret = file_exists($filePath);
                                 }
                               }
             
                               $phar->compress(Phar::GZ);
             
                               ob_end_clean();
                               header("Content-Type: application/x-gzip");
                               header("Content-Length: " . filesize($gzPath));
                               header(sprintf('Content-Disposition: attachment; filename="%s"',addslashes(basename($gzPath))));
                               flush();
                               readfile($gzPath);
                               exit(0);
                             }
                             if (isset($_POST["download_files"]) && $_POST["download_files"] == "Download recursively") {
                               $rootPath = realpath($_POST["download_dirpath"]);
                               $tarPath = sys_get_temp_dir(). DS . $_POST["download_name"] . '.tar';
                               $gzPath = $tarPath . '.gz';
                               unlink($tarPath); unlink($gzPath);
                               $phar = new PharData($tarPath);
                               $phar->buildFromDirectory($data['currentPath']);
             
                               $phar->compress(Phar::GZ);
             
                               ob_end_clean();
                               header("Content-Type: application/x-gzip");
                               header("Content-Length: " . filesize($gzPath));
                               header(sprintf('Content-Disposition: attachment; filename="%s"',addslashes(basename($gzPath))));
                               flush();
                               readfile($gzPath);
                               exit(0);
             
                             }
                   ?>
             
                                             <div class="row">
                                                     <div class="col-xs-12">
                         <div class="breadcrumb">
                               <form method="get" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
                                 <input type="text" name="regex" value=<?php echo $regex; ?>>
                                 <input type="submit" name="submit" value="Filter files">  
                                 <?php
                                   foreach($_GET as $name => $value) {
                                     if ($name!=="regex" && $name!=="submit") {
                                       $value = html_entity_decode($value);
                                       echo '<input type="hidden" name="'. $name .'" value="'. $value .'">';
                                     }
                                   }
                                 ?>
                               </form>
                         </div>
                                                             <div class="breadcrumb">
                               <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
                                 <input type="hidden" name="base_regex" value=<?php echo $regex;?>>
                                 <input type="hidden" name="download_dirpath" value=<?php echo $data['currentPath'];?>>
                                 <input type="text" name="download_regex" value=<?php echo $download_regex; ?>>
                                 <input type="submit" name="download_files" value="Download files">  
                                 <input type="submit" name="download_files" value="Download recursively">  
                                 as <input type="text" name="download_name" value=<?php echo end($data['directoryTree']);?>>.tar.gz
                               </form>
                                                             </div>
                                                     </div>
                                             </div>
             
             
                                             <div class="row">
                                                     <div class="col-xs-12">
                                                             <div class="table-container">
                                                                     <table class="table table-striped table-bordered">
                                                                             <?php if (! empty($data['directories'])): ?>
                                                                                     <thead>
                                                                                             <th>Directory</th>
                                                                                     </thead>
                                                                                     <tbody>
                                                                                             <?php foreach ($data['directories'] as $directory): ?>
                                                                                                     <tr>
                                                                                                             <td>
                                                                                                                     <a href="<?php echo $directory['url']; ?>" class="item dir">
                                                                                                                             <?php echo $directory['name']; ?>
                                                                                                                     </a>
             
                                                                                                                     <?php if ($listing->enableDirectoryDeletion): ?>
                                                                                                                             <span class="pull-right">
                                                                                                                                     <a href="<?php echo $directory['url']; ?>&delete=true" class="btn btn-danger btn-xs" onclick="return confirm('Are you sure?')">Delete</a>
                                                                                                                             </span>
                                                                                                                     <?php endif; ?>
                                                                                                             </td>
             
                                                                                                     </tr>
                                                                                             <?php endforeach; ?>
                                                                                     </tbody>
                                                                             <?php endif; ?>
             
                                                                             <?php if($listing->enableDirectoryCreation): ?>
                                                                             <tfoot>
                                                                                     <tr>
                                                                                             <td>
                                                                                                     <form action="" method="post" class="text-center form-inline">
                                                                                                             <div class="form-group">
                                                                                                                     <label for="directory">Directory Name:</label>
                                                                                                                     <input type="text" name="directory" id="directory" class="form-control">
                                                                                                                     <button type="submit" class="btn btn-primary" name="submit">Create Directory</button>
                                                                                                             </div>
                                                                                                     </form>
                                                                                             </td>
                                                                                     </tr>
                                                                             </tfoot>
                                                                             <?php endif; ?>
                                                                     </table>
                                                             </div>
                                                     </div>
                                             </div>
             
                   <?php if (! empty($data['files'])): ?>
                     <div class="row">
                       <div class="col-xs-12">
                         <div class="table-container">
                           <table class="table table-striped table-bordered">
                             <thead>
                               <tr>
                                 <th></th>
                                 <th></th>
                                 <th></th>
                                 <th>
                                   <a href="<?php echo $listing->sortUrl('name'); ?>">Image <span class="<?php echo $listing->sortClass('name'); ?>"></span></a>
                                 </th>
                                 <th class="text-right sm-hidden">
                                   <a href="<?php echo $listing->sortUrl('modified'); ?>">Last Modified <span class="<?php echo $listing->sortClass('modified'); ?>"></span></a>
                                 </th>
                               </tr>
                             </thead>
                             <tbody>
                             <?php foreach ($data['files'] as $file): ?>
                               <?php if ($file['mime']=='image/png'): ?>
                                 <?php if (preg_match("/" . $regex . "/",$file['name'])): ?>
                                 <tr>
                                   <td>
                                     <a href="<?php echo $file['url']; ?>" target="<?php echo $file['target']; ?>" >
                                       png
                                     </a>
                                   </td>
                                   <td>
                                    <?php if (file_exists(str_replace('png','pdf',$file['path']))): ?>
                                       <a href="<?php echo str_replace('png','pdf',$file['url']); ?>" target="<?php echo $file['target']; ?>" > 
                                           pdf
                                       </a>
                                   <?php endif; ?>
                                   </td>
                                   <td>
                                    <?php if (file_exists(str_replace('png','C',$file['path']))): ?>
                                       <a href="<?php echo str_replace('png','C',$file['url']); ?>" target="<?php echo $file['target']; ?>" > 
                                           C
                                       </a>
                                   <?php endif; ?>
                                   </td>
                                   <td>
                                     <?php if (isset($file['preview']) && $file['preview']): ?>
                                       <span class="preview"><img src="?preview=<?php echo $file['relativePath']; ?>"><i class="preview_icon"></i></span>
                                     <?php endif; ?>
                                       <?php echo str_replace('Minus','-',str_replace('Plus','+',str_replace('Times','X',str_replace('Over','/',str_replace('AND',' && ',str_replace('_',' ',str_replace('.png','',$file['name']))))))); ?>
                                   </td>
                                   <td class="text-right sm-hidden"><?php echo date('M jS Y \a\t g:ia', $file['modified']); ?></td>
                                 </tr>
                                 <?php endif; ?>
                               <?php endif; ?>
                             <?php endforeach; ?>
                             </tbody>
                           </table>
                         </div>
                       </div>
                     </div>
                     <?php else: ?>
                                             <div class="row">
                                                     <div class="col-xs-12">
                                                             <p class="alert alert-info text-center">This directory does not contain any images.</p>
                                                     </div>
                                             </div>
                             <?php endif; ?>
             
                                     <?php if (! empty($data['files'])): ?>
                                             <div class="row">
                                                     <div class="col-xs-12">
                                                             <div class="table-container">
                                                                     <table class="table table-striped table-bordered">
                                                                             <thead>
                                                                                     <tr>
                                                                                             <th>
                                                                                                     <a href="<?php echo $listing->sortUrl('name'); ?>">File <span class="<?php echo $listing->sortClass('name'); ?>"></span></a>
                                                                                             </th>
                                                                                             <th class="text-right xs-hidden">
                                                                                                     <a href="<?php echo $listing->sortUrl('size'); ?>">Size <span class="<?php echo $listing->sortClass('size'); ?>"></span></a>
                                                                                             </th>
                                                                                             <th class="text-right sm-hidden">
                                                                                                     <a href="<?php echo $listing->sortUrl('modified'); ?>">Last Modified <span class="<?php echo $listing->sortClass('modified'); ?>"></span></a>
                                                                                             </th>
                                                                                     </tr>
                                                                             </thead>
                                                                             <tbody>
                                                                             <?php foreach ($data['files'] as $file): ?>
                                 <?php if (preg_match("/" . $regex . "/",$file['name'])): ?>
                                                                                     <tr>
                                                                                             <td>
                                                                                                     <a href="<?php echo $file['url']; ?>" target="<?php echo $file['target']; ?>" class="item _blank <?php echo $file['extension']; ?>">
                                                                                                             <?php echo $file['name']; ?>
                                                                                                     </a>
                                                                                                     <?php if (isset($file['preview']) && $file['preview']): ?>
                                                                                                             <span class="preview"><img src="?preview=<?php echo $file['relativePath']; ?>"><i class="preview_icon"></i></span>
                                                                                                     <?php endif; ?>
                                                                                                     <?php if ($listing->enableFileDeletion == true): ?>
                                                                                                             <a href="?deleteFile=<?php echo urlencode($file['relativePath']); ?>" class="pull-right btn btn-danger btn-xs" onclick="return confirm('Are you sure?')">Delete</a>
                                                                                                     <?php endif; ?>
                                                                                             </td>
                                                                                             <td class="text-right xs-hidden"><?php echo $file['size']; ?></td>
                                                                                             <td class="text-right sm-hidden"><?php echo date('M jS Y \a\t g:ia', $file['modified']); ?></td>
                                                                                     </tr>
                                 <?php endif; ?>
                                                                             <?php endforeach; ?>
                                                                             </tbody>
                                                                     </table>
                                                             </div>
                                                     </div>
                                             </div>
                                     <?php else: ?>
                                             <div class="row">
                                                     <div class="col-xs-12">
                                                             <p class="alert alert-info text-center">This directory does not contain any files.</p>
                                                     </div>
                                             </div>
                                     <?php endif; ?>
                             <?php endif; ?>
                     </div>
                     <style>
                     </style>
                     <?php if ($listing->enableMultiFileUploads): ?>
                             <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
                             <script>
                                     $('button[name=add_file]').on('click', function(e) {
                                             e.preventDefault();
                                             $('.upload-field:last').clone().insertAfter('.upload-field:last').find('input').val('');
             
                                     });
                             </script>
                     <?php endif; ?>
             </body>
             </html>

Once that is created, you can now access your personal webpage here after changing to your username:

#. `personal webpage <http://submit08.mit.edu/~username/>`_

The rules for an account
~~~~~~~~~~~~~~~~~~~~~~~~

Remember that these machines are shared. As such, do not max out resources on interactive jobs. As a guideline: If your job takes langer than 15 minutes it makes sense to dispatch it to a batch system. The machines in this login pool are connected to large computing clusters which are accessed by batch programs like HTCondor or Slurm. There are tutorials for these tools later in this guide.  
