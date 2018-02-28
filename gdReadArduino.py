import serial
import datetime
import time


def gdStrip(erin):
	erin = erin.strip()
	eruit = ""
	for c in erin:
		asciiwaarde = ord(c)
		if asciiwaarde >= 48 and   asciiwaarde <= 57 or asciiwaarde == 45 :
			eruit = eruit + c 
	return eruit

def huidigeUur():
	hhmm = datetime.datetime.now().time()
	strhhmm = str(hhmm)
	regel   = strhhmm.split(':',3)
	return regel[0]


outputFileText = "<html>"
#open("history.html", "w").write(outputFileText)
open("history.html", "a")
ser           = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)
dataregel     = ser.readline()
lijst         = dataregel.split(';',3)
irtemp        = 0
omgevingstemp = ''
aantal        = 0
delta         = ''
vorigeirtemp = 90
eersteOmgevingstemp = 1

teller = 0
#moet 13 uur lopen van af 1700  dus tot 0600
# 13 * 60 min  * 60 seconden  = 46800 seconden min 
# tellr max wordt dus 46800 / 10 is 4680
while teller < 4680:
	teller+=1
	time.sleep(10)
	dataregel = ser.readline()
	lijst     = dataregel.split(';',3)

	aantal = 0
	for element in lijst:
		aantal = aantal +1
	if aantal == 3 :
		if eersteOmgevingstemp == 1:
			omgevingstemp = '0'
			eersteOmgevingstemp = 99
		else:
			try:
				omgevingstemp = gdStrip(lijst[0])
				irtemp        = int(lijst[1])
				delta         = gdStrip(lijst[2])
				open("index.html", "w").write("<html><body style=\"background-color:black\"></body><p style='font-size: 500px; color: white' >%d" %  irtemp+ "</p></html>")
				if abs(vorigeirtemp - irtemp) >= 2:
					now = datetime.datetime.now()
					fileRegel="%d,%s,%s," %(irtemp, omgevingstemp, delta) + now.strftime("%Y,%m,%d,%H,%M")+ ",<BR>\n"
					open("history.html", "a").write(fileRegel )


					vorigeirtemp = irtemp
			except ValueError as e: 
				print("ValueError")
				print(lijst)
				print("Teller = %d" %(teller))
				vorigeirtemp = 999



