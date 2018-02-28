#!/bin/bash

PROCESS_NUM=$(ps -ef | grep "gdAgregeer.py" | grep -v "grep" | wc -l)
        # for degbuging...
        if [ $PROCESS_NUM -ge 1 ];
        then
		echo  1
        else
		cd /var/www/html
		sudo rm /tmp/sortedhistory  
		sudo python ~/converteer.py  | sort --field-separator , --reverse --key 4,8  > /tmp/sortedhistory 
		sleep 10
		sudo python  ~/gdAgregeer.py
        fi

