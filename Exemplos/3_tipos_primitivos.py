a=int(print("-1, 0, 1"))
a=float(print("-1.0, 0.0076 , 1.0"))
a=bool(print("True False (capitalizado)"))
a=str(print("Olá, 7"))

print("O tipo primitivo é?",type(a))#Descreve tipo primitivo

print("Só tem espaços?",a.isspace())
print("É um número?",a.isnumeric())
print("É alfabético?",a.isalpha())
print("Está em minúsculas?",a.islower())
print("Está em maiúsculas?",a.isupper())
print("Está capitalizada?:",a.istitle())
