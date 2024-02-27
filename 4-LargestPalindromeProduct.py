#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:59:42 2024

@author: touaf
"""

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False



if __name__ == '__main__':
    largestPalindrome = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if isPalindrome(i * j) and (i * j) > largestPalindrome:
                largestPalindrome = i * j
    print(largestPalindrome)
                