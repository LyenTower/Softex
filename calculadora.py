while True:
    num_1= float(input('Escolha o primeiro número'))
    num_2= float(input('Escolha o segundo número'))
    operacao= input('Escolha a operação')

    if operacao == '+':
        resultado = num_1 + num_2
    elif operacao == '-':
        resultado = num_1 - num_2
    elif operacao == '*':
        resultado = num_1 * num_2
    elif operacao == '/':
        resultado = num_1 / num_2
    elif operacao !='+' or '-' or '*' or '/':
        resultado = 0


    print('A sua conta tem como resultado:{}'.format(resultado))