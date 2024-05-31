class Bijection:

	def check_duplicate(self, o):
		temp = []
		for i in o.values():
			temp.append(i)
		for i in range(0, len(temp)):
			for s in range(0, len(temp)):
				if i != s:
					if temp[i] == temp[s]:
						raise Exception("duplicate Value")

	def __init__(self, other = None):
			if type(other)==Bijection:
				self.dict1 = other.dict1.copy() #These are corrected
				self.dict2 = other.dict1.copy() # by ChatGPT
			elif type(other)==dict:
				self.check_duplicate(other)
				self.dict1 = other #main Dict
				self.dict2 = {value : key for key, value in other.items()}
			else:
				self.dict1 = {}
				self.dict2 = {}


	def __str__(self): # print(objekt) funktioniert
		temp = str(self.dict1)
		temp = temp.replace(": ", "->")
		temp = temp.replace(" ", "")
		temp = temp.replace("'", "")
		return temp

	def __getitem__(self, key): #Erklärung: ohne die Deklarierung solcher Funktionen würde z.B print(f["a"]) einen Fehler ergeben, dabei ist f das Object und "a"
		if key in self.dict1:
			return self.dict1[key]
		return None # optional

	def __setitem__(self, key, value):
		self.dict1[key]=value
		self.check_duplicate(self.dict1)
		self.dict2 = {value : key for key, value in self.dict1.items()}

	def __delitem__(self, key):
		if key in self.dict1:
			del self.dict1[key]
		return None

	def __len__(self):
		return len(self.dict1)


	def __mul__(self, other):
		temp = {}
		for key in other.dict1.keys():
			if other.dict1[key] in self.dict1:
				temp[key]=self.dict1[other.dict1[key]]
			else: raise KeyError("missing key")
		return Bijection(temp)

	def inverse(self):
		return Bijection(self.dict2)



# create a bijection
f = Bijection()

# add key-value pairs
f["hello"] = "world"
f["foor"] = "bar"
f["a"] = "z"
#f["b"] = "z"       # would raise a "duplicate value" exception

# number of elements
print(len(f))        # 3

# output and conversion to string
print(f)             # {hello->world,foo->bar,a->z}

# invert the bijection
print(f.inverse())   # {world->hello,bar->foo,z->a}
              # {"hello: world, foor: bar, a:z}
# define a second bijection, this time constructed from a dictionary literal
g = Bijection({"world": "peace", "bar": "beer", "z": "omega", "animal": "dog"})
print(g)             # {world->peace,bar->beer,z->omega,animal->dog}

# function composition of the bijections
print(g * f)         # {hello->peace,foo->beer,a->omega}

# remove a key
del f["hello"]
print(f)             # {foo->bar,a->z}