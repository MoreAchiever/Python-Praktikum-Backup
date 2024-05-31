
from tokenizer import tokenize
class Subtraction:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        l = "(" + str(self.left) + ")" if isinstance(self.left, Subtraction) else str(self.left)
        r = "(" + str(self.right) + ")" if isinstance(self.right, Subtraction) else str(self.right)
        return l + " - " + r

    def __call__(self):
        l = self.left() if isinstance(self.left, Subtraction) else int(self.left)
        r = self.right() if isinstance(self.right, Subtraction) else int(self.right)
        return l - r



def parseMinus(array):
	expr = None
	pos = 0
	while True:
		if pos < len(array):
			if array[pos]=="-" or array[pos]==")":
				raise Exception("Ausdruck endet nicht mit einem minus oder klammer")
			if isinstance(array[pos], int):
				t = array[pos]
				pos+=1
			if pos < len(array):
				if array[pos]=="(":
					tuple = parseMinus(array[pos+1 : ])
					t = tuple[0]
					pos+= tuple[1]+1
					if array[pos]!=")":
						raise Exception("Ausdruck nicht mit ')' beendet")
					pos+= 1

			if expr is None:
				expr = t
			else:
				expr = Subtraction(expr, t)
		else:
			raise Exception("Ausdruck darf nicht leer sein")
		#Operator---------------------------------------------------
		if pos < len(array):
			if array[pos]=="-":
				pos+=1
				continue
			if array[pos]==")":
				break
			if array[pos]=="(" or isinstance(array[pos], int):
				raise Exception("flascher Ausdruck")
		else:
			break


	return (expr, pos)


def parse(array):
	result = parseMinus(array)
	if result[1] != len(array):
		raise Exception("invalid symbol " + array[result[1]])
	return result[0]


input = "(40 - 5) - (18 - (13 - 10))"
expr = parse(tokenize(input))
print(expr())   # 20
print(expr)     # (40 - 5) - (18 - (13 - 10))
print(parse(tokenize("42")))