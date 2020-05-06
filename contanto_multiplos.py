# Faça um programa que receba dois inteiros x e n, com x, n > 0 e x < n, e conte o número de múltplos de x
# menores do que n.

x = int(input("Digite um número inteiro: "))
n = int(input("Digite outro número inteiro: "))


cont = 0
for i in range(1, 1000):
    a = i*x
    if a < n:
        cont += 1

print("O numero {} tem {} multiplos menores que {}.".format(x,cont,n))