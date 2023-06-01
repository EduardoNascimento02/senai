from math import factorial

def linha(tam=35):
    print('-'*tam)


def lerInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!!! Digite um NÚMERO!!\033[m')
        if ok:
            break
    return valor


def cab(txt):
    linha()
    print(txt.center(35))
    linha()

cab('FATORIAL')
valor = lerInt('Informe um valor: ')
fat = []
for c in range(1,valor):
    fat.append(c)
fat.reverse()
print(f'{valor}', end='')
for c in fat:
    print(f' x {c}', end='')
print(f' = {factorial(valor)}')
