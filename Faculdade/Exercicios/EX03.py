print("---Cálculo de notas escola de inglês JoWell Sant’ana")
#-------------------------------------------------------------------------------------------
notaImpar=1
somaImpar=0
notaPar=2
somaPar=0
#-------------------------------------------------------------------------------------------
while(notaImpar<=25):
    print("---Você está digitando as notas ímpares---")
    impar=float(input("Por favor, insira a nota do aluno de número {}: ".format(notaImpar)))
    notaImpar=notaImpar+2
    somaImpar=somaImpar+impar
#-------------------------------------------------------------------------------------------
while(notaPar<=24):
    print("---Você está digitando as notas Pares---")
    par=float(input("Por favor, insira a nota do aluno de número {}: ".format(notaPar)))
    notaPar=notaPar+2
    somaPar=somaPar+par
#-------------------------------------------------------------------------------------------
totalImpar=somaImpar/13
totalPar=somaPar/12
print("A média da parte Ímpar da turma foi: {:.1f}".format(totalImpar))
print("A média da parte Par da turma foi: {:.1f}".format(totalPar))
#-------------------------------------------------------------------------------------------
if(totalImpar>totalPar):
    print("A maior média foi da parte Ímpar da turma!")
else:
    print("A maior média foi da parte Par da turma!")