import numpy
from PIL import Image, ImageDraw
import time
from mpi4py import MPI

def mandelbrot(c, max_iter):
    # Check whether complex number belongs to Mandelbrot set
    # Returns the number of iterations
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def make_color(color, ondergrens, bovengrens, H, W, max_iter):
    for x in range(ondergrens, bovengrens):
        for y in range(0, H):
        # PIXEL COORDINATE TO COMPLEX NUMBER
            c = complex(-2 + (x / W) * (3),
                0 + (y / H) * (1.333))
            # CALCULATE NUMBER OF ITERATIONS
            m = mandelbrot(c, max_iter)
            # print("[", x, y, "]:", m)
            hue=int(255 * m / max_iter)
            saturation=(int(255))
            value=int(255 if m < max_iter else 0)
            color[x,y] = [hue, saturation, value]
    return color

def make_image(image, color, draw):
    for key in color:
        draw.point([key[0], key[1]], (color[key][0], color[key][1], color[key][2]))
    image.convert('RGB').save('TRY.png', 'PNG')
    return 0
     
def main():
    pixels = [50]
    iterations = [100]
    
    for pixel in pixels:
        for max_iter in iterations:
            W = 3
            H = int(4/3)
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
                print(ondergrens, bovengrens)
                data = make_color(color, ondergrens, bovengrens, H, W, max_iter)
                comm.send(data, dest = (rank+1)%size)
            if rank > 0:
                if rank == 63: 
                    bovengrens = W
                print('rank:', rank, '--', ondergrens, bovengrens)
                data = comm.recv(source=(rank-1)%size)
                data_rank = make_color(data, ondergrens, bovengrens, H, W, max_iter)
                comm.send(data_rank, dest=(rank+1)%size)
            if rank == 0:
                data_rank = comm.recv(source = size-1)
                make_image(image, data_rank, draw)
        

if __name__ == '__main__':

    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    start = MPI.Wtime()
    main()
    einde = MPI.Wtime()
    if rank > 0:
        print("rank:", rank, "-- time: ", einde-start, "sec")
    if rank == 0:
        print("Total runtime: ", einde-start)
            