import numpy as np 


x = np.arange(5,14).reshape(3,3)
print(x)

print()
#wartosc najnizsza kazdego rzedu
print(x.min(axis=1))
print()
#wartosc najnizsza kazdej kolumny
print(x.min(axis=0))
print()


y = np.arange(5,21).reshape(4,4)

print(y)
print()

#wartosc najnizsza kazdej kolumny
print(y.min(axis=1))
print()
#wartosc najnizsza kazdego rzedu
print(y.min(axis=0))