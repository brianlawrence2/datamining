#!/usr/bin/env python

'''This module contains functions for each descriptive statistic found in secion 2.2 of Data Mining: Concepts and Techniques'''

#allows for easy summation of a list of values
def sum(values):
    if len(values) == 1:
        return values[0]
    else:
        return values[0] + sum(values[1:])

def mean(values):
    return sum(values)/len(values)
