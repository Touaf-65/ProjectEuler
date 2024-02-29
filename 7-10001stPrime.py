#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 03:01:35 2024

@author: touaf
"""

def isPrime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

def nthPrime(n):
    primes = [2,3]
    if n in [1,2]:
        return primes[n-1]
    else:
        i = 3
        while len(primes) < n:
            i +=2 
            if isPrime(i):
                primes.append(i)
    return primes[-1]

if __name__ == '__main__':
    print(nthPrime(10001))
