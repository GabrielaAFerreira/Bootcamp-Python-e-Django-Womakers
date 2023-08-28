''' Lista de Exercícios: Extras de Python
Trata-se de quatro questões para testar o conhecimento em Python
'''

#Questão 01
'''Crie um programa que leia quanto dinheiro uma pessoa tenha
Converta para moedas estrangeiras.
'''

def convert_moeda(cart):
    dolaramer=cart/4.91
    pesoarg=cart/0.02
    dolaraust=cart/3.18
    dolarcan=cart/3.64
    francosui=cart/0.42
    euro=cart/5.36
    libraest=cart/6.21
    return print(f'Você pode comprar:\n{dolaramer:.2f} Dólares americanos, {pesoarg:.2f} Pesos Argentinos, {dolaraust:.2f} Dólares Australianos\n{dolarcan:.2f} Dólares Canadenses, {francosui:.2f} Francos Suiço, {euro:.2f} Euros\n{libraest:.2f} Libras Esterlinas')

cart=float(input('Quanto você tem na sua carteira? R$'))
convert_moeda(cart)


#Questão 02
'''Escreva um programa que pergunte quantos km o carro alugado percorreu
E a quantidade de dias alugados
Calcule o preço a se pagar
'''

def preco_carro_alug(km_rod,dias):
    return 80*dias + 0.2*km_rod

km_rod=int(input("Quantos km seu carro percorreu? "))
dias=int(input("E por quantos dias? "))

print(f'O preço a pagar é de R${preco_carro_alug(km_rod,dias)}')


#Questão 03
'''Faça um algoritmo que leia osalário de um funcionário
e mostre seu novo salário.
Se o salário for até R$1000,00 o funcionário terá 20% de aumento.
Entre R$1001,00 até R$2800,00 o funcionário terá 10% de aumento.
Acima de R$2801,00 o funcionário terá 5% de aumento.
'''

def novo_sal(sal):
    if 0<=sal<=1000:
        return sal*1.2
    elif 1001<=sal<=2800:
        return sal*1.1
    elif 2801<=sal:
        return sal*1.05
    else: print("erro")   

sal=float(input('Digite seu salário: R$'))
print(f'Seu novo salário será de R${novo_sal(sal)}')


#Questão 04
'''Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor númerico.
Ex:n=leiaInt(Digite um n)
'''

def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

numero = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número: {numero}")
