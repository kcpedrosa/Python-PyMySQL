arquivo = open('AulaPython.txt', 'r')
#to write and replace, use 'w', to add txt incrementally, use 'a'

texto = '''
Willkommen in McLarens neuem "Reiseauto" : dem McLaren GT: 
Ultraleichtes Kohlefaser-Monocoque, 
V8-Biturbo mit 620 PS, von null auf 200 km/h in 8,8 Sekunden, 
326 km/h Spitze.'''

#arquivo.write('Fahrtest')

#arquivo.write(texto)

exemplo = arquivo.readlines()
for i in exemplo:
    print(i)

arquivo.close