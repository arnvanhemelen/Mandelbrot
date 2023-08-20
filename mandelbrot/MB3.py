import numpy
from PIL import Image, ImageDraw
import time
from mpi4py import MPI

def mandelbrot(c, max_iter):
    # Check whether complex number belongs to Mandelbrot set
    # Returns the number of iterations
    z = 0 + 0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

def plot(pixel, max_iter):
    W = int((3) * pixel)
    H = int((1.333) * pixel)
    image = Image.new('HSV', (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    # DRAW MANDELBROT SET
    for x in range(0, W):
        for y in range(0, H):
        # PIXEL COORDINATE TO COMPLEX NUMBER
            c = complex(-2 + (x / W) * (3),
                0 + (y / H) * (1.333))
            # CALCULATE NUMBER OF ITERATIONS
            m = mandelbrot(c, max_iter)
            # COLOR ~ ITERATIONS
            hue = int(255 * m / max_iter)
            saturation = int(255)
            value = int(255 if m < max_iter else 0)
            # PLOT 
            draw.point([x, y], (hue, saturation, value))
    return image.convert('RGB').save("I" + str(max_iter) + "_P" + str(pixel) + '.png', 'PNG')

def main():
    pixels = [50, 500]
    iterations = [100, 1000]
    for pixel in pixels:
        for iteration in iterations:
            plot(pixel, iteration)
    return 0

if __name__ == '__main__':

    comm = MPI.COMM_WORLD
    size = comm.size
    rank = comm.rank

    start = MPI.Wtime()
    main()
    einde = MPI.Wtime()

    print(size)
    print("Node", rank, "-- execution time:", einde - start, "seconden.")