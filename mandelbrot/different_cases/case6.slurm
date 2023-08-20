#!/bin/bash     
#SBATCH --ntasks=64 --cpus-per-task=1
#SBATCH --time=02:00:00
#SBATCH --job-name case6
#SBATCH -o case6.stdout
#SBATCH -e case6.stderr

module --force purge
module load calcua/all
module load numba
module load buildtools
module load git
module load gh
module load Python
module load Pillow
module load SciPy-bundle

srun python 500_10000.py
