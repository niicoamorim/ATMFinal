nomecliente = []
cpfcliente = []
contacliente = []
saldocliente = []
inicio = 'S'
pos = int(0)
tentativalogin = int(3)
print('=' * 30)
print('{:^30}'.format('BANCO DO RONEY BOY -  O MELHOR DE MACEIO'))
print('=' * 30)

while inicio == 'S':
    verificacaocadastro = str(input('Você já tem cadastro no Banco?')).upper()
    if verificacaocadastro =='N':
        novocadastro = []
        nome = str(input('Digite seu nome:'))
        cpf = str(input('Digite seu CPF:'))
        conta = str(input('Digite seu número de conta:'))
        saldo =int(0)
        if cpf in cpfcliente:
            print('Impossivel fazer o cadastro:')
            inicio = 'S'
        else:
            nomecliente.append(nome)
            cpfcliente.append(cpf)
            contacliente.append(conta)
            saldocliente.append(saldo)


    if verificacaocadastro == 'S':
        print(f'Digite os dados abaixo para realizar login no sistema do banco. Você ainda tem {tentativalogin} tentativas.')
        validacaocpf = str(input('Digite seu CPF:'))
        validacaoconta = str(input('Digite sua conta'))

        if validacaoconta in contacliente and validacaocpf in cpfcliente:
            print('Bem vindo ao sistema do banco:')
            print('Escolha a operação que deseja realizar no sistema:')
            operacao = int(input(f'1 - Depósito. 2 - Saque. 3 - Saldo. 4 - Transferência. 5 - Sair '))

            if operacao == 1:
                valordeposito = int(input('Digite o valor a ser depositado:'))
                pos = cpfcliente.index(validacaocpf)
                saldocliente[pos] += valordeposito
                print(f'O saldo da conta {contacliente[pos]} agora é de R${saldocliente[pos]}.')

            if operacao == 2:
                valorsaque = str(input('Digite o valor a ser sacado:'))
                pos = contacliente.index(validacaoconta)
                if valorsaque > int(saldocliente[pos]):
                    print('Saldo insuficente.')
                else:
                 saldocliente[pos] -= valorsaque
                 print(f'O novo saldo da conta {contacliente[pos]} é {saldocliente[pos]}.')

            if operacao == 3:
                pos = contacliente.index(validacaoconta)
                print(f'O saldo atual da conta {contacliente[pos]} é {saldocliente[pos]}')

            if operacao == 4:
                contatransferencia = str(input('Digite a conta a ser transferida:'))
                valortransferencia = str(input('Digite o valor a ser transferido:'))
                pos = contacliente.index(validacaoconta)
                pos2 = contacliente.index(contatransferencia)
                if valortransferencia > saldocliente[pos]:
                    print('Vamor superior ao saldo da conta')
                if valortransferencia <= saldocliente[pos]:
                    saldocliente[pos] -= valortransferencia
                    saldocliente[pos2] += valortransferencia
                    print(f'Foi retirado R${valortransferencia} da conta {contacliente[pos]} e foi transferido para a conta {contacliente[pos2]}')

            if operacao ==5:
                print('Muito obrigado por acessa o sistema.')
                break

        if validacaoconta not in contacliente:
            print('Conta não cadastrada.')
            tentativalogin -= 1
        elif validacaocpf not in cpfcliente:
            print('CPF não cadastrado.')
            tentativalogin -= 1

        if tentativalogin < 0:
            print('Você está bloqueado.\n Tente daqui há 30 minutos.')
            break
