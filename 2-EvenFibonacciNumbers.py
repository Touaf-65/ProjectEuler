#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 07:40:48 2024

@author: touaf
"""

def fib(n):
    fib = [1,2]
    if n <= 2:
        return fib[0:n]
    else:
        for i in range(2,n):
            fib.append(fib[-1] + fib[-2])
    return fib

def fib2(n):
    even = [2]
    fib = [1,2]
    if n == 1:
        return fib[0]
    elif n == 2:
        return fib[1]
    else:
        while True:
            if fib[-1] >= n:
                break
            fib.append(fib[-1] + fib[-2])
            if (fib[-1] + fib[-2]) % 2 == 0:
                even.append(fib[-1] + fib[-2])
        return even[:]
    


if __name__ == '__main__':
    print(sum(fib2(4000000)))