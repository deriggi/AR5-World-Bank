import os, sys, re
from osgeo import gdal

# os.system("gdal_translate -of GTiff pr_Amon_CNRM-CM5_rcp26_r1i1p1_205601-210012.nc pr_out.tif")

# get list of files
# is beststart year valid?
# 	convert to gtiff for block of months

# v2
# is next biggest start year valid? 
# 	convert to gtiff
# 



class NCFile:
	def __init__(self, filename,startyear, startmonth, endyear, endmonth):
		self.startyear = int(startyear)
		self.startmonth = int(startmonth)
		self.endyear= int(endyear)
		self.endmonth = int(endmonth)
		self.filename = filename
		self.outpath = None
		
	def calculateStartMonth(self, astartyear):
		if astartyear < self.startyear:
			return None

		monthsFromYearDiff = (astartyear - self.startyear )*12 - 12
		monthsFromMonthDiff= 13-self.startmonth

		return monthsFromYearDiff + monthsFromMonthDiff + 1

	def createBandSwtich(self, startMonth, count):
		space = ' '
		bandlist = []
		for i in range(0, count):
			bandlist.append('-b ' + str(startMonth))
			startMonth = startMonth + 1
		return space.join(bandlist)

	def getYearDifference(self):
		return self.endyear - self.startyear

	def isProcessible(self):
		return self.getYearDifference() >20 and self.startyear >= 2000 and self.getYearDifference >= 20;

	def findBestStartYear(self, gt=0):
		startyears = [2020, 2040, 2060, 2080]
		for sy in startyears:
			diff = sy - self.startyear 
			if  sy >gt and diff > 0 and diff < 20 and (diff + sy) <= self.endyear:
				return sy
		return None

	def getNumberOfBlocks(self):
		bestStart = self.findBestStartYear();
		if bestStart is not None:
			print 'working'
			# return 80 / 20
			return (self.endyear - self.findBestStartYear() ) / 20  
		return 0

	def countBands(self):
		print self.filename
		src = gdal.Open(self.filename)
		numBands =  src.GetRasterCount()
		src = None
		return numBands

	def createGeotiffFolder(self,outfoldername):
		outpath = os.getcwd()+outfoldername;
		if not os.path.exists(outpath):
			os.makedirs(outpath)
		self.outpath = outpath

	def createAsGeotiff(self, bandinfo=''):
		firstpart = 'gdal_translate -of GTiff '
		firstpart  = firstpart + bandinfo
		command = "{0} {1} {2}{3}".format(firstpart,self.filename,self.outpath+self.filename[self.filename.rfind('\\'):self.filename.rfind('.')],'.tif');
		os.system(command)
		


def parsepath(path):

	match = re.search(r'\d\d\d\d\d\d\-\d\d\d\d\d\d\.nc',path)
	sd = None

	if match:
		matchedpart = match.group()
		matchedpart = matchedpart[0:13]
		start = matchedpart.split('-')[0]
		end = matchedpart.split('-')[1]

		startyear = start[:4]
		startmonth = start[4:]

		endyear = end[:4]
		endmonth = end[4:]
		sd = NCFile(path, startyear, startmonth, endyear, endmonth)

	return sd;


root = 'F:\\climate\\monthlypr\\v2test\\';
childfiles = os.listdir(root)

for ncfile in childfiles:
	sd  = parsepath(root + ncfile)
	if sd != None:
		sd.createGeotiffFolder('outTifffs')
		print "{0}".format(root + ncfile)
		if sd.isProcessible():
			
			# sd.createAsGeotiff()
			print "sy:\t\t{0}".format(sd.findBestStartYear())
			print "blocks:\t\t{0}".format(sd.getNumberOfBlocks())
			print "startyear:\t\t{0}".format(sd.calculateStartMonth(2020))
			calculatedStartMonth = sd.calculateStartMonth(2020) 
			if calculatedStartMonth != None:
				bandinfo = sd.createBandSwtich(int(calculatedStartMonth),20)
				sd.createAsGeotiff(bandinfo)
				
			
