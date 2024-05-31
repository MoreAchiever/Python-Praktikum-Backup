
arr = []
temp = ""


def tokenize(string):
    if string=="": return []
    def subtoken(string, temp=""):
        if len(string)>0:
            if (string[0] <= "9" and string[0] >= "0"):
                    temp+=string[0]
                    subtoken(string[1:len(string)], temp)
            else:
                arr.append(int(temp))
                temp = ""
                tokenize(string[0:len(string)])
        else:
            arr.append(int(temp))
            temp = ""
            return arr
    i = 0
    #arr = tokenize(string[0:len(string)])
    if (string[i] <= "9" and string[i] >= "0") or string[i] == "(" or string[i] == ")" or string[i] == " " or string[i] == "-":
        if (string[i] <= "9" and string[i] >= "0"):
            subtoken(string[i:len(string)], "")
           # return
        else:
            if string[i]!= " ":
                arr.append(string[i])
            tokenize(string[i+1:len(string)])
    else:
        raise Exception("ungueltiges Zeichen")
    return arr




print(tokenize("(80-10) - (17-3)-()"))
print(tokenize(""))
