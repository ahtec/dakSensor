#!/bin/bash
	NOW=$(date +%Y%m%d%H%M)
	export NOW
	echo $NOW   >> /home/pi/mylog
	mv /var/www/html/bar.html /var/www/html/$NOW-bar.html
