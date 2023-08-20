import numpy as np
from PIL import Image, ImageDraw
from mpi4py import MPI
import time 

def mandelbrot(c,max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    iterations = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            iterations[i,j] = mandelbrot(x[i] + 1j*y[j],max_iter)
    return (x,y,iterations)

def mandelbrot_image(xmin,xmax,ymin,ymax,pixels,max_iter,cmap='hot'):
    width = xmax - xmin
    height = ymax - ymin
    img_width = pixels * width
    img_height = pixels * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,max_iter)
    
    for i in z:
        for j in int(z[i]):
            hue = int(255 * z[i,j] / max_iter)
            saturation = int(255)
            value = int(255 if z[i,j] < max_iter else 0)
            draw.point([x[i,j], y[i,j]], (hue, saturation, value))
    return image.convert('RGB').save("I" + str(max_iter) + "_P" + str(pixel) + '.png', 'PNG')

mandelbrot_image(-2, 1, 0, int(4/3), 50, 100)
