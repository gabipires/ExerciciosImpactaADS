# A Entidade encontrou, na casa de seu avô, um baú com fotos recortadas de vários números grandes, ela ficou
# fascinada por todos aqueles números e até se esqueceu de perguntar o motivo deles para seu avô. Ela está
# planejando em colocá-los na parede de seu quarto, mas antes de escolher, ela gostaria de saber quantos dígitos
# primos existem em cada número. Então, faça um programa que conte quantos dígitos primos existem em cada número.

n=int(input("Quantos números você vai inserir: "))

for i in range(1,n+1):
    x=int(input("Insira um número: "))

    contador = 0
    while x != 0:
        digito = x%10
        x = x//10

        if digito == 2 or digito == 3 or digito == 5 or digito == 7:
            contador += 1


    print("Digitos primos: ", contador)