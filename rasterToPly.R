polys <- rasterToPolygons(r)
writeOGR(polys, "F:\\bangtest", "shapes", driver="ESRI Shapefile")