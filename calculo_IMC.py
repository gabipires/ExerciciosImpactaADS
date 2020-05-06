# Faça um programa que receba as características (massa e altura) de uma pessoa e retorne seu IMC - Índice de Massa
# Corporal. O valor de saída deve ser arredondado usando 2 casas decimais.

massa=float(input("Digite seu peso em kg: "))
altura=float(input("Digita sua altura em m: "))

IMC= massa/(altura*altura)


print('%.2f' % IMC)