library(raster)
makeAnom <- function(cvar, year, fyear){
	# list files in historical
	historicalDir <- paste("F:/climate/historical/",cvar,"/monthtrend_", year ,  '/', sep="")

	# list files in model
	futureDir <- paste("F:/climate/monthly/",cvar,"/monthtrendstacked_", fyear ,  '/', sep="")

	historicalFiles <- list.files(historicalDir, full.names=FALSE, pattern="\\.tif$")

	amon <- "Amon_"
	historical <- "_historical_"
	months <- c(1:12)

	# make anom dir
	anomDir <- paste("F:/climate/anom/",cvar,"_", fyear ,  '/', sep="")
	write( anomDir, stdout())
	dir.create(anomDir, recursive=TRUE)

	# for each historical file
	for (histFile in historicalFiles) {
		
		# get the model for the hist file
		amonIndex <- regexpr(amon, histFile) + nchar(amon) 
		histIndex <- regexpr(historical, histFile)  -1
		
		# get the model
		partmodel <- substr( histFile, amonIndex, histIndex)
		partmodel <- paste(partmodel,'_', sep="")
		write(partmodel, stdout())

		# get future files of this model
		futureFiles <- list.files(futureDir, full.names=FALSE, pattern=paste(".*",partmodel,".*","\\.tif$", sep=""));

		for ( futureFile in futureFiles ){
			write(futureFile,stdout())
			
			# difstack
			diffStack <- stack()

			# for each month	
			for(month in months){
				
				# get future and historic of same month
				futureRazzy <- raster(paste(futureDir, futureFile, sep=""), band=month);
				historicalRazzy <- raster(paste( historicalDir,histFile, sep=""), band=month);
				
				#  resample historical to that of future
				historicalResample <- resample(historicalRazzy, futureRazzy, method='bilinear')

				# subtract resampled historical from future
				
				if(cvar == 'pr'){
					write('doing pr', stdout())
					diffRazzy <- (futureRazzy - historicalResample)/historicalResample
				}else{
					write('doing temperature', stdout())
					diffRazzy <- futureRazzy - historicalResample
				}


				diffStack <- addLayer(diffStack,diffRazzy)

				write(month, stdout())
			}

			# write file
			outfile <- paste(anomDir,futureFile, sep="")
			write(outfile, stdout())

			# write diffstack out to file
			writeRaster(diffStack, outfile)
			
			#TODO, handle precip differently from temperature (f-h)/h
		}

	}
}

loopAnom <- function(){
	
	# cvar<-c('pr', 'tas', 'tasmin', 'tasmax')
	cvar<-c( 'pr')
	year <- 1965
	fyear<- c(20, 40, 60, 80)
	
	for (cv in cvar){
		for (fy in fyear){
			makeAnom(cv, year, fy)
		}
	}

}

loopAnom()


	# find matching model
	# create stack
	# for each month (1:12)
		# subtract historical from future
		# add to stack
	#write stack