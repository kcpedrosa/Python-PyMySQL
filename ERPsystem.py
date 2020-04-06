import matplotlib.pyplot as plt
import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,

)

autentic = False

def loginRegister():
    existingUser = 0
    autenticated = False
    masterUser = False

    if decision == 1:
        username = input('Insert username: ')
        password = input('Insert password: ')

        for line in result:
            if username == line['username'] and password == line['password']:
                if line['level'] == 1:
                    masterUser = False
                elif line['level'] == 2:
                    masterUser = True
                autenticated = True
                break
            else:
                autenticated = False

        if autenticated == False:
            print('Wrong username or password ')

    elif decision == 2:
        print('Make your registration')
        username = input('Insert username: ')
        password = input('Insert password: ')

        for line in result:
            if username == line['username'] or password == line['password']:
                existingUser = 1

        if existingUser == 1:
            print('User or password already registered, try another user/password')
        elif existingUser == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastro(username, password, level) values (%s,%s,%s) ', (username, password, 1))
                    conexao.commit()
                print('User registrated successfully')
            except:
                print('Error: cannot connect to database')

    return autenticated, masterUser

def registerProduct():
    productName=input('Insert the product name: ')
    ingredient=input('Insert ingredients: ')
    productGroup=input('Insert group for the product: ')
    price=float(input('Insert price: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into product(productName,ingredient,productGroup,price) values(%s ,%s, %s, %s) ', (productName, ingredient, productGroup, price))
            conexao.commit()
            print('Product registered successfully')
    except:
        print('Error: cannot insert data into database')

def listProduct():
    products = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from product')
            registeredProducts = cursor.fetchall()

    except:
        print('Error: cannot connect to database')

    for c in registeredProducts:
        products.append(c)


    if len(products) != 0:
        for c in range(0, len(products)):
            print(products[c]['productName'])
            print(f'O id é {products[c]["id"]}')
            print(f'The price is R$ {products[c]["price"]}')
    else:
        print('No registered product')

def deleteProduct():
    idDelete = int(input('Insert the id to delete the product register: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from product where id = {}'.format(idDelete))
    except:
        print('Error: cannot delete product, id may not exist')

def listOrders():
    orders = []
    decision = 0

    while decision != 2:
        orders.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from orders')
                orderList = cursor.fetchall()

        except:
            print('Error: no data found in database')

        for i in orderList:
            orders.append(i)

        if len(orders) != 0:
            for i in range(0, len(orders)):
                print(orders[i])
        else:
            print('No order was done')

        decision = int(input('Enter 1 to set order as delivered or 2 to go back'))

        if decision == 1:
            idDelete = int(input('Enter the orders id to set it as delivered and delete it'))

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from orders where id = {}'.format(idDelete))
                    print('Order set as DELIVERED and deleted from order list')
            except:
                print('Error: cannot set as delivered, try a valid ID')

def generateStatistics():
    nomeprodutos = []
    nomeprodutos.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from product')
            products = cursor.fetchall()
    except:
        print('Error: cannot connect to database to catch products')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from sellingstatistics')
            sold = cursor.fetchall()
            #sold will receive the content of sellingstatistics
    except:
        print('Error: cannot connect to database to cath statistics from sellingstatistics')

    state = int(input('Enter 0 to get back,\n'
                      ' 1 to search for NAME and 2 for QUANTITY '))

    if state == 1:
        decision3 = int(input('Enter 1 to search for MONEY and 2 for QUANTITY'))
        if decision3 == 1:

            for i in products:
                nomeprodutos.append(i['productName'])

            #I think these var bellow should be aside of productsName
            values = []
            values.clear()

            for h in range(0, len(nomeprodutos)):
                sumValue = -1
                for i in sold:
                    if i['name'] == nomeprodutos[h]:
                        #inversion?
                        sumValue += i['price']
                        #questionable use of sumValue = -1
                if sumValue == -1:
                    values.append(0)
                elif sumValue > 0:
                    values.append(sumValue+1)

            plt.plot(nomeprodutos, values)
            plt.ylabel('Sold quantitiy in monetary value')
            plt.xlabel('Products')
            plt.show()

        if decision3 == 2:
            uniqueGroup = []
            uniqueGroup.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from product')
                    group = cursor.fetchall()
            except:
                print('Error: unable to reach product table')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from sellingstatistics')
                    soldGroup = cursor.fetchall()
            except:
                print('Error: unable to reach sellingstatistics table')

            for i in group:
                uniqueGroup.append(i['productName'])

            uniqueGroup = sorted(set(uniqueGroup))

            finalQnt = []
            finalQnt.clear()

            for h in range(0, len(uniqueGroup)):
                quantity = 0
                for i in soldGroup:
                    if uniqueGroup[h] == i['name']:
                        #line above inverted comprd to decision == 1
                        quantity += 1
                finalQnt.append(quantity)

            plt.plot(uniqueGroup,finalQnt)
            plt.ylabel('Quantity sold')
            plt.xlabel('Products')
            plt.show()

    elif state == 2:
        decision3 = int(input('Enter 1 to search for MONEY and 2 for QUANTITY'))
        if decision3 == 1:

            for i in products:
                nomeprodutos.append(i['productGroup'])
                #nameproducts is receiving the groups [drinks, pizza etc]


            values = []
            values.clear()

            for h in range(0, len(nomeprodutos)):
                sumValue = -1
                for i in sold:
                    if i['groupSell'] == nomeprodutos[h]:
                        # inversion?
                        sumValue += i['price']
                        # questionable use of sumValue = -1
                if sumValue == -1:
                    values.append(0)
                elif sumValue > 0:
                    values.append(sumValue + 1)

            plt.plot(nomeprodutos, values)
            plt.ylabel('Total value by group')
            plt.xlabel('Products')
            plt.show()

        if decision3 == 2:
            uniqueGroup = []
            uniqueGroup.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from product')
                    group = cursor.fetchall()
            except:
                print('Error: unable to reach product table')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from sellingstatistics')
                    soldGroup = cursor.fetchall()
            except:
                print('Error: unable to reach sellingstatistics table')

            for i in group:
                uniqueGroup.append(i['productGroup'])

            uniqueGroup = sorted(set(uniqueGroup))

            finalQnt = []
            finalQnt.clear()

            for h in range(0, len(uniqueGroup)):
                quantity = 0
                for i in soldGroup:
                    if uniqueGroup[h] == i['groupSell']:
                        # line above inverted comprd to decision == 1
                        quantity += 1
                finalQnt.append(quantity)

            plt.plot(uniqueGroup, finalQnt)
            plt.ylabel('Quantity sold by group')
            plt.xlabel('Products')
            plt.show()




while not autentic:
    decision = int(input('Type 1 to LOG IN and 2 to REGISTER :'))

    #o try except facilita tratar os erros
    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastro')
            result = cursor.fetchall()

    except:
        print('Error - Connection to database failed ')

    autentic, supremeUser = loginRegister()

if autentic == True:
    print('Autenticated successfully')

    if supremeUser == True:
        userdecision = 1

        while userdecision != 0:
            userdecision = int(input('Type 0 to cancel, 1 to register a product, '
                                 '2 to list registered products,\n '
                                     'and 3 to list the orders from the tables,\n'
                                     'and 4 to view STATISTICS  '))

            if userdecision == 1:
                registerProduct()
            elif userdecision == 2:
                listProduct()

                delete = int(input('Insert 1 to delete a product or 2 to exit  '))
                if delete == 1:
                    deleteProduct()

            elif userdecision == 3:
                listOrders()

            elif userdecision == 4:
                generateStatistics()