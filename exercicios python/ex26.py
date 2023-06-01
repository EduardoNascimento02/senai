from colorama import Fore, init
init(autoreset=True)

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

def menu(lst):
    cab('MENU PRINCIPAL')
    c = 1
    for valor in lst:
        print(f'{c} - {valor}')
        c += 1
    linha()
    opc = lerInt('Sua opção: ')
    return opc

cab('TABUADA')
n = lerInt('Digite o valor que deseja ver a tabuada: ')
for c in range(1,11):
    print(f'{n} x {c} =', Fore.BLUE + f'{n*c}')

