import os

def rename(cvar, year):
	rootfolder = "F:/climate/monthly/{0}/ensemble_{1}th/".format(cvar,year)
	childfiles = os.listdir(rootfolder)

	for c in childfiles:
		parts = c.split("_")
		# print parts
		if parts[len(parts)-1] == '.tif' and len(parts) == 4 and len(parts[2]) == 1:
			
			newname = c[:11] + "0" + c[11:]
			print c
			print newname
			print
			os.rename(rootfolder+c, rootfolder+newname)


cvars = ['pr', 'tas', 'tasmin', 'tasmax' ]
ensemble = [10, 50, 90]
for cv in cvars:
	for y in ensemble:
		rename(cv,y)