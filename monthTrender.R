
library(raster)

monthTrend <- function() {
	cvars <- c('tasmax', 'tas', 'pr')
	years <- c(1965, 1985)
	for (cvar in cvars)
	{
		for (year in years)
		{
			rootDir <- paste("F:/climate/historical/",cvar,"/outgeotiff_", year , "_rotated/",sep="")
			write(rootDir, stdout())
			output_folder <- paste("F:/climate/historical/",cvar,"/monthtrend_", year ,  '/', sep="")
			dir.create(output_folder)

			path_length <- nchar(rootDir)
			allFiles <- list.files(rootDir, full.names=TRUE, pattern="\\.tif$")

			for (file in allFiles)
			{

				months = seq(1,12)
				outerStack<- stack()

				for (month in months){
					myStack <- stack()	

					factors = seq(0,19)

					for (factor in factors){
					# write(month + factor*12,stdout())
					band <- month + factor*12
					myStack <- addLayer(myStack,raster(file, band=band))

				}
				write( paste('nlayers: ', nlayers(myStack), sep="") , stdout())

				monthRaster <- stackApply(myStack, c(1), mean ) 
				outerStack <- addLayer(outerStack, monthRaster)
			}

			outfilename<-substr(file, path_length+1, nchar(file)-4)
			writeRaster(outerStack, filename=paste( output_folder , outfilename, '.tif', sep=""))
			# write outerStack to file here

		}
	}
}
}
monthTrend()
