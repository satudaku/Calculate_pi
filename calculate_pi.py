'''

How to calculate pi using points of a random unit between 0 and 1

to determine the coordinate of the point in the space between 0 and 1, we use coordinate:
coordinate x for horizontal axis
coordinate y for vertical axis
(x,y)

to determine whether the points are in the circle, we use the pythagorean theorem to
calculate the distance from the center of the circle to the point(x,y):
c**2 = a**2 + b**2
distance**2 = x**2 + y**2
if x**2 + y**2 < 1 then the square root wont be more then 1 and vice versa, so:
distance = x**2 + y**2

An area of circle = pi * r**2
An area of square = d**2 or 4 * r**2 <==we use this

to calculate pi:
Area of circle / Area of square = the number points in the circle / total number of points
pi * r**2 / 4 * r**2 = the number points in the circle / total number of points
pi / 4 = the number points in the circle / total number of points
pi = 4 * the number points in the circle / total number of points

The more points the more likely close to pi value

'''


import random
import matplotlib.pyplot as plt     #install library 'pip install matplotlib'


def calculate_pi(n):
    num_point_total = 0
    num_point_circle = 0
    circle = plt.Circle((0, 0), 1, color='b')   #circle center @ (0,0) with radius of 1 unit
    fig, ax = plt.subplots()    #create one figure and subplots
    ax.set_xlim(-1, 1)      #set x-axis and y-axis from -1 to 1
    ax.set_ylim(-1, 1)      
    ax.set_box_aspect(1)    #without this the circle would looks like oval
    ax.add_patch(circle)
    ax.grid(True)

    for i in range(n):      
        x = random.uniform(-1,1)    #set (x,y) coordinate to random units between -1 to 1
        y = random.uniform(-1,1)
        distance = x**2 + y**2      #distance between center of the firgure to the point
        
        if distance <= 1 and distance >= -1:    #weather the distance is within the circle or not
            num_point_circle += 1
            ax.plot(x, y, 'o', color='r')   #point within the circle

        else:
            ax.plot(x, y, 'o', color='y')   #point outside the circle

        num_point_total += 1
    
    return print(4 * num_point_circle / num_point_total)    #use equation to get pi


def input_num_point():
    print ('Calculation to find the value of pi using random points between 0 to 1')
    try:
        num_point = int(input('Input number of points (int) = '))     #input error handling

    except ValueError:
        print('>>>>ERROR!!! input only integers!')
        input_num_point()

    calculate_pi(num_point)

    return plt.show()       #show the figure

                
input_num_point()
