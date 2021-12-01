#!/bin/bash
WEB_LOCATION=/home/tier3/freerc/public_html/submit-users-guide

echo " Installing into: $WEB_LOCATION (hit return)"
read

sphinx-build -b html source build
make html
rsync -Cavz -delete build/ $WEB_LOCATION

exit 0
