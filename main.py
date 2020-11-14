import cv2
import numpy as np
from numpy import complex, array
import colorsys

ITERATIONS = 1000
SIZE = 700 # Image size

# Convert from number of iterations to RGB
def getColour(i):
    color = (0.4, 0.4, i*10/255.0)
    return color

# function defining a mandelbrot
def mandelbrot(x, y, iterations = ITERATIONS):
    c0 = complex(x, y)
    c = 0
    for i in range(1, iterations):
        if abs(c) > 2:
            return getColour(i)
        c = c * c + c0
    return (0.4, 0.4, ITERATIONS/255.0)


# creating the new image in RGB mode
def mandelSet(frameCount):
    pixels = np.zeros((SIZE,SIZE,3))
    for x in range(SIZE):
        # displaying the progress as percentage
       # print("%.2f %%" % (x / SIZE * 100.0))
        for y in range(SIZE):
            pixels[y, x] = mandelbrot((x - (0.75 * SIZE)) / (SIZE / 2),
                                      (y - (0.5 * SIZE)) / (SIZE / 2), frameCount)
    return pixels


    # to display the created fractal after
# completing the given number of iterations
def getFrame():
    print('Frame: ' + str(getFrame.count))
    # Create data on first call only
    if getFrame.count/(SIZE*SIZE) < 1:
            getFrame.z = mandelSet(getFrame.count)
    # Just roll data for subsequent calls
            getFrame.count +=1
    return getFrame.z

getFrame.count = 0
getFrame.z = None

while True:
    # Get a numpy array to display from the simulation
    npimage = getFrame()
    cv2.imshow('image', npimage)
    cv2.waitKey(1)
