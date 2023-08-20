#!/bin/bash     
#SBATCH --ntasks=64 --cpus-per-task=1
#SBATCH --time=00:05:00
#SBATCH --job-name try
#SBATCH -o %x.%j.stdout
#SBATCH -e %x.%j.stderr

module load calcua/2020a
module load numba
module load buildtools
module load git
module load gh
module load Python
module list

srun python try.py