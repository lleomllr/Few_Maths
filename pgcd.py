#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:39:51 2022

@author: lm174023
"""

"""recursive"""
    
def euclide(a, b, r): 
    if a==0: 
        return b 
    if b==0:
        return a 
    if(a==b): 
        return a 
    if b%a==0: 
        return b 
    else: 
        a=b
        b=r
        r=a%b
        return euclide(b, r)

"""itératif"""

def euclide_2(a, b, r): 
    r=a%b
    if b%a==0: 
        return b
    else: 
        b=a%b
        a=b
        b=r
    return a

