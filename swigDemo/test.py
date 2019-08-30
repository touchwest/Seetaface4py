from faceext import *
f = Faceext()
f.init()

print "load images and get freature."
f1 = f.getFeatures('./images/biden.jpg')
f2 = f.getFeatures('./images/biden.jpg')

print f1.data

print "start compare..."
rs1 = f.CalSimilar(f1.data, f2.data)

print "similar1:{}".format(rs1)
