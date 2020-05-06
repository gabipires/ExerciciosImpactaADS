# Escreva um programa que leia números inteiros da entrada padrão até que seja informado um número negativo.
# A cada leitura o número lido deve ser escrito na saída padrão.

num = int(input("Insira um número: "))

while num >= 0:
    print(num)
    num = int(input("Insira outro número: "))
print("FIM")