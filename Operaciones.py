#!/usr/bin/python36
__author__ = "Edu Santos PAZ"
__copyright__ = "Copyright 2017"
__credits__ = ["Emanuel Mendez", "Oscar Luis Sanchez"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Edu Santos PAZ"
__email__ = "eduardo@edsantoshn.com"
__status__ = "Development"

import math
class OperacionesMatematicas:
	"""El nombre de la clase es OperacionesMatematicas el nombre del archivo es Operaciones.py al momento de la herencia utilizaremos la siguiente momenclatura
	class NombreClaseHija(NombreDelArchivo.NombreClasePadre):"""
	def __init__(self):
		print("Bienvenid@ al Paquete de Herramientas Matematicas")

	def fibonacci(self,n):
		"""Realiza N veces el ciclo del algoritmo de fibonacci para encontrar la respuesta al ciclo, 
		Al inicio se utilizaba para obtener la cantidad de parejas de conejos se obtendria al año si iniciabamos con 1 pareja"""
		a=1
		b=0
		for i in range(n-1):
			total= a + b
			b=a
			a= total
		return a

	def exponer(self,base,exponente):
		"""Expone la base y retorna el resultado de la operacion """
		return(base**exponente)

	def raizcuadrada(self,raiz):
		"""Obtiene la raiz cuadra del numero y lo retorna"""
		return math.sqrt(raiz)

	def iva(self,subtotal):
		"""Multiplica el subtotal por el 15 por ciento y retorna el resultado de la operacion"""
		return (subtotal*0.15)

	def promedio(self,total,promedio):
		"""Divide el numero total entre el numero promedio y retorna el resultado de la operacion"""
		return(total/promedio)

	def sueldo(self,nohora,pagohora):
		"""Multiplica el numero de horas trabajadas por el pago por hora trabajada y retorna el resultado de la operacion"""
		return(nohora*pagohora)

	def par_impar(self,numero):
		"""Verifica si un numero es par o impar y retonar un mensaje con el resultado"""
		if(numero%2==0):
			return'El numero {0} es par'.format(numero)
		else:
			return'El numero {0} es impar'.format(numero)
	
	def numero(self,numero1,numero2,numero3):
		"""Verifica si un numero es la suma de los otros dos, de ser asi retorna un mensaje con el numero y cual es la suma."""
		if(numero1==numero2+numero3):
			return'El numero {0} es la suma de {1} y {2}'.format(numero1,numero2,numero3)
		elif(numero2==numero3+numero1):
			return'El numero {0} es la suma de {1} y {2}'.format(numero2,numero3,numero1)
		elif(numero3==numero1+numero2):
			return'El numero {0} es la suma de {1} y {2}'.format(numero3,numero1,numero2)
		else:
			return'Ningun numero es la suma de los otros dos'

	def multiplodetres(self,numero):
		"""Verifica si un numero es multiplo de tres de ser asi retorna el mensaje positivo caso contrario el mensaje negativo"""
		if(numero%3==0):
			return'El numero {0} es multiplo de tres'.format(numero)
		else:
			return'El numero {0} no es multiplo de tres'.format(numero)

	def factorizar(self,numero):
		"""Factoriza el numero y retorna el resultado de la operacion"""
		return math.factorial(numero)

	def resta_simple(self,numero_uno, numero_dos):
		"""Realiza una resta simple"""
		return numero_uno - numero_dos

	def suma_simple(self, numero_uno, numero_dos):
		"""Realiza una suma simple"""
		return numero_uno+numero_dos

	def division_simple(self, numero_uno, numero_dos):
		"""Realiza una division simple"""
		return numero_uno/numero_dos

	def multiplicasion_simple(self, numero_uno, numero_dos):
		"""Realiza una multiplicacion simple"""
		return numero_uno*numero_dos

	def imprimir_texto_n_veces(self, texto, n_veces):
		"""imprime un determinado texto pasado por parametro la cantidad de veces que el usuario solicito por parametro"""
		for elemento in range(0,n_veces):
			print(texto)

	def operacion_seleccionada(self, numero_uno, numero_dos, operacion):
		"""Recibe dos numeros y la operacion que desea realizar"""
		if(operacion.lower()=="suma"):
			return numero_uno+numero_dos
		elif(operacion.lower()=="resta"):
			return numero_uno-numero_dos
		elif(operacion.lower()=="division"):
			return numero_uno/numero_dos
		elif(operacion.lower()=="multiplicacion"):
			return numero_uno*numero_dos
		else:
			print 'La operacion {0} no existe o no esta controlada'.format(operacion)
			return False

	def suma_cuadrada(self, numero_inicial, numero_final):
		"""Realiza la suma cuadra desde el numero inicial hasta el numero final"""
		suma=0
		for elemento in range(numero_inicial, numero_final):
			suma+=(elemento*elemento)
		return suma



	def puntuacion_letras(self, calificacion_uno, calificacion_dos, calificacion_tres, calificacion_cuatro):
		"""recibe las cuatro notas verifica si estan en el ragon de 0-100 y retorna la letra correspondiente"""
		promedio = (calificacion_uno+calificacion_dos+calificacion_tres+calificacion_cuatro)/4
		if(promedio>=0 or promedio <=59):
			return "E"
		elif(promedio>=60 or promedio <=69):
			return "D"
		elif(promedio>=70 or promedio <=79):
			return "C"
		elif(promedio>=80 or promedio <=89):
			return "B"
		elif(promedio>=90 or promedio <=100):
			return "A"
		else:
			print("el promedio {0} esta fuera de rango de 0-100".format(promedio))
			return False
	