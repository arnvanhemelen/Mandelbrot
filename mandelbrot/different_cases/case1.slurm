#!/bin/bash     
#SBATCH --ntasks=64 --cpus-per-task=1
#SBATCH --time=02:00:00
#SBATCH --job-name case1
#SBATCH -o case1.stdout
#SBATCH -e case1.stderr

module --force purge
module load calcua/all
module load numba
module load buildtools
module load git
module load gh
module load Python
module load Pillow
module load SciPy-bundle

srun python 50_100.py