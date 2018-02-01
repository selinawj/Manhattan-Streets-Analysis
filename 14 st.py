import csv
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
#polygon 1 14 st/23 st
array1 = [(40.747697, -74.004174), (40.742088, -74.008240), (40.728512, -73.975667), (40.735536, -73.975163)]
poly1 = Polygon(array1)
x1 = 40.742088
y1 = -74.008240
x2 = 40.728512
y2 = -73.975667
m1 = (y2-y1)/(x2-x1)
a1 = -m1
b1 = 1.0
c1 = m1*x1-y1

#polygon 2 5 st/14 st
array2 = [(40.742088, -74.008240), (40.732464, -74.010074), (40.722951, -73.979776), (40.728512, -73.975667)]
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
                listing = row['listing_id']
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
# x,y = poly1.exterior.xy
# fig = plt.figure(1, figsize=(5,5), dpi=90)
# ax = fig.add_subplot(111)
# ax.plot(x, y)
# plt.show()
