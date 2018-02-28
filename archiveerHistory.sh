#!/bin/bash
PROCESS_NUM=$(ps -ef | grep "gdReadArduino.py" | grep -v "grep" | wc -l)
   if [ $PROCESS_NUM -ge 1 ];
   then
      echo  1
   else

      NOW=$(date +%Y%m%d%H%M)
      export NOW
      echo $NOW   >> /home/pi/mylog
      echo "einde"   >> /home/pi/mylog
      mv /var/www/html/history.html /var/www/html/$NOW-history.html
#####      mv /var/www/html/bar.html /var/www/html/$NOW-bar.html
#####      mv /home/pi/allbar.html   /var/www/html/allbar.html
   fi
