import sqlite3

conexao = sqlite3.connect('bancodedados')
cursor = conexao.cursor()

'''Criação da Tabela'''
#cursor.execute('CREATE TABLE clientes(id SERIAL PRIMARY KEY, nome VARCHAR(100),idade INT, saldo float)')

'''Registro dos clientes'''
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (1,"Ana",39,"350.00")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (2,"Vanessa",30,"35.20")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (3,"Mariana",23,"96.0")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (4,"Gabriela",24,"2200.0")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (5,"Letícia",18,"1550.0")')

'''Consulta e Função Agregada'''
#Selecionar o nome e a idade de clientes maiores de 30 anos
#cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
#Calcule o saldo médio dos clientes
#cursor.execute('SELECT SUM(saldo)/COUNT(*) as m_clientes FROM clientes')
#Encontre o cliente com saldo máximo
#cursor.execute('SELECT nome,saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
#Conte quantos clientes têm saldo acima de 1000
#cursor.execute('SELECT COUNT(*) as n_clientes FROM clientes WHERE saldo>1000')

'''Atualização e Remoção com Condições'''
#cursor.execute('UPDATE clientes SET saldo="4860" WHERE nome = "Vanessa"')
#cursor.execute('DELETE FROM clientes where id=5')

'''Junção de Tabelas'''
#cursor.execute('CREATE TABLE compras(id SERIAL PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor float, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (1,1,"Sabonete",9.90)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (2,1,"Pasta de Dente",5.80)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (3,4,"Papel Higiêncio",26.50)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (4,2,"Vinho",19.90)')

dados=cursor.execute('SELECT clientes.nome AS nome,compras.produto,compras.valor FROM compras INNER JOIN clientes ON compras.cliente_id=clientes.id')

for clientes in dados:
    print(clientes)

conexao.commit()
conexao.close