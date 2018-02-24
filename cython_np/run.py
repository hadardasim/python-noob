import numpy as np
import convolve_py
import convolve3f

N = 100

f = np.arange(N*N, dtype=np.float32).reshape((N,N))
print
print f.__class__
print f.shape

K = 9
g = np.arange(K*K, dtype=np.float32).reshape((K, K))

h1 = convolve_py.naive_convolve(f, g)
h2 = convolve3f.naive_convolve(f ,g)

print 'complete'
