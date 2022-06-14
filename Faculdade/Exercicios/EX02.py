print("---Resolução da votação dia da semana---")
#----------------------------------------------------------------------------
segunda=int(input("Digite a quantidade de votos para Segunda-feira: "))
terça=int(input("Digite a quantidade de votos para Terça-feira: "))
quarta=int(input("Digite a quantidade de votos para Quarta-feira: "))
quinta=int(input("Digite a quantidade de votos para Quinta-feira: "))
sexta=int(input("Digite a quantidade de votos para Sexta-feira: "))
#----------------------------------------------------------------------------
if(segunda>terça)and(segunda>quarta)and(segunda>quinta)and(segunda>sexta):
    print("Segunda-feira detêm a maior quantidade de votos!")
elif(terça>quarta)and(terça>quinta)and(terça>sexta):
    print("Terça-feira detêm a maior quantidade de votos!")
elif(quarta>quinta)and(quarta>sexta):
    print("Quarta-feira detêm a maior quantidade de votos!")
elif(quinta>sexta):
    print("Quinta-feira detêm a maior quantidade de votos!")
else:
    print("Sexta-feira detêm a maior quantidade de votos!")