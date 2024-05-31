# Zusammenarbeit mit folgenden Teilnehmern:
def statistics(data):
    summe=0
    for i in data:
        summe+=i
    mean = summe/len(data)
    var = 0
    for i in data:
        var += (i-mean)**2/len(data)
    data.sort()
    #median
    if len(data)%2!=0:
        median=data[int(len(data)/2)] #[1,2,3,4,5]
    else: median = (data[(int(len(data)/2)-1)] + data[int(len(data)/2)])/2
    dict = {"mean":mean, "variance":var, "median":median, "minimum":data[0], "maximum":data[int(len(data)-1)]}
    return dict

print(statistics([2, 4, 2.5, -1, 3]))