nomecliente = []
cpfcliente = []
contacliente= []
saldocliente = []
inicio = 'S'
print('=' * 30)
print('{:^30}'.format('NICOLAS BANK'))
print('=' * 30)

while inicio == 'S':
    verificacaocadastro = str(input('Você já tem cadastro no Banco?')).upper()
    if verificacaocadastro =='N':
        novocadastro = []
        nome = str(input('Digite seu nome:'))
        cpf = str(input('Digite seu CPF:'))
        conta = str(input('Digite seu número de conta:'))
        saldo =str(0)
        if cpf in cpfcliente:
            print('Impossivel fazer o cadastro:')
            inicio = 'S'
        else:
         nomecliente.append(nome)
         cpfcliente.append(cpf)
         contacliente.append(conta)
         saldocliente.append(saldo)
        print(nomecliente,cpfcliente,contacliente,saldocliente)


    if verificacaocadastro == 'S':
        print('Digite os dados abaixo para realizar login no sistema do banco:')
        validacaocpf = str(input('Digite seu CPF:'))
        validacaoconta = str(input('Digite sua conta'))

        if validacaoconta in contacliente and validacaocpf in cpfcliente:
            print('Bem vindo ao sistema do banco:')
            print('Escolha a operação que deseja realizar no sistema:')
            operacao = int(input(f'1 - Depósito. 2 - Saque. 3 - Saldo. 4 - Transferência. 5 - Sair '))
            if operacao == 1:
              valordeposito = str(input('Digite o valor a ser depositado:'))
              pos = validacaocpf.index(cpfcliente)
              saldocliente[pos] += valordeposito
              print(f'O saldo da conta {contacliente[pos]} agora é de R${saldocliente[pos]}.')



        if validacaoconta not in contacliente:
            print('Conta não cadastrada.')
        elif validacaocpf not in cpfcliente:
            print('CPF não cadastrado.')