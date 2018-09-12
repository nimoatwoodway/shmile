#!/bin/bash

#cancel all old printing jobs
/usr/bin/cancel -a

cd /home/pi/shmile
coffee app.coffee

exit 0
