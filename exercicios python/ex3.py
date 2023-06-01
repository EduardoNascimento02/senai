nome = input('Digite seu nome: ')
dia = int(input('Digite o dia em que você nasceu: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
idade = 2023 - ano
maioridade = 0
if 2023 - ano >= 18:
    maioridade = 'maior de idade'
else:
    maioridade = 'menor de idade'
print('='*40)
print(f'''Bom dia, {nome}!
Você tem {idade} anos e é {maioridade}''')
print('='*40)