library(raster)


rootDir <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_20/"
output_folder <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_20_rotated"

path_length <- nchar(rootDir)
allFiles <- list.files(rootDir, full.names=TRUE, pattern="\\.tif$")

lapply(allFiles, function(x){
	raster_x <- stack(x)
	raster_x_rotated <- rotate(raster_x)
	
	outfilename<-substr(x, path_length+1, nchar(x))
	outfilename<-paste(output_folder,outfilename, sep='/')
	writeRaster(raster_x_rotated, outfilename)

	# write(paste(output_folder,outfilename, sep='/'), stdout())

	})



rootDir <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_40/"
output_folder <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_40_rotated"

path_length <- nchar(rootDir)
allFiles <- list.files(rootDir, full.names=TRUE, pattern="\\.tif$")

lapply(allFiles, function(x){
	raster_x <- stack(x)
	raster_x_rotated <- rotate(raster_x)
	
	outfilename<-substr(x, path_length+1, nchar(x))
	outfilename<-paste(output_folder,outfilename, sep='/')
	writeRaster(raster_x_rotated, outfilename)

	# write(paste(output_folder,outfilename, sep='/'), stdout())

	})



rootDir <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_60/"
output_folder <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_60_rotated"

path_length <- nchar(rootDir)
allFiles <- list.files(rootDir, full.names=TRUE, pattern="\\.tif$")

lapply(allFiles, function(x){
	raster_x <- stack(x)
	raster_x_rotated <- rotate(raster_x)
	
	outfilename<-substr(x, path_length+1, nchar(x))
	outfilename<-paste(output_folder,outfilename, sep='/')
	writeRaster(raster_x_rotated, outfilename)

	# write(paste(output_folder,outfilename, sep='/'), stdout())

	})



rootDir <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_80/"
output_folder <- "C:/Users/Johnny/Documents/climatev2/tas/outgeotiff_80_rotated"

path_length <- nchar(rootDir)
allFiles <- list.files(rootDir, full.names=TRUE, pattern="\\.tif$")

lapply(allFiles, function(x){
	raster_x <- stack(x)
	raster_x_rotated <- rotate(raster_x)
	
	outfilename<-substr(x, path_length+1, nchar(x))
	outfilename<-paste(output_folder,outfilename, sep='/')
	writeRaster(raster_x_rotated, outfilename)

	# write(paste(output_folder,outfilename, sep='/'), stdout())

	})
# tenthpercentile <- function(x, na.rm=true){ return (quantile(x, c(0.10), na.rm=na.rm));} 