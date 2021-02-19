import h5py


with h5py.File("HEmbedRes_0.h5", "r") as f:
    dm = f["/DM"][()][::2, ::2].T

print(dm)
