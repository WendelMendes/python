#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=float(input("Digite o salário do funcionário: "))
salario2=salario+(15/100*salario)
print("O salário de {:.2f}R$ com acréscimo de ""15%"" será {:.2f}R$".format(salario,salario2))
