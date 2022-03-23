#Del ejercicio 36 al 47 se utilizan condicionantes y bucles
Numej = 19
Numej1 = 21
Numej2 = 102

if Numej1 < Numej :
    print('Se Cumple la condicional')

else:
       print('revise la condicionante')

print('------------------------')#Separacion entre ejercicios
if Numej1 >= Numej :
    print('Se Cumple la condicional')

else:
       print('revise la condicionante')

print('-----------------------------')#separacion entre ejercicios

estatura = float(input('¿Cuánto mides en cm?\n'))
if estatura <= 0:
	print('Nadie puede medir eso.')
elif estatura <= 100 and estatura < 150:
	print('Eres un minion.')
elif estatura == 155 and estatura <= 184:
	print('Casi eres alto.')
elif estatura  >185 and estatura <= 200:
	print('Estas muy alto.')
else:
	print('Estatura incorrecta.')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')#separacion entre ejercicios


tupla_deportes = ('Basket', 'Beisbol', 'Voly', 'PingPong')
print(tupla_deportes)
deportes = input('De la lista anterior escoge un deporte:\n')
if deportes in tupla_deportes[0]:
	print('Fino señores')
elif deportes in tupla_deportes[1]:
	print('Seguro eres borracho')
elif deportes in tupla_deportes[2]:
	print('Que buen gusto')
elif deportes in tupla_deportes[3]:
	print('Pinche demente')
else:
	print('Pinches gustos feos')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')#separacion entre ejercicios
x = 0

while x <= 65:
	print(x)
	x += 15

while x >= -1500:
	print(x)
	x -= 150

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')#separacion entre ejercicios

Consolas = ('Xbox', 'PS', 'GameCube', 'Pc')

for x in Consolas:
	print(' La consola es: ' + x + '.')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')#separacion entre ejercicios
for x in range(9, 670, 60):
	print(x)