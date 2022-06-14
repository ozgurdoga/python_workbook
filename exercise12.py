#Create a program that allows the user to enter the latitude and longitude of two points on the Earth in degrees. Your program should display the distance between the points, following the surface of the earth, in kilometers.

import math
first_point_latitude = float(input("first point latitude"))
first_point_longitude = float(input("first point longitude"))
second_point_latitude = float(input("second point latitude"))
second_point_longitude = float(input("second point longitude"))

distance = 6371.01 * math.acos(math.sin(first_point_latitude)+math.cos(first_point_latitude)*math.cos(second_point_latitude)*math.cos(first_point_longitude-second_point_longitude))

print(distance)