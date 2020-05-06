# Faça um programa que leia três notas (valores reais) de um aluno, calcule sua média aritmética e imprima uma
# mensagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer prova final. O critério de aprovação é o seguinte:
# Aprovado (média >= 7);
# Reprovado (média < 3);
# Prova final ( 3 <= média < 7).


nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))
media= (nota1 + nota2 + nota3)/3
if media>=7:
    print("aprovado")
elif 3 <= media < 7:
    print("prova final")
else:
    print("reprovado")