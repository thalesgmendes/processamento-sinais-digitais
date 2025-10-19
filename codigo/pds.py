# (|α| > 1) e decrescente(|α| < 1)

#from scipy.signal import lfilter
import matplotlib.pyplot as plt
import numpy as np

def impulso(n):
    x = list(range(-n, n+1))
    y = [0 if i !=0 else 1 for i in x]
    return x, y

def degrau (n):
    x = list(range(-n,n+1))
    y = [1 if i >=0 else 0 for i in x]
    return x, y

def rampa(n):
    x = list(range(-n, n+1))
    y = [i if i > 0 else 0 for i in x]
    return x, y


def atraso(y, n, x):
    l2 = x.copy()
    if n >=0:
        l = [0 if i < n else y[i - n] for i in range(len(y) + n)]
        for i in range(n):
            l2.append(l2[-1] + 1)
    else:
        l = [0 if i >= len(y)+n else y[i - n] for i in range(len(y) - n)]
        for i in range(-n):
            l2.insert(0 ,l2[0] - 1)
    return l, l2


def convolucao(xn, hn, n):
    soma = 0
    conv = 0
    yn = []
    for i in range(n):
        for k in range(0, i+1):
            hk = i - k
            if 0 <= hk < len(hn) and 0 <= k < len(xn) :
                conv = xn[k] * hn[hk]
            else:
                conv = 0
            soma = soma + conv

        yn.append(soma)
        soma = 0
    return yn

def convolucao2(xn, hn, n):
    soma = 0
    yn = []
    for i in range(n):
        for k in range(0, i+1):
            hk = i - k
            if hk >= 0:
                conv = xn[k] * hn(hk)
            else:
                conv = 0 
            soma += conv

        yn.append(soma)
        soma = 0
    return yn


#l = [0,1,2,3,5]
#l1 = [0.8,0,0.5,0.70,0,1.3]
#l2=[1.0,0,0.25,0.125,0,0.0625]
#l3 = convolucao2(l1, l2)
l1 = [300.0,100.0,100.0,100.0,100.0,100.0]

n = 6
n1 = list(range(n))
l2 = lambda n: 1.0*(1.005**n)
l3 = convolucao2(l1, l2, n)
n = list(range(20))
#xn = [np.cos((np.pi*i)/4) for i in n]
#n2 = list(range(20))
#xn2= [np.cos((3*np.pi*i)/8) for i in n]


#y = lfilter(b, a, x)
print(l3)
plt.stem(n1,l3)
plt.show()



