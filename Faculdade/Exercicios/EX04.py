print("---Fatorial do Hacker---")
#----------------------------------------------
tempo=int(input("Digite o tempo em minutos: "))
a=tempo-1
b=tempo
#----------------------------------------------
for i in range(1,tempo):
    c=b*a
    a=a-1
    b=c
#----------------------------------------------
print("A senha é: LIBERDADE{}".format(c))
