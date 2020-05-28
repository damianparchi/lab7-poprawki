import numpy as np 

b = np.arange(81)
print(b)
print(b.shape)
# przeksztalacamy ja na macierz 2x3
c = b.reshape((9,9))
print(c)
print(c.shape)
# przeksztalacamy ja na macierz 3x2
d = c.reshape((9,9))
print(d)
print(d.shape)
# spłaszczamy macierz zyskujac pierwotny kształt ze zmiennej b
e = d.ravel()
print(e)
print(e.shape)
# transpozycja macierzy
f = c.T
print(f)
print(f.shape)