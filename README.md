![Heavy Constructiuon](/source/img/under_construction.jpg "Construction")

# Users guide to the *subMIT* login pool

The draft users guide can be found here:

http://t3serv001.mit.edu/~freerc/build/index.html

in order to build the code and update the website do the following:

```
sphinx-build -b html source build
make html
cp -r build /home/tier3/freerc/public_html/
```

Download the following sphinx packages in order to compile

```
python3 -m pip install groundwork-sphinx-theme
python3 -m pip install sphinx-toolbox
```
