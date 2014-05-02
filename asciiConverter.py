import os, sys, re
from osgeo import gdal

def toAscii(rootPath, outfolder):
	childfiles = os.listdir(rootPath)
	createOutputDirectory(outpath)
	for child in childfiles:
		if child.rfind('.tif') == len(child)-4:
			createAsASCII( rootPath + child, 1, outfolder)

def toRegrid(rootPath, outpath, choice='all'):
	childfiles = os.listdir(rootPath)
	childfiles = getOnlyTiffs(childfiles)

	print 'choice is: {0}'.format(choice)
	print 'len of files is: {0}'.format(len(childfiles))
	if choice == 'even':
		childfiles = returnEvens(childfiles)
	elif choice == 'odd':
		childfiles = returnOdds(childfiles)

	print 'len of files is: {0}'.format(len(childfiles))
	createOutputDirectory(outpath)
	
	for child in childfiles:
		changeResolution( rootPath + child, outpath)

def getOnlyTiffs(alist):
	newlist = []
	suffix = '.tif'
	for child in alist:
		if child.rfind(suffix) == len(child)-4:
			newlist.append(child)
	return newlist

def isTiff(child):
	suffix = '.tif'
	if child.rfind(suffix) == len(child)-4:
		return True;
	return False

def returnOdds(alist):
	newlist = []
	sorted(alist, key=str.lower)
	for i in range(0,len(alist)):
		if i%2 != 0:
			newlist.append(alist[i])

	return newlist

def returnEvens(alist):
	newlist = []
	sorted(alist, key=str.lower)
	for i in range(0,len(alist)):
		if i%2==0:
			newlist.append(alist[i])

	return newlist	

def changeResolution(inpath, outfolder):
	firstpart = 'gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -r near -tr 0.5 0.5'
	command = "{0} {1} {2}{3}".format(firstpart, inpath , outfolder, inpath[inpath.rfind('/')+1 : ]);
	print command
	os.system(command)

def createOutputDirectory(outPath):
	if not os.path.exists(outPath):
		os.makedirs(outPath)
		
def createAsASCII( inpath, band, outfolder ):
	firstpart = 'gdal_translate --config GDAL_CACHEMAX 500 -of AAIGrid -b '
	firstpart  = firstpart + str(band)
	command = "{0} {1} {2}{3}_band-{4}{5}".format(firstpart, inpath , outfolder, inpath[inpath.rfind('\\')+1 : inpath.rfind('.tif')],band,'.asc');
	print command
	os.system(command)
	print

def regridBatch(year, val, choice='all'):
	toRegrid("D:/climate/monthly/{0}/outgeotiff_{1}_rotated_reproj/".format(val, year) , "D:/climate/monthly/{0}/outgeotiff_{1}_rotated_reprojected_regridded/".format(val,year) ,choice)

def regridLoop():	
	cvars = ['tas', 'tasmin', 'tasmax' ]
	years = [20, 40, 60, 80]
	for cv in cvars:
		for y in years:
			regridBatch(y, cv, 'all')

def asciibatch(var, year, intemplate, outemplate):
	inpath = intemplate.format(var,year)
	outpath = outemplate.format(var,year)
	createOutputDirectory(outpath)
	childfiles = os.listdir(inpath)
	
	for c in childfiles:
		if isTiff(c):
			for i in xrange(1,241):
				createAsASCII(inpath + c, i, outpath);

def clipLoop():	
	cvars = ['pr', 'tas', 'tasmin', 'tasmax' ]
	years = [20, 40, 60, 80]
	for cv in cvars:
		for y in years:
			asciibatch(cv,y,'F:\\climate\\monthly\\{0}\\bangladesh\\outgeotiff_{1}\\'.format(cv,y),'F:\\climate\\monthly\\{0}\\bangladesh\\outasc_{1}\\'.format(cv,y) );

clipLoop();
	


# gdal_translate -of AAIGrid -b 240 D:\\climate\\monthly\\pr\\outgeotiff_20_rotated_reprojected_regridded_nd\\pr_Amon_bcc-csm1-1_rcp26_r1i1p1_202001-203912.tif F:\climate\monthly\pr\outgeotiff_20_rotated_reprojected_regridded_nd\pr_Amon_bcc-csm1-1_rcp26_r1i1p1_202001-203912.tif

# not pr_Amon_bcc-csm1-1-m_rcp45_r1i1p1_204001-205912.tif


# regrid tasmin, tasmax, tas 

# setnodata


# gdalwarp -of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline D:\climate\monthly\pr\outgeotiff_20_rotated_backup\pr_Amon_MRI-CGCM3_rcp85_r1i1p1_202001-203912_reproj.tif  D:\climate\monthly\pr\outgeotiff_20_rotated_backup\pr_Amon_MRI-CGCM3_rcp85_r1i1p1_202001-203912_bangladesh.tif
# toAscii('D:/climate/monthly/pr/outgeotiff_20_rotated/')
# gdal_translate -of AAIGrid -b 1 D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.tif D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.asc


# gdalwarp -of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline -dstnodata 1e+020 D:\climate\monthly\pr\outgeotiff_80_rotated_reproj\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_208001-209912.tif  D:\climate\monthly\pr\outgeotiff_80_rotated_reproj\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_208001-209912_bangladesh_nd.tif

