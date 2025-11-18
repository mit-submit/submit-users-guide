# Users guide to the *subMIT* login pool

The users guide can be found [here](http://submit.mit.edu/submit-users-guide).


# For people editing

Download the following sphinx packages in order to compile (use python3)

```
yum install python-sphinx
pip install groundwork-sphinx-theme
pip install sphinx-toolbox
pip install sphinx-togglebutton
```

In order to build the code and update the website do the following

```
./bin/sphinx-it.sh
```

## Pre-Commit hooks
Activate the pre-commit hooks in the ".pre-commit-config.yaml" file for basic automatic checks on the .rst syntax and check typos via codespell.

the pre-commit hooks need
```
pip install pre-commit
```

and can be activated via:
```
pre-commit install
```

They can be run locally via
```
pre-commit run --all-files
```

or for single programs and single files
```
pre-commit run codespell --files source/access.rst
```
There are two packages "doc8" and "rstcheck" that throw lot's of errors due to strict style conversions. We can think about adjusting the code to these in the future. i didn't find a way to automatically do these changes and manually going though all of these takes a lot of time so i disabled these checks for now.
