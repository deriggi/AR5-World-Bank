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
		firstpart = 'gdal_translate -of AAIGrid -b '
		firstpart  = firstpart + str(band)
		command = "{0} {1} {2}{3}{4}".format(firstpart, inpath , outfolder, path[path.rfind('/')+1 : path.rfind('.tif')],'.asc');
		print command


def regridBatch(year, choice='all'):
	toRegrid("D:/climate/monthly/pr/outgeotiff_{0}_rotated_reproj/".format(year) , "D:/climate/monthly/pr/outgeotiff_{0}_rotated_reprojected_regridded/".format(year) ,choice)
	
regridBatch(40, 'all')
regridBatch(60, 'all')
regridBatch(80, 'all')

# not pr_Amon_bcc-csm1-1-m_rcp45_r1i1p1_204001-205912.tif

# reproject pr20batch when regrid done
# regrid rest all pr
# regrid tasmin, tasmax, tas 

# run process to regrid 40 and 60 concurrently


# gdalwarp -of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline D:\climate\monthly\pr\outgeotiff_20_rotated_backup\pr_Amon_MRI-CGCM3_rcp85_r1i1p1_202001-203912_reproj.tif  D:\climate\monthly\pr\outgeotiff_20_rotated_backup\pr_Amon_MRI-CGCM3_rcp85_r1i1p1_202001-203912_bangladesh.tif
# toAscii('D:/climate/monthly/pr/outgeotiff_20_rotated/')
# gdal_translate -of AAIGrid -b 1 D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.tif D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.asc


# gdalwarp -of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline -dstnodata -9999 D:\climate\monthly\pr\outgeotiff_80_rotated_reproj\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_208001-209912.tif  D:\climate\monthly\pr\outgeotiff_80_rotated_reproj\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_208001-209912_bangladesh_nd.tif

