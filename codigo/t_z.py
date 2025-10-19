#resultado = float(sp.re(z_abs.subs(omega, valor).evalf()))


import sympy as sp
import numpy as np

omega = sp.Symbol('omega', real=True)
j = sp.I  
zeros = []
polos = [0.8]
#zeros = [0.038, 0.034]
#polos = [1.63, -0.70]

z = 1 / (1 - 0.8 * sp.exp(j * omega))
#valor_omega = sp.pi/6

N = 0.038*sp.exp(-j*omega) + 0.034*sp.exp(-2*j*omega)
D = 1 - 1.63*sp.exp(-j*omega) + 0.70*sp.exp(-2*j*omega)
H = N / D

valor_omega = np.pi/4

def amplitude(z, valor_omega):
    z_conj = sp.conjugate(z)
    produto = sp.simplify(z * z_conj)
    z_abs = sp.sqrt(produto)
    resultado = abs(z_abs.subs(omega, valor_omega).evalf())
    print(z_abs)
    return resultado

def fase(polo, valor_omega):
    resultado = -np.arctan((polo*np.sin(valor_omega))/(1-polo*np.cos(valor_omega)))
    return resultado


def fase_sistema(zeros, polos, omega):
    N = sum([z * np.exp(-1j * omega * (i + 1)) for i, z in enumerate(zeros)])
    if len(zeros) == 0:
        N = 1  
    D = 1 - sum([p * np.exp(-1j * omega * (i + 1)) for i, p in enumerate(polos)])
    fase_total = np.angle(N / D)
    return fase_total

def fase_sistema_simbolica(zeros, polos, omega_val=None):
    omega = sp.symbols('omega', real=True)
    j = sp.I
    if len(zeros) == 0:
        N = 1
    else:
        N = sum([z * sp.exp(-j * omega * (i + 1)) for i, z in enumerate(zeros)])
    if len(polos) == 0:
        D = 1
    else:
        D = 1 - sum([p * sp.exp(-j * omega * (i + 1)) for i, p in enumerate(polos)])
    H = N / D
    fase_simbolica = sp.arg(H)
    print("Fase simbólica:", fase_simbolica)

    fase_numerica = fase_simbolica.evalf(subs={omega: omega_val})
    return fase_numerica


#print(amplitude(H, valor_omega))
#phi = fase_sistema_simbolica(zeros, polos, valor_omega)
#print(phi)
#fase_num_real = sp.re(phi)  # pega apenas a parte real
#print("Fase numérica real:", fase_num_real)




def fracoes_parciais_general(numerador_coef, polos):
    N = np.poly1d(numerador_coef)
    resultados = []
    for i, p_i in enumerate(polos):
        denom = 1
        for j, p_j in enumerate(polos):
            if j != i:
                denom *= (p_i - p_j)
        A_i = N(p_i) / denom
        resultados.append((A_i, p_i))
    return resultados

#numerador_coef = [8, -19]
#polos = [0, 2, 3]

numerador_coef = [1, 0, 0]
polos = [0.500000000000000, 0.333333333333333]

res = fracoes_parciais_general(numerador_coef, polos)
for A, p in res:
   print(f"{A:.3f}/(z - {p})")


def fracoes_parciais_expr(expr, z):
    frac = sp.apart(expr, z, full=True)
    num, den = sp.fraction(expr)
    num_poly = sp.Poly(num, z)
    numerador_coef = num_poly.all_coeffs() 
    den_fatores = sp.factor_list(den)[1]  
    polos = []
    for f, e in den_fatores:
        raiz = sp.solve(f, z)
        polos.extend(raiz * e)
    
    return numerador_coef, polos, frac

# Exemplo
z = sp.Symbol('z')
#expr = (8*z - 19)/(z*(z-2)*(z-3))
expr = z**2 / (z**2 - (5/6)*z + 1/6)

numerador_coef, polos, frac = fracoes_parciais_expr(expr, z)

print("Coeficientes do numerador:", numerador_coef)
print("Polos:", polos)
print("Frações parciais:", frac)