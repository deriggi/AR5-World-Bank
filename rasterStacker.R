
# allfiles <- list all files
rootDir <- "F:/climate/monthly/pr/monthtrend_20"
allFiles <- list.files(rootDir, full.names=TRUE)
innerParts <- list()

i <- 0

for (file in allFiles){
	part <- unlist(strsplit(file, '_'))
	part <- paste(part[3], part[4], part[5], part[6], part[7], sep='_')
	# part <- part[2:6]
	if( !(part %in% innerParts) ){
		innerParts[i] <- part
		write(part, stdout())
		i <- i +1

	}
}

for (part in innerParts){
	pat = paste(".*", part, ".*\\.tif$", sep="")
	allFiles <- list.files(rootDir, full.names=TRUE, pattern=pat)
	write(allFiles, stdout())
	write('', stdout())	
}


## TODO, use python to rename all files so they are 01 instead of 1 on months
# v <- get inner part of all in allFiles
# prestack <- for each v, get 12 from allfiles that are like it
# prestack <- sort this
# stack <- stack it and write to file