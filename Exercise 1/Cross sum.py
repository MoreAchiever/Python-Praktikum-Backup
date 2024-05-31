def quersumme(n, b):
    summe = 0
    while True:
        i = n%b #212%16=4
        n = n//b #13
        summe+=i
        if n==0: break
    return summe

print(quersumme(212, 10))
#print(21244%16)

#print(212//16)
#// für quotient
#% für rest