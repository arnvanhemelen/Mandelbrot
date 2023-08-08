import numpy
# import matplotlib.pyplot as plt

from PIL import Image, ImageDraw
import time


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

# Plot window
real_min = -2
real_max = 1
imag_min = 0
imag_max = 4/3
diff_real = real_max - real_min
diff_imag = imag_max - imag_min
# Image size (pixels)
pixels = [50]
for pixel in pixels:
    W = int((diff_real) * pixel)
    H = int((diff_imag) * pixel) 

image = Image.new('HSV', (W, H), (0, 0, 0))
draw = ImageDraw.Draw(image)

for x in range(0, W):
    for y in range(0, H):
        # Convert pixel coordinate to complex number
        c = complex(real_min + (x / W) * (real_max - real_min),
                    imag_min + (y / H) * (imag_max - imag_min))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        hue = int(255 * m / max_iter)
        saturation = int(255)
        value = int(255 if m < max_iter else 0)
        # Plot the point 
        draw.point([x, y], (hue, saturation, value))

image.convert('RGB').save('output.png', 'PNG')