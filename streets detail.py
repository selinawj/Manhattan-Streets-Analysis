import csv
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

#west houston line 1
# x1 = 40.729163
# y1 = -74.010442 * math.cos(x1)
# x2 = 40.728317
# y2 = -74.003168 * math.cos(x2)
# m_wh = (y2-y1)/(x2-x1)
# A_wh = -m_wh
# B_wh = 1
# C_wh = y1-m_wh*(-x1)

#canal st line 1
x3 = 40.725780
y3 = -74.010807 * math.cos(x3)
x4 = 40.722129
y4 = -74.005550 * math.cos(x4)
m_cs = (y4-y3)/(x4-x3)
A_cs = -m_cs
B_cs = 1
C_cs = y3-m_cs*(-x3)

#######################################

#west houston part 1 - bounded W houston/6th Ave/canal
array_wh1 = [(40.729163, -74.010442), (40.725780, -74.010807), (40.722129, -74.005550), (40.728317, -74.003168)]
#west houston part 2 - bounded W houston/6th Ave/broadway/canal
array_wh2 = [(40.728374, -74.002746), (40.721902, -74.005471), (40.719365, -74.001780), (40.725496, -73.996780)]

#east houston part 1 - bounded E houston/broadway/lafayette/canal
array_eh1 = [(40.725431, -73.996796), (40.719357, -74.001849), (40.718430, -74.000540), (40.725073, -73.995369)]
#east houston part 2 - bounded E houston/lafayette/bowery/canal
array_eh2 = [(40.725113, -73.995322), (40.718454, -74.000562), (40.717113, -73.998609), (40.716275, -73.996031), (40.724097, -73.992608)]
#east houston part 3 - bounded E houston/bowery/allen st/canal
array_eh3 = [(40.724122, -73.992645), (40.716218, -73.996035), (40.715088, -73.992537), (40.722935, -73.988621)]

#checks if point is inside boundaries
# pt = Point(40.719162, -73.995949)
# poly = Polygon(array_eh2)
# print poly.contains(pt)

#plot polygon with point
# from matplotlib import pyplot as plt
# plt.plot([40.725015], [-74.005936], marker='o', markersize=3, color="red")
# x,y = poly.exterior.xy
# fig = plt.figure(1, figsize=(5,5), dpi=90)
# ax = fig.add_subplot(111)
# ax.plot(x, y)
# plt.show()

#######################################

with open('nyc50.csv') as s:
        reader = csv.DictReader(s)
        sumPrice = 0
        count = 0.0 #in float
        for row in reader:
            #original latitude and longitude values in str
            latitude = row['latitude']
            longitude = row['longitude']
            latitude_float = float(latitude)
            longitude_float = float(longitude)
            #checks if point is inside bounded polygon
            pt = Point(latitude_float, longitude_float)
            poly = Polygon(array_eh1)
            # scaled latitude and longitude values in float
            latitude_scaled = float(latitude)
            longitude_scaled = float(longitude) * math.cos(math.radians(latitude_scaled))
            print str(latitude_scaled) + ", " + str(longitude_scaled)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # ax.scatter(in_distance, in_price, c='b', marker="s", label="first")
# ax.plot((sumPrice3/count3, sumPrice4/count4, sumPrice5/count5, sumPrice6/count6), (0.3,0.4,0.5,0.6), c='r', marker="o", label="second")
# plt.xlabel("Distance from boundary")
# plt.ylabel("Price")
# plt.legend(loc='upper left');
# plt.ylim([0,6000])
# plt.xlim([0,3])
# plt.show()
            #calculate distance from west houston
            # numerator = math.fabs(A_cs*latitude_scaled+B_cs*longitude_scaled+C_cs)
            # denominator = math.sqrt(A_cs**2+B_cs**2)
            # d = numerator/denominator
            # print d
            #calculate avg price if point is inside
        #     if poly.contains(pt):
        #         # print latitude + ', ' + longitude
        #         price = int(row['price'])
        #         print price
        #         sumPrice += price
        #         count += 1
        # avgPrice = sumPrice/count
        # print avgPrice

########################################
