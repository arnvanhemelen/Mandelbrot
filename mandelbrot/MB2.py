import numpy
from PIL import Image, ImageDraw
import time
from mpi4py import MPI


max_iter = 20

def mandelbrot(c):
    # Check whether complex number belongs to Mandelbrot set
    # Returns the number of iterations
    z = 0 + 0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return i

# WINDOW OF PLOT
real_min = -2
real_max = 1
imag_min = 0
imag_max = 4/3

# IMAGE SIZE (NUMBER OF PIXELS)
diff_real = real_max - real_min
diff_imag = imag_max - imag_min
pixels = [50, 500, 5000]
for pixel in pixels:
    W = int((diff_real) * pixel)
    H = int((diff_imag) * pixel)
    max_iters = [100, 1000, 10000] 
    for max_iter in max_iters: 
        image = Image.new('HSV', (W, H), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        # DRAW MANDELBROT SET
        for x in range(0, W):
            for y in range(0, H):
                # PIXEL COORDINATE TO COMPLEX NUMBER
                c = complex(real_min + (x / W) * (real_max - real_min),
                            imag_min + (y / H) * (imag_max - imag_min))
                # CALCULATE NUMBER OF ITERATIONS
                m = mandelbrot(c)
                # COLOR ~ ITERATIONS
                hue = int(255 * m / max_iter)
                saturation = int(255)
                value = int(255 if m < max_iter else 0)
                # PLOT 
                draw.point([x, y], (hue, saturation, value))
        image.convert('RGB').save('output_' + str(pixel) + '_' + str(max_iter) + '_.png', 'PNG')