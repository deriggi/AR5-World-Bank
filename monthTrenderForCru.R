library(raster)


calcMonthAverages <- function(cvar){
	rootDir <- paste("F:/climate/cru/",cvar,"/output/",sep="")
	dir.create(paste(rootDir, "monthtrend/", sep=""))
	
	months <- (1:12)
	for (month in months){
		stizzy <-stack()
		if(month<10){
			month <- paste('0',month,sep="")
		}
		# get all _01.asc files
		patty <- paste("_",month,"\\.asc$", sep="")

		allFiles <- list.files(rootDir, full.names=FALSE, patty)
		write(allFiles, stdout())

		for (file in allFiles){
			stizzy <- addLayer(stizzy, raster(paste( rootDir,file,  sep="")) )
		}

		# average the stack and write out

		outpath <- paste(rootDir, 'monthtrend/cru_', cvar,'_',month, '.asc', sep="")
		write(outpath, stdout())
		
		stackApply( stizzy, c(1), fun=mean, filename=outpath, na.rm=TRUE)
		write('done writing', stdout());
		write('', stdout());
		

	}
}
cvars <- c('pre')
calcMonthAverages(cvars[1])




# average them bitches



