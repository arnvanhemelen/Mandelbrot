import numpy
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


max_iter = 80

def mandelbrot(c):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return i

# Image size (pixels)
W = 600
H = 400

# Plot window
real_min = -2
real_max = 1
imag_min = 0
imag_max = 4/3

palette = []

im = Image.new('RGB', (W, H), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, W):
    for y in range(0, H):
        # Convert pixel coordinate to complex number
        c = complex(real_min + (x / W) * (real_max - real_min),
                    imag_min + (y / H) * (imag_max - imag_min))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        color = 255 - int(m * 255 / max_iter)
        # Plot the point
        draw.point([x, y], (color, color, color))

im.save('output.png', 'PNG')
