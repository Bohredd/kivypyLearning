def fatorial(numero):
    fatorialResult = 1

    for valor in range(numero,1,-1):
        fatorialResult *= valor

    return fatorialResult

valorFatorial = fatorial(4)
print(valorFatorial)