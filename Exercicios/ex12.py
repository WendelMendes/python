#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura=float(input("Digite a largura da parede em metros: "))
altura=float(input("Digite a altura da parede em metros: "))
area=largura*altura
qntd_tinta=area/2
print("A parede mede {} metros quadrados.".format(area))
print("A quantidade de latas de tintas é: {}l".format(qntd_tinta))
