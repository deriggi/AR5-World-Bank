import os, subprocess, shutil

def loopDelete():
	cvars = ['pr', 'tas', 'tasmin', 'tasmax']
	codes = getCodes('F:/climate/vectors/countries/isocodes.csv')

	for cvar in cvars:
		for code in codes:
			template = 'F:/climate/monthly/{0}/countries/{1}/'.format(cvar,code)
			if os.path.isdir(template):
				children = os.listdir(template)
				for child in children:
					if child.endswith('_'):
						print child
						shutil.rmtree(template+child)

def clipNewLines(row):
	newRow = []
	for element in row:
		element = str(element).rstrip()
		newRow.append(element)
	return newRow

def getCodes(codesfile):
	codefile = open(codesfile)
	codes = list(codefile)
	codefile.close()

	codes = clipNewLines(codes)
	
	
	return codes;

loopDelete()

