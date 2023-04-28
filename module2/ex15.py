vogais = ["a","e","i","o","u"]

letra = str(input()).lower()

if letra in vogais:
    print("É vogal!")
else:
    print("É consoante!")