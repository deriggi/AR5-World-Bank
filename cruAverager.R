library(raster)
averageCrus <- function (){

	# take the rasters that we cout from cruClipper.py and apply this to them

	# the root of the country rasters
	rootDir <- paste("F:/climate/cru/countryout/")
	
	# the csv file with the tabular output
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


countryCruAverage <- function (acode){

	# take the rasters that we cout from cruClipper.py and apply this to them

	# the root of the country rasters
	rootDir <- paste("F:/climate/cru/countryout/")
	
	# the csv file with the tabular output
	outcsv <- paste("F:/climate/cru/countryout/cruaverage.csv")

	rasterfiles <- list.files( paste(rootDir, acode, sep="") , full.names=FALSE, pattern=".*\\.tif$")

	for (razzy in rasterfiles){

		fullPath <- paste(rootDir, acode, '/',razzy,sep="")
		write(fullPath, stdout())

		themean <- cellStats ( raster( fullPath, band=1), stat='mean' )

		write(  paste(razzy, acode,   themean, sep=","), file=outcsv, append=TRUE, sep="\n" )

	}

}

countryCruAverage('HTI')




