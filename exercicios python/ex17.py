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

cab('SISTEMA SALARIAL')
salario = lerFloat('Informe seu salario: ')
linha()
if salario <= 8250.00:
    aumento = salario * 0.15
    print(f'Seu salario com o aumento de 15% fica {salario+aumento}')
else:
    aumento = salario * 0.1
    print(f'Seu salario com o aumento de 10% fica {salario+aumento}')
linha()