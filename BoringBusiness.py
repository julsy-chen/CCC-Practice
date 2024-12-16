import re

# these are the coordinates to avoid
xKeyCoords = {-1:(-5, -6, -7), 0:(-1, -2, -3, -7), 1:(-3, -7), 2:(-3, -7), 3:(-3, -5, -6, -7), 4:(-5, -7), 5:(-3, -4, -5, -7), 6:(-3, -7), 7:(-3, -4, -5, -6, -7)}
yKeyCoords = {-1: (0), -2:(0), -3:(0, -1, -2, -3, -5, -6, -7), -4:(3, 5, 7), -5:(-1, 3, 4, 5, 7), -6:(-1, 7), -7:(-1, 0, 1, 2, 3, 4, 5, 6, 7)}

xVal = -1
yVal = -5

#'''
while True:
    vector = input()
    direction = vector[0]
    if direction == "q":
        break
    else: 
        magnitude = int(re.search(r'\d+', vector).group())
        if direction == "l" or direction == "r": #changing the x value
            if direction == "l":
                magnitude = -magnitude
            xVal += magnitude
            if xVal in xKeyCoords and yVal in xKeyCoords[xVal]:
                print(f"{xVal} {yVal} DANGER")
            else:
                print(f"{xVal} {yVal} safe") 
        else: # changing the y value
            if direction == "d":
                magnitude = -magnitude
            yVal += magnitude
            if yVal in yKeyCoords and xVal in yKeyCoords[yVal]:
                print(f"{xVal} {yVal} DANGER")
            else:
                print(f"{xVal} {yVal} safe") 
#'''

'''
the RANGE of the drilling from point A to point B also must not intersect with the orignal drilling path
to do this:
'''

