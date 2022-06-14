print("---Cálculo de valor do bônus do cliente---")
#--------------------------------------------------------------------------------------------------------------
faturamentoAnual=float(input("Digite o faturamento anual do seu canal: "))
assinatura=input("Digite o nível da sua assinatura, Basic|Silver|Gold|Platinum: ")
total=0
#--------------------------------------------------------------------------------------------------------------
if(assinatura=="Basic"):
    total=faturamentoAnual*30/100
    print("Você é um usuario com assinatura Basic, o valor do bônus que o cliente deve pagar é:",total,"R$")
elif(assinatura=="Silver"):
    total=faturamentoAnual*20/100
    print("Você é um usuario com assinatura Silver, o valor do bônus que o cliente deve pagar é:",total,"R$")
elif(assinatura=="Gold"):
    total=faturamentoAnual*10/100
    print("Você é um usuario com assinatura Gold, o valor do bônus que o cliente deve pagar é:",total,"R$")
elif(assinatura=="Platinum"):
    total=faturamentoAnual*5/100
    print("Você é um usuario com assinatura Platinum, o valor do bônus que o cliente deve pagar é:",total,"R$")
else:
    print("---Ocorreu um erro, atente-se aos caracteres e tente novamente---")