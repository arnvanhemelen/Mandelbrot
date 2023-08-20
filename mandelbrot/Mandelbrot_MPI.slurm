#!/bin/bash     
#SBATCH --ntasks=64 --cpus-per-task=1
#SBATCH --time=00:05:00
#SBATCH --job-name Mandelbrot_MPI
#SBATCH -o %x.%j.stdout
#SBATCH -e %x.%j.stderr

module --force purge
module load calcua/all
module load numba
module load buildtools
module load git
module load gh
module load Python
module load Pillow
module load SciPy-bundle
module list

srun python Mandelbrot_MPI.py