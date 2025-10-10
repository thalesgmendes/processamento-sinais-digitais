#Implemente um programa para resolver a resposta a entrada nula de um sistema discreto linear e invariante no tempo – slide 32/54 (Aula_4_-_Equacoes_a_diferenca.pdf).
#O programa recebe como entrada os coeficientes de y, as condições iniciais e um vetor de índices (n), sendo que tem como saída os gamas, c1 e c2, assim como plota a solução final y0 (solução homogênea). Adicionalmente, informe se o sistema é estável ou instável.
#OBS 1: Valide o código com os dados do slide 32/54;
#OBS 2: O sistema será no máximo de segunda ordem e só terá raízes reais e distintas;
#OBS 3: Não precisa enviar nada via SIGAA. O código será analisado pelo professor na aula de sexta-feira (10/10/25).
#entrada:

import numpy as np
import matplotlib.pyplot as plt

def eq_diferenca(a, b, c, n1, n2, n):
    x = [a, b, c]
    raizes = np.roots(x)
    if len(raizes) > 1:
        coef = np.array([[raizes[0]**n1[0], raizes[1]**n1[0]], [raizes[0]**n2[0], raizes[1]**n2[0]]])
        ind = np.array([n1[1], n2[1]])
        c12 = np.linalg.solve(coef, ind)
        l2 = [c12[0]*(raizes[0]**k) + c12[1]*(raizes[1]**k) for k in n]
    else:
        c12 = n1[1] / (raizes[0]**n1[0])
        l2 = [c12*(raizes[0]**k) for k in n]

    estabilidade = "Sistema instável" if np.any(abs(raizes) >= 1) else "Sistema estável"


    return c12, raizes, l2, estabilidade

n1 = [-1, 0]
n2 = [-2, 6.25]
n = list(range(20))
c12, raizes, l2, estabilidade = eq_diferenca(1, -0.6, -0.16, n1, n2, n)
print(c12, raizes)

plt.stem(n, l2)
plt.title(estabilidade)
plt.show()