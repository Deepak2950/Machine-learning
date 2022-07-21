import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([4,12,28,52,80])
n=len(x)

sumx=x.sum()
sumy=y.sum()

meanx=sumx/n
meany=sumy/n

X=np.array([])

XX=np.array([])
Y=np.array([])
XY=np.array([])

for i in range(0,n):
    tx=x[i]-meanx
    X=np.append(X,tx)
    XX=np.append(XX,(tx*tx))
    ty=y[i]-meany
    Y=np.append(Y,ty)
    XY=np.append(XY,(tx*ty))


sumXY=XY.sum()
sumXX=XX.sum()
m=sumXY/sumXX

c=meany-(m*meanx)

def calcY(x):
  return m * x + c

mymodel = list(map(calcY, x))

print(m,c)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.xlabel("Agricultural Products")
plt.ylabel("Price")
plt.plot(x,y, linestyle = 'dashed', color="red")
plt.title("Graph")
plt.show()
