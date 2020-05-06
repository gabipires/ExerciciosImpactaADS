# Receba um numero inteiro com 3 dígitos e inverta a ordem de seus algarismos.

num = int(input("Digite um número com 3 digitos: "))

a = num%10
b = num//10
c = b%10
d = b//10

e=str(a)
f=str(b)
g=str(c)
h=str(d)

print(e+g+h)