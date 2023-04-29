quantiaPrimos = 0

for numero in range(1,100+1):
    if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
        quantiaPrimos+=1
    else:
        continue

print(quantiaPrimos)