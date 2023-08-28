''' Lista de Exercícios: Funções
Trata-se de três questões sobre Funções
'''

#Questão 01
'''Faça um programa com uma função que necessite de três argumentos
Forneça a soma deles'''

def soma(a,b,c):
    print(f'A soma é: {a+b+c}')

soma(1,2,3)


#Questão 02
''' Faça uma função que retorne o reverso de um num inteiro'''

def reverso(num):
    return int(num[::-1])

num=input('Digite um número: ')

print(f'Seu número é {num}, o reverso é: {reverso(num)}')


#Questão 03
'''Escreva um script que pergunte se o usuário quer
converter a temperatura para Celsius ou Fahrenheit
Crie uma função para cada uma e uma tereira que será um menu
'''

def celsius_to_fahren(celsius):
    return (celsius*1.8)+32

def fahren_to_celsius(fahren):
    return (fahren-32)/1.8

def menu():
    print("Vamos converter a temperatura?")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = int(input("Escolha um número: "))
    temp= float(input("Digite sua temperatura: "))
    if opcao == 1:
        print(f'Sua temperatura em Fahrenheit é: {celsius_to_fahren(temp)}')
    elif opcao == 2:
        print(f'Sua temperatura em Celsius é: {fahren_to_celsius(temp)}')
    else: print('Valor errado, reinicie o programa')

menu()