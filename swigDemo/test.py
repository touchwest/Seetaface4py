def convertToList(faceext,fdata):
    feature = []
    for i in range(0,1024):
        feature.append(faceext.getByIndex(fdata, i))
    return feature

from faceext import *
f = Faceext()
f.init()


print "load images and get freature."
f1 = f.getFeatures('./images/biden.jpg')
f2 = f.getFeatures('./images/biden.jpg')
m1 = f.getFeatures('./images/mis1.png')
m2 = f.getFeatures('./images/mis2.jpg')

print convertToList(f,f1.data)


print "start compare..."
rs1 = f.CalSimilar(f1.data, f2.data)
rs2 = f.CalSimilar(m1.data, m2.data)

print "similar1:{}".format(rs1)
print "similar2:{}".format(rs2)