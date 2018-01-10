#!/bin/bash

export PATH=/Selenium/bin/:$PATH
Xvfb :10 -ac &
export DISPLAY=:10

sed -i '/implicitly/d' $1
python $1
