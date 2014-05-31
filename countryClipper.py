import os, subprocess, sys, re
from osgeo import gdal

def clipraster(rasterpath, shapepath, outpath, countrycode, fieldName):

	# shape, inraster, outraster
	outname = rasterpath[rasterpath.rfind('/')+1: ]
	outfullpath = outpath + outname[:outname.rfind('.')]+'.tif'
	
	command = "gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -of GTiff -cwhere \"{4} = \'{0}\' \" -cutline {1} -crop_to_cutline -dstnodata 1e+020 -cblend 2 {2}  {3}".format(countrycode, shapepath, rasterpath, outfullpath, fieldName)
	print command
	print
	subprocess.call(command, shell=True)

def createOutputDirectory(outPath):
	if not os.path.exists(outPath):
		os.makedirs(outPath)

def clipToShapefile(rasterdirectory, shapefilepath, outputdirectory, countrycode, fieldName):
	createOutputDirectory(outputdirectory)
	childlist = os.listdir(rasterdirectory)
	counter = 0;
	suffix = '.tif'
	for c in childlist:
		if c.rfind(suffix) == len(c)-4:
			fullc = rasterdirectory + c
			clipraster(fullc, shapefilepath, outputdirectory, countrycode, fieldName)
			counter = counter+1
		
def getCodes(codesfile):
	codefile = open(codesfile)
	codes = list(codefile)
	codefile.close()

	codes = clipNewLines(codes)
	
	
	return codes;

def getIsoCodes():
	codefile = open("C:/Users/Johnny/Documents/countrycodes/isocodes.csv")
	codes = list(codefile)
	codefile.close()

	codes = clipNewLines(codes)
	
	
	return codes;

def getBasinIds():
	codefile = open("F:/climate/vectors/basins/basincodes.csv")
	codes = list(codefile)
	codefile.close()
	codes = clipNewLines(codes)
	
	return codes;

def clipNewLines(row):
	newRow = []
	for element in row:
		element = str(element).rstrip()
		newRow.append(element)
	return newRow	

		# clipToShapefile( 'D:\\climate\\monthly\\{0}\\outgeotiff_{1}_rotated_reprojected_regridded_nd\\'.format(var,year), 'C:\Users\Johnny\Documents\climatev2\shapefiles\BGD_adm\BGD_adm0.shp',"F:\\climate\\monthly\\{0}\\bangladesh\\outgeotiff_cblend{1}\\".format(var,year) )


def getExcludes():
	excludes = ['ABW', 'NIU', 'PCN', 'NFK', 'ATF', 'FLK', 'TCA', 'GGY', 'JEY', 'MLT', 'AIA', 'AND', 'ASM', 'ATG','BMU', 'BRB' ,'CCK']
	excludes = excludes + ['CXR','CYM','DMA','GIB','GRD','IOT','KNA', 'LCA','LIE','MAC','MCO','MNP','MSR','MYT','NRU','PLW','SGP']
	excludes = excludes + ['SHN','SMR','TKL','VCT','VGB','VIR']
	return excludes;


## Could easily generalise  this and basin function
# def clipBatchBaseData(var, year, countrycode):

# 	clipToShapefile( 'F:/climate/monthly/{0}/monthtrendstacked_{1}/'.format(var, year), 'C:/Users/Johnny/BoundaryData/wbshapes2010/World_Polys_Low.shp',"F:/climate/monthly/{0}/countries/{2}/monthtrendstacked_{1}_/".format(var,year, countrycode) , countrycode, 'ISO_CODES')


def clipBatchBaseData(var, year, countrycode, shapepath, outputtemplate, fieldname):

	clipToShapefile( 'F:/climate/monthly/{0}/monthtrendstacked_{1}/'.format(var, year), shapepath, outputtemplate.format(var,year, countrycode) , countrycode, fieldname)	






def clipBatchEnsembleData(var, year, countrycode, shapepath, outputtemplate, fieldname):

	clipToShapefile( 'F:/climate/monthly/{0}/ensemblestacked_{1}/'.format(var, year), shapepath, outputtemplate.format(var,year, countrycode) , countrycode, fieldname)


# def clipBatchEnsembleData(var, year, basinId):

# 	clipToShapefile( 'F:/climate/monthly/{0}/ensemblestacked_{1}/'.format(var, year), 'F:/climate/vectors/basins/basins_proj.shp',"F:/climate/monthly/{0}/basins/{2}/ensemblestacked_{1}_/".format(var,year, basinId) , basinId)



def clipLoopBaseData(shapepath, outputtemplate,fieldname, codesfile):	

	excludes  = getExcludes()
	countrycodes = getCodes(codesfile)
	
	cvars = ['pr', 'tas', 'tasmin', 'tasmax']
	years = [ 20, 40, 60, 80 ]
	for countrycode in countrycodes:
		if countrycode not in excludes:
			for cv in cvars:
				for y in years:
					clipBatchBaseData(cv, y, countrycode, shapepath, outputtemplate, fieldname)



def clipLoopBasinEnsembleData():	

	
	basinIds = getBasinIds()
	
	cvars = ['pr', 'tas', 'tasmin', 'tasmax']
	years = [ 10, 50, 90 ]

	for basinId in basinIds:
			for cv in cvars:
				for y in years:
					clipBatchBasinEnsembleData(cv, y, basinId)

def clipLoopEnsemble(shapepath, outputtemplate,fieldname, codesfile):	

	countrycodes = getCodes(codesfile)
	
	cvars = ['pr', 'tas', 'tasmin', 'tasmax']
	years = [ 10, 50, 90 ]
	for countrycode in countrycodes:
			for cv in cvars:
				for y in years:
					clipBatchEnsembleData(cv, y, countrycode)

# getIsoCodes()

# clipLoopBasinEnsembleData();

clipLoopBaseData('F:/climate/vectors/regions/CKP_regions_dissolved_low/regions_proj.shp', 'F:/climate/monthly/{0}/regions/{2}/ensemblestacked_{1}_/', 'FID', 'F:/climate/vectors/regions/CKP_regions_dissolved_low/regions_proj.csv' )

# gdalwarp -cblend 2-of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline -dstnodata 1e+020 F:\climate\monthly\pr\monthtrend_20\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_202001-203912_1.tif  F:\bantest_1.tif

