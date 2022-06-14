#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco=float(input("Digite o preço do produto: "))
desconto=5/100*preco
preco2=preco-desconto
print("O produto de valor {}R$ com desconto de ""5%"" será {:.2f}R$".format(preco,preco2))