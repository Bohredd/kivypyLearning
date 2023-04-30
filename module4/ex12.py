def somaItemLista(*args):
    multiplicacao = 1
    for numero in args:
        multiplicacao *= numero

    print(multiplicacao)

lista = [1,2,3,4,5]

somaItemLista(*lista)