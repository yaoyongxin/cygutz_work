#!/bin/bash

#SBATCH --mail-user=ykent@iastate.edu 
#SBATCH --mail-type=end
#SBATCH --partition=compute 
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --job-name=Pr

# record start date and host
date
hostname

mpirun -np 32 pgrun.py

# record end date
date

