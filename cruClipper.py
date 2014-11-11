import os, subprocess, sys, re
from osgeo import gdal

def clipraster(rasterpath, shapepath, outpath, countrycode, fieldName):

	# shape, inraster, outraster
	outname = rasterpath[rasterpath.rfind('/')+1: ]
	
	outdir = outpath + countrycode +  '/'
	createOutputDirectory(outdir)

	outfullpath = outpath + countrycode +  '/' + outname[:outname.rfind('.')]+'.tif'
	

	command = "gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -of GTiff -s_srs EPSG:4326 -cwhere \"{4} = \'{0}\' \" -cutline {1} -crop_to_cutline -dstnodata 1e+020 -cblend 2 {2}  {3}".format(countrycode, shapepath, rasterpath, outfullpath, fieldName)
	print command
	print
	subprocess.call(command, shell=True)

def convertToTiff(asciiraster, basepath):
	outname = asciiraster[asciiraster.rfind('/')+1: asciiraster.rfind('.asc') ]

	command = 'gdal_translate --config GDAL_CACHEMAX 500 -of GTiff -a_srs EPSG:4326 {0} {1}'.format(asciiraster, basepath  + outname + '.tif')
	# print command
	subprocess.call(command, shell=True)



def clipNewLines(row):
	newRow = []
	for element in row:
		element = str(element).rstrip()
		newRow.append(element)
	return newRow	


def createOutputDirectory(outPath):
	if not os.path.exists(outPath):
		os.makedirs(outPath)


def getTiffsFromDirectory(rasterDirectory):
	rs = getRastersFromDirectory(rasterDirectory)
	asciis = []
	for r in rs:
		if r.endswith('.tif'):
			asciis.append( rasterDirectory + r )

	return asciis;


def getAsciisFromDirectory(rasterDirectory):
	rs = getRastersFromDirectory(rasterDirectory)
	asciis = []
	for r in rs:
		if r.endswith('.asc'):
			asciis.append( rasterDirectory + r )

	return asciis;

def getRastersFromDirectory(rasterDirectory):
	childlist = os.listdir(rasterDirectory)
	return childlist

def getIsoCodes():
	codefile = open("C:/Users/Johnny/Documents/countrycodes/isocodes.csv")
	codes = list(codefile)
	codefile.close()
	codes = clipNewLines(codes)
	
	return codes;

def clipBatch(rasterdirectory, shapefile, outpath, codes, fieldName):
	
	rasters = getTiffsFromDirectory(rasterdirectory)
	
	# for each raster, get 
	for code in codes:
		for raster in rasters:
			print 'trying {0} and {1}'.format(raster, code)
			clipraster(raster, shapefile, outpath, code, fieldName )


#######################3
def run():
	clipBatch('F:/climate/cru/09_12/pre/pre/', 'F:/climate/vectors/countries/World_Polys_Low.shp', 'F:/climate/cru/09_12/pre/pre/countryoutput/' , getIsoCodes(), 'ISO_CODES')	

def convertAll():
	rasterRoot = 'F:/climate/cru/09_12/pre/pre/';
	asciis = getAsciisFromDirectory(rasterRoot)
	for ascii in asciis:
		convertToTiff(ascii, rasterRoot)

run()