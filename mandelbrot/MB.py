import numpy
from PIL import Image, ImageDraw
import time

def mandelbrot(c):
    z = 0
    for i in range(max_iter):
        if ((z.real*z.real + z.imag*z.imag) >= 4):
            return i
        z = z*z + c
    return max_iter

start = time.time()

max_iter = 100
pixel = 50
# Plot window
real_min = -2
real_max = 1
imag_min = 0
imag_max = 4/3
W = int((real_max - real_min)*pixel)
H = int((imag_max - imag_min)*pixel)

im = Image.new('HSV', (W, H), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, W):
    for y in range(0, H):
        # Convert pixel coordinate to complex number
        c = complex(real_min + (x / W) * (real_max - real_min),
                    imag_min + (y / H) * (imag_max - imag_min))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        hue=int(255 * m / max_iter)
        saturation=(int(255))
        value=int(255 if m < max_iter else 0)
        # PLOT 
        draw.point([x, y], (hue, saturation, value))
im.convert('RGB').save('output.png', 'PNG')

end = time.time()
print(end - start, "seconden")