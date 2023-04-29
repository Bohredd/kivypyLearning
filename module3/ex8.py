numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

inicio = int(input())
fim = int(input())

for i in range(inicio,fim+1,1):
    if i == numero1 or i == numero2 or i == numero3:
        pass
    else:
        print(i)