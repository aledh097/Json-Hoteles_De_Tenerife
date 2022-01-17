#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import os

print "------------------------------------------"
print "A= LISTAR NOMBRE DE LOS HOTELES JUNTO A SU COORDENADA"
print "B= NUMERO DE HOTELES EN EL FICHERO JSON"
print "C= BUSCAR DIRECCION SEGUN NOMBRE DE HOTEL"
print "D= BUSCAR HOTELES SEGUN SU TIPO"
print "E= DEVUELVE EL NOMBRE DEL HOTEL SEGUN SU ID"
print "F= DEVUELVE LA DIRECCION DEL HOTEL SEGUN SU GEOCODIGO"
print "G= GENERAR FICHERO HTML CON INFORMACIÓN DE LOS HOTELES"
print "EXIT= PARA SALIR"

print "------------------------------------------"
tecla=str.upper(raw_input("Opcion: "))

directory = os.getcwd()

while tecla!="EXIT":
	if tecla=="A":
		fichero=open(directory+"/hoteles.json","r")
		lineas=json.loads(fichero.readline())
		doc=lineas["docs"]
		for l in doc:
			print l["NOMBRE"]
			print l["geometry"]["coordinates"]

	if tecla=="B":
		fichero=open(directory+"/hoteles.json","r")
		lineas=json.loads(fichero.readline())
		doc=lineas["docs"]
		contador=0
		for l in doc:
			contador=contador+1
		print "Numero de hoteles: %s" % (contador)

	if tecla=="C":
		buscador=raw_input("Dime el nombre del hotel: ")
		fichero=open(directory+"/hoteles.json","r")
		lineas=json.loads(fichero.readline())
		doc=lineas["docs"]
		for l in doc:
			if l["NOMBRE"]==buscador:
				print l["DIRECCION"]

	if tecla=="D":
		buscador=raw_input("Dime el tipo de hotel: ")
		fichero=open(directory+"/hoteles.json","r")
		lineas=json.loads(fichero.readline())
		doc=lineas["docs"]
		for l in doc:
			if unicode(l["TIPO"])==unicode(buscador):
				print l["NOMBRE"]
			
	if tecla=="e" or tecla=="E":
		buscador=int(raw_input("Dime el ID del hotel: "))
		fichero=open(directory+"/hoteles.json","r")
		lineas=json.loads(fichero.readline())
		doc=lineas["docs"]
		for l in doc:
			if l["FID_1"]==buscador:
				print l["NOMBRE"]

	if tecla=="F":
		buscador=raw_input("Dime el ID del hotel: ")
		fichero=open(directory+"/hoteles.json","r")
		lineas=json.loads(fichero.readline())
		doc=lineas["docs"]
		for l in doc:
			if l["GEOCODIGO"]==buscador:
				print l["DIRECCION"]
	
	if tecla=="G":
		fichero=open("hoteles.json","r")
		lineas=json.loads(fichero.readline())
		doc=lineas["docs"]
		f=open("index.html","w")
		for l in doc:
			nom=l["NOMBRE"]
			di=l["DIRECCION"]
			y=str(l["GRAD_Y"])
			x=str(l["GRAD_X"])
			url="http://www.openstreetmap.org/way/109089302#map=17/"+y+"/"+x
			a="<h1>"+nom+"</h1>"
			b="<p>"+di+"</p>"
			c='<a href="'+url+'">Mapa</a>'
			f.write(a+"\n")
			f.write(b+"\n")
			f.write(c+"\n")
			f.write("\n")
		f.close()
			
	print "------------------------------------------"
	print "A= LISTAR NOMBRE DE LOS HOTELES JUNTO A SU COORDENADA"
	print "B= NUMERO DE HOTELES EN EL FICHERO JSON"
	print "C= BUSCAR DIRECCION SEGUN NOMBRE DE HOTEL"
	print "D= BUSCAR HOTELES SEGUN SU TIPO"
	print "E= DEVUELVE EL NOMBRE DEL HOTEL SEGUN SU ID"
	print "F= DEVUELVE LA DIRECCION DEL HOTEL SEGUN SU GEOCODIGO"
	print "G= GENERAR FICHERO HTML CON INFORMACIÓN DE LOS HOTELES"
	print "EXIT= PARA SALIR"

	print "------------------------------------------"
	tecla=str.upper(raw_input("Opcion: "))

		
