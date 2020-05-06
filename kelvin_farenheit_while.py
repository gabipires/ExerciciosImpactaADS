azul = "\033[0;0m\033[0;34m"
branco = '\033[m'

while True:
    msg_a="Me passe T em Celsius e converto para Farenheit ou "
    msg_b="escreva saida para sair: "
    celsius= input(msg_a + msg_b)
    if celsius == "saida":
        break
    try:
        celsius = float(celsius)
        kelvin = celsius + 273.15
        print(azul,"Valor convertido para Kelvin:", branco, "%.2f" % kelvin)
    except ValueError: #aqui especificamos o erro que queremos tratar
        print("Entrada inesperada")
        pass

print ("FIM!")