# Universidade Federal de Campina Grande - UFCG 
# Departamento de Sistemas e Computacao - DSC
# Curso de Ciencias da Computacao
# Gerson Sales Araujo de Freitas Junior	114210216
# Jose manoel dos Santos Ferreira 	114211020
# Drivers in College

import pygame, pygame.mixer, sys, imp
DA = ""
Dimg = "Jogo/"
Modulo, Diretorio, Descricao = imp.find_module("Mouse", [DA + "Botoes_menu/"])
mouse = imp.load_module("Mouse", Modulo, Diretorio, Descricao)
mouse = mouse.Mouse()


class Loja:
    def __init__(self):
        #Carregamento das imagens dos botoes
        self.preco_MOFF = [pygame.image.load(Dimg + "Loja/Botoes/Ps_" + str(x) + "_MOFF.png") for x in range(16)]
        self.preco_MON = [pygame.image.load(Dimg + "Loja/Botoes/Ps_" + str(x) + "_MON.png") for x in range(16)]
        self.Voltar_aba = [(357, 410, 35, 40), pygame.image.load(Dimg + "Loja/Botoes/Aba_voltar_MOFF.png"), 
                                               pygame.image.load(Dimg + "Loja/Botoes/Aba_voltar_MON.png")]
        self.Ir_aba = [(407, 410, 35, 40), pygame.image.load(Dimg + "Loja/Botoes/Aba_ir_MOFF.png"), 
                                           pygame.image.load(Dimg + "Loja/Botoes/Aba_ir_MON.png")]
        self.Sair_loja = [(600, 430, 65, 30), pygame.image.load(Dimg + "Loja/Botoes/Sair_MOFF.png"), 
                                              pygame.image.load(Dimg + "Loja/Botoes/Sair_MON.png")]
        
        #Carregamento das imagens da tela
        self.Aba_conserto = pygame.image.load(Dimg + "Loja/Abas/Aba_conserto.png")
        self.Aba_fases = pygame.image.load(Dimg + "Loja/Abas/Aba_fases.png")
        self.Aba_personalizar = pygame.image.load(Dimg + "Loja/Abas/Aba_personalizar.png")
        self.Imagem_loja = pygame.image.load(Dimg + "Loja/Abas/Imagem_loja.png")

        #Alternancia entre abas
        self.Aba_atual = 0

        #Precos das fases/dano/personalizacao
        self.Preco_fase = [(2, 800), (3, 1000), (4, 1500), (5, 2000), (6, 2500), (7, 3000), (8, 3500), (9, 4000)]
        self.Preco_conserto = [(10, 100), (50, 500), (100, 800)]
        self.Preco_cores = [(0, "Rosa"), (1, "Roxo"), (2, "Amarelo"), (3, "Azul"), (4, "Verde"), (5, "Vermelho"), 200]

        #Sons da loja

        self.Loja_erro = pygame.mixer.Sound(Dimg + "Cenario/Sons/Loja_erro.wav")
        self.Loja_compra = pygame.mixer.Sound(Dimg + "Cenario/Sons/Loja_compra.wav")


    def Escreve_na_tela(self, screen, Texto, Tamanho, Posicao):
        Fonte = pygame.font.Font(Dimg + "Cenario/Font/AbyssinicaSIL-R.ttf", Tamanho)
#        Fonte.set_bold(True)
        Texto_tela = Fonte.render(str(Texto), 1, (30, 30, 30))
        screen.blit(Texto_tela, tuple(Posicao))

        
        

    def Menu_loja(self, screen, event, (Pontos, Fase, Dano, Cor)):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #imagem da loja
            screen.blit(self.Imagem_loja, (0, 0))
            
            #Dano/Fase/Pontos atual
            self.Escreve_na_tela(screen, "P$" + str(Pontos), 30, (50, 30))
            self.Escreve_na_tela(screen, "Fase: " + str(Fase), 20, (650, 10)) 
            self.Escreve_na_tela(screen, "Dano: " + str(Dano), 20, (650, 30)) 
            self.Escreve_na_tela(screen, "Cor: " + self.Preco_cores[Cor][1], 20, (650, 50)) 


            #Blita uma aba FASES e seus respectivos botoes
            if self.Aba_atual == 0: 
                screen.blit(self.Aba_fases, (0, 0))
                Coord_x = 215
                Coord_y = 280
                for preco in range(2, 10):
                    Rect_img = self.preco_MOFF[preco].get_rect()
                    Click, Sobre =  mouse.Verifica_click(screen, event, [(Coord_x, Coord_y, Rect_img[2], Rect_img[3]),
                                                        self.preco_MOFF[preco], self.preco_MON[preco]])[1:]
                    if Sobre == False:
                        Texto = "Comprar Fase %d" %(self.Preco_fase[preco - 2][0])
                        self.Escreve_na_tela(screen, Texto, 40, (250, 30)) 
                    if Click:
                        pygame.mouse.set_pos(pygame.mouse.get_pos()[0] - 1, pygame.mouse.get_pos()[1])
                        if Fase == self.Preco_fase[preco - 2][0]:
                            if Pontos >= self.Preco_fase[preco - 2][1]:
                                Fase += 1
                                Pontos -= self.Preco_fase[preco - 2][1]
                                self.Loja_erro.stop()
                                self.Loja_compra.play()
                                self.Escreve_na_tela(screen, "P$", 30, (Coord_x + 10, Coord_y - 40))#comprado
                            else: 
                                self.Loja_erro.stop()
                                self.Loja_erro.play()
                                self.Escreve_na_tela(screen, "X", 50, (90, 20)) #Pontos insuficientes

                        else:
                            self.Loja_erro.stop()
                            self.Loja_erro.play()
                            self.Escreve_na_tela(screen, "X", 50, (Coord_x + 15, Coord_y - 50)) #so fase atual

                    Coord_x += 100
                    if Coord_x == 615:
                        Coord_x = 215
                        Coord_y += 100
                    
            #Blita a aba CONSERTO e seus respectivos botoes
            elif self.Aba_atual == 1: 
                screen.blit(self.Aba_conserto, (0, 0))
                Coord_x = 260
                Coord_y = 350
                for preco in range(3):
                    Rect_img = self.preco_MOFF[preco].get_rect()
                    Click, Sobre = mouse.Verifica_click(screen, event, [(Coord_x, Coord_y, Rect_img[2], Rect_img[3]),
                                                           self.preco_MOFF[preco], self.preco_MON[preco]])[1:]
                    if Sobre == False:
                        Texto = "Menos %d de dano" %(self.Preco_conserto[preco][0])
                        self.Escreve_na_tela(screen, Texto, 40, (250, 20))
                    if  Click:
                        if Dano > 0:
                            pygame.mouse.set_pos(pygame.mouse.get_pos()[0] - 1, pygame.mouse.get_pos()[1])
                            if Pontos >= self.Preco_conserto[preco][1]:
                                Dano -= self.Preco_conserto[preco][0]
                                Pontos -= self.Preco_conserto[preco][1]
                                self.Loja_erro.stop()
                                self.Loja_compra.play()
                            else: 
                                self.Loja_erro.stop()
                                self.Loja_erro.play()
                                self.Escreve_na_tela(screen, "X", 50, (90, 20))
                        else:
                            self.Loja_erro.stop()
                            self.Loja_erro.play()
                    Coord_x += 110
    
            #Blita a aba PERSONALIZAR e seus respectivos botoes
            else: 
                screen.blit(self.Aba_personalizar, (0, 0))
                Coord_x = 180
                Coord_y = 260
                for preco in range(10, 16):
                    Rect_img = self.preco_MOFF[preco].get_rect()
                    Click, Sobre = mouse.Verifica_click(screen, event, [(Coord_x, Coord_y, Rect_img[2], Rect_img[3]),
                                                           self.preco_MOFF[preco], self.preco_MON[preco]])[1:]
                    if Sobre == False:
                        Texto = "Pintar de %s!" %(self.Preco_cores[preco - 10][1])
                        self.Escreve_na_tela(screen, Texto, 40, (250, 20)) 
                    if Click:
                        pygame.mouse.set_pos(pygame.mouse.get_pos()[0] - 1, pygame.mouse.get_pos()[1])
                        if Cor != self.Preco_cores[preco - 10][0]:
                            if Pontos >= self.Preco_cores[-1]:
                                Cor = self.Preco_cores[preco - 10][0]
                                Pontos -= self.Preco_cores[-1]
                                self.Loja_erro.stop()
                                self.Loja_compra.play()
                                self.Escreve_na_tela(screen, "P$", 30, (Coord_x + 10, Coord_y + 10))#comprou cor
                            else: 
                                self.Loja_erro.stop()
                                self.Loja_erro.play()
                                self.Escreve_na_tela(screen, "X", 50, (90, 20))#Pontos insuficientes 
                        else:
                            self.Loja_erro.stop()
                            self.Loja_erro.play()
                            self.Escreve_na_tela(screen, "X", 50, (Coord_x + 10, Coord_y)) #Voce ja possui esta cor
                    Coord_x += 75


            #AVANCAR ou RETROCEDER uma aba
            Click, Sobre = mouse.Verifica_click(screen, event, self.Voltar_aba)[1:]
            if Sobre == False:
                self.Escreve_na_tela(screen, "Anterior", 40, (330, 20)) 
            if Click:
                if self.Aba_atual == 0: self.Aba_atual = 2
                else: self.Aba_atual -= 1
                pygame.mouse.set_pos(pygame.mouse.get_pos()[0] - 1, pygame.mouse.get_pos()[1])

            Click, Sobre = mouse.Verifica_click(screen, event, self.Ir_aba)[1:]
            if Sobre == False:
                self.Escreve_na_tela(screen, "Proximo", 40, (330, 20)) 
            if Click:
                if self.Aba_atual == 2: self.Aba_atual = 0
                else: self.Aba_atual += 1
                pygame.mouse.set_pos(pygame.mouse.get_pos()[0] - 1, pygame.mouse.get_pos()[1])
            
            #Sair da loja
            if mouse.Verifica_click(screen, event, self.Sair_loja)[1]:
                return (Pontos, Fase, Dano, Cor)


            pygame.display.flip()



#pygame.init()
#Tela = pygame.display.set_mode((800, 600))
#loja = Loja()
#Pontos = 200000
#Fase = 2
#Dano = 300
#Cor = 1
#Pontos, Fase, Dano, Cor = loja.Menu_loja(Tela, True, (Pontos, Fase, Dano, Cor))
#print Pontos
#print Fase
#print Dano
#print Cor


