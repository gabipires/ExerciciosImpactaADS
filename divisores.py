# Ler um número inteiro N e calcular todos os seus divisores.

n=int(input("Insira um número inteiro: "))

for i in range(1,n+1):
    if n%i == 0:
        print(i)