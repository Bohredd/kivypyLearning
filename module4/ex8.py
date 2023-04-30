def argsIndefinidosDicts(**kwargs):
    resultado = {} # define o resultado como um dicionario
    for dicionario in kwargs.values():
        resultado.update(dicionario)
        print(resultado)

dicionarioTeste = {'a':1, 'b':'diogo'}

argsIndefinidosDicts(dicionarioTest=dicionarioTeste)