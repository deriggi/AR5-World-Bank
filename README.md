## Climate data processing
Here I will host the simple scripts and processes I have used for the climate data processing I'm doing for the World Bank. Most of the work was done with the r package called raster. I also did some processing with gdal using the osgeo4w toolset

## Converting to GeoTiff
A python script was used to pluck out the years we wanted from the netcdf and then convert them to GeoTiff. The end result was geotiff files in full time-series from 2020-2039, 2040-2059, 2060-2079, and 2080-2099. 

### Rotating the files
Many climate models a longitudnal scale which runs from 0 -> 360 instead of the standard 0 -> -180. For these data sets we first had to rotate the data

![Alt text](images/rotation.png)

[Iterating through many files and rotating them](https://github.com/deriggi/AR5-World-Bank/blob/master/rotateAll.R)

### Rotating the files




