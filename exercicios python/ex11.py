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



cab('CONVERSOR DE TEMPERATURA')
tempc = lerFloat('Digite a temperatura em celsius: ')
tempf = (9*tempc+160)/5
cab('TEMPERATURAS')
print(f'''TEMPERATURA EM C° = {tempc}C°
TEMPERATURA EM F° = {tempf}F°''')
