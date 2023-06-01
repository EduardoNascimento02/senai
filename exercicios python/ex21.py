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

cab('SISTEMA OLIMPICO')
nota = lerInt('Informe a porcentagem da nota: ')
linha()
if nota <= 50:
    print('\033[0;30;1mCERTIFICADO DE PARTICIAPÇÃO\033[m','\U0001f3c5')
elif nota > 50 and nota <= 60:
    print('\033[0;30;1mCERTFICADO DE MENÇÃO HONROSA\033[m','\U0001f3c5')
elif nota > 60 and nota <=70:
    print('\033[0;36;1mMEDALHA DE BRONZE\033[m','\U0001f949')
elif nota > 70 and nota <=90:
    print('\033[0;37;1mMEDALHA DE PRATA\033[m','\U0001f948')
elif nota > 90:
     print('\033[0;33;1mMEDALHA DE OURO \033[m','\U0001f947')
linha()