from colorama import init, Fore
init(autoreset=True)
while True:
    valor = int(input('Digite um valor: '))
    if valor < 0:
        break
    if valor & 2 == 0:
        print(f'{valor} é '+ Fore.BLUE + 'par')
    else:
        print(f'{valor} é ' + Fore.RED + 'ímpar')