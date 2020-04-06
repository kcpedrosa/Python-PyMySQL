
while True:
    try:
        x = int(input('digite sua idade: '))
        print(f'sua idade é {x}')
        break
    except:
        print('digite a idade corretamente')
    finally:
        print('obrigado por usar o sistema')

