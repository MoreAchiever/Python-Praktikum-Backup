# Zusammenarbeit mit folgenden Teilnehmern:
def loop(n):
    arr = [[1]]
    for i in range(1,n+1):
        temp = [1]
        for t in range(1,i+1):
            temp.append(None)
        temp[len(temp)-1]=1
        arr.append(temp)

    for i in range(0,len(arr)):
        for t in range(0,len(arr[i])):
            if arr[i][t] is None:
                arr[i][t] = arr[i-1][t]+arr[i-1][t-1]
    return arr

#i love this kind of exercises <3

print(loop(5))