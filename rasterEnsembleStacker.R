
# allfiles <- list all files
library(raster)
yearsies <- c(10, 50, 90)
climatevars <- c("pr", "tas", "tasmin", "tasmax")
for (cv in climatevars){

	for (year in yearsies){
		rootDir <- paste("F:/climate/monthly/", cv, "/ensemble_", year, "th" ,sep="")

		allFiles <- list.files(rootDir, full.names=TRUE)
		innerParts <- list()

		i <- 0

		for (file in allFiles){
			part <- unlist(strsplit(file, '_'))
			# write(part[2], stdout())

			# need last half of 1 and 2
			p1 <- unlist(strsplit(part[2],'\\/'))[2]
			
			pattern <- paste(p1, part[3], sep='_')
			write(pattern, stdout())

			
			if( !(pattern %in% innerParts) ){
				innerParts[i] <- pattern
				i <- i +1

			}
		}

		for (innerPart in innerParts){
			pat = paste(".*", innerPart, ".*\\.tif$", sep="")
			allFiles <- list.files(rootDir, full.names=TRUE, pattern=pat)
			
		# 	# sort this, should be 12
			allFiles <- sort(allFiles)
			write(allFiles, stdout())
			write('', stdout())
			if(length(allFiles) != 12){
				write(" not 12!", stdout())
				write(allFiles, stdout())
				write('', stdout())	

			}else{
				stizzy <- stack()
				for(rasty in allFiles){
					stizzy <- addLayer(stizzy, rasty)
				}
				destinationfolder <- paste("F:/climate/monthly/",cv,"/ensemblestacked_", year, "/" , sep="")
				
				dir.create(destinationfolder)
				writeRaster(stizzy, format="GTiff", filename=paste(destinationfolder, innerPart, ".tif",  sep="") )
			}
		}
	}
}

## TODO, use python to rename all files so they are 01 instead of 1 on months
# v <- get inner part of all in allFiles
# prestack <- for each v, get 12 from allfiles that are like it
# prestack <- sort this
# stack <- stack it and write to file