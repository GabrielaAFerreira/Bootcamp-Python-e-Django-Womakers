''' Lista de Exercícios: Listas, Tuplas e Dicionários
Trata-se de quatro questões sobre Listas, tuplas e dicionários
'''

#Questão 01
''' Faça um programa que peça quatro notas de 10 alunos
Calcule e armaze em uma lista média de cada aluno
Imprima o número de alunos com média maior ou igual a 7.0
'''

#Essa não é uma das melhores formas de fazer essa questão
#Pensar em maneiras de tornar mais dinâmico

lista_notas=[]
while len(lista_notas)<10:
    print("Digite as notas do aluno:")
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    nota3=float(input('Nota 3: '))
    nota4=float(input('Nota 4: '))
    media=(nota1+nota2+nota3+nota4)/4
    lista_notas.append(media)

media7=sum(1 for media in lista_notas if media >=7.0)
print(f'A quantidade de alunos com média maior ou igual a 7.0 é: {media7}')


#Questão 02
'''Faça um programa que o usuário coloque seu nome
Mostre o nome dele de trás para frente em letras maiusculas
'''

nome=input("Digite seu nome: \nExemplo: mariana, Ághata.\n")
print(f'Seu nome invertido é: {nome.upper()[::-1]}')


#Questão 03
'''Escreva um programa onde todos os valores de um dicionário são emetidos
Se sim imprima True, se não Falso'''

def ver_val(dic):
    for val in dic.values():
        if val is None:
            return False
    return True

# Exemplo
ex_dic = {'a': 5, 'b': None, 'c': 'valor'}

print(f'Seu dicionário é {ex_dic}')
print(ver_val(ex_dic))


#Questão 04
'''Utilizando listas faça um programa de 5 perguntas sobre um crime.
'''

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

def fazer_perg(perg):
    resposta = input(perg + " (Sim ou Não): ").lower()
    return resposta == "sim"

respostas_positivas = 0

for perg in perguntas:
    if fazer_perg(perg):
        respostas_positivas += 1

if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
