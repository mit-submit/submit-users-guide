<<<<<<< HEAD
# README
## Examples for *subMIT* cluster.

~~~sh
# Quick Documentation
# ===================
# 
# The files which are required/recommended:
# 
# 
#  a) submit
# 
#     this is the configuration file of your condor submission that defines what the condor submission
#     is suppose to do. There are always three components: 1 - input, 2 - executable, 3 - output and
#     well if you want of course some parameters. The submit file can be rather long and tedious to
#     create, it is therefore a good idea to generate it.
# 
#  c) base_sub
# 
#     basic condor configuration file that applies to all jobs in this batch.
#
#  b) generate_sub
# 
#     this is a little script that will construct the configuration used for condor submission. The
#     reason why you want to have a script to generate your submit file is that it is very repetitive
#     and error prone to write those down explicitely, of course you can.
# 
#
# The steps are roughly outlined below but use the 'new' script to re-run from scratch
# 

# start fresh (delete error, output and log files)
rm *.err *.out *.log

# generate the submission script
./generate_sub 1 15

# submit it to condor
condor_submit submit

# LNS Computing Workshop for documentation
https://indico.cern.ch/event/999848/
~~~
=======
# Users guide to the *subMIT* login pool

## Introduction

The subMIT login pool is designed to let users login safely prepare and tests their research computing tasks and submit them to the large computing resource of their choice. There are for now a limited number of resources connected but we are working on quickly expanding the available resources.

We have HTcondor connection to the Tier-2 computing cluster at Bates, the Tier-2 integration cluster (aka Tier-3) in building 24, the engaging cluster and the OSG. For CMS users the global CMS queue is also seemlesly integrated.

### How to get an account

To make login convenient and secure we allow login to the subMIT pool using ssh keys only. Users of submit can go to our submit portal to upload their ssh key (or a number of keys). Upload of ssh keys is secured through MIT touchstone authentication. This means users need to have an MIT account.

It is very straight forward to obtain an MIT guest account if you do not have one. A sponsor - usually a faculty you are working with - can request a guest account for you. The information needed is the first, last name and the birthday. See the [sponsoring web page](https://ist.mit.edu/guest-accounts). Please note: the process has to be started by the sponsor! The response by MIT IS&T has been very quick in the past, we have so far received all account requests in less than 4 hours.

### Heavy duty calculations

## Getting started

### How to get an account

### The rules for an account

## Things that work and what does not work

### Do this

### Do not do this

## Getting your programs to run

### Software you need

#### Native system

#### CVMFS

#### Conda

#### Containers

### Running you application

#### Running locally

#### Using batch systes to run at any given resource
>>>>>>> ea7403580aff273b05999e19fa31770d71eed356
