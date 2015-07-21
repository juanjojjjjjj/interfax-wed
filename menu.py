#!/usr/bin/python
# -*- encoding: utf-8 -*-

###Indice del menu
#importamos la libreria GPIO
import RPi.GPIO as GPIO

#Definimos el modo BCM
GPIO.setmode(GPIO.BCM)

#Desactivo Errores
GPIO.setwarnings(False)

#Importamos la libreria time
import time

#Importamos la libreria para comandos de la consola/shell
import os

#Ahora definimos Todos los pines del 2-11 como salida
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

#Defino las variables
tiempoensegundos = 8
sleep = time.sleep

#Creo la función para salir de todo y desactivar correctamente los GPIO

#Función para importar GPIO
def importarGPIO():
	#importamos la libreria GPIO
	import RPi.GPIO as GPIO

	#Definimos el modo BCM
	GPIO.setmode(GPIO.BCM)

	#Desactivo Errores
	GPIO.setwarnings(False)

	#Importamos la libreria time
	import time

	#Ahora definimos Todos los pines del 2-11 como salida
	GPIO.setup(1, GPIO.OUT)
	GPIO.setup(2, GPIO.OUT)
	GPIO.setup(3, GPIO.OUT)
	GPIO.setup(4, GPIO.OUT)
	GPIO.setup(5, GPIO.OUT)
	GPIO.setup(6, GPIO.OUT)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(8, GPIO.OUT)
	GPIO.setup(9, GPIO.OUT)
	GPIO.setup(10, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)

	#Importamos la libreria para comandos de la consola/shell
	import os

def exitmenu():
	print("Desactivando todos los GPIO y limpiando sistema")

	os.system("espeak -ves 'Bueno, si te has cansado de esto me voy. Adios'")

	sleep(2)
	GPIO.cleanup()
	sleep(3)
	exit

def lucesaleatorias_a():
	importarGPIO()

	os.system("espeak -ves 'Hola, estoy encendiendo las luces de forma aleatoria nivel 1'")

	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	sleep(2)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(4, GPIO.HIGH)
	sleep(1)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	sleep(2)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.HIGH)
	sleep(1)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	sleep(2)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(9, GPIO.LOW)
	GPIO.output(10, GPIO.HIGH)
	sleep(1)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(11, GPIO.HIGH)
	sleep(1)
	GPIO.output(11, GPIO.LOW)
	print('Fin de la función')

	GPIO.cleanup()

def lucesaleatorias_b():
	importarGPIO()
	os.system("espeak -ves 'Hola, estoy encendiendo las luces de forma aleatoria nivel 2'")

	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)
	sleep(1)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(11, GPIO.HIGH)
	sleep(1)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.LOW)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.LOW)
	sleep(1)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(9, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)
	sleep(1)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)
	sleep(1)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(11, GPIO.HIGH)
	sleep(1)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.LOW)
	sleep(1)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)
	sleep(1)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)
	sleep(1)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)
	sleep(1)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(9, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)

	GPIO.cleanup()

def lucesfijas():
	importarGPIO()
	os.system("espeak -ves 'Hola, estoy encendiendo las luces de forma fija'")

	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)

def seleccionargpioaencender():
	importarGPIO()
	os.system("espeak -ves 'Introduce el número de LED'")

	while True:
	print """
Escribe el número de GPIO según BCM que quieras encender
		Recuerda que solo funcionan valores desde el 2 al 27

Número elegido:
"""
	seleccionGPIO=input("-->")
	if seleccionGPIO => 1 | seleccionGPIO =< 27:
		GPIO.output(seleccionGPIO, GPIO.HIGH)
		print "El GPIO" seleccionGPIO "se ha activado a 3,3V"

	else:
		print "Esta opción es incorrecta, selecciona un número del 2 al 27"


while True:
	print """
Elige una opción:

1 Para encender todos los LED
2 Para encender de forma aleatoria 1
3 Para encender de forma aleatoria 2
4 Seleccionar GPIO para activar
5 Seleccionar GPIO para apagar
6 Desactivar todos los LED
"""
	opcion=input("-->")
	if opcion == 1:
		lucesfijas()
		print "Las luces están fijas"
	elif opcion == 2:
		lucesaleatorias_a()

	elif opcion == 3:
		lucesaleatorias_b()

	elif opcion == 6:
		print("nos vemos")
		exitmenu()


	else:
		print "Esta opción es incorrecta, selecciona un número del 1 al 6"




