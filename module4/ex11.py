def somaItemLista(*args):
    soma = 0
    for numero in args:
        soma += numero

    print(soma)

lista = [1,2,3,4,5]

somaItemLista(*lista)