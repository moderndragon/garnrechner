#/usr/bin/python
# -*- coding: utf-8 -*-

#This tool calculates the amount of needed yarn for a cardweaving project.

# measurement unit
unit = raw_input("Which unit do you use?\nPlease type m for meters or f for feet:")

# number of holes per card; usually, but not always, 4
nh = int(raw_input("How many holes per card do you use?"))

# number of cards
nc = int(raw_input("How many cards do you use?"))

# nhtot = number of holes in total
nhtot = nc * nh

# length of warp; maybe to be taken over from wlc.py
lw = float(raw_input("How long is your warp?"))

# ncol = number of colours
# The maximal number of colours for cardweaving is usually 3.
ncol = int(raw_input("How many colours does your pattern use?\nPlease type '2' or '3':"))

# col1 = first colour
col1 = raw_input("Please name your first colour:")

# hc1 = number of holes with colour 1
hc1 = int(raw_input("How many holes of your pattern are in that colour?"))

# length of skein; use could be simplified if I check if all the skeins are equal via an additional if statement
sc1 = int(raw_input("How much yarn is on a skein of this yarn (yards/meters)?"))

# col2 = second colour
col2 = raw_input("Please name your second colour:")

# hc2 = number of holes with colour 2
hc2 = int(raw_input("How many holes of your pattern are in that colour?"))

# length of skein
sc2 = int(raw_input("How much yarn is on a skein of this yarn (yards/meters)?"))

#length of yarn needed for col1
lcol1 = lw * hc1

# number of skeins of col1
nsk1 = lcol1//sc1 +1

#length of yarn needed for col2
lcol2 = lw * hc2

# number of skeins of col2
nsk2 = lcol2//sc2 +1

if ncol == 2:
	print "You need", nsk1, "balls of", col1, "yarn\nand", nsk2, "balls of", col2, "yarn."

else:
	# col3 = third colour.
	col3 = raw_input("Please name your third colour:")
	
	# hc3 = number of holes with colour 3
	hc3 = int(raw_input("How many holes of your pattern are in that colour?"))
	
	# length of skein
	sc3 = int(raw_input("How much yarn is on a skein of this yarn (yards/meters)?"))
	
	#length of yarn needed for col3
	lcol3 = lw * hc3
	
	# number of skeins of col3
	nsk3 = lcol3//sc3 +1
	
	print "You need", nsk1, "balls of", col1, "yarn,\n", nsk2, "balls of", col2, "yarn\nand", nsk3, "balls of", col3, "yarn."

print "Your pattern uses", nhtot * lw, unit, "of yarn."
