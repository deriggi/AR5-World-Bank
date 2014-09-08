library(raster, year)

rotateAll<- function (cvar, year){

	rootDir <- paste("F:/climate/historical/",cvar,"/outgeotiff_", year,"/", sep="")
	output_folder <- paste("F:/climate/historical/",cvar,"/outgeotiff_",year,"_rotated/", sep="")
	write(output_folder,stdout());

	dir.create(output_folder)

	path_length <- nchar(rootDir)
	allFiles <- list.files(rootDir, full.names=TRUE, pattern="\\.tif$")

	lapply(allFiles, function(x){
		raster_x <- stack(x)
		raster_x_rotated <- rotate(raster_x)

		outfilename<-substr(x, path_length+1, nchar(x))
		outfilename<-paste(output_folder,outfilename, sep='/')
		writeRaster(raster_x_rotated, outfilename)

	# write(paste(output_folder,outfilename, sep='/'), stdout())

	})
}

runRotation <- function (){
	years <- c('1965', '1985')
	cvars <- c('tasmin','tasmax','tas','pr')
	for (year in years){
		for (cvar in cvars){
			rotateAll(cvar,year)
		}
	}
}

runRotation();


# tenthpercentile <- function(x, na.rm=true){ return (quantile(x, c(0.10), na.rm=na.rm));} 
# disaggall <- function(x, na.rm=true){ return (disaggregate(x, fact=6, na.rm=na.rm, method='bilinear'));} 

# v1_high <- stackApply(v1, indices, disaggall, filename='D:\\climate\\monthly\\pr\\outgeotiff_20_rotated_backup\\pr_Amon_bcc-csm1-1_rcp26_r1i1p1_202001-203912_as.tif', bylayer=TRUE, format='ascii', numbers='TRUE')