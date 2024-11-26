"""
 * author: Ohidul Islam
 * created on 26-11-2024-11h-18m
 * copyright 2024
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata
import os

plt.rcParams.update({"font.family": "Times New Roman", "font.size": 18})


# csv file loading
path = "ewfd_Hz_data_back_prop_port1.csv"

####################################################################


def csv_load(path):
    '''load a csv file created from comsol data export.
    return x,y coordinates and corresponding value.
    '''

    df = pd.read_csv(path, delimiter=",", skiprows=8)
    df.columns = ["X", "Y", "data"]
    print("csv file loaded")

    # column data extraction
    x = df["X"].values
    y = df["Y"].values
    data = df["data"].values

    return [x, y, data]

####################################################################


def create_image_from_data(points=100, x=[], y=[], data=[], filename=''):
    '''

    '''
    # Create a grid for X and Y
    x_unique = np.linspace(x.min(), x.max(), points)
    y_unique = np.linspace(y.min(), y.max(), points)
    X_grid, Y_grid = np.meshgrid(x_unique, y_unique)
    print("XY grid created")

    abs_hz_grid = griddata((x, y), data, (X_grid, Y_grid), method="linear")
    print("image data interpolated")

    # Plot the colormap
    plt.figure(figsize=(8, 6))
    plt.pcolormesh(X_grid, Y_grid, abs_hz_grid, shading="auto", cmap="hot")
    plt.axis('off')

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"image saved at this location: {filename}")


# plt.show()
