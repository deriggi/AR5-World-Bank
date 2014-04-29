import os, sys, re
from osgeo import gdal

prmodels = []
prmodels.append(['bcc-csm1-1',float(1e+020)])
prmodels.append(['BNU-ESM',float(1e+020)])
prmodels.append(['CanESM2',float(1e+020)])
prmodels.append(['CNRM-CM5',float(1e+020)])
prmodels.append(['CSIRO-Mk3-6-0',float(1e+020)])
prmodels.append(['IPSL-CM5A-LR',float(1e+020)])
prmodels.append(['IPSL-CM5B-LR',float(1e+020)])
prmodels.append(['IPSL-CM5A-MR',float(1e+020)])
prmodels.append(['MIROC5',float(1e+020)])
prmodels.append(['MIROC5-ESM',float(1e+020)])
prmodels.append(['MIROC-ESM-CHEM',float(1e+020)])
prmodels.append(['MRI-CGCM3',float(1e+020)])
prmodels.append(['MRI-ESM1',float(1e+020)])

# print prmodels

def translateFiles(dirpath):
	# get list of all files
	suffix = '.tif'
	newfolder = dirpath + "_nd\\"
	createOutputDirectory(newfolder);

	childlist = os.listdir(dirpath);
	# make nd folder
	for c in childlist:
		if c.rfind(suffix) == len(c)-4:
			print
			print c
			original = dirpath + '\\' + c
			newfile = newfolder  + c
			command = 'gdal_translate --config GDAL_CACHEMAX 500 -stats -a_nodata 1.0e+020 {0} {1}'.format(original, newfile)
			print command
			os.system(command)
		
		# gdal_translate -a_nodata 1.0e+020

def createOutputDirectory(outPath):
	if not os.path.exists(outPath):
		os.makedirs(outPath)



cvars = ['pr']
years = [20, 40, 60, 80]
folder = ['rotated', 'rotated_reproj', 'rotated_reprojected_regridded']

for cv in cvars:
	for y in years:
		for f in folder:
			translateFiles("D:\\climate\\monthly\\{0}\\outgeotiff_{1}_{2}".format(cv, y, f))

# tasmodels = []
# tasmodels.append(['MPI-ESM',float(1e+020)])
# tasmodels.append(['ACCESS1-3',float(1e+020)])


# tasmaxmodels = []
# tasmodels.append(['CCSM4',float(1e+020)])
# tasmodels.append(['CESM1-BGC',float(1e+020)])
# tasmodels.append(['CESM1-CAM5',float(1e+020)])
# tasmodels.append(['NorESM1-M',float(9.969209968386869e+036)])

# tasminmodels  =[]
# tasminmodels.append(['FIO-ESM', float(1e+020)])



