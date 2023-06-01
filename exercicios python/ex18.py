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

cab('SISTEMA DE VIAGENS')
dist = lerFloat('Informe apenas o valor da distancia em km de sua viagem: ')
linha()
if dist <= 200:
    preco = dist * 0.50
    print(f'{dist}km - R${preco} | R$0,50 POR KM')
else:
    preco = dist * 0.45
    print(f'{dist}km - R${preco} | R$0,45 POR KM')