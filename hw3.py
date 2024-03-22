import numpy as np
x=0
y=0
z=0

for y in np.arange(40, 1, -1):
    for x in np.arange(40, 1, -1):
        if 0.32*x+0.22*y>=8 and 0.11*x+0.09*y>=3 and 0.15*x+0.10*y>=4:
            min=35*x+25*y
            print(x,y)
print(min)

        