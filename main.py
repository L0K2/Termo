import Gerar_palavra as gp
import os
from os import system
import time
from time import sleep

class Main:

    win_game = ""
    mds = gp.Gerar_palavra()
    mds.PegarPalavras()
    Palavra_chave = mds.RetornarValor()

    def __init__(self):
        mds = gp.Gerar_palavra()
        mds.PegarPalavras()
        self.input = ""
        os.system('color')

    def Input(self):
        self.input = input("\033[34m{}".format("Digite uma palavra: "))


    def Verificar_pos_correta(self):
        char_palavra_chave = list(Main.Palavra_chave)
        char_Input = list(self.input)
        for letra in self.input:
            lis_count = Main.Palavra_chave.count(letra)
            if lis_count >= 1 :
                if char_Input[0] == char_palavra_chave[0]:
                    print("\033[32m{}".format(letra))  # Verde
                    Main.win_game = self.input
                else:
                    print("\033[33m{}".format(letra))  # Amarelo
                char_Input.pop(0)
                char_palavra_chave.pop(0)
            if lis_count == 0:
                print("\033[31m{}".format(letra)) # Vermelho
                char_Input.pop(0)
                char_palavra_chave.pop(0)




    def Jogo(self):
        num_tentativa = 0
        while num_tentativa < 7:
                    m = Main()       
                    m.Input()
                    m.Verificar_pos_correta()
                    if Main.win_game == Main.Palavra_chave:
                        print("Você Ganhou!")
                        sleep(5)
                        break
                    num_tentativa = num_tentativa + 1
        if num_tentativa == 7:
            print("Você perdeu!")



m = Main()
m.Jogo()


"""
Amarelo = \033[33m{}
Verde = \033[32m{}
Vermelho = \033[31m{}


                if letra in self.Lista:
                    print("\033[33m{}".format(letra))
                    #print("esta na lista")
                else:
                    print("\033[32m{}".format(letra))

"""
