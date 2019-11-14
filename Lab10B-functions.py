#################################################
######## RYAN MIDDLE                    #########
######## Lab 10B - Function Definitions #########
######## Section - C                    #########
#################################################
        
# Imports
import math

################################################
########   Function 1 : PrintOutput    #########
################################################

def PrintOutput(a):
    print("OUTPUT", a)
    

################################################
########   Function 2 : TriangleArea   #########
################################################

def TriangleArea(a,b):
    c=a*b*0.5
    PrintOutput(c)

################################################
########   Function 3 : FeetToMeters   #########
################################################

def FeetToMeters(a):
    b=a*0.3048
    PrintOutput(b)

################################################
########   Function 4 : PolarCoords    #########
################################################

def PolarCoords(x,y):
    r=sqrt((x**2)+(y**2))
    theta=math.atan(y/x)
    PrintOutput(r)
    PrintOutput(theta)
################################################
########   Function 5 : EurosToDollars #########
################################################

def EurosToDollars(a):
    b=a/1.12
    PrintOutput(b)
