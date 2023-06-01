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

cab('MAIOR E MENOR VALOR')
valores = list()
maior = menor = 0
for c in range(0,3):
    valores.append(lerFloat(f'Digite o {c} valor: '))
    if c == 0:
        menor = maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
linha()
print(f'''O maior valor é {maior}
O menor valor é {menor}''')
linha()