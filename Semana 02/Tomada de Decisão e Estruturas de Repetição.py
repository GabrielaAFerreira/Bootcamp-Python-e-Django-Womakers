''' Lista de Exercícios: Tomada de Decisão e Estruturas de Repetição
Trata-se de três questões para aplicar if, else, while e for
'''

#Questão 01
'''Faça um programa que peça dois números e imprima o maior'''

num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
if num1>num2:
    print(f'{num1} é o maior valor.')
else: print(f'{num2} é o maior valor.')

#Questão 02
'''Faça um programa que pergunte o turno que você estude
Peça para digitar M-matutino ou V-Vespertino ou N-Noturno
Imprima a mensagem Bom dia, Boa tarde, Boa noite ou Valor Inválido'''

turno=input('Qual turno você estuda? \nExemplo: M, para matutino; V, para Vespertino; ou N, para Noturno\n')
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else: print("Valor Inválido!")


#Questão 03
'''Faça um programa que peça uma nota, entre zero e dez
Mostre uma mensagem caso o valor seja inválido e continue pedindo até um valor válido'''

while True:
    nota=float(input('Digite uma nota de 0 a 10: '))
    if 0<=nota<=10:
        print(f'Sua nota é {nota}')
        break
    else: print ("Valor inválido, tente novamente")