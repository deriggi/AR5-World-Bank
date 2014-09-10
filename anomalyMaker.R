cvar<-'pr'
year <- 1965

fyear<- 20
# list files in historical
historicalDir <- paste("F:/climate/historical/",cvar,"/monthtrend_", year ,  '/', sep="")

# list files in model
futureDir <- paste("F:/climate/monthly/",cvar,"/monthtrendstacked_", fyear ,  '/', sep="")

historicalFiles <- list.files(historicalDir, full.names=FALSE, pattern="\\.tif$")

amon <- "Amon_"
historical <- "_historical_"
months <- c(1:12)

# for each historical file
for (histFile in historicalFiles) {
	
	# get the model for the hist file
	amonIndex <- regexpr(amon, histFile) + nchar(amon) 
	histIndex <- regexpr(historical, histFile)  -1
	
	# get the model
	partmodel <- substr( histFile, amonIndex, histIndex)
	write(partmodel, stdout())

	# get future files of this model
	futureFiles <- list.files(futureDir, full.names=FALSE, pattern=paste(".*",partmodel,".*","\\.tif$", sep=""));
		
	for ( futureFile in futureFiles ){
		write(futureFile,stdout())
		
		# for each month	
		for(month in months){

			# get future and historic of same month
			futureRazzy <- raster(paste(futureDir, futureFile, sep=""), band=month);
			historicalRazzy <- raster(paste( historicalDir,histFile, sep=""), band=month);
			
			# TODO resample historical to that of future

			# subtract resampled historical from future
			diffRazzy <- futureRazzy - historicalRazzy
			meanDiff <- cellStats(diffRazzy, stat='mean')
			write(meanDiff, stdout());
				
		}

	}

}

	# find matching model
	# create stack
	# for each month (1:12)
		# subtract historical from future
		# add to stack
	#write stack