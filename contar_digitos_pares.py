var = int(input())

tamanho = 0

while var !=0:
    digito = var%10
    var = var//10
    if digito % 2 == 0:
        tamanho += 1

print(tamanho)