#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:01:28 2021

@author: sherif
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import math

def plot_confidence_ellipse(mean,cov):
    temp1 = (cov[0][0]+cov[1][1])/2
    temp2 = pow(cov[0][0]-cov[1][1],2)/2 + pow(cov[0][1],2)
    lambda1 = temp1+math.sqrt(temp2)
    lambda2 = temp1-math.sqrt(temp2)
    if (cov[0][1] == 0):
        if (cov[0][0]>=cov[1][1]):
            theta = 0
            print('theta=',theta*180/np.pi)
        else:
            theta = 90
            print('theta=',theta*180/np.pi)
    else:
        theta = math.atan2(lambda1-cov[0][0], cov[0][1])
        print('theta=',theta*180/np.pi)
        
    
    ells = [Ellipse((mean[0], mean[1]), math.sqrt(lambda1), math.sqrt(lambda2), theta*180/np.pi)]
    a = plt.subplot(111, aspect='equal')
    for e in ells:
        e.set_clip_box(a.bbox)
        e.set_alpha(0.6)
        a.add_artist(e)
    plt.xlim(-2, 17)
    plt.ylim(-2, 15)

    plt.show()