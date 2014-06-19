library(raster)

toMm <- function(x, na.rm=TRUE){ 
	mm <- x*30*3600*24;
	return (mm);
}

toCelsius <- function(y, na.rm=TRUE){ return  (y - 273.15) }

convertData <- function(){
	indices <- c(1:12)
	cvars <- c('pr','tas', 'tasmin', 'tasmax')
	# years <- c(20, 40, 60, 80)
	years <- c(10, 50, 90)

	for (year in years){
		for (cvar in cvars){
			# rootDir <- paste('F:/climate/monthly/',cvar,'/countries/BGD/ensemblestacked_',year,'_/', sep='')

			# rootDir <- paste('F:/climate/monthly/',cvar,'/monthtrendstacked_',year,'/', sep='')
			rootDir <- paste('F:/climate/monthly/',cvar,'/ensemblestacked_',year,'/', sep='')
			
			allFiles <- list.files(rootDir, full.names=FALSE, pattern=".*\\.tif$")
			
			for (oneFile in allFiles){
				stizzy <- stack( paste(rootDir,oneFile, sep="") )
				outdir <- paste(rootDir,'converted/',sep="")

				dir.create( outdir )
				outpath <- paste( outdir,oneFile, sep="")

				if(cvar == 'pr'){
									
					stackApply(stizzy, indices, toMm, filename=outpath )

				}else{

					stackApply(stizzy, indices, toCelsius, filename=outpath )

				}

				# stackApply( filename='' )
				
			}
		}
	}
}

convertData()
