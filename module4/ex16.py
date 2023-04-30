def contaLetras(string):
    maiusculas = 0
    minusculas = 0
    for letra in string:
        if letra.isupper():
            maiusculas += 1
        else:
            minusculas += 1
    print(f"Maisculas: {maiusculas} Minusculas: {minusculas}")

contaLetras("Zika Do BagulhO")