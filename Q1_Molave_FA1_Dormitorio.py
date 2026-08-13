# This lets us use the math library.
import math
# Gets the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
#Gets the coordinates of the second point 
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# The solution shows how to calculate distance using the distance formula.
d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))  
print("The distance between the two points is ", d)

"""Doing this formative assessment, I applied many things in the Math lib. I used math.sqrt, math.pow, and many more. We also refreshed our minds about the 5 steps of Computational Thinking."""