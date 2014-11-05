
library(raster)

# cvars <- ('pr', 'tas', 'tasmin', 'tasmax')

doAnomEnsemble <- function(cvar){
	tenthpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.10), na.rm=na.rm));}
	fiftiethpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.50), na.rm=na.rm));}
	ninetiethpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.90), na.rm=na.rm));}

	percentilefunctions <-  c(tenthpercentile, fiftiethpercentile, ninetiethpercentile)
	outnames <- c('ensemble_10th/', 'ensemble_50th/', 'ensemble_90th/')
	rcps <- c('rcp26', 'rcp45', 'rcp60', 'rcp85')
	months <- c(1:12)
	startyears <- c(2020,2040,2060,2080)
	write('starting',stdout())

	pindex <- 0
	for (pfunc in percentilefunctions){
		pindex <- pindex + 1
		for (sy in startyears){
			
			write(paste('year:', sy), stdout())

			# F:\climate\anom\masked\pr_20
			rootDir <- paste("F:/climate/anom/masked/",cvar,"_",sy-2000,"/",sep="")
			output_folder <- paste("F:/climate/anom/masked/",cvar,"/",outnames[pindex], sep="")
			dir.create(output_folder, recursive=TRUE)
			write('created folder', stdout())
			for (rcp in rcps){
				
				allFiles <- list.files(rootDir, full.names=TRUE, pattern=paste(".*",rcp,".*\\.tif$", sep=""))
				write( paste('creatign from ', allFiles[1], sep="") )
				template_raster <- raster(allFiles[1], band=1)
				write(paste('rcp', rcp), stdout())

				yearLongStack <- stack()
				write('entering month loop', stdout())
				
				for (month in months){
					
					write(paste('month', month), stdout())
					myStack <- stack()
					
					write('reading all files', stdout())

					# make a stack by plucking out the same month from every file
					for (x in allFiles){
						resampled_x <- resample(raster(x, band=month), template_raster, method='bilinear')
						myStack <- addLayer(myStack,resampled_x)
						# write(nlayers(myStack), stdout())
					}

					write('taking percentile', stdout())

					aMonthRaster <- stackApply(myStack, c(1), fun=pfunc)
					# TODO accumulate a stack of 12 and write out
					yearLongStack <- addLayer(yearLongStack, aMonthRaster)

				}
				
				write(paste(output_folder,paste(rcp,sy,'.tif',sep='_') ), stdout())
				# TODO accumulate a stack of 12 and write out
				writeRaster ( yearLongStack, filename=paste(output_folder,paste(rcp,sy,'.tif',sep='_') ))

			}
		}
	}
}
doAnomEnsemble('pr')
doAnomEnsemble('tas')
doAnomEnsemble('tasmax')
doAnomEnsemble('tasmin')