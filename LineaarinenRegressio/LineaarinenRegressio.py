import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

plt.style.use('seaborn')
plt.title("otsikko")
Xs = np.array([1,2,3,4,5], dtype=np.float64)
Ys = np.array([5,4,6,5,6], dtype=np.float64)

def laske_m_ja_b(xs,ys):
    #m = ((mean(xs)*mean(ys))-mean(sum(xs)*sum(ys))/((mean(xs)**2)-mean(xs**2)))
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
        ((mean(xs) **2) - mean(xs *xs)))
    b = (mean(ys))-m*(mean(xs))
    return m,b

m,b =laske_m_ja_b(Xs,Ys)

reg_line = [(m*x) + b for x in Xs]

ennuste = 10
ennuste_y = (m * ennuste) + b
ennuste_line = [(m*x)+b for x in range(int(Xs[-1]),ennuste+2)]

plt.scatter(Xs,Ys)
plt.plot(Xs,reg_line)
plt.plot(range(int(Xs[-1]),ennuste+2), ennuste_line)
plt.scatter(ennuste,ennuste_y)

plt.show()