def pontos():
    print('=' * 30)


cadastro= []
novodeposito = str('S')
novaoperacao =  str('S')
inicio = 'S'
pos = int(0)
pos2 = int(0)
pos3 = int(0)
pos4 = int(0)
tentativalogin = int(3)
pontos()
print('    NICOLAS BANK    ')
pontos()

while inicio == 'S' and tentativalogin > 0:

    verificacaocadastro = str(input('Você já tem cadastro no Banco?')).upper()
    while verificacaocadastro =='N':
        nome = str(input('Digite seu nome:'))
        cpf = str(input('Digite seu CPF:'))
        conta = str(input('Digite seu número de conta:'))
        saldo =int(0)
        if cpf in cadastro or conta in cadastro:
            print('Impossivel fazer o cadastro.')
            inicio = 'S'
        else:
            cadastro.append(nome)
            cadastro.append(cpf)
            cadastro.append(conta)
            cadastro.append(saldo)
            inicio = 'S'
            verificacaocadastro = 'S'
        novocadastro = str(input('Deseja realizar um novo cadastro?')).upper()
        if novocadastro == 'S':
           verificacaocadastro = 'N'
           inicio = 'S'

    while verificacaocadastro == 'S' and tentativalogin > 0:

        print(f'Digite os dados abaixo para realizar login no sistema do banco. Você ainda tem {tentativalogin} tentativas.')
        validacaocpf = str(input('Digite seu CPF:'))
        validacaoconta = str(input('Digite sua conta'))

        while validacaoconta in cadastro and validacaocpf in cadastro and novaoperacao == 'S':
            tentativalogin = 3
            print('Bem vindo ao sistema do banco:')
            print('Escolha a operação que deseja realizar no sistema:')
            operacao = int(input(f'1 - Depósito. \n2 - Saque. \n3 - Saldo. \n4 - Transferência. \n5 - Sair '))

            while operacao == 1:
                valordeposito = int(input('Digite o valor a ser depositado:'))
                pos = int(cadastro.index(validacaocpf))
                pos2 = pos+3
                pos2 += valordeposito #print(f'O saldo da conta {cadastro[pos]} agora é de R${cadastro[pos2]}.')
                novodeposito = str(input( 'Deseja fazer um novo depósito? S/N ')).upper()
                if novodeposito == 'N':
                    novaoperacao = 'S'
                    operacao = ' '

            if operacao == 2:
                valorsaque = int(input('Digite o valor a ser sacado:'))
                pos = cadastro.index(validacaoconta)
                pos2 = pos+3
                if valorsaque > (cadastro[pos2]):
                    print('Saldo insuficente.')
                else:
                 cadastro[pos2] -= valorsaque
                 print('O novo saldo da conta {} é {}.'.format(cadastro[pos],cadastro[pos2]))

            if operacao == 3:
                pos = cadastro.index(validacaoconta)
                pos2 = pos+3
                print(f'O saldo atual da conta {cadastro[pos]} é {cadastro[pos2]}')

            if operacao == 4:
                contatransferencia = str(input('Digite a conta a ser transferida:'))
                valortransferencia = int(input('Digite o valor a ser transferido:'))
                pos = cadastro.index(validacaoconta)
                pos2 = pos + 3
                pos3 = cadastro.index(contatransferencia)
                pos4 = pos3 + 3
                if valortransferencia > cadastro[pos2]:
                    print('Vamor superior ao saldo da conta')
                if valortransferencia <= cadastro[pos2]:
                    cadastro[pos2] -= valortransferencia
                    cadastro[pos4] += valortransferencia
                    print(f'Foi retirado R${valortransferencia} da conta {cadastro[pos]} e foi transferido para a conta {cadastro[pos3]}')

            if operacao == 5:
                print('AQUI')
                novaoperacao = 'S'
                operacao = ' '
                verificacaocadastro = 'N'
                break

        if validacaoconta not in cadastro:
          print('Conta não cadastrada.')
          tentativalogin -= 1

        elif validacaocpf not in cadastro:
            print('CPF não cadastrado.')
if tentativalogin == 0:
 print('Você está bloqueado.\n Tente daqui há 30 minutos.')