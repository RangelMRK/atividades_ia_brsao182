# EXERCICIO PRATICO 2
# Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.

def registro():
    notas = []
    print("Digite as notas dos alunos (digite 'fim' para encerrar):")
    while True:
        nota = input("Nota: ")
        if nota.lower() == "fim":
            break
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10:
                notas.append(nota_float)
            else:
                print("Digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print("A média da turma é:", round(media, 2))
    else:
        print("Nenhuma nota foi registrada.")

print("Bem-vindo ao Registro de Notas!")
registro()
