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

idade = lerInt('Informe sua idade: ')
linha()
if idade >= 18:
    print('Você é maior de idade!!')
else:
    print('Você é menor de idade!')
linha()