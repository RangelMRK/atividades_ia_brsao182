# Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou usuário digite 'sair'.


def verificadorSenha():
    while True:
            senha = input('Digite uma senha para cadastro, a senha deve conter letras, conter pelo menos um número e ser maior que 8 caracteres\n')
            if len(senha) < 8:
                print("Senha Inválida, deve conter mais de 8 Caracteres")
            elif any(chr.isdigit() for chr in senha) == False:
                print("Senha Inválida, deve conter pelo menos um número")      
            elif any(chr.isalpha() for chr in senha) == False:
                print("Senha Inválida, deve conter letras")   
            else:
                print("Senha Salva!")
                break
            
verificadorSenha()