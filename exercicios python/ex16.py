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

cab('SISTEMA RODOVIARIO')
vel = lerFloat('Digite a velocidade do carro: ')
linha()
if vel > 80:
    print('Acima da velocidade de 80km/h permitido, \033[0;31mMULTADO!!\033[m')
else:
    print('Velocidade abaixo do limite de velocidade!')
linha()