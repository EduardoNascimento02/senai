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


cab('TABUDA')
n = lerInt('Digite o valor da tabuada que deseja ver: ')
linha()
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
linha()
