pr = raster("C:\\Users\\Johnny\\Documents\\climatev2\\testproutTifffs\\pr_Amon_CNRM-CM5_rcp26_r1i1p1_205601-210012.tif")
pr_rotated <- rotate(pr)
plot(pr_rotated)
writeRaster(pr_rotated, "C:\\Users\\Johnny\\Documents\\climatev2\\testproutTifffs\\pr_cnrm_rotated_2.tif")
