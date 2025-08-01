"""Importer Module"""
import rasterio
import pathlib

from pathlib import Path
from rasterio import DatasetReader, DatasetBase

# path to raster file
raster_path = pathlib.Path('/Users/martinreger/Desktop/Python/pysasd/pysasd/data/dop_kacheln/dop10rgbi_32_346_5632_1_nw_2025.jp2')

def read_rasterfile(filepath: Path) -> dict:
    """
    Function to read a rasterfile into rasterio DatasetReader

    :param filepath: Path to rasterfile
    """

    with rasterio.open(
        fp=filepath,
        mode="r"
        ) as src:

        band_1_data = src.read(1)
        band_2_data = src.read(2)
        band_3_data = src.read(3)
        band_4_data = src.read(4)

        band_data = {"band_1": band_1_data,
                     "band_2": band_2_data,
                     "band_3": band_3_data,
                     "band_4": band_4_data}

        return band_data

print(read_rasterfile(raster_path)["band_1"])
