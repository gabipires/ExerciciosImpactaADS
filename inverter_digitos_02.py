# Inverter os dígitos um numero inteiro qualquer

var = int(input("Digite um número"))

saida=0
tamanho = len(str(var))
posicao = tamanho - 1

while var > 0:
    digito = var%10
    var=var//10
    saida += digito*10**posicao
    posicao -=1

print(saida)