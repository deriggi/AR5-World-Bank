tenthpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.10), na.rm=na.rm));}
fiftiethpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.50), na.rm=na.rm));}
ninetiethpercentile <- function(x, na.rm=TRUE){ return (quantile(x, c(0.90), na.rm=na.rm));}

library(raster)

# cvars <- ('pr', 'tas', 'tasmin', 'tasmax')
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

		# F:\climate\monthly\pr\monthtrendstacked_20
		rootDir <- paste("F:/climate/monthly/tasmax/monthtrendstacked_",sy-2000,"/",sep="")
		output_folder <- paste("F:/climate/monthly/tasmax/",outnames[pindex], sep="")
		dir.create(output_folder)

		for (rcp in rcps){
			
			allFiles <- list.files(rootDir, full.names=TRUE, pattern=paste(".*",rcp,".*\\.tif$", sep=""))
			template_raster <- raster(allFiles[1], band=1)
			write(paste('rcp', rcp), stdout())

			for (month in months){
				
				write(paste('month', month), stdout())
				myStack <- stack()
				
				# make a stack by plucking out the same month from every file
				for (x in allFiles){
					resampled_x <- resample(raster(x, band=month), template_raster, method='bilinear')
					myStack <- addLayer(myStack,resampled_x)
					# write(nlayers(myStack), stdout())
				}

				stackApply(myStack, c(1), fun=pfunc, filename=paste(output_folder,paste(rcp,sy,month,'.tif',sep='_'), sep=''))

			}

			
		}
	}
}

# rename each file so it has full path


# lapply(allFiles, function(x){
# 	 resampled_x <- resample(raster(x, bands=1), template_raster, method='bilinear')
# 	 myStack <- addLayer(myStack,resampled_x)
# 	 write(nlayers(myStack), stdout())
# });

# stackApply(myStack, c(1), fun=tenthpercentile, filename=paste(output_folder,'rcp26test1.tif', sep=''))






# lapply(allFiles, function(x){
# 	raster_x <- stack(x)
# 	raster_x_rotated <- rotate(raster_x)

# 	outfilename<-substr(x, path_length+1, nchar(x))
# 	outfilename<-paste(output_folder,outfilename, sep='/')
# 	writeRaster(raster_x_rotated, outfilename)

# 	# write(paste(output_folder,outfilename, sep='/'), stdout())

# 	})