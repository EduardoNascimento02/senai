from time import sleep

def linha(tam=35):
    print('-'*tam)


def lerFloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(msg)).replace(',', '.')
            try:
                valor = float(n)
                ok = True
            except ValueError:
                print('\033[0;31mERRO!!! Digite um valor valido\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mERRO!! Digite algo\033[m')
        if ok:
            break
    return valor



def cab(txt):
    linha()
    print(txt.center(35))
    linha()

cab('CALCULADORA')
v1 = lerFloat('Digite o primeiro valor: ')
v2 = lerFloat('Digite o segundo valor: ')
menu = ['ADIÇÃO','SUBTRAÇÃO','DIVISÃO','MULTIPLICAÇÃO']
opc = 0
while True:
    n = 1
    linha()
    for c in menu:
        print(f'[{n}] - {c}')
        n += 1
    opc = lerFloat('Selecione a opção que deseja [999 p/ parar]: ')
    linha()
    if opc == 1:
        print(f'{v1} + {v2} = {v1+v2}')
        sleep(3)
    if opc == 2:
        print(f'{v1} - {v2} = {v1-v2}')
        sleep(3)
    if opc == 3:
        print(f'{v1} / {v2} = {v1/v2}')
        sleep(3)
    if opc == 4:
        print(f'{v1} x {v2} = {v1*v2}')
        sleep(3)
    if opc == 999:
        print('Encerrando programa...')
        sleep(3)
        break