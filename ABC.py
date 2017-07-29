from cancion import*

class NodoABC(object) :
	def __init__(self, valor: Cancion) :
		self.clave1 = valor.interprete
		self.clave2 = valor.titulo
		self.valor = valor
		self.izq = None
		self.der = None
		
	def enOrden(self):
		a = []
		if self is not None:
			if self.izq is not None:
				a+=self.izq.enOrden()
			a.append(self.valor.aString())
			if self.der is not None:
				a+=self.der.enOrden()
		return a
	
	def enOrden2(self):
		a = []
		if self is not None:
			if self.izq is not None:
				a+=self.izq.enOrden2()
			a.append(self.valor)
			if self.der is not None:
				a+=self.der.enOrden2()
		return a

class ArbBCanciones(object) :
	def __init__(self) :
		self._raiz = None
		self._tam = 0
		
	def __len__(self) :
		return self._tam
		
	def busca(self, subArb, i, t) :
		if subArb is None:
			return None
		elif i < subArb.clave1 :
			return self.busca(subArb.izq, i, t)
		elif i >  subArb.clave1 :
			return self.busca(subArb.der, i, t)
		elif i == subArb.clave1 :
			if t < subArb.clave2 :
				return self.busca(subArb.izq, i, t)
			elif t > subArb.clave2 :
				return self.busca(subArb.der, i, t)
		else :
			return subArb
	
	def contiene(self, i, t) :
		return self.busca(self._raiz, i, t) is not None
	
	def inserta(self, subArb, valor) :
		if subArb is None :
			subArb = NodoABC(valor)
		elif valor.interprete < subArb.clave1 :
			subArb.izq = self.inserta(subArb.izq, valor)
		elif valor.interprete > subArb.clave1 :
			subArb.der = self.inserta(subArb.der, valor)
		elif valor.interprete == subArb.clave1 :
			if valor.titulo < subArb.clave2 :
				subArb.izq = self.inserta(subArb.izq, valor)
			elif valor.titulo > subArb.clave2 :
				subArb.der = self.inserta(subArb.der, valor)
		else :
			sys.exit("Error, se esta insertando una cancion que ya existe.")
		return subArb
	
	def insertar(self, valor) :
		self._raiz = self.inserta(self._raiz, valor)
		self._tam += 1
	"""
	def inOrden(self, subArb):
		if subArb is not None :
			self.inOrden(subArb.izq)
			print("[{0}]".format(subArb.valor.aString()))
			self.inOrden(subArb.der)
	"""	
	def printinOrden(self):
		print(self._raiz.enOrden())
		
	def minimo(self, subArb) :
		if subArb is None :
			return None
		elif subArb.izq is None :
			return subArb
		else :
			return self.minimo(subArb.izq)
		
	def elimina(self, subArb, i, t):
		if subArb is None :
			return subArb
		elif subArb.clave1 > i :
			subArb.izq = self.elimina(subArb.izq, i, t)
			return subArb
		elif subArb.clave1 < i :
			subArb.der = self.elimina(subArb.der, i, t)
			return subArb
		elif subArb.clave1 == i :
			if subArb.clave2 > t :
				subArb.izq = self.elimina(subArb.izq, i, t)
				return subArb
			elif subArb.clave2 < t :
				subArb.der = self.elimina(subArb.der, i, t)
				return subArb
			else :
				if subArb.izq is None and subArb.der is None :
					return None
				elif subArb.izq is None or subArb.der is None :
					if subArb.izq is not None :
						return subArb.izq
					else :
						return subArb.der
				else:
					temp = self.minimo(subArb.der)
					subArb.clave1,subArb.clave2,subArb.valor = temp.clave1,temp.clave2,temp.valor
					subArb.der = self.elimina(subArb.der,temp.clave1,temp.clave2)
					return subArb

	def eliminar(self, i, t):
		self._raiz = self.elimina(self._raiz, i, t)
		self._tam -= -1