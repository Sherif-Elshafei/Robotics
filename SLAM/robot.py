#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:59:32 2021

@author: sherif
"""
class Robot:
    def __init__(self, initial_loc, sensor_cov=[[1,0],[0,1]], motion_cov=[[1,1],[1,2]]):
        self.x = initial_loc
        self.sensor_cov = sensor_cov #covariance of the measurement error
        self.motion_cov = motion_cov #covariance of the motion error
    
    def u_to_cov(self,u,motion_cov):
        #The coviariance of the sensing process is variant of the motion traversed.
        #That is why we have to have a motion_cov to be dependent on the motion. 
        N=(1/1)*np.sqrt(u[0]*u[0] + u[1]*u[1])
        return [[x*N for x in y] for y in motion_cov]
        
    def move(self, u):
        #cov_t = u_to_cov(u, self.motion_cov)#2x2 covariance matrix. since motion_cov changes as 
                                            #robot takes more steps, cov gets cascadedly worse. 
                                            #The update to motion_cov is cascadedly made here. 
                                            #The formula to update cov can be found
        cov_t = self.u_to_cov(u,self.motion_cov)
        self.x += 1*u + np.random.multivariate_normal([0,0], cov_t)#Simple motion model. New location is old
                                                                 #location + motion command*delta t + error
        
    def sense(self):
        # the relationship between z and x depends on the sensor. 
        #The main idea is that measurements by the sensor shall correct x.
        
        #sensor_cov could have changed had we have the cov of the sensing mechanism variant of the sensing process
        z = self.x + np.random.multivariate_normal([0,0], self.sensor_cov)  
        return z #z is the result of measuring distance of the robot to known-location landmarks.