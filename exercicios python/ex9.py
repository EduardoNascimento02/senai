def linha(tam=35):
    print('-'*tam)


def cab(txt):
    linha()
    print(txt.center(35))
    linha()


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



cab('SISTEMA SALARIAL')
sal = lerFloat('informe seu salario para o reajuste: ')
reajuste = sal*0.12
cab('SISTEMA SALARIAL')
print(f'''SALARIO REAJUSTADO PARA MENOS: {sal-reajuste}
SALARIO ATUAL: {sal}
SALARIO REAJUSTADO PARA MAIS: {sal+reajuste}''')