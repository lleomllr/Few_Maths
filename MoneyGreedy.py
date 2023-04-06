#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:10:05 2022

@author: lm174023
"""

def rendumonnaie(a): 
    S=[]
    i=0
    L=[500, 200, 100, 50, 20, 10, 5, 2, 1]
    n=a
    while n>0: 
        if n>=L[i]: 
            n=n-L[i]
            S.append(L[i])
        else: 
            i=i+1
    print(S)
    
    
    
def sac(p, q, k): 
    volume=30
    valeur=0
    q=[13, 12, 8, 10]
    p=[7, 4, 3, 3]
    nbp=len(p)
    while volume>0 and nbp>0:
        i=maxi(p)
        if volume>q[i]: 
            volume -= q[i]
            valeur+=q[i]*p[i]
            p[i]=0
            nbp=-1
        else: 
            valeur+=volume*p[i]
            volume=0
    print(valeur)
    
def maxi(L): 
    m=L[0]
    imax=0
    for i in range(1, len(L)): 
        if L[i]>m: 
            m=L[i]
            imax=i
    return imax 
