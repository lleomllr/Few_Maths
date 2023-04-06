#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:31:01 2022

@author: lm174023
"""

def syracuse(n): 
    x=[n]
    if n==1: 
        x[n]=x
    while x[n]!=1: 
        if x[n]%2==0: 
            x[n]=x[n+1]
            x[n+1]=x[n]/2
        else: 
            x[n]=x[n+1]
            x[n+1]=3*x[n]+1
    return x[n]