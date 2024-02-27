#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:31:36 2024

@author: touaf
"""

"""
un nombre est premier s'il n'est divisible que par un et lui mm.
autrement, avec p un nombre premier, qlq soit n != 1 et n != p, p%n != 0

"""

def isPrime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

def largePrimeFactor(n):
    for i in range(2,n//2 + 1):
        if n % i == 0 and isPrime(i):
            largePrimeFactor = i
    return largePrimeFactor

if __name__ == '__main__':
    
    print(largePrimeFactor(600851475143))
    