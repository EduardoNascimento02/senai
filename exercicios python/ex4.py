import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
linha = lambda x:'='*x
n1 = int(input('Digite valor 1: '))
n2 = int(input('Digite valor 2: '))
n1,n2 = n2,n1
print(linha(30))
print('Valor 1 :', Fore.BLUE + f'{n1}', 'Valor 2 :', Fore.BLUE + f'{n2}')
print(linha(30))