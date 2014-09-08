library(raster)
doIt <- function (thevar, arealUnit){
	rootDir <- paste("F:/climate/monthly/",thevar, "/",arealUnit,"/", sep="")
	outcsv <- paste("F:/climate/monthly/", thevar, "/",arealUnit,"/model_means.csv", sep="")
	years = c("20", "40", "60", "80")
	template = "monthtrendstacked_"

	boundarycodes <- list.files(rootDir, full.names=FALSE)
	sort(boundarycodes)
	months <- c(1:12)

	for ( acode in boundarycodes ){

		for ( y in years ){	

			fullPath <- paste(rootDir,acode,'/',template, y,'_/',sep="")
			write( fullPath, stdout() )

			rasterfiles <- list.files(fullPath, full.names=FALSE, pattern=".*\\.tif$")

			for (razzy in rasterfiles){
				
				write(razzy, stdout())

				for (month in months){
					
					themean <- cellStats ( raster( paste(fullPath,razzy,  sep=""), band=month), stat='mean' )
					
					write(  paste(razzy, acode,  month, themean, sep=",") , file=outcsv, append=TRUE, sep="\n" )
					
				}

			}

			write('', stdout())

		}
	}
}

doItEnsembleStyle <- function (thevar, arealUnit){
	rootDir <- paste("F:/climate/monthly/",thevar, "/",arealUnit,"/", sep="")
	outcsv <- paste("F:/climate/monthly/", thevar, "/",arealUnit,"/ensemble_means.csv", sep="")
	years = c("10", "50", "90")
	template = "ensemblestacked_"

	boundarycodes <- list.files(rootDir, full.names=FALSE)
	months <- c(1:12)

	for ( acode in boundarycodes ){

		for ( y in years ){	

			fullPath <- paste(rootDir,acode,'/',template, y,'/',sep="")
			write( fullPath, stdout() )

			rasterfiles <- list.files(fullPath, full.names=FALSE, pattern=".*\\.tif$")

			for (razzy in rasterfiles){
				
				write(razzy, stdout())

				for (month in months){
					
					themean <- cellStats ( raster( paste(fullPath,razzy,  sep=""), band=month), stat='mean' )
					
					write(  paste(razzy, acode,  month, themean, sep=","), file=outcsv, append=TRUE, sep="\n" )
					
				}

			}

			write('', stdout())

		}
	}
}


# firstCellAverage <- function (){
# 	rootDir <- "F:/climate/monthly/pr/countries/BGD/ensemblestacked_50_/converted/"
# 	allFiles <- list.files(rootDir, full.names=FALSE, pattern=".*\\.tif$")
# 	months <- c(1:12)

# 	for ( aFile in allFiles ){
		
# 		fullPath <- paste(rootDir,aFile,sep="")
# 		write(aFile,stdout())
# 		for (month in months){
# 			theval <- getValues ( raster(fullPath, band=month) )[1]
			
# 			write( theval, stdout())
			
# 		}
# 		write('', stdout())
# 	}
# }


doItEnsembleStyle('pr', 'regions')
doItEnsembleStyle('tas', 'regions')
doItEnsembleStyle('tasmin', 'regions')
doItEnsembleStyle('tasmax', 'regions')