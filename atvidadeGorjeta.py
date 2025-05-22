# Crie uma função que calcule a gorjeta a ser deixada em um restaurante baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

# Parâmetros:
# valor_conta(float): O valor total da conta
# porcentagem_gorjeta(float): A porcentagem da gorjeta (Ex: 15 para 15%)

# Retorna:
# float: O valor da gorjeta calculada


def gorjeta():
    print('Digite o valor total da conta:')
    valor_conta = float(input())
    print('Digite a porcentagem que gostaria de dar de gorjeta:')
    porcentagem_gorjeta = float(input())

    gorjeta = valor_conta * (porcentagem_gorjeta/100)

    print('O valor da gorjeta desta conta é de R$', gorjeta)

gorjeta()