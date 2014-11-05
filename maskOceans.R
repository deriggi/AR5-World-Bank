library(raster)


maskAllLoop <- function(maskT){
	cvars <- c('pr','tas', 'tasmin', 'tasmax')
	years <- c(20, 40, 60, 80)
	# years <- c(10, 50, 90)

	for (cvar in cvars){
		for (y in years){
			maskAll(maskT,cvar,y)
		}
	}
}

maskAll <- function(maskTemplate, cvar, year){
	basePath <- "F:/climate/anom/"
	landcover <- raster(maskTemplate)
	# rootFolder <- paste("F:/climate/monthly/",cvar,"/ensemblestacked_",year,"/converted/", sep="")
	rootFolder <- paste(basePath,cvar,"_",year,'/', sep="")

	allFiles <- list.files(rootFolder, full.names=FALSE, pattern=".*\\.tif$")

	template_raster <- raster(aWeeCru)

	outdir <- paste(basePath, 'masked/' ,cvar, '_',year ,'/',sep="")
	dir.create(outdir, recursive=TRUE)

	for (oneFile in allFiles){
		
		thisPath <-  paste(rootFolder,oneFile, sep="") 
		thisRaster <- stack(thisPath)

		peerfolderPath <- substr(rootFolder, 0, nchar(rootFolder)-10)

		

		outpath <- paste(outdir,oneFile,sep="")

		write(outdir, stdout())
		
		resampled_template <- resample(template_raster, thisRaster, method='bilinear')

		mask(thisRaster, resampled_template, filename=outpath)

	}

}

aWeeCru <- "F:/climate/raster/cru_ts_3_10_01.1901.2009.pre_1901_1.asc"
maskAllLoop(aWeeCru)