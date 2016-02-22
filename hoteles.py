import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import ast
print "------------------------------------------"
print "A= LISTAR NOMBRE DE LOS HOTELES JUNTO A SU COORDENADA"
print "B= NUMERO DE HOTELES EN EL FICHERO JSON"
print "C= BUSCAR DIRECCION SEGUN NOMBRE DE HOTEL"
print "D= BUSCAR HOTELES SEGUN SU TIPO"

print "------------------------------------------"
tecla=raw_input("Opcion: ")

if tecla=="a" or tecla=="A":
	fichero=open("/home/usuario/prueba/prueba/hoteles.json","r")
	lineas=json.loads(fichero.readline())
	doc=lineas["docs"]
	for l in doc:
		print l["NOMBRE"]
		print l["geometry"]["coordinates"]

if tecla=="b" or tecla=="B":
	fichero=open("/home/usuario/prueba/prueba/hoteles.json","r")
	lineas=json.loads(fichero.readline())
	doc=lineas["docs"]
	contador=0
	for l in doc:
		contador=contador+1
	print "Numero de hoteles: %s" % (contador)

if tecla=="c" or tecla=="C":
	buscador=raw_input("Dime el nombre del hotel: ")
	fichero=open("/home/usuario/prueba/prueba/hoteles.json","r")
	lineas=json.loads(fichero.readline())
	doc=lineas["docs"]
	for l in doc:
		if l["NOMBRE"]==buscador:
			print l["DIRECCION"]

if tecla=="d" or tecla=="D":
	buscador=raw_input("Dime el tipo de hotel: ")
	fichero=open("/home/usuario/prueba/prueba/hoteles.json","r")
	lineas=json.loads(fichero.readline())
	doc=lineas["docs"]
	for l in doc:
		if unicode(l["TIPO"])==unicode(buscador):
			print l["NOMBRE"]
