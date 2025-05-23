# Crie um arquivo chamado minhas_notas.txt. 
# Grave 3 frases nele usando open com 'w'. Depois, adicione 2 frases novas usando 'a'. 
# Por fim, leia e imprima o conteúdo com with.”

def escrever():
    notas = open("pythonManipular\minhas_notas.txt", "w")
    notas.write("Frase 1: Esta é minha primeira frase")
    notas.write("\nFrase 2: Esta é minha segunda frase")
    notas.write("\nFrase 3: Esta é minha terceira frase")
    notas.close()

def adicionar():
    notas = open("pythonManipular\minhas_notas.txt", "a")
    notas.write("\nFrase 4: Esta frase foi adicionada")
    notas.write("\nFrase 5: Esta frase também foi adicionada!")
    notas.close()

def leitura():
    with open("pythonManipular\minhas_notas.txt") as notas:
        print(notas.read())


escrever()
adicionar()
leitura()