#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = int(input("Digite a quantidade de kilometros percorridos: "))
aluguel = float(input("Digite a quantidade de dias pelo quais ele foi alugado: "))
valorKm = km * 0.15
valorAluguel = aluguel * 60
valorTotal = valorAluguel + valorKm
print("O total a pagar é: {:.2f}R$".format(valorTotal))
