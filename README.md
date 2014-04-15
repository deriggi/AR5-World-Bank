## Climate data processing
Here I will host the simple scripts and processes I have used for the climate data processing I'm doing for the World Bank

### Rotating the files
Many climate models a longitudnal scale which runs from 0 -> 360 instead of the standard 0 -> -180. PUT PICTURE HERE AND STUFF

My first thought was to use the crop and set extent features of GDAL or R where you pluck the eastern half of the file and then set it's extent to -180 -> 0. This is not a bad solution but you then half to stitch the rasters back together and there are all kinds of opportunities for off by one errors.

I'm forging ahead with the raster package of R using the rotate function


