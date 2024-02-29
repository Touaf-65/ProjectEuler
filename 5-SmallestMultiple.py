#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:50:52 2024

@author: touaf
"""
def isPrime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    divs, tuples = [], {}
    while n != 1:
        for i in range(2,n+1):
            if n % i == 0 and isPrime(i) :
                divs.append(i)
                n = n//i
    for i in divs:
        if i not in tuples:
            tuples[i] = divs.count(i)
    return tuples

def ppcm(m,n):
    """returns the smallest multiple of two integers"""
    divs = divisors(m)
    for i in divisors(n).keys():
        if i not in divs.keys():
            divs[i] = divisors(n)[i]
        else:
            if divisors(n)[i] > divs[i]:
                divs[i] = divisors(n)[i]
    print(divs)
    
def ppcm2(list):
    """returns the smallest multiple of a list of integers"""
    divs = divisors(list[0])
    for n in list[1:]:
        for i in divisors(n).keys():
            if i not in divs.keys():
                divs[i] = divisors(n)[i]
            else:
                if divisors(n)[i] > divs[i]:
                    divs[i] = divisors(n)[i]
    prod = 1
    for i,y in divs.items():
        prod *= i**y

    return prod
         

    
if __name__ == '__main__':


     print(ppcm2([i for i in range(1,21)]))
        
    