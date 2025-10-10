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

def convolucao2(xn, hn):
    soma = 0
    yn = []
    for n in range(len(xn)):
        for k in range(0, n+1):
            hk = n - k
            if hk >= 0:
                conv = xn[k] * hn(hk)
            else:
                conv = 0 
            soma += conv

        yn.append(soma)
        soma = 0
    return yn

l = [0,1,2,3,5]
l1 = [0.8,0,0.5,0.70,0,1.3]
l2=[1.0,0,0.25,0.125,0,0.0625]
#l2 = lambda n: 0.5**n
l3 = convolucao2(l1, l2)
n = list(range(len(l1)))
plt.stem(n,l1)
plt.show()
print(l3)


