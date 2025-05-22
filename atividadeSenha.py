# Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou usuário digite 'sair'.


def verificadorSenha():
    while True:
            senha = input('Digite uma senha para cadastro\n')
            if len(senha) > 8 and any(chr.isdigit() for chr in senha):
                print("Senha Salva!")
                break
            else:
                 (print("Senha incorreta, deve conter pelo menos um número e ser maior que 8 caracteres"))

verificadorSenha()