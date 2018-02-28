#!/bin/bash

PROCESS_NUM=$(ps -ef | grep "gdReadArduino.py" | grep -v "grep" | wc -l)
   if [ $PROCESS_NUM -ge 1 ];
   then
      echo  1
   else
      cd /var/www/html
      sudo python    /home/pi/OncegdReadArduino.py  >>/tmp/gdRead.log
   fi

