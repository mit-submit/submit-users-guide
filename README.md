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

### Login pool and local work

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
