tenthpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.10), na.rm=na.rm));}
fiftiethpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.10), na.rm=na.rm));}
ninetiethpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.10), na.rm=na.rm));}

library(raster)
rootDir <- "D:/climate/monthly/pr/outgeotiff_20_rotated_reprojected_regridded_nd/"
output_folder <- "F:/climate/monthly/pr/ensemble_10th/"

rcps <- c('rcp26', 'rcp45', 'rcp60', 'rcp85')
months <- c(1:12)

for (rcp in rcps){
	
	for (month in months){
		
		allFiles <- list.files(rootDir, full.names=TRUE, pattern=paste(".*",rcp,".*\\.tif$", sep=""))
		myStack <- stack()
		template_raster <- raster(allFiles[1], bands=1)
		
		for (x in allFiles){
			resampled_x <- resample(raster(x, bands=month), template_raster, method='bilinear')
			myStack <- addLayer(myStack,resampled_x)
			write(nlayers(myStack), stdout())
		}
		
		stackApply(myStack, c(1), fun=tenthpercentile, filename=paste(output_folder,paste(rcp,month,'.tif',sep='_'), sep=''))

	}

	
}

# run this for each decadal start thing


# lapply(allFiles, function(x){
# 	 resampled_x <- resample(raster(x, bands=1), template_raster, method='bilinear')
# 	 myStack <- addLayer(myStack,resampled_x)
# 	 write(nlayers(myStack), stdout())
# });

# stackApply(myStack, c(1), fun=tenthpercentile, filename=paste(output_folder,'rcp26test1.tif', sep=''))






# lapply(allFiles, function(x){
# 	raster_x <- stack(x)
# 	raster_x_rotated <- rotate(raster_x)

# 	outfilename<-substr(x, path_length+1, nchar(x))
# 	outfilename<-paste(output_folder,outfilename, sep='/')
# 	writeRaster(raster_x_rotated, outfilename)

# 	# write(paste(output_folder,outfilename, sep='/'), stdout())

# 	})