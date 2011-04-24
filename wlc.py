#/usr/bin/python
# -*- coding: utf-8 -*-

#This little tool calculates the length of the warp needed for a given length of woven ribbon.

unit = raw_input("Please specify if you want to use inches or centimeters.\nUse 'in' for inches or 'cm' for cm:")
lr = int(raw_input("Please specify the desired length of the finished ribbon:"))


if unit == 'cm':
	lw = int(lr + lr*0.2 + 50)
	print "Your warp should be min.", lw, "centimetres long."
else:
	lw = int(lr + lr*0.2 + 20)
	print "Your warp should be min.", lw, "inches long."

