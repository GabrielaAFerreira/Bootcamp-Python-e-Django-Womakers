''' Lista de Exercícios: Conceitos Básicos em Python
Trata-se de quatro questões para aplicar o básico de programação
'''

#Questão 01
''' Faça um Programa que peça um número 
e então mostre a mensagem:-> O número informado foi [número]
'''
num=int(input("Por favor digite um número: "))
print(f'Seu número foi {num}')

#Questão 02
''' Faça um programa que peça dois números e imprima a soma'''

num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
print(f'A soma de seus dois números é: {num1+num2}')

#Questão 03
'''Faça um programa que peça a temperatura em graus Celsius
e transforme em Fahrenheit '''

celsius=float(input('Digite a temperatura em Celsius: '))
fahren=(celsius*1.8)+32
print(f'Em Fahrenheit isso corresponde a {fahren}')

#Questão 04
'''Faça um programa que pergunte
quanto você ganha por hora e o número de horas trabalhadas em um mês
Calcule e mostre o total do seu salário do mês'''

ganhohora=float(input('Digite quanto você ganha por hora: R$ '))
horatrab=float(input('Digite quantas horas você trabalho esse mês: '))
salmes=ganhohora*horatrab
print(f'Seu salário desse Mês é R${salmes:.2f}')
