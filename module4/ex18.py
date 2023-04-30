def ehPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def verificaPrimosNaLista(*args):
    numerosPrimos = []
    for numero in args:
        if ehPrimo(numero):
            numerosPrimos.append(numero)

    print(numerosPrimos)

numerosVerificar = [1,3,7,8,9,11,14]

verificaPrimosNaLista(*numerosVerificar)