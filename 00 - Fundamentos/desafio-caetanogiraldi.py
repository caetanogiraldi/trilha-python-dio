menu = '''
Escolha a opção desejada

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match opcao:
        case '0':
            break

        case '1':
            valor = float(input('Informe o valor do depósito: '))

            if valor > 0:
                saldo += valor
                extrato += f'Depósito: R$ {valor:.2f}\n'

            else:
                print(f'Operação falhou! O valor informado é inválido - ({valor})')

        case '2':
            if numero_saques >= LIMITE_SAQUES:
                print(f'Operação falhou! Número máximo de saques excedido - ({LIMITE_SAQUES})')
                break

            valor = float(input('Informe o valor do saque: '))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite

            if excedeu_saldo:
                print(f'Operação falhou! Você não tem saldo suficiente -  (R$ {saldo})')

            elif excedeu_limite:
                print(f'Operação falhou! O valor do saque excede o limite - (R$ {limite})')                

            elif valor > 0:
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                numero_saques += 1
                print(f'Quantidade de saques(s) restante(s): {LIMITE_SAQUES - numero_saques}')

            else:
                print(f'Operação falhou! O valor informado é inválido - R$ ({valor})')

        case '3':
            print(" EXTRATO ".center(20, "="))
            print(f'Não foram realizadas movimentações' if not extrato else extrato)
            print(f'\nSaldo: R$ {saldo:.2f}')
            print("".center(20, "="))

        case _:
            print(f'Operação inválida, por favor selecione novamente a operação desejada - ({opcao})')
