def retiraRepetidos(*args):
    listaAtualizada = []
    for item in args:
        if str(item) in listaAtualizada:
            continue
        else:
            listaAtualizada.append(str(item))
    
    print(listaAtualizada)

numeros = [1,2,3,3,4,5,5]

retiraRepetidos(*numeros)