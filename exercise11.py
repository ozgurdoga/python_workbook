#In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km). Use your research skills to determine how to convert from MPG to L/100 km. Then create a program that reads a value from the user in American units and displays the equivalent fuel efficiency in Canadian units.

#Solution:
#To convert miles per gallon to liters per 100km, just divide 235.21 by the number of miles per gallon. For example, if you're converting 24 MPG to liters per 100km, divide 235.21 by 24 to get 9.8. Therefore, 24 MPG is equal to 9.8 liters per 100km.

input = float(input("Please Enter MPG: "))
convert = 235.21
print(f"Equivalent fuel efficiency in Canadian Units = {convert/input} L/100 km ")