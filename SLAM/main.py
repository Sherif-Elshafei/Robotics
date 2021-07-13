#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:59:32 2021

@author: sherif
"""
import utilities
import robot

# Real robot
robot = Robot([0,0.1])

# Control inputs
# this can be replaced later by the results from motion estimation from sequence of images
U = [(10,0), (0,5), (-11,0), (7,7)]
U = np.asarray(U)

# Initial belief
#Location of the robot now is at [0,0] with a cov 
mean = [0,0]
cov = np.array([[2.0,0.002],[0.002, 4.0]])

#Covariance of the measurement
Q = robot.sensor_cov

for u in U:
    # Move the robot
    print("inside u in U")
    robot.move(u)
    
    # Update the belief based on motion model
    #mean, cov_t = prob_motion(mean, u, motion_cov)
    mean += u
    
    # Additive error
    cov += robot.u_to_cov(u,robot.motion_cov) #cov_t is the prediction covariance
    
    # Measurement
    z = robot.sense()

    # Kalman gain
    k = np.dot(cov, np.linalg.inv(cov + Q)) # Q is the covariance of the measurement
    mean = mean + np.dot(k,(z-mean))
    cov = np.dot(np.identity(2) - k, cov)
    
    plot_confidence_ellipse(mean, cov)
    
