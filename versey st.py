import csv
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
#polygon 1 chambers st/versey st
array1 = [(40.717737, -74.014077), (40.714785, -74.016180), (40.711394, -74.008638), (40.714192, -74.006321)]
poly1 = Polygon(array1)
x1 = 40.714785
y1 = -74.016180
x2 = 40.711394
y2 = -74.008638
m1 = (y2-y1)/(x2-x1)
a1 = -m1
b1 = 1.0
c1 = m1*x1-y1

#polygon 2 versey st/rector st
array2 = [(40.714785, -74.016180), (40.713582, -74.017050), (40.713444, -74.016320), (40.712102, -74.016599), (40.709288, -74.017715), (40.707434, -74.011954), (40.711394, -74.008638)]
poly2 = Polygon(array2)


with open('data.csv') as s:
        reader = csv.DictReader(s)
        for row in reader:
            #original latitude and longitude values in str
            latitude = row['latitude']
            longitude = row['longitude']
            latitude_scaled = float(latitude)
            longitude_scaled = float(longitude)
            pt = Point(latitude_scaled, longitude_scaled)
            if poly1.contains(pt):
                perpendicular_gradient = -1/m1
                # eqn of line
                a = -perpendicular_gradient
                b = 1.0
                c = perpendicular_gradient * latitude_scaled - longitude_scaled
                # find intersection point
                x = (c1-c)/(-a1+a)
                y = -a1*x-c1
                # perpendicular distance by Pythagoras' theorem
                distance = math.sqrt((y-longitude_scaled)**2+(x-latitude_scaled)**2)
                price = row['price']
                # print latitude + ", "+ longitude+", "+str(x)+", "+ str(y)+", "+ str(price) + ", " + str(distance*100000)
                print str(price) + ", " + str(distance*100000)
            if poly2.contains(pt):
                perpendicular_gradient = -1/m1
                # eqn of line
                a = -perpendicular_gradient
                b = 1.0
                c = perpendicular_gradient * latitude_scaled - longitude_scaled
                # find intersection point
                x = (c1-c)/(-a1+a)
                y = -a1*x-c1
                # perpendicular distance by Pythagoras' theorem
                distance = math.sqrt((y-longitude_scaled)**2+(x-latitude_scaled)**2)
                price = row['price']
                # print str(price) + ", " + str(distance*100000)

#plot polygon with point
# x,y = poly2.exterior.xy
# fig = plt.figure(1, figsize=(5,5), dpi=90)
# ax = fig.add_subplot(111)
# ax.plot(x, y)
# plt.show()
