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
d = 'drop table pessoas'
e = 'drop table teste2'
#voce pode colocar cursor.execute(d) que pessoas sera dropada
x = 'create table teste (nome varchar(10));'
y = 'create table teste2 (nome varchar(10) not null, cpf int primary key);'

#cursor.execute('create table pessoas (nome varchar(50), idade int, endereco varchar(50), cpf int );')

with conexao.cursor() as cursor:
    cursor.execute(y)
print('processo concluido')