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


cab('QUANDO VOCÊ FARÁ 100 ANOS?')
idade = lerInt('Informe sua idade: ')
ano = 2023 + (100-idade)
linha()
print(f'Você tendo agora {idade} anos, fará 100 anos no ano de {ano}')
linha()
