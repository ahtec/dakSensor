# dakSensor
python and shell programming for reading sensor data and creating website to present 
pi:~ $ crontab -l 
# m h  dom mon dow   command 
30 05 * * * /home/pi/startBar.sh >/dev/null 2>&amp;
1 00 17 * * * /home/pi/startgdReadArduino.sh >/dev/null 2>&amp;
1 01 06 * * * /home/pi/allhistory.sh  >allbar.html    

root:/home/pi# crontab -l 
# m h  dom mon dow   command 
45 16 * * * /home/pi/archiveerHistory.sh >> /home/pi/myjob.log 
15 06 * * * /home/pi/moveAllbar.sh >> /home/pi/myjob.log 
00 05 * * * /home/pi/archiveerBar.sh >> /home/pi/myjob.log
