library(raster)
cvar <- 'tasmin' # tasmin tasmax pr
years <- c(20,40,60,80)
for (year in years){
	rootDir <- paste("D:/climate/monthly/",cvar,"/outgeotiff_", year , "_rotated_reprojected_regridded_nd/",sep="")
	write(rootDir, stdout())
	output_folder <- paste("F:/climate/monthly/",cvar,"/monthtrend_", year ,  '/', sep="")
	path_length <- nchar(rootDir)
	allFiles <- list.files(rootDir, full.names=TRUE, pattern="\\.tif$")

	for (file in allFiles){
		
		months = seq(1,12)
		
		for (month in months){
			myStack <- stack()	

			factors = seq(0,19)

			for (factor in factors){
				# write(month + factor*12,stdout())
				band <- month + factor*12
				myStack <- addLayer(myStack,raster(file, band=band))

			}
			write( paste('nlayers: ', nlayers(myStack), sep="") , stdout())
			outfilename<-substr(file, path_length+1, nchar(file)-4)

			stackApply(myStack, c(1), mean, filename=paste( output_folder , outfilename, '_' , month , '.tif', sep="") ) 
		}
	}
}

