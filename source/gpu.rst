GPU resources
-------------

SubMIT also has access to several GPUs. In this section we will review how to access these machines and add them to your workflow.

submit-gpu login
~~~~~~~~~~~~~~~~

Submit allows interactive login access to GPUs through slurm. From submit, you have access to the submit-gpu server pool which contains four servers, each fitted with 2 GPUs as well as the submit-gpu1080 server pool which has several machines each fitted with 4 1080 GPUs.. This allows users to interactively test their GPU applications by simply logging into these machines through slurm using the salloc command shown below:

.. code-block:: sh

      salloc --partition=submit-gpu --cpus-per-gpu=1 --gres=gpu:1

or to the submit-gpu1080 partition:

.. code-block:: sh

      salloc --partition=submit-gpu1080 --cpus-per-gpu=1 --gres=gpu:1

If you want more than one gpu for an interactive session, you can request more with the following:

.. code-block:: sh

      salloc --partition=submit-gpu1080 --cpus-per-gpu=1 --gres=gpu:4


CUDA
~~~~

Compute Unified Device Architecture (CUDA) is a parallel computing platform and application programming interface (API) that allows software to use certain types of graphics processing unit (GPU) for general purpose processing. CUDA is available on the submit-gpu machines inherently. In order to check which CUDA version is installed you can use the command below. Make sure this version fits your workflow.

.. code-block:: sh

      nvcc --version

Slurm with GPUs
~~~~~~~~~~~~~~~

The submit-gpu machines are connected to the submit slurm cluster as the "submit-gpu" partition. This means that you can also scale up GPU applications through the use of slurm in order to access all of the GPUs available. Keep in mind that these are shared resources so use these machines responsibly. In addition to the submit-gpu partition, there are additional GPUs available through submit-gpu1080. A sample slurm job designed to run on the submit-gpu machines is available in our `GPU tutorial <https://submit.mit.edu/submit-users-guide/tutorials/tutorial_5.html>`_, and more info is available in our Githup `slurm 1080 <https://github.com/mit-submit/submit-examples/tree/main/gpu/slurm_gpu1080>`_ example.

A cuda example with slurm can be found here:
`slurm cuda <https://github.com/mit-submit/submit-examples/gpu/slurm_gpu>`_


Condor with GPUs
~~~~~~~~~~~~~~~~

The MIT T2 and T3 both have access to GPU machines through Condor. An example of how to access these resources through Condor is shown below

If you wish to submit jobs to GPU machines in T3/T2, you need to add additonal line in the script (only through glidein submission):

.. code-block:: sh

       RequestGPus=1

If you wish to submit jobs to GPU machines in CMS global pool, you need to add additional line in the script:

.. code-block:: sh

       RequestGPus=1
       +RequiresGPU=1

Some example scripts to run GPUs with condor can be found here:
`condor gpu <https://github.com/mit-submit/submit-examples/tree/main/gpu/condor_gpu>`_
