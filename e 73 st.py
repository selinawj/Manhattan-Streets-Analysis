import csv
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
#polygon 1 e 73 st/79 st
array1 = [(40.777002, -73.963737), (40.773135, -73.966548), (40.766618, -73.950991), (40.770339, -73.947837)]
poly1 = Polygon(array1)
x1 = 40.773135
y1 = -73.966548
x2 = 40.766618
y2 = -73.950991
m1 = (y2-y1)/(x2-x1)
a1 = -m1
b1 = 1.0
c1 = m1*x1-y1

#polygon 2 73 st/67 st
array2 = [(40.773135, -73.966548), (40.769258, -73.969370), (40.763009, -73.954189), (40.766618, -73.950991)]
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
# x,y = poly2.exterior.xy
# fig = plt.figure(1, figsize=(5,5), dpi=90)
# ax = fig.add_subplot(111)
# ax.plot(x, y)
# plt.show()
