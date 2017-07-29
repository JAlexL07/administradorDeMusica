from ABC import*

class LR(object) :
	def __init__(self) :
		self.contenido = ArbBCanciones()
	
	def agregarLista(self, na: str) :
		f = open(na+".txt",'r')
		archivo = f.read()
		linea = archivo.splitlines()
		array = [None for i in range(len(linea))]
		for i in range(len(linea)) :
			array[i] = linea[i].split(';')
			array[i] = Cancion(array[i][1],array[i][0],array[i][2])
			self.contenido.insertar(array[i])
		
		f.close()
		
	def eliminarCancion(self, i: str, t: str) :
		self.contenido.eliminar(i, t)
		
	def obtenerLR(self) :
		return self.contenido._raiz.enOrden2()
	
	def mostrarLR(self) :
		self.contenido.printinOrden()