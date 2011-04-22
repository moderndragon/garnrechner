#!/usr/bin/python

# Meter pro Knaeuel von Garn a
la = int(raw_input('Bitte gib an, wieviele Meter auf einem Knaeuel des ersten Garns sind:'))

# Meter pro Knaeuel von Garn b
lb = int(raw_input('Bitte gib an, wieviele Meter auf einem Knaeuel des zweiten Garns sind:'))

# Anzahl der Knaeuel von Garn a
x = int(raw_input('Bitte gib an, wieviele Knaeuel des ersten Garns verwendet werden (ganze Zahl):'))

# Gesamtlaenge
ltot = la * x

# benoetigte Knaeuel von Garn b
y = x * la // lb + 1

print "Die insgesamt benoetigte Garnlaenge ist", ltot, "Meter."
print "Du benoetigst", y, "Knaeuel von Garn b."
