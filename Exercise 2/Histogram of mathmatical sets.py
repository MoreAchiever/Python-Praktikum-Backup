def histogram(lists):
	Dict = {}
	for i in range(0,len(lists)):
		lists[i].sort()
		temp = tuple(list(dict.fromkeys(lists[i])))
		if temp not in Dict.keys():
			Dict[(temp)]=1
		else:
			Dict[(temp)]+=1
	return Dict

print(histogram([["a","b","a"],["b"],["a","b"]]))
