#! /usr/bin/python3

# First try at cartopy

# This did NOT work:    pip3 install cartopy
# but this did          sudo apt install python3-cartopy

# Yeah - this example works!!!

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.image import imread

def main():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    ax.set_global()

    # Loading the stock image doesn't work in pyinstall but ...
    #    ax.stock_img()
    # ... we can load it directly instead and viola, it works
    fname='../data/50-natural-earth-1-downsampled.png'
    print('fname=',fname)
    img = imread(fname)
    ax.imshow(img, origin='upper', transform=ccrs.PlateCarree(), extent=[-180, 180, -90, 90])


    ax.coastlines()

    ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.PlateCarree())
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.Geodetic())

    plt.show()


if __name__ == '__main__':
    main()

