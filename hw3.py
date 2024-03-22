import numpy as np
x=0
y=0
z=0

for z in np.arange(0, 20, 0.1):
    for x in np.arange(0, 20, 0.1):
        for y in np.arange(0, 20, 0.1):
            if x+y<=8 and 2*x+z<=9 and 2*z+y<=4:
                max=3*x+2*y+5*z
                print(x,y,z)
print(max)

        