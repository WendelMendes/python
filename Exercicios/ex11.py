#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro=float(input("Digite a quantidade de dinheiro em R$: "))
dolar=dinheiro/4.87
print("Você meu amigo pode comprar U${:.2f}.".format(dolar))
