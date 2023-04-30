def inverteLista(*args):
    invertida = args[::-1]
    invertida.strip('')
    print(invertida)

lista = ['d','i','o','g','o']

inverteLista(*lista)