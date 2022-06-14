#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
a=float(input("Digite um número: "))
dobro=a*2
triplo=a*3
raiz=a**(1/2)
print("O dobro do número {} é: {} \nseu triplo é {} \ne sua raiz quadrada é {:.3f}".format(a,dobro,triplo,raiz))
