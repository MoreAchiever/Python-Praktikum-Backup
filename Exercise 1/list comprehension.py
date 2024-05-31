# Zusammenarbeit mit folgenden Teilnehmern:
def comprehend(a):
	return [element.upper() for element in a if element[0]!="z" and element[0]!="Z"]


print(comprehend(["Hallo", "Welt", "Zeitung", "lesen"]))