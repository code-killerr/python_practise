import mpld3
from django.conf import settings
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex
import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
import random
def popu(req):    
        # 更改投影方式
    plt.figure(figsize=(16,8))
    m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
    m.drawcoastlines()
    m.drawcountries(linewidth=1.5)
    #m.readshapefile('E:\python\python\python_practise\Django\HelloWorld\HelloWorld\china_line_shp\region', 'china', drawbounds=True)
    m.readshapefile('E:\python\python\python_practise\Django\HelloWorld\HelloWorld\gadm36_CHN_shp\gadm36_CHN_1', 'china', drawbounds=True)
    #m.readshapefile('E:\python\python\python_practise\Django\HelloWorld\HelloWorld\gadm36_TWN_shp/gadm36_TWN_1', 'taiwan', drawbounds=True)
    #ax = plt.gca()
    #for nshape, seg in enumerate(m.china):
        #poly = Polygon(seg, facecolor=(random.uniform(1,0),random.uniform(1,0),random.uniform(1,0)))
        #ax.add_patch(poly)
    #for nshape, seg in enumerate(m.taiwan):
     #   poly = Polygon(seg, facecolor=(random.uniform(1,0),random.uniform(1,0),random.uniform(1,0)))
      #  ax.add_patch(poly)
    # 显示结果
    #fig = plt.gcf()
    #html_graph = mpld3.fig_to_html(fig)
    #aaa=html_graph
    #plt.close()
    #print('2333333333333')
    #return HttpResponse(html_graph)