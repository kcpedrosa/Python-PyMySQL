import pymysql.cursors

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'interacaopython',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = conexao.cursor()
a = input('Digite seu nome: ')
b = input('Digite seu endereco: ')
z = 'create table cadastro(id int primary key auto_increment, nome varchar(30) not null, endereco varchar(300));'


#cursor.execute('create table pessoas (nome varchar(50), idade int, endereco varchar(50), cpf int );')

with conexao.cursor() as cursor:
    cursor.execute('insert into cadastro(nome, endereco) values ("{}","{}")'.format(a,b))
    conexao.commit()
print('processo concluido')