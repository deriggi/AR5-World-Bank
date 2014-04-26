import os, sys, re
from osgeo import gdal

def toAscii(rootPath, outfolder):
	childfiles = os.listdir(rootPath)
	createOutputDirectory(outpath)
	for child in childfiles:
		if child.rfind('.tif') == len(child)-4:
			createAsASCII( rootPath + child, 1, outfolder)

def toRegrid(rootPath, outpath):
	childfiles = os.listdir(rootPath)
	createOutputDirectory(outpath)
	for child in childfiles:
		if child.rfind('.tif') == len(child)-4:
			changeResolution( rootPath + child, outpath)


def changeResolution(inpath, outfolder):
	firstpart = 'gdalwarp -r near -tr 0.5 0.5'
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

# toAscii('D:/climate/monthly/pr/outgeotiff_20_rotated/')
toRegrid("D:/climate/monthly/pr/outgeotiff_20_rotated_backup/", "D:/climate/monthly/pr/outgeotiff_20_rotated_backup_regrid/")

# gdal_translate -of AAIGrid -b 1 D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.tif D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.asc

