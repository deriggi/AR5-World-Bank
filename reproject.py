import os, sys, re
from osgeo import gdal

def reprojectFile(infile, outfolder):
	template = 'gdalwarp -of GTiff -t_srs EPSG:4326 {0} {1}'
	command = template.format(infile, outfolder+infile[infile.rfind('/')+1:])
	os.system(command)

def reprojectAll(rootfolder, outfolder):
	childfiles = os.listdir(rootfolder)
	createOutputDirectory(outfolder)
	for c in childfiles:
		if c.rfind('.tif') == len(c)-4:
			reprojectFile(rootfolder+c, outfolder)

def createOutputDirectory(outPath):
	if not os.path.exists(outPath):
		os.makedirs(outPath)

def reprojectYear(cvar, year):
	reprojectAll('D:/climate/monthly/{0}/outgeotiff_{1}_rotated/'.format(cvar, year), 'D:/climate/monthly/{0}/outgeotiff_{1}_rotated_reproj/'.format(cvar,year))

cvars = ['tasmin', 'tasmax']
years = [20, 40, 60, 80]
for cv in cvars:
	for y in years:
		reprojectYear(cv, y)
