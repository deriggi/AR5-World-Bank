## Climate data processing
Here I will host the simple scripts and processes I have used for the climate data processing I'm doing for the World Bank. Most of the work was done with the r package called raster. I also did some processing with gdal using the osgeo4w toolset

### Rotating the files
Many climate models a longitudnal scale which runs from 0 -> 360 instead of the standard 0 -> -180. For these data sets we first had to rotate the data

![Alt text](rotate.png)




