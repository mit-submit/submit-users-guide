#!/bin/bash
#WEB_LOCATION=/home/tier3/paus/public_html/submit-users-guide
WEB_LOCATION=paus@submit04.mit.edu:/var/www/html/submit-users-guide

echo " Installing into: $WEB_LOCATION (hit return)"
read

sphinx-build -b html source build
make html

echo "\
rsync -Cavz --delete build/ $WEB_LOCATION"
rsync -Cavz --delete build/ $WEB_LOCATION
