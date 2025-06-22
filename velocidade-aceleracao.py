import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

print("Insira a função posição: ")
exp = sp.sympify(input())

exp_velocidade = sp.diff(exp)
exp_aceleracao = sp.diff(exp_velocidade)

print("s(t): " + str(exp))

print("v(t): " + str(exp_velocidade))

print("a(t): " + str(exp_aceleracao))

t = sp.Symbol('t')

func = sp.lambdify(t, exp, 'numpy')
func_velocidade = sp.lambdify(t, exp_velocidade, 'numpy')
func_aceleracao = sp.lambdify(t, exp_aceleracao, 'numpy')

print("Insira o valor inicial do intervalo de tempo")
tempo_inicial = input()
print("Insira o valor final do intervalo de tempo")
tempo_final = input()
tempo = np.linspace(int(tempo_inicial), int(tempo_final))

valores = func(tempo)
valores_velociade = func_velocidade(tempo)
valores_aceleracao = func_aceleracao(tempo)

plt.plot(tempo,valores, label='s(t)', color='blue')
plt.plot(tempo,valores_velociade, label='v(t)', color='red')
plt.plot(tempo,valores_aceleracao, label='a(t)', color='green')
plt.grid(True)
plt.show()