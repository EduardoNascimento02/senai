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


valor = lerInt('Digite um valor:')
linha()
print(f'''Metade: {valor/2}
Valor: {valor}
Dobro: {valor*2}
Triplo: {valor*3}''')
linha()