quantiaPares = 0

for numero in range(1,100+1):
    if numero % 2 == 0:
        quantiaPares+=1
    else:
        continue

print(quantiaPares)