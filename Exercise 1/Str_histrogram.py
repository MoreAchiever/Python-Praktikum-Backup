# Zusammenarbeit mit folgenden Teilnehmern:
def histogram(strings):
    dict = {}
    for i in strings:
        if i not in dict.keys():
            dict[i]=strings.count(i)
    return dict

print(histogram(["foo", "bar", "check", "foo", "check", "door"]))


