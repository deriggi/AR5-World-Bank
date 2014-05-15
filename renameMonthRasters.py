import os

def rename(cvar, year):
	rootfolder = "F:/climate/monthly/{0}/monthtrend_{1}/".format(cvar,year)
	childfiles = os.listdir(rootfolder)

	for c in childfiles:
		parts = c.split("_")
		if len(parts[len(parts)-1]) == 5:
			newname = c[:len(c)-5] + "0" + parts[len(parts)-1]
			
			os.rename(rootfolder+c, rootfolder+newname)


cvars = ['pr', 'tas', 'tasmin', 'tasmax' ]
years = [20, 40, 60, 80]
for cv in cvars:
	for y in years:
		rename(cv,y)