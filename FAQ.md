# Frequently Asked Question catalog

The Tier-2 computing center is located at the High Performance Research Computing Facility at Bates. It is a resource with close to twenty thousand computing slots and about eight petabyte of storage space. The facility is mostly used by LHC experiments (CMS, LHCb) but some resources are available to the LNS community. Also other experiments, like CLAS12 recently, have bought hardware which is seamlessly included in the center. The maintance of the resources is taken care of at Bates. These resources can be accessed through the subMIT computing infrastructure, where jobs are prepared and submitted for execution.

The [github repository](https://github.com/mit-submit/submit-examples) summarizes a number of simple examples and the presentations at our [recent workshop](https://indico.cern.ch/event/999848) go through a number in-depth examples of more experienced users and include detailed explanation and discussion of applications of new or simply interested users.

The workshop brought up a number of questions which we summarize here and will continue to maintain.

### How to get an account

To make login convenient and secure we allow login to the subMIT pool using ssh keys only. Users of submit can go to our submit portal to upload their ssh key (or a number of keys). Upload of ssh keys is secured through MIT touchstone authentication. This means users need to have an MIT account.


It is very straight forward to obtain an MIT guest account if you do not have one. A sponsor - usually a faculty you are working with - can request a guest account for you. The information needed is the first, last name and the birthday. See the [sponsoring web page](https://ist.mit.edu/guest-accounts). Please note: the process has to be started by the sponsor! The response by MIT IS&T has been very quick in the past, we have so far received all account requests in less than 4 hours.

### Can I use a different version of the c++ compiler (gcc)?

There are many different versions of various packages available and distributed through our CVMFS file system. The c++ compiler in its gcc implementation in particular. Try out the following list command to see what is available:

       ls /cvmfs/sft.cern.ch/lcg/contrib/gcc

There are packaged versions for the various standard linux releases. To setup gcc version 11 for the present installation of our subMIT system you would do the following:

       source /cvmfs/sft.cern.ch/lcg/contrib/gcc/11/x86_64-centos7/setup.sh

### Does the subMIT setup support "MPI"?

The short answer to this question is no. There are two limitations to using MPI on the computing Tier-2 computing center at Bates. First, there is limited interconnectivity between worker nodes (typically 1 Gb/sec = "weak coupling") and secondly our batch system (HTCondor) does not support the allocation of several workernodes in parallel. Condor could be set up to use MPI but we don’t do this because MPI would not run efficiently.

If needed we can set up a job to use order of 40 cores on one machine but this would need to be carefully coordinated.

### Can one mount a Docker file via Singularity?

Docker containtainers can be loaded via singularity and there is a lot of information at OSG sites on how to properly do this [here](https://support.opensciencegrid.org/support/solutions/articles/12000024676).

### Does CVFMS have a local MIT server or global?

MIT has both the global CVMFS servers are all available and we also maintain a local CVMFS infrastructure that we manage internally, but this server is also only availble at he local sites (MIT).

### Are WM allocated one per job, or is it possible that multiple jobs share the node

One node can have multiple jobs run on it.  Each job runs in its own area so they don’t interfere

### Can we freely access the large storage space?

We currently support each user to have 1TB of free space on our disks. Groups can request more space to be made available in a shared area. If more storage is needed, please reach out to the SubMIT team; depending on the quantity, some contribution to the project's funds to purchase new disks for storage may be arranged.

### Independently, when a job is submitted to OSG, does it have any higher priority compared to directly accessing OSG resource by their login nodes?

You can change which clusters you wanna access by changing a line in the condor submit requirements. you can also connect them with logical OR if you don’t care priorities at OSG are difficult to predict because they depend on a number of parameters generally we expect priorities to be very similar.

### Is there a preference between using a simple submit script and a DAGman?

One condor_submit script is the simplest and in many cases sufficient solution for your task. DAGman gives you more options but is also more complicated.

### How do you guarantee the worker nodes you submit to have my software (ex. Julia) installed?

If some of the worker nodes do not have the proper software installed (ex. Julia) this needs to be brought to the attention of the system administrators so the problem can be fixed. This should not be the case though. A quick patch if this only applies to few machines, would be to submit twice as many jobs as needed to have enough output in case half fail or explicitely exclude the failing worker nodes by using the requirements.

A much better solution is to use a [singularity image which has your software installed (ex. julia)](https://support.opensciencegrid.org/support/solutions/articles/12000073449) installed. This means any machine will have your software (ex. Julia) through the mounted CVMFS image. The main failure mode then would be that the CVMFS mount fails.

### What happens if a job fails?

Look at the error and output files -- they generally have enough information to debug. Sometimes it is hard to track down what happens and a simple re-submission might do the trick.

### Can one resubmit a job automatically?

It is possible, but you would not want this to be automatic because it could go into an infinite loop. Some software exists but is application-specific. DAGman produces rescue files and can restart from a failed state.

### Why do some jobs fail on certain machines?

Generally worker nodes are supposed to be interchangable but sometimes they are not. Failures are often because of local miconfigurations or failed services. In other cases worker nodes are in fact different.

As an example, some of our machines are over 10 years old and do not support SSE4 instructions. The library might be available on such old machines but it does no provide the assembly instructions needed to execute the given library. You can add a requirement for SSE4 instructions to be present on the workers were your job is executed:

   requirements = has_sse4_1 && ...

### Who has access to the GPUs on subMIT?

Anyone who has access to subMIT can submit to BOSCOGroup to get GPU access. For now the number of GPU slots available is limited but we are working on purchasing more GPU enabled machines.

### Could there be an LNS Slack cluster channel to ask questions?

There is a Slack for subMIT with a "help-desk" channel but it is not yet open to everyone. We will make this open to everyone if there is interest so users can help each other and only elevate to higher-ups if necessary

### Is there a resource to look up nodes and memory resources?

All nodes have are guaranteed to provide at least 2 GB per compute slot. We do have some machines that provide at least 3 GB
per slot. Those limits are not strictly enforced but it is wise not to go over those limits by to much because it can cause entire machines to fail.

### Does anyone do ML at MIT right now, and what resources are you currently using?

Complete hodgepodge of places to get GPUs -- pain to deal with all these: Lincoln Lab computers, Satori ....

### Is there a difference between using Condor to submit 100 jobs at once and just submitting the 100 jobs individually?

The syntax is different and it usually takes longer to submit jobs one-by-one but if the setup is correct the results are identical.

### What is the best procedure to tell someone that a certain folder should be synchronized?

We are presently re-organizing our CVMFS server where areas will be automatically distributed. Each user will have access to at least one user group and will be able to copy data into areas which are automatically mirrored into the CVMFS server.

Typicallyit takes 40 minutes for folders to be synchronized to CVMFS and thus be available on each worker node. This may change in the future. Questions will be manged through our slack channel.

### How do we move files around? Is there a better solution than copying around SSH keys that does not involve buying a hard drive?

The solution depends on how much space is needed. For O(100 GB), people should be given space on our mass storage that is accessible to worker nodes. For small amounts of storage like this, discussing this wastes more money (in terms of labor costs) than the disk would cost.

GridFTP is a more secure way to copy files instead of using SSH keys, but it requires an OSG certificate or something equivalent. One can apply for a certificate which also allows other things, like submitting to other clusters.

### What applications might require >2 GB of RAM?

Lattice QCD, IceCube simulations took several GB, even after splitting up the runs into smaller ones, ....

### Are there constraints on cores available, especially given the 24 hour limit?

Most cores/node is 48 (with 2 GB each). Memory is not physically assigned to a specific core (machine has a bunch of memory combined that is allocated to specific cores). Memory is not strictly enforced but jobs can be killed if they use too much.

Failure modes with memory starvation can lead to worker nodes dieing and the node has to be power cycled. This will automatically trigger an investigation into what went wrong. Do not spawn multiple jobs to try to get more resources, since this can quickly lead to the entire cluster crashing. Always test a few dozen jobs or so before trying to run several thousand. If you submit from submit.mit.edu, jobs will be automatically monitored for excessive memory usage and will be killed if they use too much.

Our computing centers are production clusters (running close to 24/7), so people will be unhappy if you crash the cluster.

### Is there a way to see the attributes of the worker nodes in an overview to optimize usage on submit.mit.edu?

_this answer needs to be completely reworked_

There is an intermediate machine, so it’s not possible to see machine attributes directly. One really only needs to check user inputs against machine attributes. One solution: submit a test job and use this to get information about target machine

### Is there a per-user limit on concurrently running jobs?

Short answer is 'no', but you will usually not get all slots on a specific machine (jobs are farmed out to random machines).
One can configure a part of the cluster where jobs accumulate on specific machines, but this is not currently set up.

### Does condor support job dependency?

DAGman will do this [see Spencer’s talk](https://indico.cern.ch/event/999848/contributions/4208731/) I set the requirements as

       requirements = BOSCOGroup == "bosco_reserve" && BOSCOCluster == "ce03.cmsaf.mit.edu"

and use the GPU example “condor_tensorflow.py”. I got “lbgpu0001.cmsaf.mit.edu \n False”.

### Should I set some environments before I use this example?

See examples in GitHub (https://github.com/mit-submit/submit-examples/blob/main/condor_gpu/condor.sub)

### How do I use gfal tools on submit?

Setup gfal tools from CVMFS:

       source /cvmfs/grid.cern.ch/centos7-ui-test/etc/profile.d/setup-c7-ui-example.sh
       
### How to request large storage space on Tier2 cluster?
Users who work on CMS, LHCb, Clas12 experiments are guaranteed space in Tier2 storage as those experiments made contributations to the hardware.
Other LNS or CTP groups could have space allocated even though it would be limited to a couple of terabytes.

First you need to obtain a grid certificate either through your own experiment/collaboration, or get one from OSG (Open Science Grid) as described [here](https://opensciencegrid.org/docs/security/user-certs/).
There are various authorities that can issue grid certificates, MIT is not one of them. If you see something like this as an output
of voms-proxy-info command

       identity  : /DC=org/DC=cilogon/C=US/O=Massachusetts Institute of Technology/

it means you converted the wrong certificate into the pem format.

After you have created a proxy send an e-mail to maxi@mit.edu including the output of the

       voms-proxy-info -all

command. Please do not forget to cc the leader of your LNS research group. Please also say what experiment you work on.
Your request will be handled and the results will be e-mailed back.

To be able to access this directory you have to use gfal tools which are described [here](http://submit.mit.edu/tips.html#tier2).
There is a low limit on the size of the files that can be written into the storage. Anything below 100 MBs is considered to be bad 
for storage.

