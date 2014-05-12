import os

cvars = ['pr', 'tas', 'tasmin', 'tasmax' ]
years = [20, 40, 60, 80]
for cv in cvars:
	for y in years:
		rootfolder = "D:\\climate\\monthly\\{0}\\outgeotiff_{1}_rotated_reprojected_regridded_nd\\".format(cv, y)
		childfiles = os.listdir(rootfolder)
		out = open('D:\\delivered_global_files.txt'.format(cv,y), 'a')
		for c in childfiles:
			print rootfolder + c
			if c.rfind('.tif') == len(c) - 4:
				out.write(rootfolder+c + '\n');