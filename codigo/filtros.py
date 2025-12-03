import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin
from scipy.signal import freqz
from pds import convolucao
#fc = (wc / (2*np.pi)) * fs
#h = firwin(22, cutoff=fc, fs=fs, window="boxcar")


def h_d(n, M, wc):
    return np.where(
    n == M/2,
    wc/np.pi,
    np.sin(wc * (n - M/2)) / (np.pi * (n - M/2)))

def fir (M, wc):
    h = []
    for n in range(M+1):
        h_w = h_d(n, M, wc) * 1
        h.append(h_w)
    return np.array(h)

M = 21
wc = 0.2 * np.pi
fs = 10000
h = fir(M, wc)

w, H = freqz(h)
fc = (w / (2*np.pi)) * fs
magnitude_db = 20 * np.log10(np.abs(H))
fase = np.angle(H) * 180 / np.pi

plt.subplot(2, 1, 1)
plt.plot(fc, magnitude_db, linewidth=2)
plt.xlabel("Frequência [Hz]")
plt.ylabel("Magnitude [dB]")
plt.title("Resposta em Frequência do Filtro FIR")
plt.grid(True, which="both", ls="--", lw=0.5, alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(fc, fase, linewidth=2)
plt.xlabel("Frequência [Hz]")
plt.ylabel("Fase")
plt.grid(True, which="both", ls="--", lw=0.5, alpha=0.7)
plt.tight_layout()
plt.show()


t = np.arange(0, 0.01, 1/fs)
x2 = np.cos(2*np.pi*2000*t)

n = len(t)
y = convolucao(x2.tolist(), h, n)

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.stem(t, x2)
plt.title("Sinal de entrada (2000 Hz)")
plt.grid()

plt.subplot(3,1,3)
plt.stem(t, y)
plt.title("Sinal filtrado")
plt.grid()

plt.tight_layout()
plt.show()








