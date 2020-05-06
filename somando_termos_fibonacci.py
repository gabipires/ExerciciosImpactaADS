# Ambrósio estava observando as séries, e ficou impressionado com a série de Fibonacci. A série de Fibonacci
# é enunciada recursivamente como o enésimo termo da série é a soma dos dois termos anteriores. Já os termos iniciais
# são: t1=1 e t2=1. Sabendo disto, Ambrósio solicitou que faça um programa que some vários termos da sequência
# de Fibonacci.

def fibonaci (indice):
    if indice == 1:
        saida = 1
    elif indice == 2:
        saida = 1
    else:
        termo_a=1
        termo_b=1
        contador  = 3
        while contador <= indice:
            fibonaci = termo_a + termo_b
            termo_a = termo_b
            termo_b = fibonaci
            contador  += 1
        saida = fibonaci
    return saida

numero_de_termos = int(input("Digite o número de termos que você deseja somar: "))
contador = 0
soma = 0

while contador < numero_de_termos:
    indice = int(input("Digite o índice da série: "))
    soma += fibonaci(indice)
    contador += 1

print(soma)


