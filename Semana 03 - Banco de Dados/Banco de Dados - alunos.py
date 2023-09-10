import sqlite3

conexao = sqlite3.connect('bancodedados')
cursor = conexao.cursor()

'''Criação da Tabela'''
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100),idade, curso VARCHAR(100))')

'''Registro dos alunos'''
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Ana",39,"Farmácia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2,"Vanessa",30,"Design")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3,"Mariana",23,"Química")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4,"Gabriela",24,"Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5,"Letícia",18,"Engenharia")')
#cursor.execute('UPDATE alunos SET curso="História" WHERE nome = "Ana"')

'''Consultas Básicas'''
#Selecionar todos os registros da tabela "alunos"
#cursor.execute('SELECT * FROM alunos')
#Selecionar o nome e a idade dos alunos com mais de 20 anos
#cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
#Selecionar os alunos do curso de "Engenharia" em ordem alfabética
#cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
#Contar o número total de alunos na tabela
#cursor.execute('SELECT COUNT(*) as n_alunos FROM alunos')

'''Atualização e Remoção'''
#cursor.execute('UPDATE alunos SET idade="24" WHERE nome = "Gabriela"')
#cursor.execute('DELETE FROM alunos where id=5')

#for alunos in dados:
#    print(alunos)


conexao.commit()
conexao.close