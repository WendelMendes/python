tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(10,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))
#----------------------------------------------------------------------------------
for numero in range(1,int(input("Digite um numero para determinar o fim: ")),1):
print ("	" + str(numero))
#----------------------------------------------------------------------------------
#“para a variável x no intervalo entre 0 e 9, faça:”.
#
numero=int(input("Digite um numero: "))
while numero<100:
    print("	" + str(numero))
    numero=numero+1
print("Laço encerrado....")
#----------------------------------------------------------------------------------------------
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()
# PRIMEIRO PROBLEMA A SER RESOLVIDO
while doenca_infectocontagiosa!="SIM" and  doenca_infectocontagiosa!="NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
