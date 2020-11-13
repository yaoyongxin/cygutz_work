#!/usr/bin/env python
from mpi4py import MPI
import os, tempfile, shutil
from pygrisb.run.gwien import run_gwien


def pgrun_tmp():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    path = f"V{rank}"
    if os.path.isdir(path):
        os.chdir(f"{path}/case")
        wdir = os.getcwd()
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpworkdir = f"{tmpdir}/case"
            os.mkdir(tmpworkdir)
            for item in os.listdir():
                if os.path.isfile(item):
                    shutil.copy(item, tmpworkdir)
            os.chdir(tmpworkdir)
            run_gwien(spinorbit=True)
            for item in os.listdir():
                if os.path.isfile(item):
                    shutil.copy(item, wdir)


def pgrun(tmp="/tmp"):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    path = f"V{rank}"
    if os.path.isdir(path):
        os.chdir(f"{path}/case")
        run_gwien(spinorbit=True)


if __name__ == "__main__":
    pgrun()
