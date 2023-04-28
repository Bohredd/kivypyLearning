num1 = int(input())
num2 = int(input())
num3 = int(input())

print("-"*10)

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