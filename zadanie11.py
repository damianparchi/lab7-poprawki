import numpy as np 


x = np.arange(1,13)
print(x)
print()
y = np.arange(1,13).reshape(3,4)
print(y)
z = np.arange(1,13).reshape(4,3)
print(z)
v = np.arange(1,13).reshape(2,6)
print(v)

a = z.ravel()
print("\n",a)

b = x.ravel()
print("\n",b)

c = y.ravel()
print("\n",c)

d = v.ravel()
print("\n",d)
