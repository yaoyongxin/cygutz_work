import numpy
import matplotlib.pyplot as plt


data = numpy.loadtxt("results.dat").T
# zero-point shift
data_fit = [numpy.linspace(data[0][0], data[0][-1], 300)]
for i in range(1, data.shape[0]):
    z = numpy.polyfit(data[0], data[i], 3)
    p = numpy.poly1d(z)
    data_fit.append(p(data_fit[0]))
    emin = numpy.min(data_fit[-1])
    data[i] -= emin
    data_fit[-1] -= emin
    print(f"{i}: min z_se = {data_fit[0][data_fit[-1].argmin()]:.3f}")


labels = ["LDA", "U=5", "U=8", "U=10"]
for i in range(1, 5):
    plt.plot(data[0], data[i], "o", label=labels[i-1])
    plt.plot(data_fit[0], data_fit[i], "-")
    plt.xlabel(r"z$_{Se}$")
    plt.ylabel("E(Ryd.)")
    plt.legend()
plt.show()
