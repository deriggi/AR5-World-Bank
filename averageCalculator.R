library(raster)
doIt <- function (){
	rootDir <- "F:/climate/monthly/tas/countries/"
	years = c("20", "40", "60", "80")
	template = "monthtrendstacked_"
	boundarycodes <- list.files(rootDir, full.names=FALSE)
	months <- c(1:12)

	for ( acode in boundarycodes ){

		for ( y in years ){	

			fullPath <- paste(rootDir,acode,'/',template, y,'/',sep="")
			write( fullPath, stdout() )

			rasterfiles <- list.files(fullPath, full.names=TRUE, pattern=".*\\.tif$")

			for (razzy in rasterfiles){
				
				write(razzy, stdout())

				for (month in months){
					
					themean <- cellStats ( raster(razzy, band=month), stat='mean' )
					
					write(  paste('month ', month,' ', themean, sep=""), stdout() )
					
				}

			}

			write('', stdout())

		}
	}
}

firstCellAverage <- function (){
	rootDir <- "F:/climate/monthly/pr/countries/BGD/ensemblestacked_50_/converted/"
	allFiles <- list.files(rootDir, full.names=FALSE, pattern=".*\\.tif$")
	months <- c(1:12)

	for ( aFile in allFiles ){
		
		fullPath <- paste(rootDir,aFile,sep="")
		write(aFile,stdout())
		for (month in months){
			theval <- getValues ( raster(fullPath, band=month) )[1]
			
			write( theval, stdout())
			
		}
		write('', stdout())
	}
}


doIt()