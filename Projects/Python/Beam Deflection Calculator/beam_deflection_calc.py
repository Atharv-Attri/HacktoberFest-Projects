import numpy as np
import matplotlib.pyplot as plt

print("""
Current mode: Single fixed end, single point load

|                        F
|                        |
|                       \|/
|---------------------------------
| x-->
|<----------a----------->
|<---------------L--------------->
|
|
""")

F = float(input('Input F in N:\n'))
L = float(input('Input L in m:\n'))
a = float(input('Input a in m:\n'))
E = float(input('Input E in GPa:\n'))
I = float(input('Input I in mm^4:\n'))
xQuery = float(input('Input x in m:\n'))

# Convert to SI units
E = E*pow(1000,3)
I = I/pow(1000,4)

X = np.arange(0, L+L/1000, L/1000).tolist()
Y = []
for x in X:
  if x >= 0 and x <= a:
    Y.append(-F*x*x/6/E/I*(3*a-x))
  elif x >= a and x <= L:
    Y.append(-F*a*a/6/E/I*(3*x-a))

x = xQuery
if x >= 0 and x <= a:
  y = -F*x*x/6/E/I*(3*a-x)
elif x >= a and x <= L:
  y = -F*a*a/6/E/I*(3*x-a)

print('Deflection at ',x,' m = ',y,' m')

fig, ax = plt.subplots(nrows=1, ncols=1)
plt.plot(X,Y)
plt.plot(x,y,'rD')
plt.annotate(f"({x},{y})",(x,y))
plt.ylabel('Deflection (m)')
plt.xlabel('x (m)')
fig.savefig('graph.png')
