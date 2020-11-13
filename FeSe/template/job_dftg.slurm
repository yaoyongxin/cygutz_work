#!/bin/bash

#SBATCH --mail-user=ykent@iastate.edu 
#SBATCH --mail-type=end
#SBATCH --partition=normal
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --job-name=FeSe-VV

# record start date and host
date
hostname

/home/ykent/GWIEN/bin/run_gwien.py >& log

# record end date
date

