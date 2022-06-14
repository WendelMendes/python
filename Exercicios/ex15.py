#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input("Digite um temperatura em graus Celsius: "))
fahrenheit = celsius * 1.8 + 32
print ("Celsius {:.1f}ºC, convertida para Fahrenheit será: {:.1f}ºF".format(celsius,fahrenheit))