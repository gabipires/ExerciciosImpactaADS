# Escreva uma função que receba como entrada um número e retorne a quantidade de dígitos pares que o compõem.
# Exemplo: 234 tem 3 dígitos, mas apenas 2 são pares

def conta_digitos_pares(var):
    tamanho = 0
    while var !=0:
        digito = var%10
        var = var//10
        if digito % 2 == 0:
            tamanho += 1

    return tamanho

