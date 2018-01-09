#!/bin/bash

export PATH=/Selenium/bin/:$PATH
Xvfb :10 -ac &
export DISPLAY=:10

python $1
