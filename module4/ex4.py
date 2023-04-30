def media(num1,num2,num3):
    mediaVal = num1+num2+num3
    mediaVal/=3
    return mediaVal

mediaValor = media(7,6,5)

print(mediaValor)

def listaCrescente(num1,num2,num3):
    maior = num1
    if num2 > maior:
        print(num1)
        maior = num2
    else:
        print(num2)

    if num3 > maior:
        maior = num3
    else:
        print(num3)

    print(maior)

listaCrescente(7,3,5)