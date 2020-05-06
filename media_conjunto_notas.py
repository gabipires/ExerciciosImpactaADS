# Em uma escola, um professor deve realizar três avaliações por semestre. Para o cálculo da nota final, ele pode usar
# três diferentes métodos de cálculo de médias:
# Média aritmética ("a");
# Média ponderada ("p"): nesse caso, o programa deve perguntar também os pesos de cada nota;
# Média harmônica ("h"): pode ser definida pela quantidade de notas dividida pela soma do inverso de cada nota.
# Faça um programa que calcula as três médias para um conjunto de 3 notas. Na saída também deve ser identificado a
# qual média cada valor se refere.

nota1= float(input("Nota 1: "))
nota2= float(input("Nota 2: "))
nota3= float(input("Nota 3: "))

peso_nota1=int(input("Peso 1: "))
peso_nota2=int(input("Peso 2: "))
peso_nota3=int(input("Peso 3: "))


aritmetica= (nota1 + nota2 + nota3)/3
a=round(aritmetica,1)

ponderada=((nota1*peso_nota1) + (nota2*peso_nota2) + (nota3*peso_nota3))/(peso_nota1+peso_nota2+peso_nota3)
p=round(ponderada,1)

harmonica= 3/((1/nota1) + (1/nota2) + (1/nota3))
h=round(harmonica,1)

print("a: {}".format(a))
print("p: {}".format(p))
print("h: {}".format(h))