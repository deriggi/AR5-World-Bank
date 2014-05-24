import os, sys, re
from osgeo import gdal

def clipraster(rasterpath, shapepath, outpath):

	# shape, inraster, outraster
	outname = rasterpath[rasterpath.rfind('/')+1: ]
	outfullpath = outpath + outname[:outname.rfind('.')]+'.tif'
	
	command = "gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -of GTiff -cutline {0} -crop_to_cutline -dstnodata 1e+020 -cblend 2 {1}  {2}".format(shapepath, rasterpath, outfullpath)
	print command
	os.system(command)

def createOutputDirectory(outPath):
	if not os.path.exists(outPath):
		os.makedirs(outPath)

def clipToShapefile(rasterdirectory, shapefilepath, outputdirectory):
	createOutputDirectory(outputdirectory)
	childlist = os.listdir(rasterdirectory)
	counter = 0;
	suffix = '.tif'
	for c in childlist:
		if c.rfind(suffix) == len(c)-4:
			fullc = rasterdirectory + c
			clipraster(fullc, shapefilepath, outputdirectory)
			counter = counter+1
		

def clipBatch(var, percentile):
	clipToShapefile( 'F:/climate/monthly/{0}/ensemble_{1}th/'.format(var, percentile), 'C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp',"F:/climate/monthly/{0}/bangladesh/ensemble_{1}/".format(var,percentile) )
	# clipToShapefile( 'D:\\climate\\monthly\\{0}\\outgeotiff_{1}_rotated_reprojected_regridded_nd\\'.format(var,year), 'C:\Users\Johnny\Documents\climatev2\shapefiles\BGD_adm\BGD_adm0.shp',"F:\\climate\\monthly\\{0}\\bangladesh\\outgeotiff_cblend{1}\\".format(var,year) )


def clipLoop():	
	cvars = ['tasmax']
	years = [10, 50, 90]
	for cv in cvars:
		for y in years:
			clipBatch(cv, y)

clipLoop();
# gdalwarp -cblend 2-of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline -dstnodata 1e+020 F:\climate\monthly\pr\monthtrend_20\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_202001-203912_1.tif  F:\bantest_1.tif

