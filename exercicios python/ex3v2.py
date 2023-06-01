from datetime import date
import math
data_atual = date.today()
nome = input('Digite seu nome: ')
dia = int(input('Digite o dia em que você nasceu: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
data = date(ano,mes,dia)
maioridade = 0
idade_dias = data_atual - data
idade = math.floor(idade_dias.days / 365)
if idade_dias.days < 6570:
    maioridade = 'menor de idade'
else:
    maioridade = 'maior de idade'
  
print('='*40)
print(f'''Bom dia, {nome}!
Você tem {idade} anos e é {maioridade}''')
print('='*40)