# EXERCÍCIO PRÁTICO 1

# Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

#  1. A calculadora deve solicitar ao usuário que insira dois números e uma operação.

#  2. As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

#  3. O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

#  4. Trate os seguintes erros:

#     - Entrada inválida (não numérica) para os números

#     - Divisão por zero

#     - Operação inválida

#  5. Use try/except para capturar e tratar os erros apropriadamente.

#  6. Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

#  7. Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

def numeros():
    while True:
        try:
            num1 = float(input('Insira o primeiro número: '))
            break
        except ValueError:
            print('Entrada inválida, por favor digite um número válido!')

    while True:
        try:
            num2 = float(input('Insira o segundo número: '))
            break
        except ValueError:
            print('Entrada inválida, por favor digite um número válido!')

    return num1, num2

def operadores(num1, num2):
    while True:
        print('''Qual operação deseja realizar?
        1. + (adição)
        2. - (subtração)
        3. * (multiplicação)
        4. / (divisão)
        0. Sair da calculadora''')

        try:
            operador = int(input('Escolha uma opção: '))
        except ValueError:
            print('Entrada inválida, por favor insira um número de 0 a 4.')
            continue

        if operador == 0:
            print('Saindo da Calculadora!')
            return None

        if operador == 1:
            return num1 + num2
        elif operador == 2:
            return num1 - num2
        elif operador == 3:
            return num1 * num2
        elif operador == 4:
            try:
                return num1 / num2
            except ZeroDivisionError:
                print('Erro: Não é possível dividir por zero. Tente novamente.')
        else:
            print('Operação inválida. Tente novamente.')
            
        
def calculadora():
    num1, num2 = numeros()
    resultado = operadores(num1, num2)
    if resultado != None:
        print('O resultado de sua conta é: ', resultado)


print('''Bem vindo a Calculadora!
Será pedido que insira dois números separadamente, após deverá escolher um das operações: + (adição), - (subtração), * (multiplicação) e / (divisão).''')

calculadora()
