#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os, sys
# input measurement unit
unit = raw_input("Please specify a measurement unit (yards or meters):")

# length of yarn sample
l1 = int(raw_input("please specify the length of your yarn sample:"))

# weight of yarn sample
w1 =  int(raw_input("please specify the weight of your yarn sample:"))

# weight of other skein
w2 = int(raw_input("please specify the weight of the other skein:"))

# calculation
l2 = l1 * w2 / w1

print "The length of your skein is approx.", l2, unit
