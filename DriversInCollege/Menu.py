# Universidade Federal de Campina Grande - UFCG 
# Departamento de Sistemas e Computacao - DSC
# Curso de Ciencias da Computacao
# Gerson Sales Araujo de Freitas Junior	114210216
# Jose manoel dos Santos Ferreira 	114211020
# Drivers in College

import pygame,sys, os
from pygame import *
from Botoes_menu.Mouse import *
from Botoes_menu.Novo_jogo import *
from Jogo.Ranking import *
from Botoes_menu.Sobre import *
from Botoes_menu.Ajustes import *
from Jogo.Movimento import *
from pygame.mixer import * 
from Jogo.Game_data import *





#iniciar pygame
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

#criar tela 
Tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drivers in Collge")
#pygame.display.toggle_fullscreen()

game_data = Game_data_read()

#Carrega as imagens  e define tamanho e coordenadas para a colisao
Novo_jogo = [(124, 179, 145, 30), pygame.image.load("Imagens/Novo_jogo_MOFF.png"), pygame.image.load("Imagens/Novo_jogo_MON.png"),]
Novo_jogo_2 = [(490, 410, 145, 30), pygame.image.load("Imagens/Novo_jogo_MOFF.png"), pygame.image.load("Imagens/Novo_jogo_MON.png"),]
Ranking = [(139, 237, 115, 30), pygame.image.load("Imagens/Ranking_MOFF.png"), pygame.image.load("Imagens/Ranking_MON.png")]
Sobre = [(157, 297, 80, 30), pygame.image.load("Imagens/Sobre_MOFF.png"), pygame.image.load("Imagens/Sobre_MON.png")]
Sair = [(164, 357, 65, 30), pygame.image.load("Imagens/Sair_MOFF.png"), pygame.image.load("Imagens/Sair_MON.png")]
Conf_sair_sim = [(280, 310, 50, 30), pygame.image.load("Imagens/Sair_sim_MOFF.png"), pygame.image.load("Imagens/Sair_sim_MON.png")]
Conf_sair_nao = [(470, 310, 50, 30), pygame.image.load("Imagens/Sair_nao_MOFF.png"), pygame.image.load("Imagens/Sair_nao_MON.png")] 
X_menu = [(620, 160, 20, 20), pygame.image.load("Imagens/X_MOFF.png"), pygame.image.load("Imagens/X_MON.png")]
Continuar = [(170, 410, 140, 30), pygame.image.load("Imagens/Continuar_MOFF.png"), pygame.image.load("Imagens/Continuar_MON.png"),
              pygame.image.load("Imagens/English_MOFF.png"), pygame.image.load("Imagens/English_MON.png")]
Conf = [(730, 535, 40, 40), pygame.image.load("Imagens/Conf_MON.png"), pygame.image.load("Imagens/Conf_MOFF.png")]
Reset_ranking = [(520, 410, 110, 30), pygame.image.load("Imagens/Resetar_MOFF.png"), pygame.image.load("Imagens/Resetar_MON.png"),]

#Carrega os sons do menu
Sons_menu = [pygame.mixer.Sound("Botoes_menu/Sons/Mouse_ON.wav"), pygame.mixer.Sound("Botoes_menu/Sons/Mouse_click.wav")]




#Atribuicao das classes
Mouse = Mouse()
Menu_novo_jogo = Menu_novo_jogo()
Menu_ranking = Menu_ranking("Jogo/")
Menu_sobre = Menu_sobre()
Menu_ajustes = Menu_ajustes()
Jogo = Jogo()
#Alternancia entre telas
Tela_menu = True
Tela_novo_jogo = False
Tela_ajustes = False
Tela_ranking = False
Tela_sobre = False
Tela_sair = False
Tela_jogo = False
#Escolha do idioma
Idioma_portugues = True
Idioma_ingles = False

#Escolha Tela_cheia
Tela_cheia_off = True
Tela_cheia_on = False

#Sons do mouse
Som_mouse = [None for x in range(14)]
Reproduzir_som = [True] 
Tocar_musica = True
Volume = 1.


#loop principal
while True:
    #Limpar Tela
    Tela.fill(0)

    #Captura os comandos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #Menu: imprime na tela
    if Tela_menu:

        #Executa a musica do menu
        if Tocar_musica:
            pygame.mixer.music.load("Botoes_menu/Sons/Som_menu.wav")
            pygame.mixer.music.set_volume(Volume)
            pygame.mixer.music.play(-1)
            Tocar_musica = False


        #Faz o carregamento da imagem do menu e blita na tela
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0)) 
        #event.type == 5 captura o click do mouse
        #Novo_jogo: verifica click (ON/OFF)
        Tela_menu, Tela_novo_jogo, Som_mouse[0]= Mouse.Verifica_click(Tela, event, Novo_jogo, Tela_menu, Tela_novo_jogo)
        #Ranking: verifica click  (ON/OFF)
        Tela_menu, Tela_ranking, Som_mouse[1] = Mouse.Verifica_click(Tela, event, Ranking, Tela_menu, Tela_ranking)
        #Sobre: verifica click (ON/OFF)
        Tela_menu, Tela_sobre, Som_mouse[2] = Mouse.Verifica_click(Tela, event, Sobre, Tela_menu, Tela_sobre)
        #Sair: verifica click (ON/OFF)
        Tela_menu, Tela_sair, Som_mouse[3] = Mouse.Verifica_click(Tela, event, Sair, Tela_menu, Tela_sair)
        #Ajustes: verifica click (ON/OFF)
        Tela_menu, Tela_ajustes, Som_mouse[4] = Mouse.Verifica_click(Tela, event, Conf, Tela_menu, Tela_ajustes)

    #Novo_jogo: imprime na  tela
    if Tela_novo_jogo:
        #imprime as imagens da tela NOVO JOGO
        Menu_novo_jogo.Imprime_tela(Tela)
        #verifica se clicou no botao FECHAR
        Tela_novo_jogo, Tela_menu, Som_mouse[5]= Mouse.Verifica_click(Tela, event, X_menu, Tela_novo_jogo, Tela_menu)
        #Se clica em CONTINUAR continuara da fase em que o jogador parou
        if Jogo.Obter_nivel() != 1:
            #Verifica se clicou no botao continuar
            Tela_novo_jogo, Tela_jogo, Som_mouse[6] = Mouse.Verifica_click(Tela, event, Continuar, Tela_novo_jogo, Tela_jogo)
        #Verifica se clicou no botao continuar
        Tela_novo_jogo, Tela_jogo, Som_mouse[7] = Mouse.Verifica_click(Tela, event, Novo_jogo_2, Tela_novo_jogo, Tela_jogo)
        #Se clicar em NOVO_JOGO iniciara da primeira fase
        if Rect(Novo_jogo_2[0]).collidepoint(pygame.mouse.get_pos()):
            if event.type == 5 and pygame.mouse.get_pressed()[0]:
                Jogo.Definir_nivel(1)
                Game_data.Game_data_write(1, 0, 0, 0, 2, 0)

        #Roda a tela do jogo enquanto ela estiver ativa
        if Tela_jogo:
            #Para a musica do menu quando entrar no jogo
            Tocar_musica = True
            pygame.mixer.music.stop()
            Tela_menu, Tela_jogo = Jogo.Iniciar(Tela_menu, Tela_jogo, Tela_cheia_on, game_data, Volume)
       
    #Ranking: imprime na  tela
    if Tela_ranking:
        #Imprime na tela o ranking e as imagens do RANKING 
        Menu_ranking.Imprime_tela(Tela)
        #Verifica se clicou no botoX(fechar)
        Tela_ranking, Tela_menu, Som_mouse[8] = Mouse.Verifica_click(Tela, event, X_menu, Tela_ranking, Tela_menu)
        Resetar, Som_mouse[9] = Mouse.Verifica_click(Tela, event, Reset_ranking)[1:]
        if Resetar:
            Menu_ranking.Reset_ranking()
    #Ajustes: imprime na tela
    if Tela_ajustes:
        #Imprime as imagens na tela de AJUSTES     
        Menu_ajustes.Imprime_tela(Tela)
        #Verifica se o mouse esta sobre o botao FECHAR
        Tela_ajustes, Tela_menu, Som_mouse[10] = Mouse.Verifica_click(Tela, event, X_menu, Tela_ajustes, Tela_menu)
        #Verifica se o mouse esta sobre botoes e se esta clicando em VOLUME
        Volume = Menu_ajustes.Altera_volume(event, Sons_menu)
        #Verifica se o mouse esta clicando no botao IDIOMA
        #Idioma_portugues, Idioma_ingles = Menu_ajustes.Altera_idioma(Tela, event, Idioma_portugues, Idioma_ingles)
        #Verifica se o mouse esta clicando no botao TELA_CHEIA 
        Tela_cheia_on, Tela_cheia_off = Menu_ajustes.Altera_tela_cheia(Tela, event, Tela_cheia_on, Tela_cheia_off)

    #Sobre: imprime na tela
    if Tela_sobre:
        #imprime as imagens do sobre e as informacoes SOBRE
        Menu_sobre.Imprime_tela(Tela)
        #Verifica se esta clicando no X(fechar)
        Tela_sobre, Tela_menu, Som_mouse[11] = Mouse.Verifica_click(Tela, event, X_menu, Tela_sobre, Tela_menu)


    #Sair: imprime na tela
    if Tela_sair:
        #imprime na tela a transparencia da janela  SAIR
        Tela.blit(pygame.image.load("Imagens/Menu.png"), (0, 0))
        Tela.blit(pygame.image.load("Imagens/Transparencia_menu_sair.png"), (0, 0))
        #Verifica se esta clicando no SAIR_SIM
        Tela_sair, Tela_menu, Som_mouse[12] = Mouse.Verifica_click(Tela, event, Conf_sair_sim, Tela_sair, Tela_menu, 1)
        #Verifica se esta clicando no SAIR_NAO
        Tela_sair, Tela_menu, Som_mouse[13] = Mouse.Verifica_click(Tela, event, Conf_sair_nao, Tela_sair, Tela_menu)

    #Executa o som de cada botao 
    Mouse.Possibilidade_click(Sons_menu, Som_mouse, Reproduzir_som, Volume)

    #Inicia a tela do jogo
    if Tela_jogo:
        Jogo.iniciar()

    #Atualiza a tela a cada iteracao do WHILE
    pygame.display.flip()
