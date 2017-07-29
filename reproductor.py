from pygame import mixer
from cancion import*

class Reproductor(object) :
	def __init__(self, c: Cancion) :
		self.actual = c
		mixer.init()
	
	def cargarCancion(self, c: Cancion) :
		self.actual = c
	
	def reproducir(self) :
		mixer.music.load(self.actual.ubicacion)
		mixer.music.play()
		
	def parar(self) :
		mixer.music.stop()
		
	def pausa(self) :
		mixer.music.pause()	

	def estaTocandoCancion(self) :
		return mixer.music.get_busy()