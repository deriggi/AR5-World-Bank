library(raster)
doIt <- function (){
	rootDir <- "F:/climate/monthly/tas/countries/BGD/ensemblestacked_50_/converted/"
	allFiles <- list.files(rootDir, full.names=FALSE, pattern=".*\\.tif$")
	months <- c(1:12)

	for ( aFile in allFiles ){
		
		fullPath <- paste(rootDir,aFile,sep="")
		write(aFile,stdout())
		for (month in months){
			themean <- cellStats ( raster(fullPath, band=month), stat='mean' )
			
			write( themean, stdout())
			
		}
		write('', stdout())
	}
}

doIt()