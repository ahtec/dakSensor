import serial
import datetime
import time

outputFileText = "<html>"
open("history.html", "w").write(outputFileText)
ser = serial.Serial('/dev/ttyUSB0', 9600)

dataregel = ser.readline()
lijst     = dataregel.split(';',3)

omgevingstemp = int(lijst[0])
irtemp        = int(lijst[1])
delta         = lijst[2]
now = datetime.datetime.now()
fileRegel=" %d | %d | %s |" %(irtemp, omgevingstemp, delta) + now.strftime("%Y-%m-%d %H:%M:%S")+ "<BR>"
open("history.html", "a").write(fileRegel )
open("index.html", "w").write("<html><strong>%d" %  irtemp+ "</strong></html>")
localtime   = time.localtime(time.time())
laatstetime = time.localtime(time.time())

while 1:
	vorigeirtemp = irtemp

	dataregel = ser.readline()
	lijst     = dataregel.split(';',3)
	aantal = 0
	for element in lijst:
		aantal = aantal +1

	if aantal == 3 :
		omgevingstemp = int(lijst[0])
		irtemp        = int(lijst[1])
		delta         = lijst[2]

		time.sleep(10)
		if abs(vorigeirtemp - irtemp) >= 2:
			laatstetime = time.localtime(time.time())
			now = datetime.datetime.now()
			fileRegel=" %d | %d | %s |" %(irtemp, omgevingstemp, delta) + now.strftime("%Y-%m-%d %H:%M:%S")+ "<BR>"
			print fileRegel
			open("history.html", "a").write(fileRegel )
			open("index.html", "w").write("<html><strong>%d" %  irtemp+ "</strong></html>")

#			open("history.html", "a").write(irtemp+"|" + omgevingstemp + "|" +delta+"|"  + now.strftime("%Y-%m-%d %H:%M:%S")+ "<BR>")
#			open("index.html", "w").write("<html><strong>" +  irtemp+ "</strong></html>")


