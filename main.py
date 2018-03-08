import optparse

import matplotlib.pyplot as plt
import numpy as np

import generator

p = optparse.OptionParser()
p.add_option('--len', '-l')
p.add_option('--cor_len', '-c')
options, arguments = p.parse_args()

g = generator.LaggedFibonacciGenerator()
randArray = g.rand_array(int(options.len))

print(g.math_expect(randArray))
print(g.dispersion(randArray))
freq = g.test(randArray)

for k, v in freq.items():
    if v != 1:
        print(v)

d = g.show_histo(randArray)

hist = np.zeros(10, 'float')
x = np.zeros(10, 'float')

for key, value in d.items():
    for i in np.arange(0.1, 1.1, 0.1):
        if (i - 0.1) <= key < i:
            hist[int(i * 10) - 1] += value
            continue

for i in range(1, 10):
    x[i] = i / 10

plt.plot(x, hist, color='g')
plt.show()
t = range(10, int(options.cor_len), 20)
crl3 = g.auto_correlation(randArray, 3, t)
crl5 = g.auto_correlation(randArray, 5, t)
crl10 = g.auto_correlation(randArray, 10, t)
plt.plot(list(t), crl3, 'g', color='g')
plt.plot(list(t), crl5, 'b', color='b')
plt.plot(list(t), crl10, 'r', color='r')
plt.show()
