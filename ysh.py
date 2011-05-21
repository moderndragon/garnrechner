#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os, sys 
# name of yarn a
na = raw_input("What is the name of the yarn given in the pattern?")

# meters per skein of yarn a
la = int(raw_input("How many meters is a skein of the yarn given in the pattern? "))

#name of yarn b
nb = raw_input("What is the name of your yarn?")

# meters per skein of yarn b
lb = int(raw_input("How many meters is a skein of your yarn? "))

# number of skeins of yarn a
x = int(raw_input("please specify the number of skeins given in the pattern (integer): "))

# total length
ltot = la * x

# number of necessary skeins of yarn b
y = x * la // lb + 1

print "You need", ltot, "meters of yarn for your project."
print "You need", y, "skeins of",  nb,"."
