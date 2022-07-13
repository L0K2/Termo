import Gerar_palavra as gp

class Main:

    win_game = ""
    mds = gp.Gerar_palavra()
    mds.PegarPalavras()
    Palavra_chave = mds.RetornarValor()

    def __init__(self):
        mds = gp.Gerar_palavra()
        mds.PegarPalavras()
        #self.Palavra = mds.RetornarValor()
        self.input = ""

    def Input(self):
        self.input = input("\033[34m{}".format("Digite uma palavra: "))


    def Verificar_pos_correta(self):
        for letra in self.input:
            lis_count = Main.Palavra_chave.count(letra)
            if lis_count >= 1 :
                index_Lista = Main.Palavra_chave.index(letra)
                index_Input = self.input.index(letra)
                if index_Lista == index_Input:
                    print("\033[32m{}".format(letra)) #Verde
                    Main.win_game = self.input
                else:
                    print("\033[33m{}".format(letra)) #Amarelo
            if lis_count == 0:
                print("\033[31m{}".format(letra))




    def Jogo(self):
        num_tentativa = 0
        while num_tentativa < 7:
                    m = Main()
                    print(Main.Palavra_chave)
                    m.Input()
                    m.Verificar_pos_correta()
                    if Main.win_game == Main.Palavra_chave:
                        print("Você Ganhou!")
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