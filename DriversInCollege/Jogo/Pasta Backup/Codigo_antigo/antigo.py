import pygame,sys, os
from pygame import * 
class Mouse:
    
    def coordenadas_cursor(self):
        return pygame.mouse.get_pos()

    def seleciona_imagem(self, (x, y, larg, alt)):
        area_imagem = Rect(x, y, larg, alt)
        return area_imagem



#iniciar pygame
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

#criar tela 
Tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drivers in Collge")
#pygame.display.toggle_fullscreen()



#Carrega as imagens  e define tamanho e coordenadas para a colisao
Novo_jogo = [(124, 179, 145, 30), pygame.image.load("Imagens/Novo_jogo_MOFF.png"), pygame.image.load("Imagens/Novo_jogo_MON.png")]
Ranking = [(139, 237, 115, 30), pygame.image.load("Imagens/Ranking_MOFF.png"), pygame.image.load("Imagens/Ranking_MON.png")]
Sobre = [(157, 297, 80, 30), pygame.image.load("Imagens/Sobre_MOFF.png"), pygame.image.load("Imagens/Sobre_MON.png")]
Sair = [(164, 357, 65, 30), pygame.image.load("Imagens/Sair_MOFF.png"), pygame.image.load("Imagens/Sair_MON.png")]
Conf_sair_sim = [(280, 310, 50, 30), pygame.image.load("Imagens/Sair_sim_MOFF.png"), pygame.image.load("Imagens/Sair_sim_MON.png")]
Conf_sair_nao = [(470, 310, 50, 30), pygame.image.load("Imagens/Sair_nao_MOFF.png"), pygame.image.load("Imagens/Sair_nao_MON.png")] 
Conf = [(730, 535, 40, 40), pygame.image.load("Imagens/Conf_MON.png"), pygame.image.load("Imagens/Conf_MOFF.png")]
X_menu = [(620, 160, 20, 20), pygame.image.load("Imagens/X_MOFF.png"), pygame.image.load("Imagens/X_MON.png")]
Continuar = [(510, 410, 110, 20), pygame.image.load("Imagens/Continuar_MOFF.png"), pygame.image.load("Imagens/Continuar_MON.png")]
Volume_menos = [(215, 265, 20, 20), pygame.image.load("Imagens/Volume_menos_MOFF.png"), pygame.image.load("Imagens/Volume_menos_MON.png")]
Volume_mais = [(565, 265, 20, 20), pygame.image.load("Imagens/Volume_mais_MOFF.png"), pygame.image.load("Imagens/Volume_mais_MON.png")]
Volume_barra = [True, True, True, True, True, pygame.image.load("Imagens/Volume_barra.png")]
Idioma = [(300,330, 150, 30), pygame.image.load("Imagens/Portugues_MOFF.png"), pygame.image.load("Imagens/Portugues_MON.png"), 
              pygame.image.load("Imagens/English_MOFF.png"), pygame.image.load("Imagens/English_MON.png")]
Tela_cheia = [(330, 380, 120, 30),  pygame.image.load("Imagens/Tela_cheia_off_MOFF.png"), pygame.image.load("Imagens/Tela_cheia_off_MON.png"), 
              pygame.image.load("Imagens/Tela_cheia_on_MOFF.png"), pygame.image.load("Imagens/Tela_cheia_on_MON.png")]



 


#Alternacao entre os menus
Mouse = Mouse()
Tela_menu = True
Tela_novo_jogo = False
Tela_ajustes = False
Tela_ranking = False
Tela_sobre = False
Tela_sair = False
Idioma_portugues = True
Idioma_ingles = False
Tela_cheia_off = True
Tela_cheia_on = False


#loop principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #print Mouse.coordenadas_cursor()
    
    #Menu: imprime na tela
    if Tela_menu: 
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0)) 

        #event.type == 5 captura o click do mouse

        #Novo_jogo: verifica click (ON/OFF)
        if Mouse.seleciona_imagem(Novo_jogo[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Novo_jogo[2], (Novo_jogo[0][0], Novo_jogo[0][1]))
            if event.type == 5:
                Tela_menu = False
                Tela_novo_jogo = True
        else:
            Tela.blit(Novo_jogo[1], (Novo_jogo[0][0], Novo_jogo[0][1]))


        #Ranking: verifica click  (ON/OFF)
        if Mouse.seleciona_imagem(Ranking[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Ranking[2], (Ranking[0][0], Ranking[0][1]))
            if event.type == 5:
                Tela_menu = False
                Tela_ranking = True
        else:
            Tela.blit(Ranking[1], (Ranking[0][0], Ranking[0][1]))


        #Sobre: verifica click (ON/OFF)
        if Mouse.seleciona_imagem(Sobre[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Sobre[2], (Sobre[0][0], Sobre[0][1]))
            if event.type == 5:
                Tela_menu = False
                Tela_sobre = True
        else:
            Tela.blit(Sobre[1], (Sobre[0][0], Sobre[0][1]))

       
        #Sair: verifica click (ON/OFF)
        if Mouse.seleciona_imagem(Sair[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Sair[2], (Sair[0][0], Sair[0][1]))
            if event.type == 5:
                Tela_menu = False
                Tela_sair = True
        else:
            Tela.blit(Sair[1], (Sair[0][0], Sair[0][1]))


        #Ajustes: verifica click (ON/OFF)
        if Mouse.seleciona_imagem(Conf[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Conf[2], (Conf[0][0], Conf[0][1]))
            if event.type == 5:
                Tela_menu = False
                Tela_ajustes = True
        else:
            Tela.blit(Conf[1], (Conf[0][0], Conf[0][1]))

    #Novo_jogo: imprime na  tela
    if Tela_novo_jogo:
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Nome_novo_jogo.png"), (300, 150))
        Tela.blit(pygame.image.load("Imagens/Vaga.png"),(420, 260))
        Tela.blit(pygame.image.load("Imagens/Arrows.png"), (200, 250))
        
        if Mouse.seleciona_imagem(X_menu[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(X_menu[2], (X_menu[0][0], X_menu[0][1]))
            if event.type == 5:
                Tela_menu = True
                Tela_novo_jogo = False
        else:
            Tela.blit(X_menu[1], (X_menu[0][0], X_menu[0][1]))

        if Mouse.seleciona_imagem(Continuar[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Continuar[2], (Continuar[0][0], Continuar[0][1]))
            #if event.type == 5:
             #   Tela_menu = True
              #  Tela_novo_jogo = False
        else:
            Tela.blit(Continuar[1], (Continuar[0][0], Continuar[0][1]))


    #Ranking: imprime na  tela
    if Tela_ranking:
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Nome_ranking.png"), (300, 150))
        
        #Abre e imprime na tela o arquivo texto com o RANKING
        Fonte =  pygame.font.Font("Font/AbyssinicaSIL-R.ttf", 20)
        Rank = open("Ranking/testes.txt", "r")
        Cord_x = 200
        Cord_y = 250
        for colocado in Rank:
            Rank_print = Fonte.render(colocado, 1, (80, 80, 80))
            Tela.blit(Rank_print, (Cord_x, Cord_y))
            if colocado[0] != "5":
                Cord_y += 30
            else:
                Cord_x = 400
                Cord_y = 250
        #-----

        #Verifica se o mouse esta clicando no botao X(fechar)
        if Mouse.seleciona_imagem(X_menu[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(X_menu[2], (X_menu[0][0], X_menu[0][1]))
            if event.type == 5:
                Tela_menu = True
                Tela_ranking = False
        else:
            Tela.blit(X_menu[1], (X_menu[0][0], X_menu[0][1]))



    #Ajustes: imprime na tela
    if Tela_ajustes:
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Nome_ajustes.png"), (300, 150))
        Tela.blit(pygame.image.load("Imagens/Volume.png"), (310, 220))
        Tela.blit(pygame.image.load("Imagens/Barra_volume.png"), (245, 260))
        Tela.blit(pygame.image.load("Imagens/Idioma.png"), (150, 330))
        Tela.blit(pygame.image.load("Imagens/Tela_cheia.png"), (183, 380))       

        #Verifica se o mouse esta sobre o botao FECHAR
        if Mouse.seleciona_imagem(X_menu[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(X_menu[2], (X_menu[0][0], X_menu[0][1]))
            if event.type == 5:
                Tela_menu = True
                Tela_ajustes = False
        else:
            Tela.blit(X_menu[1], (X_menu[0][0], X_menu[0][1]))

        #Verifica se o mouse esta sobre os botoes de VOLUME
        if Mouse.seleciona_imagem(Volume_menos[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Volume_menos[2], (Volume_menos[0][0], Volume_menos[0][1]))
           

            #Verifica se esta clicando no botao volume MENOS
            if event.type == 5 and Volume_barra[4]:
                    Volume_barra[4] = False
            elif event.type == 5 and Volume_barra[3]:
                    Volume_barra[3] = False
            elif event.type == 5 and Volume_barra[2]:
                    Volume_barra[2] = False
            elif event.type == 5 and Volume_barra[1]:
                    Volume_barra[1] = False
            elif event.type == 5 and Volume_barra[0]:
                    Volume_barra[0] = False             
        else:
            Tela.blit(Volume_menos[1], (Volume_menos[0][0], Volume_menos[0][1]))

        #Verifica se o mouse esta sobre o botao VOLUME
        if Mouse.seleciona_imagem(Volume_mais[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Volume_mais[2], (Volume_mais[0][0], Volume_mais[0][1]))

            #Verifica se esta clicando no botao volume MAIS
            if event.type == 5 and Volume_barra[0] == False:
                    Volume_barra[0] = True
            elif event.type == 5 and Volume_barra[1] == False:
                    Volume_barra[1] = True
            elif event.type == 5 and Volume_barra[2] == False:
                    Volume_barra[2] = True
            elif event.type == 5 and Volume_barra[3] == False:
                    Volume_barra[3] = True
            elif event.type == 5 and Volume_barra[4] == False:
                    Volume_barra[4] = True                  
        else:
            Tela.blit(Volume_mais[1], (Volume_mais[0][0], Volume_mais[0][1]))

        #Imprime as imagens do volume de acordo com os parametros TRUE/FALSE
        if Volume_barra[0]:
            Tela.blit(Volume_barra[5],(250, 265))
        if Volume_barra[1]:
            Tela.blit(Volume_barra[5],(310, 265))
        if Volume_barra[2]:
            Tela.blit(Volume_barra[5],(370, 265))
        if Volume_barra[3]:
            Tela.blit(Volume_barra[5],(430, 265))
        if Volume_barra[4]:
            Tela.blit(Volume_barra[5],(490, 265))
        #----

        #Verifica se o mouse esta clicando no botao IDIOMA

        if Mouse.seleciona_imagem(Idioma[0]).collidepoint(Mouse.coordenadas_cursor()):
            if Idioma_portugues:
                Tela.blit(Idioma[2], (Idioma[0][0], Idioma[0][1]))
                if event.type == 5:
                    Idioma_ingles = True
                    Idioma_portugues = False
            else:
                 Tela.blit(Idioma[4], (Idioma[0][0], Idioma[0][1]))               
                 if event.type == 5:
                    Idioma_portugues = True
                    Idioma_ingles = False
        else:
            if Idioma_portugues:
                Tela.blit(Idioma[1], (Idioma[0][0], Idioma[0][1]))   
            
            else:
                Tela.blit(Idioma[3], (Idioma[0][0], Idioma[0][1]))

        #Verifica se o mouse esta clicando no botao TELA CHEIA
        if Mouse.seleciona_imagem(Tela_cheia[0]).collidepoint(Mouse.coordenadas_cursor()):
            if Tela_cheia_on:
                Tela.blit(Tela_cheia[4], (Tela_cheia[0][0], Tela_cheia[0][1]))
                if event.type == 5:
                    Tela_cheia_on = False
                    tela_cheia_off = True
                    pygame.display.set_mode((800, 600))
 
            else:
                 Tela.blit(Tela_cheia[2], (Tela_cheia[0][0], Tela_cheia[0][1]))               
                 if event.type == 5:
                    Tela_cheia_off = False
                    Tela_cheia_on = True
                    pygame.display.toggle_fullscreen()
        else:
            if Tela_cheia_on:
                Tela.blit(Tela_cheia[3], (Tela_cheia[0][0], Tela_cheia[0][1]))   
            
            else:
                Tela.blit(Tela_cheia[1], (Tela_cheia[0][0], Tela_cheia[0][1]))

    #Sobre: imprime na tela
    if Tela_sobre:
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Nome_sobre.png"), (300, 150))
        
        #Abre e imprime na tela o arquivo de texto
        Fonte =  pygame.font.Font("Font/AbyssinicaSIL-R.ttf", 17)
        Sobre_arquivo = open("Sobre/Sobre.dat", "r")
        Cord_y = 200
        for Sobre_texto in Sobre_arquivo:
            Sobre_print = Fonte.render(Sobre_texto, 1, (80, 80, 80))
            Tela.blit(Sobre_print, (220, Cord_y))
            Cord_y += 20
        #----

        #Verifica se o mouse esta clicando no botao X(fechar)
        if Mouse.seleciona_imagem(X_menu[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(X_menu[2], (X_menu[0][0], X_menu[0][1]))
            if event.type == 5:
                Tela_menu = True
                Tela_sobre = False
        else:
            Tela.blit(X_menu[1], (X_menu[0][0], X_menu[0][1]))
            

    #Sair: imprime na tela
    if Tela_sair:
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Transparencia_menu_sair.png"), (0, 0))
        if Mouse.seleciona_imagem(Conf_sair_sim[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Conf_sair_sim[2], (Conf_sair_sim[0][0], Conf_sair_sim[0][1]))
            if event.type == 5:
                pygame.quit()
                sys.exit()
        else:
            Tela.blit(Conf_sair_sim[1], (Conf_sair_sim[0][0], Conf_sair_sim[0][1]))
        if Mouse.seleciona_imagem(Conf_sair_nao[0]).collidepoint(Mouse.coordenadas_cursor()):
            Tela.blit(Conf_sair_nao[2], (Conf_sair_nao[0][0], Conf_sair_nao[0][1]))
            if event.type == 5:
                Tela_sair = False
                Tela_menu = True

        


        else:
            Tela.blit(Conf_sair_nao[1], (Conf_sair_nao[0][0], Conf_sair_nao[0][1]))
    pygame.display.flip()
