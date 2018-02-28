import sys	
def gdLeesfileRegel(fh):
	eruit = ''
	while True:
		filecharacter = fh.read(1)
		if not filecharacter :
			break
		else:
			asciiwaarde = ord(filecharacter)
			if asciiwaarde == 60:
					eruit = eruit  + filecharacter+ "\n"
					break
			if asciiwaarde >= 48 and   asciiwaarde <= 57 or asciiwaarde == 45 or asciiwaarde == 44 :
					eruit = eruit + filecharacter
	return eruit	



regeluitfile = ""
open("history.html", "r")
ifile  = open('history.html','r')
#ofile =  open("historyout.html", "a")

regeluitfile = gdLeesfileRegel(ifile)
fileEof = False
if not regeluitfile:
	fileEof = True

while not fileEof:
#	ofile.write(regeluitfile )
	sys.stdout.write(regeluitfile)
	regeluitfile = gdLeesfileRegel(ifile)
	if not regeluitfile:
		fileEof = True
ifile.close
#ofile.close



