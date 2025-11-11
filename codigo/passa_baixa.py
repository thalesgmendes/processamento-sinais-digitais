import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sympy as sp


def passa_baixa(num, den):
    tf = signal.TransferFunction(num, den)
    w, mag, phase = signal.bode(tf)
    mag = 10**(mag/20)
    s = sp.Symbol('s')
    num_poly = sum(coef * s**i for i, coef in enumerate(num[::-1]))
    den_poly = sum(coef * s**i for i, coef in enumerate(den[::-1]))
    G = num_poly / den_poly
    return w, mag, phase, G, tf 


f_in = 1
tau = 2

t = np.linspace(0, 20, 2000)

x_t = np.cos(f_in * t)

num = [1]
den = [tau, 1]

w, mag, phase, G, tf = passa_baixa(num, den)
t, y, _ = signal.lsim(tf,x_t, t)


print("G(s) =", G)

plt.figure(figsize=(8, 6))

plt.subplot(3,1,1)
plt.plot(t, x_t, label='Entrada (cosseno)')
plt.plot(t, y, label='Saída do sistema')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.semilogx(w, mag)
plt.title("Diagrama de Bode - SciPy")
plt.ylabel("Amplitude")
plt.grid(True, which="both", ls="--", lw=0.5)

plt.subplot(3, 1, 3)
plt.semilogx(w, phase)
plt.xlabel("Frequência (rad/s)")
plt.ylabel("Fase (graus)")
plt.grid(True, which="both", ls="--", lw=0.5)

plt.tight_layout()
plt.show()

