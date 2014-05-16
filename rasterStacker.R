
# allfiles <- list all files
library(raster)
yearsies <- c(20, 40, 60, 80)
climatevars <- c("pr", "tas", "tasmin", "tasmax")
for (cv in climatevars){

	for (year in yearsies){
		rootDir <- paste("F:/climate/monthly/", cv, "/monthtrend_", year, sep="")

		allFiles <- list.files(rootDir, full.names=TRUE)
		innerParts <- list()

		i <- 0

		for (file in allFiles){
			part <- unlist(strsplit(file, '_'))
			part <- paste(part[3], part[4], part[5], part[6], part[7], sep='_')
			# part <- part[2:6]
			if( !(part %in% innerParts) ){
				innerParts[i] <- part
				write(part, stdout())
				i <- i +1

			}
		}

		for (part in innerParts){
			pat = paste(".*", part, ".*\\.tif$", sep="")
			allFiles <- list.files(rootDir, full.names=TRUE, pattern=pat)
			
			# sort this, should be 12
			sort(allFiles)
			if(length(allFiles) != 12){
				write(" not 12!", stdout())
				write(allFiles, stdout())
				write('', stdout())	

			}else{
				stizzy <- stack()
				for(rasty in allFiles){
					stizzy <- addLayer(stizzy, rasty)
				}
				destinationfolder <- paste("F:/climate/monthly/",cv,"/monthtrendstacked_", year, "/" , sep="")
				dir.create(destinationfolder)
				writeRaster(stizzy, format="GTiff", filename=paste(destinationfolder, part, ".tif",  sep="") )
			}
		}
	}
}

## TODO, use python to rename all files so they are 01 instead of 1 on months
# v <- get inner part of all in allFiles
# prestack <- for each v, get 12 from allfiles that are like it
# prestack <- sort this
# stack <- stack it and write to file