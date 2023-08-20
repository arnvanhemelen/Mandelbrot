#!/bin/bash     
#SBATCH --ntasks=64 --cpus-per-task=1
#SBATCH --time=02:00:00
#SBATCH --job-name run_different_cases
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

srun python 50_100.py
srun python 50_1000.py
srun python 50_10000.py
srun python 500_100.py
srun python 500_1000.py
srun python 500_10000.py