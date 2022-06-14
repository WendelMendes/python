#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print("-"*30)
print(" "*13,"Olá"," "*13)
print("-"*30)
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
total=nota1+nota2
media=total/2 #total/quantidade
print("A média correpondente as duas notas do aluno {} e {} é de {:.1f}!".format(nota1,nota2,media))
