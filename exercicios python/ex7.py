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


cab('SISTEMA DE NOTAS')
nome = input('Digite o nome do aluno: ')
nota1 = lerFloat('Digite a primeira nota: ')
nota2 = lerFloat('Digite a segunda nota: ')
nota3 = lerFloat('Digite a terceira nota: ')
media = (nota1+nota2+nota3)/3
passou = ''
if media > 7:
    passou = 'acima da'
elif media == 7:
    passou = 'na'
else:
    passou = 'abaixo da'
cab(f'NOTAS DE {nome.upper()}')
print(f'''Nota 1 = {nota1}
Nota 2 = {nota2}
Nota 3 = {nota3}
Media = {media:.2f} 
O aluno {nome} está {passou} media''')
