# Definir Variables
monto = float(input("Por favor, ingrese el monto gastado: "))
categoria = input("Ingrese la categoría a la cual pertenece el gasto: ")
descripcion = input("Describa las características del gasto: ")
fecha = input("Ingrese la fecha en que realizó el gasto (dd/mm/aaaa): ")

# Mostrar en pantalla un resumen de la información recopilada
print(f"El día {fecha}, usted realizó un gasto por el monto de ${monto:.2f}, en concepto de {categoria}, con las siguientes características: {descripcion}.")

# Pseudocódigo
#Algoritmo tp_1
	#// declaración de variables
	#Definir fecha Como Cadena
	#Definir categoria Como Cadena
	#Definir descripcion Como Cadena
	#Definir monto Como Real
	#// solicitar datos al usuario
	#Escribir 'Ingrese la fecha del gasto (dd/mm/aaaa)'
	#Leer fecha
	#Escribir 'Ingrese categoria de gasto (por ejemplo: almacén, carnicería, transporte)'
	#Leer categoria
	#Escribir 'Ingrese Descripción del gasto (por ejemplo: colectivo, remis, alimento, varios)'
	#Leer descripcion
	#Escribir 'Ingrese el monto del gasto'
	#Leer monto
	#Escribir 'el día ', fecha, ' usted realizó un gasto de $', monto, ', en concepto de ', descripcion, ' dentro de la categoría ', categoria
#FinAlgoritmo