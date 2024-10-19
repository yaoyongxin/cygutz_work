import h5py, numpy


h1e = numpy.zeros((6,6))
lambdac1 = [[0.4134611, 0.62315535, 0.02807221],
        [0.62315535, 0.91191622, 0.83644965],
        [0.02807221, 0.83644965, 0.17398815]]
d1 = [[0.81105864, 0.20047146, 0.81811896],
        [0.60408813, 0.92569668, 0.27452124],
        [0.04184087, 0.36753563, 0.00894037]]

lambdac1 = numpy.asarray(lambdac1)
d1 = numpy.asarray(d1)
lambdac = numpy.zeros((6,6))
d = numpy.zeros((6,6))
lambdac[::2, ::2] = lambdac[1::2, 1::2] = lambdac1
d[::2, ::2] = d[1::2, 1::2] = d1

with h5py.File("HEmbed.h5", "a") as f:
    f["/impurity_0/D"][()] = d.T
    f["/impurity_0/H1E"][()] = h1e
    f["/impurity_0/LAMBDA"][()] = lambdac.T


