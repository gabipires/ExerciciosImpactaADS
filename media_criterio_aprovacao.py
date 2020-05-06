# Escreva um programa que receba as notas e a presença de um aluno, calcule a média e imprima a situação final do aluno.
# No semestre são feitas 3 provas, p1, p2 e p3, e faz-se a média ponderada com pesos 2, 2 e 3, respectivamente.
# Os critérios para aprovação são:
# 1 - Frequência mínima de 75%.
# 2 - Média final mínina de 6.0 (calculada com uma casa de precisão).
# E devem ser considerados os casos especiais descritos para a impressão dos resultados, com uma mensagem
# personalizada para cada situação.

p1=float(input("Nota prova 1: "))
p2=float(input("Nota prova 2: "))
p3=float(input("Nota prova 3: "))

media= (p1*2 + p2*2 + p3*3)/7
media= round(media,1)

frequencia=float(input("Frequência: "))
frequencia_calculada=int(frequencia)

msg_frequencia="Frequencia: {}%".format(frequencia_calculada)
msg1= "Aluno aprovado com louvor!"
msg2="Aluno aprovado!"
msg3="Aluno de recuperacaoo!"
msg4="Aluno reprovado!"
msg5="Aluno reprovado por faltas!"

if frequencia_calculada<75:
    print(msg_frequencia)
    print("Media: {}".format(media))
    print(msg5)

elif frequencia_calculada>=75:
    if media > 9:
        print(msg_frequencia)
        print("Media: {}".format(media))
        print(msg1)

    if 6 <= media <= 9:
        print(msg_frequencia)
        print("Media: {}".format(media))
        print(msg2)

    if 4 <= media < 6:
        print(msg_frequencia)
        print("Media: {}".format(media))
        print(msg3)

    if media < 4:
        print(msg_frequencia)
        print("Media: {}".format(media))
        print(msg4)

else:
    pass