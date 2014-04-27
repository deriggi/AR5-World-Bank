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


def regridBatch(year):
	toRegrid("D:/climate/monthly/pr/outgeotiff_{0}_rotated/".format(year) , "D:/climate/monthly/pr/outgeotiff_{0}_rotated_regrided/".format(year) )
	
regridBatch(20)
# gdalwarp -of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline D:\climate\monthly\pr\outgeotiff_20_rotated_backup\pr_Amon_MRI-CGCM3_rcp85_r1i1p1_202001-203912_reproj.tif  D:\climate\monthly\pr\outgeotiff_20_rotated_backup\pr_Amon_MRI-CGCM3_rcp85_r1i1p1_202001-203912_bangladesh.tif
# toAscii('D:/climate/monthly/pr/outgeotiff_20_rotated/')
# gdal_translate -of AAIGrid -b 1 D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.tif D:/climate/monthly/pr/outgeotiff_20_rotated/pr_Amon_MRI-ESM1_esmrcp85_r1i1p1_202001-203912.asc

