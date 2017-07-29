#
# ADM
#
# Descripcion: Modulo de Reproduccion
#
# Autores: Br.Jean Alexander
#		   Br.Diego Pedroza
from lr import*
from reproductor import*
import sys

def proxima_Cancion(lista,cancion):
	if cancion == lista[len(lista)-1]:
		return lista[0]
	else:
		sig = lista.index(cancion)+1
	return lista[sig]
	
def muestraOpciones():
	print(" Por favor, ingrese alguna de las siguientes\
 opciones:\n\
 1. Cargar lista de reproducción\n\
 2. Mostrar lista de reproducción\n\
 3. Eliminar Canción\n\
 4. Reproducir\n\
 5. Pausar\n\
 6. Parar\n\
 7. Próxima canción\n\
 8. Salir del administrador de música\n")

def EleccionOpcion():
	i=0
	while True:
		
		try:
			muestraOpciones()
			opcion=int(input("Ingrese opción: "))
			print("\n")
			assert(any(opcion==i for i in range(1,9)))
			break
		except:
			print("Opción inválida\n")
			i +=1
			if i>10:
				print("Máximo de intentos alcanzado")
				sys.exit(12)
				
	return opcion

while True:
	opcion=EleccionOpcion()
	if opcion == 8:
		print("Gracias por usar nuestro modulo")
		sys.exit()
		
	elif opcion == 1 :
		i=0
		
		while True:
			try:
				try:
					archivo = str(input("Introduzca la ubicación del archivo\
 txt, sin el.txt: "))
					lista = LR()
					lista.agregarLista(archivo)
					L = lista.obtenerLR()
					rec = Reproductor(L[0])
					print("Ha sido cargada existosamente\n")
				except:
					print("Error al agregar")
				break
			except:
				print("Archivo inválido\n")
				i = i + 1
				if i >5:
					print("Ha alcanzado el máximo de intentos\n")
					break
					

	elif opcion == 2:
		try:
			lista.mostrarLR()
			print("\n")
		except:
			print("No existe lista de reproducción")
	
	elif opcion == 3:
		i=0
		i=str(input("Introduzca el nombre del interprete: "))
		t=str(input("Introduzca el título de la canción: "))
		try:
			lista.eliminarCancion(i,t)
		except:
			print("No existe lista para eliminar")
	
	elif opcion == 4:
		try:
			if (len(L) == 0):
				print("Agrege una lista que tenga canciones")
			else:
				if rec.estaTocandoCancion():
					print("El reproductor esta reproduciendo la cancion "+rec.actual.titulo)
					mixer.music.unpause()
					continue
				else:
					rec.reproducir()
		except:
			print("Agrege una lista que tenga canciones")
					
	elif opcion == 5:
		try:
			if (len(L) == 0):
				print("Agrege una lista que tenga canciones")
			else:
				rec.pausa()
		except:
			print("Agrege una lista que tenga canciones")	

	elif opcion == 6:
		try:
			if (len(L) == 0):
				print("Agrege una lista que tenga canciones")
			else:
				rec.parar()
		except:
			print("Agrege una lista que tenga canciones")	
		
	elif opcion == 7:
		try:
			if (len(L) == 0):
				print("Agrege una lista que tenga canciones")
			else:
				if rec.estaTocandoCancion():
					rec.parar()
				NEXT = proxima_Cancion(L,rec.actual)
				rec.cargarCancion(NEXT)
				rec.reproducir()
		except:
			print("Agrege una lista que tenga canciones")	
