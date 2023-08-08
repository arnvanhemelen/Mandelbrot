# File wetppr-env.sh
# Prepare environment for Python/C++/Fortran development
# You must 'source' this file
module load numba
module load buildtools
module load git
module load gh
module load Python
module load Pillow
module load SciPy-bundle

# list all loaded modules
module list 

# allow to install python packages locally
export PYTHONUSERBASE=/data/antwerpen/gst/guest005/.local
mkdir -p ${PYTHONUSERBASE}
export PATH="$PATH:${PYTHONUSERBASE}/bin"