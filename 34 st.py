import csv
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
#polygon 1 34 st/28 st
array1 = [(40.757025, -74.004874), (40.753100, -74.007267), (40.739054, -73.973589), (40.743248, -73.972216)]
poly1 = Polygon(array1)
x1 = 40.757025
y1 = -74.004874
x2 = 40.743248
y2 = -73.972216
m1 = (y2-y1)/(x2-x1)
a1 = -m1
b1 = 1.0
c1 = m1*x1-y1

#polygon 2 40 st/34 st
array2 = [(40.760716, -74.001990), (40.757025, -74.004874), (40.743248, -73.972216), (40.747012, -73.969140)]
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
                # print str(price) + ", " + str(distance*100000)
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
                print str(price) + ", " + str(distance*100000)

#plot polygon with point
# x,y = poly2.exterior.xy
# fig = plt.figure(1, figsize=(5,5), dpi=90)
# ax = fig.add_subplot(111)
# ax.plot(x, y)
# plt.show()
