#!/bin/bash

export PATH=/Selenium/bin/:$PATH
Xvfb :10 -ac &
export DISPLAY=:10

sed -i '/implicitly/d' $SCRIPT_PATH_NAME
python $SCRIPT_PATH_NAME
