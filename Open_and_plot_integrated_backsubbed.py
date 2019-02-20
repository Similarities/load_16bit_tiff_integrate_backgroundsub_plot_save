#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:54:54 2019

@author: similarities
"""

import matplotlib.pyplot as plt
import numpy as np


class Open_and_Plot_Picture:
        def __init__(self, filename, filedescription, xlabel, ylabel,xmin, xmax, ymin, ymax):
            self.filename = filename
            self.filedescription= filedescription
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.ymin = ymin
            self.xmin = xmin
            self.ymax = ymax
            self.xmax = xmax
            self.picture = np.empty([])
            self.integrated= np.empty([])
            self.x_backsubstracted=np.empty([2048, 2048])


        def open_file(self):
            self.picture = plt.imread(self.filename)
            #plt.figure(10)
            #plt.imshow (self.picture, label=self.filedescription)
            #plt.title(self.filedescription, fontdict=None, loc='center', pad=None)
            #plt.legend() #handles=[plot]
            #plt.ylabel(self.ylabel)
            #plt.xlabel(self.xlabel)
            return self.picture
            
        def integrate_and_plot(self):
            self.integrated = np.sum(self.picture[:,self.xmin:self.xmax], axis = 1)          
            #plt.figure(1)
            #plt.plot(self.integrated,label=self.filedescription,linewidth=0.5)
            #plt.legend()
            return self.integrated
        
        def background(self):
            back_mean=np.mean(self.picture[:, 1692:2048], axis = 1)
            i=1
            j=0
            N=len(self.picture)-1
            
            while i<= N:
                
                self.x_backsubstracted[::,i] = self.picture[::,i]- back_mean[i]

                i = i+1
                
                
            plt.figure(3)
            
            plt.imshow(self.x_backsubstracted)
            self.integrated= np.sum(self.x_backsubstracted[:,self.xmin:self.xmax], axis = 1)

            plt.figure(4)
            plt.plot(self.integrated,label=self.filedescription + "backsubbed",linewidth=0.5)

            plt.legend()
            print(len(self.integrated), 'length of ROI')
            np.savetxt(self.filedescription + '_backsubbed_integrated', self.integrated, delimiter='', fmt='%1.4e')   # use exponential notation
            return self.integrated
        
       # def grating_function(self):
          #  N = len
           # while
           # self.integrated[i,0] = f(x)*self.integrated[i,0]
           # create new x array: make 2D array






            
        



Picture1=Open_and_Plot_Picture('spectro1__Fri Jan 25 2019_14.21.28_20.tif', '20190125_20', 'px', 'px',0,1500,0,2048)
Picture1.open_file()
#Picture1.integrate_and_plot()
Picture1.background()

Picture2=Open_and_Plot_Picture('spectro1__Fri Jan 25 2019_14.35.18_29.tif', '20190125_29', 'px', 'px',0,1500,0,2048)
Picture2.open_file()
#Picture2.integrate_and_plot()
Picture2.background()