# Escreva um programa em Python 3 para somar os n primeiros termos da seguinte série:
# - 1 + 1/2 - 1/3 + 1/4 - 1/5 + ...
# A saída deve ser uma unica linha contendo apenas o resultado da somatória formatado para exibir 6 casas de precisão.

n = int(input("Quantos termos você deseja somar? "))

soma = 0
for i in range(1,n+1):
    fracao= 1/(i)
    if i%2 == 1:
        fracao = -fracao
    soma += fracao
print("{:6f}".format(soma))