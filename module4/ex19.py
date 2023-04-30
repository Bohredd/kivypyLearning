def verificaPares(*args):
    for numero in args:
        if numero % 2 == 0:
            print(numero)

lista = [1,2,4,7,9,11,14]

verificaPares(*lista)