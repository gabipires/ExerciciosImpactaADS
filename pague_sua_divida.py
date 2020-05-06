# Crie um programa que receba como entrada o valor total de uma dívida (número natural maior que zero) e o valor
# máximo que o devedor pode pagar todo mês (número natural maior que zero). O programa deve exibir o restante da
# dívida antes e depois de cada pagamento mensal até que a dívida zere. Obs.: quando a dívida é menor do que o máximo
# que o devedor pode pagar, ele pagará exatamente quanto deve, jamais pagará um valor superior.

total_divida= int(input("Total da dívida: "))
valor_maximo=int(input("Valor máximo a ser pago: "))

while total_divida > 0:

    nova_divida = total_divida - valor_maximo

    if total_divida >= valor_maximo:
        print("(antes)", total_divida)
        print("(depois)", nova_divida)


    else:
        print("(antes)", total_divida)
        print("(depois)", 0)

    total_divida = nova_divida