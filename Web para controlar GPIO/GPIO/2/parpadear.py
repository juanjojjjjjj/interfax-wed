#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Importar libreria GPIO
import RPi.GPIO as GPIO

#Definir modo de trabajo para la placa BCM 
GPIO.setmode(GPIO.BCM)

#Desactivo Errores
GPIO.setwarnings(False)

#Importamos la libreria time
import time

#Importamos la libreria para comandos de la consola/shell
import os

#Definir GPIO como Salida
GPIO.setup(1, GPIO.OUT)

#Asigno valor alto para que tenga corriente la salida de 3,3v por GPIO
GPIO.output(1, GPIO.HIGH)

#Pausar 1 segundo
sleep(1)

#Detener salida
GPIO.output(1, GPIO.LOW)

#Pausar 1 segundo
sleep(1)

#Asigno valor alto para que tenga corriente la salida de 3,3v por GPIO
GPIO.output(1, GPIO.HIGH)

#Pausar 1 segundo
sleep(1)

#Detener salida
GPIO.output(1, GPIO.LOW)

#Asigno valor alto para que tenga corriente la salida de 3,3v por GPIO
GPIO.output(1, GPIO.HIGH)

#Pausar 1 segundo
sleep(1)

#Detener salida
GPIO.output(1, GPIO.LOW)

#Pausar 1 segundo
sleep(1)

#Asigno valor alto para que tenga corriente la salida de 3,3v por GPIO
GPIO.output(1, GPIO.HIGH)

#Pausar 1 segundo
sleep(1)

#Detener salida
GPIO.output(1, GPIO.LOW)

#Asigno valor alto para que tenga corriente la salida de 3,3v por GPIO
GPIO.output(1, GPIO.HIGH)

#Pausar 1 segundo
sleep(1)

#Detener salida
GPIO.output(1, GPIO.LOW)

#Pausar 1 segundo
sleep(1)

#Asigno valor alto para que tenga corriente la salida de 3,3v por GPIO
GPIO.output(1, GPIO.HIGH)

#Pausar 1 segundo
sleep(1)

#Detener salida
GPIO.output(1, GPIO.LOW)

#Limpiar GPIO
GPIO.cleanup()