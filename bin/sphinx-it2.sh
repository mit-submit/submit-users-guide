#!/bin/bash
sphinx-build -b html source build
if [ ".$?" != ".0" ]
then
    echo " Sphinx build failed ... please fix."
    exit 1
fi

make html
if [ ".$?" != ".0" ]
then
    echo " Making the html sources failed ... please fix."
    exit 2
fi

# hack to get colors right - overwrite theme pygments file.
echo "\
cp css/pygments.css build/_static/"
cp css/pygments.css build/_static/
rsync -avh build/ /home/submit/mamoore/public_html/user_guide/
