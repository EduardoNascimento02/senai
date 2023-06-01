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


valor = lerInt('Digite o valor:')
linha()
print(f'''Antecessor: {valor-1}
Valor: {valor}
Sucessor: {valor+1}''')
linha()