# Inverta os digitos de um numero inteiro de 5 digitos.

num=int(input("Digite um número inteiro de 5 digitos: "))

a = num%10
b = (num//10)%10
c = (num//100)%10
d = (num//1000)%10
e = (num//10000)%10

print(str(a)+str(b)+str(c)+str(d)+str(e))