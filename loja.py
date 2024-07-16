listagem = ('Lápis', 1.74,
            'Canetas', 22.49,
            'Borracha', 1.99,
            'Caderno', 19.99,
            'Estojo', 24.99,
            'Transferidor', 4.19,
            'Compasso', 9.99,
            'Mochila', 149.99,
            'Livro', 34.94)

Lapis = 1.74
Canetas = 22.49
Borracha = 1.99
Caderno = 19.99
Estojo = 24.99
Transferidor = 4.19
Compasso = 9.99
Mochila = 149.99
Livro = 34.94

contagem = 0
valorT = 0
while True:
    print('-' * 40)
    compras = str(input('Olá, deseja comprar algo? [S/N] ')[0].upper().strip())
    if compras == 'N':
        print('-' * 40)
        print(f'{"Tudo bem, volte sempre":^40}')
        print('-' * 40)
        break
    elif compras != 'N' and compras != 'S':
        print('Alternativa invalida, tente novamente...')
    else:
        print('-' * 40)
        print('Bem-vindo(a) ao meu mercado!')
        print('-' * 40)
        contagem = float(input('Informe quanto de dinheiro você tem: R$ '))
        print('-' * 40)
        print(f'{"Certo, veja nossos produtos.":^40}')
        print('-' * 40)
        print(f'{"Listagem de preços":^40}')
        for pos in range(0, len(listagem)):
            if pos % 2 == 0:
                print(f'{listagem[pos]:.<30}', end='')
            else:
                print(f'R${listagem[pos]:>3.2f}')
        print('-=-' * 20)
        while True:
            comprass = str(input('Diga o que deseja comprar: ')).upper().strip()
            if comprass == 'LAPIS':
                comprass = Lapis
                valorT += comprass
            elif comprass == 'CANETAS':
                comprass = Canetas
                valorT += comprass
            elif comprass == 'BORRACHA':
                comprass = Borracha
                valorT += comprass
            elif comprass == 'CADERNO':
                comprass = Caderno
                valorT += comprass
            elif comprass == 'ESTOJO':
                comprass = Estojo
                valorT += comprass
            elif comprass == 'TRANSFERIDOR':
                comprass = Transferidor
                valorT += comprass
            elif comprass == 'COMPASSO':
                comprass = Compasso
                valorT += comprass
            elif comprass == 'MOCHILA':
                comprass = Mochila
                valorT += comprass
            elif comprass == 'LIVRO':
                comprass = Livro
                valorT += comprass
            else:
                print('Não temos isto, diga algo da lista.')
            continuar = input('continuar compras? [S/N] ')[0].upper().strip()
            if continuar == 'N':
                print(f'O total foi de R${valorT:>3.2f} nas suas compras')
                if contagem < valorT:
                    print('-' * 40)
                    print('Você não tem dinheiro suficiente.')
                elif contagem > valorT:
                    print('-' * 40)
                    print(f'O seu troco é de R${(contagem - valorT):>3.2f}')
                    break
    print('-' * 40)
    print(f'{"Volte sempre":^40}')
    print('-' * 40)
    break
