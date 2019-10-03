#!/usr/bin/env python
#-*- coding:utf-8 -*-
def bubble_sort(str):
    for i in  range(len(str) -1):
        for j in range(len(str)-i-1):
            if str[j] > str[j+1]:
                str[j],str[j+1]=str[j+1],str[j]
    return str
str=[1,345,454,345,12,45,45,33,2,1,4]
print (bubble_sort(str))