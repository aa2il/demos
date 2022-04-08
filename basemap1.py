#! /usr/bin/python3

#Draw an etopo relief image.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

import mpl_toolkits
mpl_toolkits.__path__.append('/usr/lib/python2.7/dist-packages/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

ISELECT=4

if ISELECT==1:
    # setup Lambert Conformal basemap.
    # set resolution=None to skip processing of boundary datasets.
    m = Basemap(width=12000000,height=9000000,projection='lcc',
                resolution=None,lat_1=49.,lat_2=51,lat_0=55,lon_0=-107.)
    m.etopo()

elif ISELECT==2:
    m = Basemap(llcrnrlon=-130.,llcrnrlat=20.,urcrnrlon=-50.,urcrnrlat=45.,
                projection='lcc',lat_0=30,lon_0=-100.,
            resolution ='l',area_thresh=1000.)
    m.shadedrelief()
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.drawmapboundary(fill_color='#99ffff')
    #m.fillcontinents(color='coral',lake_color='aqua')   # Doesn't work
    #m.drawparallels(np.arange(10,70,20),labels=[1,1,0,0])
    #m.drawmeridians(np.arange(-100,0,20),labels=[0,0,0,1])

elif ISELECT==3:
    m = Basemap(projection='cyl', resolution='c',
                llcrnrlat=-90, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180,
                fix_aspect=False)
    m.shadedrelief()
    m.drawstates()

else:

    # create the map
    #m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
    #              projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
    
    m = Basemap(llcrnrlon=-121,llcrnrlat=20,urcrnrlon=-62,urcrnrlat=51,
                  projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

    # load the shapefile, use the name 'states'
    m.readshapefile('st99_d00', name='states', drawbounds=True)
    ax = plt.gca()

    ATOLL_CUTOFF = 0.005
    confirmed=['Arkansas (AR)','California (CA)','Colorado (CO)','Florida (FL)','Idaho (ID)', \
               'Kansas (KS)','Louisiana (LA)','Montana (MT)','North Carolina (NC)','Nebraska (NE)', \
               'Ohio (OH)','Oklahoma (OK)','Oregon (OR)','South Carolina (SC)','Texas (TX)','Utah (UT)', \
               'Virginia (VA)','Washington (WA)','Wisconsin (WI)','Wyoming (WY)']
    confirmed2 = []
    for s in confirmed:
        a=s.split('(')
        confirmed2.append(a[0].strip())

    for i, shapedict in enumerate(m.states_info):
        seg=None
        color='white'
        if shapedict['NAME'] in confirmed2:
            seg = m.states[int(shapedict['SHAPENUM'] - 1)]
            color='red'
            
        # Translate the noncontiguous states:
        # Only include the 8 main islands of Hawaii so that we don't put dots in the western states.
        if shapedict['NAME'] == 'Hawaii' and float(shapedict['AREA']) > ATOLL_CUTOFF:
            if not seg:
                seg = m.states[int(shapedict['SHAPENUM'] - 1)]
            #print('seg=',seg)
            #seg = list(map(lambda (x,y): (x + 5200000, y-1400000), seg))
            seg = list(map(lambda xy: (xy[0] + 5200000, xy[1]-1400000), seg))
                    
        # Alaska is large - rescale it
        elif shapedict['NAME'] == 'Alaska':
            if not seg:
                seg = m.states[int(shapedict['SHAPENUM'] - 1)]
            #print('seg=',seg)
            #seg = list(map(lambda (x,y): (0.35*x + 1100000, 0.35*y-1300000), seg))
            seg = list(map(lambda xy: (0.35*xy[0] + 1100000, 0.35*xy[1]-1300000), seg))

        if seg:
            poly = Polygon(seg, facecolor=color, edgecolor='black', linewidth=.5)
            ax.add_patch(poly)
    
plt.show()
