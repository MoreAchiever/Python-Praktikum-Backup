
# ctrl + / : toggle comment
def tokenize(string):
    arr = []
    temp = ""
    for element in string:
        if (element<="9" and element>="0") or element=="(" or element==")" or element==" " or element=="-":
            pass
        else:
            raise Exception("ungueltiges Zeichen")
        try:
            temp+=str(int(element))

        except:
            if temp!="":
                arr.append(int(temp))
                temp = ""
            if element!=" ":
                arr.append(element)
    if temp!="": arr.append(int(temp))
    return arr

print(tokenize("(80-10) - (17-3)"))
#print(tokenize("ABC"))


