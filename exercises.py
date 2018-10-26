# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:36:23 2018

@author: owner
"""

def linear(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i
        
    return None