import pymysql.cursors

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'interacaopython',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with conexao.cursor() as cursor:
    cursor.execute('select * from cadastro')
    #podemos fazer busca apenas por select nome from cadastro
    resultado = cursor.fetchall()

print(resultado)

for dado in resultado:
    print(f'o nome do cliente é {dado["nome"].upper()} e seu endereço é {dado["endereco"]}')