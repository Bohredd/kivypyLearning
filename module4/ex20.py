def ehPalindromo(string):
    stringInvertida = string[::-1]
    qualRotacao = 0
    for letra in string:
        if letra != stringInvertida[qualRotacao]:
            return False
        qualRotacao += 1

    return True

if ehPalindromo('arara'):
    print("É palíndromo!")
else:
    print("Não é palíndromo!")