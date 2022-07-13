import random

class Gerar_palavra:
    file = open("Lista_de_palavras.txt","r")
    read = file.readlines()
    lista = []

    def PegarPalavras(self):
        for line in Gerar_palavra.read:
            if line[-1] == '\n':
                Gerar_palavra.lista.append(line[:-1])
            else:
                Gerar_palavra.lista.append(line)

    def RetornarValor(self):
        s = random.randint(0,3)
        palavra_chave = Gerar_palavra.lista[s]
        return palavra_chave