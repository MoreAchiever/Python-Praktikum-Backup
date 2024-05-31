def isPermutation(list1, list2):
	copy2 = list2.copy()
	if len(list1) != len(list2):
		return False
	i=0
	while len(copy2)!=0:
		if i>=len(list1): return False
		if list1[i] in copy2:
			copy2.remove(list1[i])
		i += 1
	return True

#alternative Lösung
#def isPermutation(list1, list2):
#	copy2 = list2.copy()
#	if len(list1) != len(list2):
#		return False
#	for i in list1:
#		try:
#			copy2.remove(i)
#		except: pass
#	if len(copy2)==0: return True
#	return False

print(isPermutation([1, "test", 3.14159, [], True, []], [1, "test", 3.14159, [], True, "test"]))
print(isPermutation([1, "test", 3.14159, [], True], ["test", True, [], 1, 3.14159]))
print(isPermutation([1, "test", 3.14159, [], True, []], [1, "test", 3.14159, [], True, "test"]))