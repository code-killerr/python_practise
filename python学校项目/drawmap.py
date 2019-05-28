# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:30:59 2019

@author: CodeKiller
"""

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import random

def printcolor():
    plt.figure(figsize=(16,8))
    m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
    m.drawcoastlines()
    m.drawcountries(linewidth=1.5)
    m.readshapefile('gadm36_TWN_shp/gadm36_TWN_1', 'taiwan', drawbounds=True)
    m.readshapefile('gadm36_CHN_shp/gadm36_CHN_1', 'china', drawbounds=True)
    ax = plt.gca()
    for nshape, seg in enumerate(m.china):
        poly = Polygon(seg, facecolor=(random.uniform(1,0),random.uniform(1,0),random.uniform(1,0)))
        ax.add_patch(poly)
    for nshape, seg in enumerate(m.taiwan):
        poly = Polygon(seg, facecolor=(random.uniform(1,0),random.uniform(1,0),random.uniform(1,0)))
        ax.add_patch(poly)
    plt.show()
    
def earth():
        # 更改投影方式
    map = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 0) #’ortho’指正射投影，具体参数后面再讨论；后面两个参数是设置中心点
    
    # 给整个地图上蓝色
    map.drawmapboundary(fill_color = 'aqua')
    
    # 给陆地涂上珊瑚色，湖泊涂上蓝色
    map.fillcontinents(color = 'coral', lake_color = 'aqua')
    
    # 画图
    map.drawcoastlines()
    
    # 显示结果
    plt.show()