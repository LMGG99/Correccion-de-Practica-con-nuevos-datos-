#Los ultimos ejercicios estan enfocados en diccionarios

juego1 = {
	'Tipo': 'Accion',
	'Nombre': 'Grand Thef Auto v',
	'Costo': '455.78'
}
print('El juego', juego1['Nombre'], 'cuesta', juego1['Costo'], '$.')

print('Caracteristicas del juego')
for x in juego1:
	print(x, '=', juego1[x] + '.')

del juego1['Costo']
print(juego1['Nombre'])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('Si quisiera comprar el gta v y otro juego el costo seria el siguiente')
def Costos(costo1, costo2):
	print(costo1 + costo2)

Costos(455.78, 1200)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Epoca(*args):
	pass
Epoca('1999', '2000', '2001', '2002')#Aqui Tendriamos 4 argumentos
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Epoca(*args):
 print('En ese tiempo de ', args[1], 'es cuando naci.', 'En esa epoca de ', args[0], 'tenia 3 añitos.')

Epoca('2002','1999')

def gastos(*args):
	Canasta = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El gasto total del super es de:', Canasta)

gastos(31, 423, 133, 221, 495)
