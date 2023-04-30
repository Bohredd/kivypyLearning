def estaIntervalo(numero):
    if numero >= 1 or numero <= 100:
        return True
    else:
        return False
    
if estaIntervalo(50):
    print("Está!")
else:
    print("Não está!")