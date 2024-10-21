import h5py, numpy



fnames = [
        "delta_Pu_0/HEmbed_history.h5",
        "delta_Pu_10/HEmbed_history.h5",
        "delta_Pu_19/HEmbed_history.h5",
        ]

# get V2E
with h5py.File("delta_Pu_0/GParam.h5", "r") as f:
    v2e = f["/impurity_0/V2E"][()]
    u = f["/"].attrs["dc_u_avg_list"][0]
# u as the energy unit
v2e /= u
print(f"u = {u} as the energy unit.")


d57_list = numpy.zeros((0, 2), dtype=complex)
l57_list = numpy.zeros((0, 2), dtype=complex)
h57_list = numpy.zeros((0, 2), dtype=complex)

for fname in fnames:
    with h5py.File(fname, "r") as f:
        d57_list = numpy.vstack((d57_list, f["/impurity_0/d_history"][()][:, [0, 6], [0, 6]]))
        l57_list = numpy.vstack((l57_list, f["/impurity_0/lambda_history"][()][:, [0, 6], [0, 6]]))
        h57_list = numpy.vstack((h57_list, f["/impurity_0/h1e_history"][()][:, [0, 6], [0, 6]]))

# shift
l57_list += h57_list[:, 0:1]
h57_list[:, 1] -= h57_list[:, 0]

h57_list[:, 0] -= h57_list[:, 0]

# gauge convention
d57_list[:, :] = -abs(d57_list)
l57_list *= -1

# unit
l57_list /= u
h57_list /= u
d57_list /= u

# real
assert(abs(l57_list.imag).max() < 1e-10)
assert(abs(h57_list.imag).max() < 1e-10)
assert(abs(d57_list.imag).max() < 1e-10)
l57_list = l57_list.real
h57_list = h57_list.real
d57_list = d57_list.real

print("ranges:")
print(f"E-5/2: [{h57_list[:,0].min():.4f}, {h57_list[:,0].max():.4f})")
print(f"E-7/2: [{h57_list[:,1].min():.4f}, {h57_list[:,1].max():.4f})")
print(f"ε-5/2: [{l57_list[:,0].min():.4f}, {l57_list[:,0].max():.4f})")
print(f"ε-7/2: [{l57_list[:,1].min():.4f}, {l57_list[:,1].max():.4f})")
print(f"ν-5/2: [{d57_list[:,0].min():.4f}, {d57_list[:,0].max():.4f})")
print(f"ν-7/2: [{d57_list[:,1].min():.4f}, {d57_list[:,1].max():.4f})")
