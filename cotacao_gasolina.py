# Você cansou de tantas fake news sobre o preço da gasolina nos EUA e resolver calcular os valores por conta própria.
# Porém, descobriu que nos EUA a gasolina tem preço cotado em dólar/galão, enquanto que no Brasil é usado real/litro.
# Por isso, resolveu escrever um programa que realize as conversões e cálculos para você, facilitando a comparação dos
# preços da gasolina nos EUA e no Brasil.
# O seu programa irá receber o valor em dólares de um galão de gasolina nos EUA (1 galão equivale a 3,7854 litros, mas
# para facilitar trabalhe com 3,8 litros), o valor em reais do litro no Brasil e a cotação do dólar em reais.
# Com base nisso, seu programa deve determinar o valor da gasolina nos EUA em reais/litro e informar aonde a gasolina
# está mais barata (ou se é igual).

galao_dolares_EUA=float(input("Preco do galao em dolares: "))
litro_reais_BRA=float(input("Preco do litro da gasolina no Brasil: "))
cotacao_dolar=float(input("Cotacao dolar: "))

preco_litro_EUA=(galao_dolares_EUA/3.8)*cotacao_dolar

print('Gasolina EUA: R$ %.2f' % preco_litro_EUA)
print('Gasolina Brasil: R$ %.2f' % litro_reais_BRA)

if preco_litro_EUA > litro_reais_BRA:
    print("Mais barata no Brasil")

elif preco_litro_EUA < litro_reais_BRA:
    print("Mais barata nos EUA")

else:
    print("Igual")