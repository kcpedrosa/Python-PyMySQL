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
a = 'joao'
b= '777'
c='jose'
d='888'


#cursor.execute('create table pessoas (nome varchar(50), idade int, endereco varchar(50), cpf int );')

with conexao.cursor() as cursor:
    cursor.execute('insert into teste2 values ("{}", "{}")'.format(c,d))
print('processo concluido')