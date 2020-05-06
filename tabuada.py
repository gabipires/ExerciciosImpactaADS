# Escreva um programa que imprima a tabuada de um número.

numero= int(input("Tabuada do número: "))
x=1

while x <= 10:
    print("{} x {} = {}".format(numero,x,x*numero))
    x = x+1