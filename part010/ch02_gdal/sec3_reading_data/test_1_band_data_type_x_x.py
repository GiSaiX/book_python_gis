# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import gdalconst
dir(gdalconst)

################################################################################
from osgeo import gdal
rds = gdal.Open("/gdata/geotiff_file.tif")
band = rds.GetRasterBand(1)
band.DataType
