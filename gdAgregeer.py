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
				break
			if asciiwaarde >= 48 and   asciiwaarde <= 57 or asciiwaarde == 45 or asciiwaarde == 44 :
					eruit = eruit + filecharacter
	return eruit	




ifile  = open('/tmp/sortedhistory')
vorige = 0
min = 999
kleurviatemperatuur = 0.0
inverteerdekleur = 0.0
rownum = 0
regeluitfile = ""
bewaarderow = ""
vorigedag    = ''
voriguur    = ''
vorigeminute = ''
fileregel = "<!DOCTYPE html><style> .chart div {  font: 10px sans-serif;  background-color: steelblue;  text-align: right;  padding: 3px;  margin: 1px;  color: white;}</style> <div class='chart'>"
open("bar.html", "w").write(fileregel )
regeluitfile = gdLeesfileRegel(ifile)
row = regeluitfile.split(",")
fileEof = False

while not fileEof:
	if vorigeminute <> row[7]  :	
		doorgaan = True
		min = 999
		while doorgaan:

			if min > int(row[0]) :
				min = int(row[0])

			vorigeminute = row[7]
			vorigedag    = row[5]
			voriguur     = row[6]
			vorigemaand  = row[4]
			vorigjaar    = row[3]
			regeluitfile = gdLeesfileRegel(ifile)
			if not regeluitfile:
				fileEof = True
				doorgaan = False
				break
			row = regeluitfile.split(",")
			if vorigeminute <> row[7] :
				minpixels = 250 - (min * 3)
				kleurviatemperatuur = ((min + 30.0)/60.0)*255
				inverteerdekleur = 255 - kleurviatemperatuur
				fileregel = "<div style='width: %dpx; background-color:rgb(%d, 0, %d)'>%d graden  op %s %s %s om %s:%s </div>" %(minpixels,kleurviatemperatuur,inverteerdekleur,min,vorigjaar,vorigemaand,vorigedag,voriguur,vorigeminute)
				open("bar.html", "a").write(fileregel )
				doorgaan = False

if min > int(row[0]) :
	min = int(row[0])

#print "verwerk laatste"	
######### start new ########
minpixels = 250 - (min * 3)
kleurviatemperatuur = ((min + 30.0)/60.0)*255
inverteerdekleur = 255 - kleurviatemperatuur
######### end  new ########
					
fileregel = "<div style='width: %dpx; background-color:rgb(%d, 0, %d)'>%d graden  op %s %s %s om %s:%s </div>" %(minpixels,kleurviatemperatuur,inverteerdekleur,min,vorigjaar,vorigemaand,vorigedag,voriguur,vorigeminute)
open("bar.html", "a").write(fileregel )

ifile.close()



