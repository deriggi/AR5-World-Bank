library(raster)


maskAllLoop <- function(maskT){
	cvars <- c('pr','tas', 'tasmin', 'tasmax')
	years <- c(20, 40, 60, 80)

	for (cvar in cvars){
		for (y in years){
			maskAll(maskT,cvar,y)
		}
	}
}

maskAll <- function(maskTemplate, cvar, year){
	
	landcover <- raster(maskTemplate)
	rootFolder <- paste("F:/climate/monthly/",cvar,"/monthtrendstacked_",year,"/converted/", sep="")

	allFiles <- list.files(rootFolder, full.names=FALSE, pattern=".*\\.tif$")

	template_raster <- raster(aWeeCru)

	for (oneFile in allFiles){
		
		thisPath <-  paste(rootFolder,oneFile, sep="") 
		thisRaster <- raster(thisPath)

		peerfolderPath <- substr(rootFolder, 0, nchar(rootFolder)-10)

		outdir <- paste(peerfolderPath,'masked/',sep="")
		dir.create(outdir)

		outpath <- paste(outdir,oneFile,sep="")

		write(outdir, stdout())
		
		resampled_template <- resample(template_raster, thisRaster, method='bilinear')

		mask(raster(thisPath), resampled_template, filename=outpath)

			# outfolder <- 
	}

}

aWeeCru <- "F:/climate/raster/cru_ts_3_10_01.1901.2009.pre_1901_1.asc"
maskAllLoop(aWeeCru)