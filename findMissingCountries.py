import os

sampleRootCountries = 'F:/climate/monthly/tas/countries/'
def getIsoCodes():
	codefile = open("C:/Users/Johnny/Documents/countrycodes/isocodes.csv")
	codes = list(codefile)
	codefile.close()

	codes = clipNewLines(codes)

	excludes  = ['AFG', 'CRI', 'ZAR', 'ETH', 'NER', 'KEN', 'BFA', 'BWA', 'IDN', 'MOZ', 'MWI', 'PHL']

	codes = codes + excludes
	
	return codes;



def clipNewLines(row):
	newRow = []
	for element in row:
		element = str(element)
		if element.rfind('\n') != -1:
			element = element[0:element.rfind('\n')]
		newRow.append(element)
	return newRow	

def getFolderCodes():
	folders = os.listdir(sampleRootCountries)
	return folders

def getEmptyFolders():
	codes = getFolderCodes()
	for code in codes:
		children = os.listdir(sampleRootCountries + code + '/monthtrendstacked_20_/')
		if len(children) == 0:
			print code + ' is empty'

getEmptyFolders()

def getIsoCodesNotFoundInFolders():
	fc = getFolderCodes()
	iso = getIsoCodes()

	for isocode in iso:
		if isocode not in fc:
			print isocode 