from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,5))
map = Basemap(projection='moll', lat_0=0, lon_0=0)

map.drawmapboundary()
map.drawcoastlines()

xs, ys = map(180/np.pi*ra, 180/np.pi*dec)

map.scatter(xs, ys, marker='X', color='black', label='Source')

plt.legend(bbox_to_anchor=(0.3, 1.0))