import csv
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
#polygon 1 broome st/houston st
array1 = [(40.72860842830248, -74.00530099868774), (40.724445530905136, -74.00598764419554), (40.72421786494403, -74.0045714378357), (40.723307193311804, -74.00296211242676), (40.72083530749972, -73.99768352508545), (40.71948548899755, -73.99435758590698), (40.714894, -73.979515), (40.719293, -73.977219), (40.7251610474272, -73.99530172348022), (40.72540497175607, -73.99686813354492), (40.728364515715036, -74.00287628173828), (40.72860842830248, -74.00530099868774)]
poly1 = Polygon(array1)
x1 = 40.724445530905136
y1 = -74.00598764419554
x2 = 40.714894
y2 = -73.979515
m1 = (y2-y1)/(x2-x1)
a1 = -m1
b1 = 1.0
c1 = m1*x1-y1

#polygon 2 canal st/broome st
array2 = [(40.724577, -74.007759), (40.723703, -74.007931), (40.71717609748506, -73.99888515472412), (40.71424858464975, -73.98967981338501), (40.71174383259811, -73.98109674453735), (40.71488289002164, -73.97953033447266), (40.71945296291278, -73.99448633193968), (40.723290931205135, -74.00309085845947), (40.72420160305987, -74.00463581085205)]
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
                # print str(price) + ", " + str(distance*100000)

#plot polygon with point
# x,y = poly2.exterior.xy
# fig = plt.figure(1, figsize=(5,5), dpi=90)
# ax = fig.add_subplot(111)
# ax.plot(x, y)
# plt.show()
