import os, sys, re
from osgeo import gdal

def reprojectFile(infile, outfolder):
	template = 'gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -of GTiff -t_srs EPSG:4326 {0} {1}'
	command = template.format(infile, outfolder+infile[infile.rfind('/')+1:])
	print command
	os.system(command)
	print '==========='
	print ''

def reprojectAll(rootfolder, outfolder):
	excludes = ['pr_Amon_bcc-csm1-1_rcp60_r1i1p1_202001-203912.tif','pr_Amon_bcc-csm1-1_rcp45_r1i1p1_202001-203912_nd.tif','pr_Amon_bcc-csm1-1_rcp45_r1i1p1_202001-203912.tif','pr_Amon_bcc-csm1-1_rcp26_r1i1p1_202001-203912.tif','pr_Amon_bcc-csm1-1-m_rcp60_r1i1p1_202001-203912.tif','pr_Amon_bcc-csm1-1-m_rcp45_r1i1p1_202001-203912.tif','pr_Amon_bcc-csm1-1-m_rcp26_r1i1p1_202001-203912.tif','a_reproj_test.tif']
	childfiles = os.listdir(rootfolder)
	createOutputDirectory(outfolder)
	for c in childfiles:
		if c.rfind('.tif') == len(c)-4 and c not in excludes:
			reprojectFile(rootfolder+c, outfolder)

def createOutputDirectory(outPath):
	if not os.path.exists(outPath):
		os.makedirs(outPath)

def reprojectYear(cvar, year):
	reprojectAll('D:/climate/monthly/{0}/outgeotiff_{1}_rotated_regrid/'.format(cvar, year), 'D:/climate/monthly/{0}/outgeotiff_{1}_rotated_reprojected_regridded/'.format(cvar,year))

cvars = ['pr']
years = [20]
for cv in cvars:
	for y in years:
		reprojectYear(cv, y)


# gdalwarp -of GTiff -t_srs EPSG:4326 {0} {1}

# C:\>gdalwarp -of GTiff -cutline C:/Users/Johnny/Documents/climatev2/shapefiles/BGD_adm/BGD_adm0.shp -crop_to_cutline -dstnodata -9999 D:\climate\monthly\pr\outgeotiff_20_rotated_reproj\pr_Amon_CanESM2_rcp45_r1i1p1_202001-203912.tif  D:\climate\monthly\pr\outgeotiff_80_rotated_reproj\canesm_bangladesh_nd.tif