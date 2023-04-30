def obrigatorioFacultativo(numero1, numero2 = ''):
    if numero2:
        print(numero1,numero2)
    else:
        print(numero1)

obrigatorioFacultativo(3,7)