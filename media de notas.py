#faça um programa que informa a media de notas de um aluno, de acordo com os valores inseridos

nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
media = (nota1 + nota2)/2
print (f'Como o aluno tirou {nota1} na primeira prova \n e {nota2} na segunda prova, a media é {media: .1f}')