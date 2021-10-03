import random
import matplotlib.pyplot as plt  # install library 'pip install matplotlib'


def calculate_pi(n):
    num_point_total = 0
    num_point_circle = 0
    circle = plt.Circle((0, 0), 1, color='b')    # circle center @ (0,0) with radius of 1 unit
    fig, ax = plt.subplots()  # create one figure and subplots
    ax.set_xlim(-1, 1)  # set x-axis and y-axis from -1 to 1
    ax.set_ylim(-1, 1)
    ax.set_box_aspect(1)  # without this the circle would looks like oval
    ax.add_patch(circle)
    ax.grid(True)

    for i in range(n):
        # set (x,y) coordinate to random units between -1 to 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2  # distance between center of the firgure to the point

        if distance <= 1 and distance >= -1:  # weather the distance is within the circle or not
            num_point_circle += 1
            ax.plot(x, y, 'o', color='r')  # point within the circle

        else:
            ax.plot(x, y, 'o', color='y')  # point outside the circle

        num_point_total += 1

    pi = 4 * num_point_circle / num_point_total  # use equation to get pi
    plt.figtext(0.02, 0.95, 'π = ' + str(pi))
    print('The estimate pi using', n, 'points is', pi)

    return


def input_num_point():
    try:
        # input error handling
        num_point = int(input('Input number of points (int) = '))

    except ValueError:
        print('>>>>ERROR!!! input only integers!')
        input_num_point()

    calculate_pi(num_point)

    return plt.show()  # show the figure


print('Calculation to find the value of pi using random points between 0 to 1')
input_num_point()
