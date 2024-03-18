from math import pi,sin,cos

def derivative_of_sin(x,h):
    return (sin(x+h) - sin(x))/h

h = 0.1
x_values = []
for i in range(int(-pi/h), int(pi/h)+1):
    x_values.append(i*h)

for x in x_values:
    derivative = derivative_of_sin(x,h)
    actual_cos = cos(x)
    print(f"At x = {x}, Derivative os sin(x) = {derivative},Cos(x) = {actual_cos}")