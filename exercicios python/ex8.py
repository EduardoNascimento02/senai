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

cab('CONVERSOR')
valor = lerFloat('Digite apenas o valor em metros: ')
cm = valor*100
mm = cm*10
cab('VALORES')
print(f'''Metro = {valor}m
Centimetros = {cm:.2f}cm
Milimetros = {mm:.2f}mm''')