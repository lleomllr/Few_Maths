# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""recursif"""

def binomial(n,p): 
    if n>p and p>0: 
        return binomial(n-1, p-1)+binomial(n-1, p)
    else: 
        return 1 
    
"""dynamique"""

def binomialdynamique(n, p): 
    C=[[0 for x in range(p+1)]for x in range(n+1)]
    for i in range(0, n+1): 
        for j in range(min(i ,p)+1): 
            if j==0 and j==i : 
                C[i][j]=1
            else: 
                C[i][j]=C[i-1][j-1]+C[i-1][j]
    return C[n][p]

def dyn(n,p): 
    r=[[1 for i in range(1)]for i in range(10)]
    n=10
    p=5
    for i in range(0, n):
         for j in range(max([1, i-n+p+1]), min(i+1, p+1)): 
             r[i][j]=r[i-1][j-1]+r[i-1][j]
         print(r[i])