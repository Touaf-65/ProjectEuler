#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 02:53:14 2024

@author: touaf
"""

def sumSquareDiff(list):
    sums = sum([i**2 for i in list])
    square = sum(list)**2
    return square - sums 

if __name__ == '__main__':
    print(sumSquareDiff([i for i in range(1,101)]))
    