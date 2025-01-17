Tutorial 2: Batch Job (HTCondor and Slurm)
------------------------------------------

.. tags:: Slurm, Condor, GPU

This Tutorial describes several options to set up your batch computing jobs from subMIT to HTCondor and Slurm.

See the relevant sections in the User's Guide for `HTCondor <https://submit.mit.edu/submit-users-guide/running.html#id1>`_ and `Slurm <https://submit.mit.edu/submit-users-guide/running.html#id2>`_ for more information.

HTCondor
~~~~~~~~

This section will show you several ways to submit jobs through HTCondor.
Here, you can see how to form your condor submission to control your jobs.
A very simple example is shown below with several more complex examples afterwards.

A simple example
................

Let's start with a very simple script.
Let's run the following script in the HTCondor job.
Let's call it script.sh. 

.. code-block:: sh

      #!/bin/bash

      echo "I am a HTCondor job!"
      echo "I have landed in $hostname"
      echo "I have recieved parameter $1"
      echo "That's all!"

and the corresponding condor.sub file to run it on the T3. 

.. code-block:: sh

      universe              = vanilla
      request_disk          = 1024
      executable            = script.sh
      arguments             = $(ProcId)
      output                = $(ClusterId).$(ProcId).out
      error                 = $(ClusterId).$(ProcId).err
      log                   = $(ClusterId).$(ProcId).log
      +DESIRED_Sites        = "mit_tier3"
      queue 1

This submission script submit a single (`queue 1`) job, with `$(ProcID)=0` to the MIT T3 that will execute `script.sh`, and will produce log, output, and error files in your local directory.

Now you can submit your job:

.. code-block:: sh

      condor_submit condor.sub

After you have submitted your jobs, it is important to be able to monitor their progress.

The first step in monitoring jobs is to check which jobs are running. This can be done with the command below:

.. code-block:: sh

       # This will show the number of jobs in the Done, Running and Idle states
       condor_q

       # If you want more information about a job you can look into it here
       condor_q -l <jobid> 

       # If you are interested in knowing which machines your jobs are running on you can examine that as well
       condor_q -r <jobid>

Jobs can often stay in the Idle state or be moved into a Hold state. In order to analyze this you can use the analyze of condor.

.. code-block:: sh

       # Check on the status of a job if it is stuck in Idle or moved to Hold
       condor_q -analyze <jobid>

       # If more information is needed
       condor_q -better-analyze <jobid> 

If you made a mistake during submission, you can also cancel your jobs. This should be done if any mistakes were made in order to free up the queue.

.. code-block:: sh

       # You can remove a broken job
       condor_rm <jobid>

       # If you want to remove all of your jobs
       condor_rm <username>

Once the job runs, you can check the `.out` file for the expected output.

Congratulations! You have submitted your first batch computing jobs on HTCondor. Let's complicate this a bit now!

A more complicated example
..........................

We now want to run a simple python script that takes as input, and run it over many inputs.

Here is the python script.
Save it to a file called `analyze.py`.

.. code-block:: python

      import sys

      def main():
          if len(sys.argv) != 2:
              print("Usage: python script.py <argument>")
              sys.exit(1)
          
          arg = sys.argv[1]
          print(f"Processing argument: {arg}")
          # Simulate some work
          result = int(arg) ** 2
          print(f"Result for {arg}: {result}")
      
      if __name__ == "__main__":
          main()

The shell script that executes this is as follows.
Save it to a file called `run_analysis.sh`.

.. code-block:: sh

      #!/bin/bash

      echo "I am a HTCondor job!"
      echo "I have landed in $hostname"
      echo "I have recieved parameter $1"
      echo "I will now run: python analyze.py $1"
      python analyze.py $1
      echo "That's all!"

We want to run over a whole list of inputs.
Let's write those to a file, called `inputs.txt`

.. code-block:: sh

      0
      1
      1
      2
      3
      5
      8
      13
      21
      34
      55
      89

In our submission scrpit, we can now queue one job per input, and pass to each job the input as an argument.
We pass both the python and the shell scripts to the worker-node, so that it can execute them.

.. code-block:: sh

      universe              = vanilla
      executable            = run_analysis.sh
      arguments             = $(arg)
      transfer_input_files  = script.py, run_script.sh
      output                = output_$(arg).txt
      error                 = error_$(arg).txt
      log                   = log_$(arg).txt
      +DESIRED_Sites        = "mit_tier3"
      queue arg from inputs.txt

Try running this, and make sure that everything worked!

We can now move on to a more realistic example.

A realistic example
...................

We have for now neglected the software environment of the job, tacitly assuming that whatever OS, libraries, and python versions existed on the worker-nodes were sufficient and acceptable.
More typically, you will want to operate in an homogenous environment that you understand (or even control), and will need some particular software that is not natively installed on the worker-nodes.
We provide an example for how to do this with singularity, but you can check out the User's Guide section on `containers <https://submit.mit.edu/submit-users-guide/program.html>`_ and `HTCondor <https://submit.mit.edu/submit-users-guide/running.html#id1>`_ for alternatives and more details.

This is the script we want to run now.

.. code-block:: python

      import sys
      import numpy as np
      
      def main():
          if len(sys.argv) != 2:
              print("Usage: python script.py <argument>")
              sys.exit(1)
          
          # Get the input argument
          arg = int(sys.argv[1])
          
          # Generate a NumPy array based on the input
          array = np.linspace(0, arg, num=10)
          
          # Perform some calculations
          squared = array**2
          summed = np.sum(squared)
          
          # Save results to a file
          output_file = f"result_{arg}.txt"
          with open(output_file, "w") as f:
              f.write(f"Input: {arg}\n")
              f.write(f"Array: {array.tolist()}\n")
              f.write(f"Squared: {squared.tolist()}\n")
              f.write(f"Sum of squares: {summed}\n")
          
          print(f"Results for input {arg} written to {output_file}")
      
      if __name__ == "__main__":
          main()

In order to ensure a consistent environment across worker-nodes and ensure we have a consistent and particular version of python and libraries like numpy, we use a singularity container.
We can do this by specifying it in our submission script,

.. code-block:: sh

      +SingularityImage     = "/cvmfs/singularity.opensciencegrid.org/htc/rocky\:9"

We have picked a standard singularity image that provides a rocky9 distribution with some basic software like python already installed.
You can play around with this singularity on subMIT to make sure our python script works there.

.. code-block:: sh

      singularity shell /cvmfs/singularity.opensciencegrid.org/htc/rocky\:9
      Apptainer> python3 analyze.py

Finally, we want to transfer the output file of the python script using XRootD to our ceph space on subMIT.
We can do this with the following,

.. code-block:: sh

      #!/bin/bash

      echo "I am a HTCondor job!"
      echo "I have landed in $hostname"
      echo "I am supposed to be inside a singularity container: $APPTAINER_NAME"
      echo "I have recieved parameter $1"
      echo "I will now run: python analyze.py $1"
      python analyze.py $1
      echo "Transferring output: xrcdp result_$1.txt root://submit50.mit.edu//data/user/<your path>/"
      export X509_USER_PROXY=x509
      xrcdp result_$1.txt root://submit50.mit.edu//data/user/<your path>/
      echo "That's all!"

However, in order to use XRootD, we need to pass our x509 key to the job.
(See the `User's Guide <https://submit.mit.edu/submit-users-guide/storage.html#the-storage-filesystem>`_ for how to set up the authentication for the first time.)
On subMIT, initialize your x509 proxy and put it somewhere accessible. We do this by setting the environment variable `X509_USER_PROXY`,

.. code-block:: sh
      
      export X509_USER_PROXY="/home/submit/$USER/x509"
      voms-proxy-init --valid 100:00:00

The final submission script will look like,

.. code-block:: sh

      universe              = vanilla
      executable            = run_analysis.sh
      arguments             = $(arg)
      transfer_input_files  = script.py, run_script.sh,/home/submit/$USER/x509
      output                = output_$(arg).txt
      error                 = error_$(arg).txt
      log                   = log_$(arg).txt
      +SingularityImage     = "/cvmfs/singularity.opensciencegrid.org/htc/rocky\:9"
      +DESIRED_Sites        = "mit_tier2,mit_tier3"
      queue arg from inputs.txt

Congratulations! You are ready to submit real HTCondor jobs now!

Slurm:
~~~~~~

Slurm works on the Submit machines themselves, or on LQCD machines at MIT. Unlike HTCondor, ``/home/submit``, ``/work/submit``, and ``/data/submit`` are all mounted across all machines available to you on slurm. 

Below is a sample about how to submit a slurm job to the submit machines. Save the following into a file named ``submit.sh``.

.. code-block:: sh

      #!/bin/bash
      #
      #SBATCH --job-name=test
      #SBATCH --output=res_%j.txt
      #SBATCH --error=err_%j.txt
      #
      #SBATCH --time=10:00
      #SBATCH --mem-per-cpu=100
      
      srun hostname
      srun ls -hrlt

The following can then be run below

.. code-block:: sh

       sbatch submit.sh

Controlling/Analyzing Jobs:
...........................

Similar to HTCondor, Slurm has command line options to monitor and control your jobs. This section gives a couple of simple examples on how to monitor your slurm jobs on submit.

The first step in monitoring jobs is to check which jobs are running. This can be done with the command below:

.. code-block:: sh

       # This will show the number of jobs and their states.
       squeue -u <username>

       # You can also ask for the jobs on the different clusters with the -M option. You can also use a specific cluster (e.g. submit, lqcd).
       squeue -M all -u <username>

In order to analyze your jobs you can use the scontrol feature of slurm.

.. code-block:: sh

       # Check on the status of a job
       scontrol show jobid -dd <jobid>

       # If more information is needed
       sstat --jobs=<jobid> 

       # A more organized way to look at this information is through the format option. In order to see all options use --helpformat. An example is below
       sstat --jobs=<jobid> --format=jobid,maxrss,ntasks

If you made a mistake during submission, you can also cancel your jobs. This should be done if any mistakes were made in order to free up the queue.

.. code-block:: sh

       # You can remove a broken job
       scancel <jobid>

       # If you want to remove all of your jobs
       scancel -u <username>

       # If need be you can also change the state of the job with scontrol to suspend, remove, hold or release
       scontrol suspend <jobid>

Slurm also has the sacct command to help you to look at information from past jobs. These commands are similar to the sstat commands but are used for jobs that have finished rather than jobs currently running.

.. code-block:: sh

       # Look at information from your hobs after they have finished running. You can use the --long to get the non-abbreviated version
       sacct --jobs=<jobid> --long

       # Look at all of your recent jobs
       sacct --user=<username>

       # You can also use the format options to get specific information in the same way that sstat was used above
       sacct --jobs=<jobid> --format=jobid,maxrss,ntasks

       # A nice summary of a job is available through the seff command
       seff <jobid>

Submit:
.......

The default is to run on submit. If you would like to specify, you can add the following to the submit.sh

.. code-block:: sh

     #SBATCH --partition=submit

submit-gpu:
...........

Some 1080 GPUs are available. The advantage of this partition is that there are approximately 50 GPUs available. In order to use the submit-gpu partition, add the following to the submission script:

.. code-block:: sh

     #SBATCH --partition=submit-gpu

If 1080s are not sufficient for your workflow, you can use the a30 partition. If you would like to use these GPUs, you should instead add to your submission script:

.. code-block:: sh

     #SBATCH --partition=submit-gpu-a30



