class Statistics:
    def __init__(self, arr):
        self.array = arr

    def mean(self):
        summe = 0
        for i in self.array:
            summe+=i
        return summe/len(self.array)

    def variance(self):
        var = 0
        for i in self.array:
            var += ((i-self.mean())**2)/len(self.array)
        return var

    def median(self):
        array = self.array.copy()
        array.sort()
        if len(array)%2!=0:
            median=array[int(len(array)/2)]
        else: median = (array[(int(len(array)/2)-1)] + array[int(len(array)/2)])/2
        return median

    def minimum(self):
        array = self.array.copy()
        array.sort()
        return array[0]

    def maximum(self):
        array = self.array.copy()
        array.sort()
        return array[len(array)-1]


stat = Statistics([2, 4, 2.5, -1 , 3])
print(stat.mean())       # 2.1
print(stat.variance())   # 2.84
print(stat.median())     # 2.5
print(stat.minimum())    # -1
print(stat.maximum())    # 4