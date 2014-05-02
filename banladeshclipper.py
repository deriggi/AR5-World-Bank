import os, sys, re
from osgeo import gdal

def clipraster(rasterpath, shapepath, outpath):

	# shape, inraster, outraster
	outname = rasterpath[rasterpath.rfind('\\')+1: ]
	outfullpath = outpath + outname[:outname.rfind('.')]+'clipped.tif'
	
	command = "gdalwarp -of GTiff -cutline {0} -crop_to_cutline -dstnodata 1e+020 {1}  {2}".format(shapepath, rasterpath, outfullpath)
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
		

def clipBatch(var, year):
	clipToShapefile( 'D:\\climate\\monthly\\{0}\\outgeotiff_{1}_rotated_reprojected_regridded_nd\\'.format(var,year), 'C:\Users\Johnny\Documents\climatev2\shapefiles\BGD_adm\BGD_adm0.shp',"F:\\climate\\monthly\\{0}\\bangladesh\\outgeotiff_{1}\\".format(var,year) )


def clipLoop():	
	cvars = ['tas', 'tasmin', 'tasmax' ]
	years = [20, 40, 60, 80]
	for cv in cvars:
		for y in years:
			clipBatch(cv, y)

clipLoop();
# gdalwarp -of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline -dstnodata 1e+020 D:\climate\monthly\pr\outgeotiff_80_rotated_reproj\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_208001-209912.tif  D:\climate\monthly\pr\outgeotiff_80_rotated_reproj\pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_208001-209912_bangladesh_nd.tif