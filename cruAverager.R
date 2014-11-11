library(raster)
averageCrus <- function (){
	rootDir <- paste("F:/climate/cru/countryout/")
	outcsv <- paste("F:/climate/cru/countryout/cruaverage.csv")
	boundarycodes <- list.files(rootDir, full.names=FALSE)

	sort(boundarycodes)
	
	for ( acode in boundarycodes ){

		rasterfiles <- list.files( paste(rootDir, acode, sep="") , full.names=FALSE, pattern=".*\\.tif$")

		for (razzy in rasterfiles){
			
			fullPath <- paste(rootDir, acode, '/',razzy,sep="")
			write(fullPath, stdout())

			themean <- cellStats ( raster( fullPath, band=1), stat='mean' )

			write(  paste(razzy, acode,   themean, sep=","), file=outcsv, append=TRUE, sep="\n" )

		}
	}

}

averageCrus()

# doItEnsembleStyle <- function (thevar, arealUnit){
# 	rootDir <- paste("F:/climate/monthly/",thevar, "/",arealUnit,"/", sep="")
# 	outcsv <- paste("F:/climate/monthly/", thevar, "/",arealUnit,"/ensemble_means.csv", sep="")
# 	years = c("10", "50", "90")
# 	template = "ensemblestacked_"

# 	boundarycodes <- list.files(rootDir, full.names=FALSE)
# 	months <- c(1:12)

# 	for ( acode in boundarycodes ){

# 		for ( y in years ){	

# 			fullPath <- paste(rootDir,acode,'/',template, y,'/',sep="")
# 			write( fullPath, stdout() )

# 			rasterfiles <- list.files(fullPath, full.names=FALSE, pattern=".*\\.tif$")

# 			for (razzy in rasterfiles){
				
# 				write(razzy, stdout())

# 				for (month in months){
					
# 					themean <- cellStats ( raster( paste(fullPath,razzy,  sep=""), band=month), stat='mean' )
					
# 					write(  paste(razzy, acode,  month, themean, sep=","), file=outcsv, append=TRUE, sep="\n" )
					
# 				}

# 			}

# 			write('', stdout())

# 		}
# 	}
# }


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


do