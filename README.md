# Calculate_pi
Python code to estimate pi value using random points between 0 to 1.

To determine the coordinate of the point in the space between 0 and 1, we use coordinate:
```
Coordinate x for horizontal axis
Coordinate y for vertical axis
(x,y)
```
To determine whether the points are in the circle, we use the pythagorean theorem to
calculate the distance from the center of the circle to the point (x,y):
```
c**2 = a**2 + b**2
distance**2 = x**2 + y**2
```
If x**2 + y**2 < 1 then the square root wont be more then 1 and vice versa, so:
```
distance = x**2 + y**2
```
To get area of circle and figure:
```
Area of circle = pi * r**2
Area of figure is same as a square = d**2 or 4 * r**2 <==we use this
```
To calculate pi:
```
Area of circle / Area of square = the number points in the circle / total number of points
pi * r**2 / 4 * r**2 = the number points in the circle / total number of points
pi / 4 = the number points in the circle / total number of points
pi = 4 * the number points in the circle / total number of points
```
The more points the more likely close to pi value.
