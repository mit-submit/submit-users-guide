#!/bin/bash
WEB_LOCATION=paus@submit04.mit.edu:/var/www/html/submit-users-guide

if [ ".$1" != "." ]
then
   WEB_LOCATION="$1"
fi

echo " Installing into: $WEB_LOCATION (hit return)"
read

sphinx-build -b html source build
make html

# hack to get colors right - overwrite theme pygments file.
echo "\
cp css/pygments.css build/_static/"
cp css/pygments.css build/_static/

echo "\
rsync -Cavz --delete build/ $WEB_LOCATION"
rsync -Cavz --delete build/ $WEB_LOCATION
