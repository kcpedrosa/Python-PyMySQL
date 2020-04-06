dados = [0,1,2,3,4, 'mordor', 7.5,'sword']

dados.insert(3, 'sauron')
#insere sauron na pos 3

print(dados)

dados.pop(2)
dados.remove('sword')

print(dados)

magic = ['globin deck','is','noob stuff']
magic.reverse()
print(magic)

numbers = [1,2,5,0,99]
numbers.sort(reverse=True)
print(numbers)
print(sum(numbers))

manynumbers = list(range(1,101))
#pode usar um for i in range(1,101) e entao x.append(i)
print(manynumbers)