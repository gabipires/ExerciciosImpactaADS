# Faça um programa que dado um número inteiro n, imprima n linhas, onde cada linha deve seguir o seguinte padrão:

# 1
# 22
# 333
# 4444
# ...
# nnnnnnnnnn

n=int(input("Digite um número: "))

for i in range(1,n+1):
    a = str(i)
    print(a*i)