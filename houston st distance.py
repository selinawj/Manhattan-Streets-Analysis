import csv
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
#polygon 1 houston st/canal st
array1 = [(40.729163, -74.010442), (40.728317, -74.003168), (40.717259, -73.998948), (40.714397, -73.990268), (40.722285, -73.986309), (40.725082, -73.995278), (40.725464, -73.996748), (40.728358, -74.002842)]
poly1 = Polygon(array1)
x1 = 40.729163
y1 = -74.010442
x2 = 40.722285
y2 = -73.986309
m1 = (y2-y1)/(x2-x1)
a1 = -m1
b1 = 1.0
c1 = m1*x1-y1

#polygon 2 14 st/houston
array2 = [(40.742128, -74.008202), (40.739356, -74.009683), (40.729163, -74.010442), (40.728365, -74.002859), (40.725479, -73.996733), (40.725113, -73.995360), (40.720771, -73.981316), (40.728479, -73.975737)]
poly2 = Polygon(array2)
x3 = 40.729163
y3 = -74.010442
x4 = 40.722285
y4 = -73.986309
m2 = (y4-y3)/(x4-x3)
a2 = -m2
b2 = 1.0
c2 = m2*x3-y3

with open('nyc50.csv') as s:
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
                perpendicular_gradient = -1/m2
                # eqn of line
                a = -perpendicular_gradient
                b = 1.0
                c = perpendicular_gradient * latitude_scaled - longitude_scaled
                # find intersection point
                x = (c2-c)/(-a2+a)
                y = -a2*x-c2
                # perpendicular distance by Pythagoras' theorem
                distance = math.sqrt((y-longitude_scaled)**2+(x-latitude_scaled)**2)
                price = row['price']
                # print str(price) + ", " + str(distance*100000)

#polygon 3 morningside heights -- could it be due to school ranking??
