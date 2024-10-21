import h5py, numpy



# get V2E
with h5py.File("GParam.h5", "r") as f:
    v2e = f["/impurity_0/V2E"][()]
    u = f["/"].attrs["dc_u_avg_list"][0]
# u as the energy unit
v2e /= u
print(f"u = {u} as the energy unit.")

with h5py.File("../ref_hemb/HEmbed.h5", "r") as f:
    d5, d7 = f["/impurity_0/D"][()][[0, 6], [0, 6]]
    h5, h7 = f["/impurity_0/H1E"][()][[0, 6], [0, 6]]
    l5, l7 = f["/impurity_0/LAMBDA"][()][[0, 6], [0, 6]]

# shift
h7 -= h5
l5 += h5
l7 += h5

# energy shift
print(f"Energy shift: {h5.real*14}")

h5 -= h5

# gauge convention
d5 = -d5*numpy.conj(d5)/abs(d5)
d7 = -d7*numpy.conj(d7)/abs(d7)


print(h5/u, h7/u)
print(l5/u, l7/u)
print(d5/u, d7/u)

dmat = numpy.diag([d5]*6 + [d7]*8)/u
hmat = numpy.diag([h5]*6 + [h7]*8)/u
lmat = numpy.diag([l5]*6 + [l7]*8)/u

with h5py.File("HEmbed.h5", "a") as f:
    f["/impurity_0/D"][()] = dmat
    f["/impurity_0/H1E"][()] = hmat
    f["/impurity_0/LAMBDA"][()] = lmat
    f["/impurity_0/V2E"][()] = v2e
