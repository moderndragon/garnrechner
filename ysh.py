#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os, sys 

# meters per skein of yarn a
la = int(raw_input("please specify the length of the yarn you want to substitute:"))

# meters per skein of yarn b
lb = int(raw_input("please specify the length of your yarn:"))

# number of skeins of yarn a
x = int(raw_input("please specify the number of skeins given in the pattern (integer):"))

# total length
ltot = la * x

# number of necessary skeins of yarn b
y = x * la // lb + 1

print "You need", ltot, "meters of yarn for your project."
print "You need", y, "skeins of your yarn."