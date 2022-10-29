frase = input('Linha de texto para encriptar: ')
num = int(input('Valor de deslocamento: '))
while num < 1 or num > 26:
    num = int(input('Número fora de alcance. Valor de deslocamento: '))

for i in frase: 
    if not i.isalpha():
        print(i, end='')
        continue
    y = i.lower()

    x = ord(y) + num
    if x > 122: x -= 26
    x = chr(int(x))
    if i.isupper(): x = x.upper()
    print(x, end='')