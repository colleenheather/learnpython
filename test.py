from sys import argv
name, r = argv
r = int(r)
area = 3.14 * r
circumfernce = 2 * r * 3.14

print "Radius: %s" % (r)

print "Area: %s" % (area)

print "Circumfernce: %s" % (circumfernce)

print "Volume: %s" % (3/4.0 * 3.14 * r ** 3)


