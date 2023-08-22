import numpy as np
from PIL import Image, ImageDraw
import time
from mpi4py import MPI

def mandelbrot(c):
    # Check whether complex number belongs to Mandelbrot set
    # Returns the number of iterations
    z = c
    for n in range(max_iter):
        if z.real * z.real + z.imag * z.imag > 4.0:
            return n
        z = z*z + c
    return max_iter

def make_color(color, ondergrens, bovengrens, H, W):
    for x in range(ondergrens, bovengrens):
        for y in range(0, H):
        # PIXEL COORDINATE TO COMPLEX NUMBER
            c = complex(-2 + (x / W) * (3),
                0 + (y / H) * (1.333))
            # CALCULATE NUMBER OF ITERATIONS
            m = mandelbrot(c)
            # print("[", x, y, "]:", m)
            hue=int(255 * m / max_iter)
            saturation=(int(255))
            value=int(255 if m < max_iter else 0)
            color[x,y] = [hue, saturation, value]
    return color

def make_image(image, color, draw):
    for key in color:
        draw.point([key[0], key[1]], (color[key][0], color[key][1], color[key][2]))
    image.convert('RGB').save('MB_' + str(pixel) + str(max_iter) + '.png', 'PNG')
    return 0
     
def main():
    H = int(4/3)
    W = int(3)
    W = W * pixel
    H = H * pixel
    image = Image.new('HSV', (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    color = {}
    # number of pixels divided by 64 nodes
    ondergrens = int(W / 64 * (rank%size))
    bovengrens = int(W / 64 * ((rank+1)%size))
    # start with node 0 and work up to node 63
    # then send back data to node 0
    if rank == 0:
        data = make_color(color, ondergrens, bovengrens, H, W)
        comm.send(data, dest = (rank+1)%size)
    if rank > 0:
        if rank == 63: 
            bovengrens = W
        data = comm.recv(source=(rank-1)%size)
        data_rank = make_color(data, ondergrens, bovengrens, H, W)
        comm.send(data_rank, dest=(rank+1)%size)
    if rank == 0:
        data_rank = comm.recv(source = size-1)
        make_image(image, data_rank, draw)

if __name__ == '__main__':

    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size
    pixel = 50
    max_iter = 100

    start = MPI.Wtime()
    main()
    einde = MPI.Wtime()
    if rank == 0:
        print("Total runtime: ", einde-start)
        print(pixel, max_iter)