def pontos():
    print('=' * 30)


cadastro= []
novodeposito = str('S')
novaoperacao =  str('S')
inicio = 'S'
tentativalogin = int(3)
conta = int(0)
pontos()
print('    NICOLAS BANK    ')
pontos()

while inicio == 'S' and tentativalogin > 0:

    verificacaocadastro = str(input('Você já tem cadastro no Banco?')).upper()
    while verificacaocadastro =='N':
        nome = str(input('Digite seu nome:'))
        cpf = str(input('Digite seu CPF:'))
        if cpf in cadastro:
            print('CPF já cadastrado.')
            inicio = 'S'
        else:
            conta += + 1
            saldo = int(0)
            cadastro.append(nome)
            cadastro.append(cpf)
            cadastro.append(conta)
            cadastro.append(saldo)
            print('Sua conta é:',conta)
            inicio = 'S'
            verificacaocadastro = 'S'
        novocadastro = str(input('Deseja realizar um novo cadastro?')).upper()
        if novocadastro == 'S':
           verificacaocadastro = 'N'
           inicio = 'S'

    while verificacaocadastro == 'S' and tentativalogin > 0:

        print(f'Digite os dados abaixo para realizar login no sistema do banco. Você ainda tem {tentativalogin} tentativas.')
        validacaocpf = str(input('Digite seu CPF:'))
        validacaoconta = int(input('Digite sua conta:'))

        while validacaoconta in cadastro and validacaocpf in cadastro and novaoperacao == 'S':
            tentativalogin = 3
            print('Bem vindo ao sistema do banco:')
            print('Escolha a operação que deseja realizar no sistema:')
            operacao = int(input(f'1 - Depósito. \n2 - Saque. \n3 - Saldo. \n4 - Transferência. \n5 - Voltar Início '))

            while operacao == 1:
                valordeposito = int(input('Digite o valor a ser depositado:'))
                posicaocontadepositada = cadastro.index(validacaocpf)
                saldocontadepositada = posicaocontadepositada + 2
                cadastro[saldocontadepositada] += valordeposito #print(f'O saldo da conta {cadastro[pos]} agora é de R${cadastro[pos2]}.')
                print(cadastro)
                novodeposito = str(input( 'Deseja fazer um novo depósito? S/N ')).upper()
                if novodeposito == 'N':
                    novaoperacao = 'S'
                    operacao = '0'

            if operacao == 2:
                valorsaque = int(input('Digite o valor a ser sacado:'))
                posicaocontadesaque = int( cadastro.index( validacaocpf ) )
                saldocontadesaque = posicaocontadesaque + 2
                print( cadastro )
                if cadastro[saldocontadesaque] < valorsaque:
                    print('Saldo insuficente.')
                else:
                 cadastro[saldocontadesaque] -= int(valorsaque)
                 print('O novo saldo da conta é {}.'.format(cadastro[saldocontadesaque]))

            if operacao == 3:
                posicaoconta = cadastro.index(validacaoconta)
                saldo = posicaoconta + 1
                print('O saldo atual da conta é ',cadastro[saldo])

            if operacao == 4:
                contatransferencia = str(input('Digite a conta a ser transferida:'))
                valortransferencia = int(input('Digite o valor a ser transferido:'))
                posicaocontadepositante = cadastro.index(validacaoconta)
                saldocontadepositante = posicaocontadepositante + 1
                posicaocontadepositada = cadastro.index(contatransferencia)
                saldocontadepositada = posicaocontadepositada + 2
                if valortransferencia > cadastro[saldocontadepositante]:
                    print('Vamor superior ao saldo da conta')
                if valortransferencia <= cadastro[saldocontadepositante]:
                    cadastro[saldocontadepositante] -= valortransferencia
                    cadastro[saldocontadepositada] += valortransferencia
                    print(f'Foi retirado R${valortransferencia} da conta {cadastro[posicaocontadepositante]} e foi transferido para a conta {cadastro[posicaocontadepositada]}')

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
