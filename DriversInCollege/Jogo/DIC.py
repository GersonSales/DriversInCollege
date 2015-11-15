# Universidade Federal de Campina Grande - UFCG 
# Departamento de Sistemas e Computacao - DSC
# Curso de Ciencias da Computacao
# Gerson Sales Araujo de Freitas Junior	114210216
# Jose manoel dos Santos Ferreira 	114211020
# Drivers in College

import pygame, math, sys, time, random, imp, Game_data, Cenario, Loja
from pygame.locals import *
from Ranking import *
from Cenario import Cenario
from pygame.mixer import *
from Loja import Loja
#Importar o modulo mouse. Ps: arquivo em outro diretorio
DA = ""
Modulo, Diretorio, Descricao = imp.find_module("Mouse", [DA + "Botoes_menu/"])

#pygame.mixer.init()
pygame.mixer.pre_init(22100)



#Variavel com acesso global para informar ao programa a fase atual
Numero_fase = Game_data.Game_data_read()[0] 

#Diretorio dos arquivos da pasta Jogo
diretorio_imagens = "Jogo/Cenario/"
diretorio_rank = "Jogo/"

#Iniciar modulos importados
mouse = imp.load_module("Mouse", Modulo, Diretorio, Descricao)
mouse = mouse.Mouse()
ranking = Menu_ranking(diretorio_rank)
cenario = Cenario()
loja = Loja()

#Definir o tamanho da Tela
Tamanho_tela_x = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_tela"][0]
Tamanho_tela_y = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_tela"][1]

#Variavel responsavel pelo backup da posicao do carro
contador_backup = 0


#FUNCAO responsavel por criar um mada de acordo com Tamanho_mapa
def clamp(x, minimo, maximo):
    return max(minimo, min(maximo, x))
 
class Camera:

    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x, self.min_y = min_x, min_y
        self.max_x, self.max_y = max_x, max_y
        self.x = min_x
        self.y = min_y

    def center_on(self, x, y):
        new_x = x - Tamanho_tela_x / 2
        new_y = y - Tamanho_tela_y / 2
        self.x = clamp(new_x, self.min_x, self.max_x)
        self.y = clamp(new_y, self.min_y, self.max_y)



#Modulo responsavel por toda as funcoes do carro e de jogo
class Carro:
    global Numero_fase
    def __init__(self, game_data):
        #Direcoes do carr0
        self.DIREITA = 0
        self.ESQUERDA = 1

        #Permitir colisoes com carros/paredes e permitir movimento
        self.colid_movimento = False
        self.colidir = True 
        self.colidir_parede = False
        self.movimenta = True

        #SOM
        self.Carro_parado = pygame.mixer.Sound(diretorio_imagens + "Sons/Carro_parado.wav")
        self.Carro_colide = pygame.mixer.Sound(diretorio_imagens + "Sons/Carro_colide.wav")

        #Posicao inicial do carro baseado no novo redimensionamento da tela
        self.virtual_x = cenario.Fases["Fase_" + str(Numero_fase)]["Virtual_x"]
        self.virtual_y = cenario.Fases["Fase_" + str(Numero_fase)]["Virtual_y"]
        self.backup_x, self.backup_y = 567, 456
        
        #Angulo inicial do carro
        self.angle = cenario.Fases["Fase_" + str(Numero_fase)]["Angulo_inicial"]
        self.backup_angle = self.angle

        #Velocidade Inicial do carro
        self.velocidade = cenario.Fases["Fase_" + str(Numero_fase)]["Velocidade_inicial"]

        #Carregamento da imagem do carro/vaga/barra_dano
        self.Cor_carro = game_data[4]
        self.image = [pygame.image.load(diretorio_imagens + "Carros/Car_" + str(x) + ".png") for x in range(6)]
        self.Vaga_imagem = pygame.image.load(diretorio_imagens + "Carros/Vaga.png")
        self.Dano = pygame.image.load(diretorio_imagens + "Botoes/Dano.png")
        self.Barra_dano = pygame.image.load(diretorio_imagens + "Botoes/Barra_dano.png")
        self.Preenchimento_barra = pygame.image.load(diretorio_imagens + "Botoes/Preenchimento_barra.png")
        self.original = [pygame.image.load(diretorio_imagens + "Carros/Car_" + str(x) + ".png") for x in range(6)]

        #Cria retangulo do carro
        self.rect = self.image[self.Cor_carro].get_rect()

        #Tamannho da tela e coordenadas do mapa
        self.x, self.y = Tamanho_tela_x/2, Tamanho_tela_y/2
        self.offset_x, self.offset_y = self.virtual_x - Tamanho_tela_x/2, self.virtual_y - Tamanho_tela_y/2

        #Dano do carro
        self.Dano_carro = game_data[2] + game_data[5]

        #Dano de cada fase
        self.Dano_fase = 0 
        self.Lista_pontuacao = []
        
        #Pontos iniciais de cada fase
        self.Pontuacao_inicial = 2000

        #Registra tempo
        self.tempo_x = time.time()
        self.tempo_pausa = 0
        self.tempo_pausa_2 = 0

        #Resultado final de cada fase
        self.Total_tempo = game_data[1]
        self.Total_dano = game_data[2] + game_data[5]
        self.Total_pontos = game_data[3]
       
        #Volume dos sons
        self.Volume_sons = 1.

    #Salvar estado atual do jogo
    def Escrever_dados(self):
        Game_data.Game_data_write(Numero_fase, self.Total_tempo, self.Total_dano, self.Total_pontos, self.Cor_carro, self.Dano_fase)

    def Itens_loja(self):
        global Numero_fase
        return (self.Total_pontos, Numero_fase, self.Dano_carro, self.Cor_carro)

    #Interacao de itens com a loja
    def Altera_itens_loja(self, (Pontos, Fase, Dano, Cor)):
        global Numero_fase
        Numero_fase = Fase
        self.Dano_carro = Dano
        self.Cor_carro = Cor
        self.Total_pontos = Pontos
        self.Resetar_carro()



    #Mudar Direcao do carro de acordo com a velocidade e a angulacao do carro
    def Mudar_direcao(self, direcao):
        DIREITA = self.DIREITA
        ESQUERDA = self.ESQUERDA    
        if direcao == DIREITA:
                self.angle += (self.velocidade/9) * 0.5 
        elif direcao == ESQUERDA:
                self.angle -= (self.velocidade/9) * 0.5
        if self.angle >= 360:
            self.angle = self.angle - 360
        if self.angle < 0:
            self.angle = 360 + self.angle
           
    
    def Movimentacao(self,key):
        
        global contador_backup,Numero_fase
        

       #Variavel para informar quado devera ser feito um backup da posicao 
        DIREITA = self.DIREITA
        ESQUERDA = self.ESQUERDA    
 
        #Variaveis responsaveis pela angulacao do carro
        self.velocidadex = math.sin(self.angle * (math.pi/180)) * (self.velocidade/9)
        self.velocidadey = math.cos(self.angle * (math.pi/180)) * (self.velocidade/9) * -1

        #Verificar qual tecla esta sendo pressionada e move o carro na direcao correta
        if key[K_UP] and self.movimenta:
            if self.velocidade < 60:
                self.velocidade += 2 
        if key[K_DOWN] and self.movimenta:
            if self.velocidade > -50:
                self.velocidade -= 2

        #Mover o carro para tras
        if  self.velocidade < 0:
            self.virtual_x += self.velocidadex
            self.virtual_y += self.velocidadey
            if self.velocidadex != 0.0 or self.velocidadey != 0.0:
                self.colidir = True
                contador_backup += 1
            if key[K_RIGHT]:
                self.Mudar_direcao(DIREITA)
            elif key[K_LEFT]:
                self.Mudar_direcao(ESQUERDA)
            if key[K_DOWN] == False:
                self.velocidade += 1
            if key[K_UP]:
                self.velocidade += 2

        #Mover o carro para frente
        elif  self.velocidade > 0:
            self.virtual_x += self.velocidadex
            self.virtual_y += self.velocidadey
            if self.velocidadex != 0.0 or self.velocidadey != 0.0:
                self.colidir = True
                contador_backup += 1
            if key[K_RIGHT]:
                self.Mudar_direcao(DIREITA)
            elif key[K_LEFT]:
                self.Mudar_direcao(ESQUERDA)
            if key[K_UP] == False:
                self.velocidade -= 1
            if key[K_DOWN]:
                self.velocidade -= 2
        else:
            self.colidir_parede = True
        #SOM
        if self.velocidade == 0:
            self.Carro_parado.set_volume(self.Volume_sons / 8)
            self.Carro_parado.play()
        elif -10 <= self.velocidade <= 10:
            self.Carro_parado.set_volume(self.Volume_sons / 7)
            self.Carro_parado.play()
        elif -30 <= self.velocidade <= 30:
            self.Carro_parado.set_volume(self.Volume_sons / 5)
            self.Carro_parado.play()
        else:
            self.Carro_parado.set_volume(self.Volume_sons / 3)
            self.Carro_parado.play()

        #Reseta posicao do carro
        if (key[K_SPACE] and self.movimenta) or ((self.rect[2], self.rect[3]) == (0, 0)) or self.colid_movimento:
            self.Resetar_carro()
            self.colid_movimento = False

        #Girar a imagem do carro na angulacao correta e obter um retangulo da imagem do carro principal
        self.image =  pygame.transform.rotozoom(self.original[self.Cor_carro], self.angle * -1 , 1.).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center = (self.virtual_x, self.virtual_y))

        #Faz um "backup" das variaveis de movimento pra quando o carro bater voltar pra tais posicoes
        if contador_backup == 8:
            self.backup_x = self.virtual_x
            self.backup_y = self.virtual_y
            self.backup_angle = self.angle
            contador_backup = 0 

    #Responsavel por resetar o carro
    def Resetar_carro(self):
        self.virtual_x = cenario.Fases["Fase_" + str(Numero_fase)]["Virtual_x"]
        self.virtual_y = cenario.Fases["Fase_" + str(Numero_fase)]["Virtual_y"]
        self.angle = cenario.Fases["Fase_" + str(Numero_fase)]["Angulo_inicial"]
        self.velocidade = cenario.Fases["Fase_" + str(Numero_fase)]["Velocidade_inicial"]
     
    #Efeito colisao real                       
    def Colidir_carro(self):
        global contador_backup, Numero_fase
        #SOM
        pygame.mixer.stop()
        if self.Volume_sons > .0: self.Carro_colide.set_volume(0.1)
        else: self.Carro_colide.set_volume(0.1)
        self.Carro_colide.play()
        self.virtual_x, self.virtual_y = self.backup_x, self.backup_y
        self.angle = self.backup_angle
        self.Dano_carro += abs(self.velocidade) * 4 
        self.Dano_fase += abs(self.velocidade) * 4
        self.velocidade = 0
        if self.Dano_carro >= 900:
            Numero_fase = 10
            self.Dano_carro = 0

    #impossibilitar carro de realizar movimentos
    def Travar_carro(self):
        self.velocidade = 0
        self.velocidadex = 0
        self.velocidadey = 0
        self.Carro_parado.stop()

    #Responsavel por mostrar todos os itens na tela e fazer com que eles interajam entre si
    def draw(self, screen, camera, event, loop = True):
    
        if loop:
            #Salvar jogo
            self.Escrever_dados()

            #Cria tempo em segundos
            self.tempo_y = time.time()

            self.tempo_y = self.tempo_y - self.tempo_pausa_2
            self.tempo = self.tempo_y - self.tempo_x

            #Cores
            branco, preto = (255, 255, 255), (0, 0, 0)
    
            #Desenha a imagem da vaga na tela
            Vaga_x = cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_vaga"][0]
            Vaga_y = cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_vaga"][1]
            Vaga_angulo = cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_vaga"][2]
            self.Vaga = screen.blit(pygame.transform.rotate(self.Vaga_imagem, Vaga_angulo),                                                          (-camera.x + Vaga_x, -camera.y + Vaga_y))

            #Desenha a imagem do carro na tela
            self.rect = screen.blit(self.image, self.rect.move(-camera.x + 255 , -camera.y - 126))

            #Dicionario com as coordenadas do local dos carros da fase 
            Dic_fases = cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_carros"]

            #Lista com as informacoes dos carros do cenario
            Lista_carros = [] 

            #Carrega imagens dos carros e define os retangulo do mesmos
            x = 0
            for img in range(len(Dic_fases)):

                Carro_angulo = Dic_fases[x][2]
                Lista_carros.append(pygame.transform.rotozoom(cenario.Lista_carros[x].convert(), Carro_angulo, 1.).convert())
                x += 1
            
            #Cria uma mascara do carro principal apenas com os devidos pixels para colisao
            Lista_colorkey = [imagem.set_colorkey(preto) for imagem in Lista_carros]
            Lista_rect_carros = [retangulo.get_rect() for retangulo in Lista_carros]
            Lista_mask_carros = [pygame.mask.from_surface(carro) for carro in Lista_carros]        
    
            #Armazena os pontos principais dos carros e cria uma mascara de cada carro
            for Coord in range(len(Dic_fases)):
                if Coord >= len(Lista_carros):
                    Coord -= (Coord / 2)
                pos_1 = Dic_fases[Coord][0]
                pos_2 = Dic_fases[Coord][1]
                self.image_mask = pygame.mask.from_surface(self.image)
                self.rect.topleft = (self.rect[0], self.rect[1])
                Lista_rect_carros[Coord] = screen.blit(Lista_carros[Coord], (-camera.x + pos_1, -camera.y + pos_2))
                Lista_rect_carros[Coord].topleft = (-camera.x + pos_1, -camera.y + pos_2)
                carros_mask = Lista_mask_carros[Coord]
                ofset_x, ofset_y = (Lista_rect_carros[Coord].left - self.rect.left), (Lista_rect_carros[Coord].top - self.rect.top)

#--------------------------------------POSSIVEL FUNCAO------------------------------------------------------------------------------------
                #Verifica se o carro do cenario vai se movimentar na tela
                try:
                    pos_carro = cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_carros"][Coord][0]
                    tamanho_mapa = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_mapa"][0]

                    if Dic_fases[Coord][3]:

                        if (self.image_mask.overlap(Lista_mask_carros[Coord],(ofset_x, ofset_y)) != None) and self.colidir:
                            self.colid_movimento = True
                        else:
                            cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_carros"][Coord][0] += 8
                        if pos_carro > tamanho_mapa:
                            
                            cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_carros"][Coord][0] = -500

                    else:
                        if (self.image_mask.overlap(Lista_mask_carros[Coord],(ofset_x, ofset_y)) != None) and self.colidir:
                            self.colid_movimento = True
                        else:
                            cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_carros"][Coord][0] -= 8

                        if pos_carro < -200:
                            cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_carros"][Coord][0] =  tamanho_mapa + 200
                except: pass
                       
                #Verifica se existe colisao entre as mascaras(carros)
                if (self.image_mask.overlap(Lista_mask_carros[Coord],(ofset_x, ofset_y)) != None) and self.colidir:
                    self.Colidir_carro()   
                    self.colidir = False
                    

            #Verifica se a fase contem barreiras, caso exista: blita e cria colisao
            try:
                #Dicionario com as coordenadas do local das barreiras da fase 
                Dic_barreira = cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_barreira"]
    
                #Carrega imagens das barreiras e define os retangulo do mesmos
                Lista_barreira = []
                x = 0
                for img in range(len(Dic_barreira)):
                    Barreira_angulo = Dic_barreira[x][2]
                    Lista_barreira.append(cenario.Fases["Fase_" + str(Numero_fase)]["Imagem_barreira"][x].convert())
                    x += 1
                Lista_colorkey = [imagem.set_colorkey(preto) for imagem in Lista_barreira]
                Lista_rect_barreira = [retangulo.get_rect() for retangulo in Lista_barreira]
                Lista_mask_barreira = [pygame.mask.from_surface(barmask) for barmask in Lista_barreira]  
    
    
                for Coord in range(len(Dic_barreira)):
    
                    if Coord >= len(Lista_barreira):
                        Coord -= (Coord / 2)
                    pos_1 = Dic_barreira[Coord][0]
                    pos_2 = Dic_barreira[Coord][1]
                    self.image_mask = pygame.mask.from_surface(self.image)
                    self.rect.topleft = (self.rect[0], self.rect[1])
        
                    Lista_rect_barreira[Coord] = screen.blit(Lista_barreira[Coord], (-camera.x + pos_1, -camera.y + pos_2))
                    Lista_rect_barreira[Coord].topleft = (-camera.x + pos_1, -camera.y + pos_2)
                    Barreira_mask = Lista_mask_barreira[Coord]
    
                    ofset_x, ofset_y = (Lista_rect_barreira[Coord].left - self.rect.left),                                                            (Lista_rect_barreira[Coord].top - self.rect.top)

                    #verifica se existe colisao entre o carro principal e as barreiras
                    if (self.image_mask.overlap(Lista_mask_barreira[Coord], (ofset_x, ofset_y)) != None) and self.colidir:
                        self.Colidir_carro()   
                        self.colidir = False
     
            except: pass
#-----------------------------------------------------------------------------------------------------------------------------------------


            #Verifica se na fase existe ambientacao, caso exista: blita imagen
            try:
                Arvores = cenario.Fases["Fase_" + str(Numero_fase)]["Ambientacao"]
                Pos_arvores = cenario.Fases["Fase_" + str(Numero_fase)]["Posicao_ambientacao"]
                for arv in range(len(Pos_arvores)):
                 
                    screen.blit(pygame.transform.rotozoom(Arvores[0].convert_alpha(), Pos_arvores[arv][2], 1.),                                                                      (-camera.x + Pos_arvores[arv][0], -camera.y + Pos_arvores[arv][1]))
            except: pass

            #Quando o carro estiver sobre a vaga: passa de fase
            if self.Vaga.contains(self.rect) or Numero_fase == 10:
                self.Travar_carro()
                loop = self.Finalizar_nivel(screen, camera, event)
            return not(loop), loop

    #Pausar jogo
    def Pausar_jogo(self, screen, Tela_pausa, Pausa_img):
        while Tela_pausa[0]:
            self.tempo_pausa = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        Tela_pausa[0] = False

            self.tempo_pausa_2 = self.tempo_pausa - self.tempo_y

                       

    #Responsavel por por na tela imagem do dano e do tempo
    def Botoes_jogo(self, screen, camera):
        screen.blit(self.Dano.convert_alpha(), (545  , 542))
        screen.blit(self.Barra_dano, (600, 550))
        self.Lista_preenchimendo = [not(bool(x)) for x in range(1, 31)]
        x = 605
        for barra in range(1, 31):
            if barra <= self.Dano_carro/30:
                screen.blit(self.Preenchimento_barra, (x, 550))
                x += 5
        Fonte = pygame.font.Font(diretorio_imagens + "Font/AbyssinicaSIL-R.ttf", 30)
        Tempo = Fonte.render("Tempo: %.3f" %self.tempo, 1, (0, 0, 0))
        Pontos = Fonte.render("P$%.2f" %self.Total_pontos, 1, (0, 0, 0))
        screen.blit(Tempo, (315, 540))
        screen.blit(Pontos, (150, 540))
    
    #Tela de finalizacao de nivel
    def Finalizar_nivel(self, screen, camera, event):
        global Numero_fase
        if self.movimenta:
            self.Pontuacao_fase = self.Pontuacao_inicial - (int(self.tempo * 10)  + self.Dano_fase)
            if self.Pontuacao_fase > 0:
                self.Lista_pontuacao.append((self.tempo, self.Dano_fase, self.Pontuacao_fase))
            else:
                self.Lista_pontuacao.append((self.tempo, self.Dano_fase, 0))
            self.Total_tempo += self.tempo
            self.Total_dano += self.Dano_fase
            self.Total_pontos += self.Pontuacao_fase
            self.Dano_fase = 0
        self.tempo_x = self.tempo_y
        self.movimenta = False
        Proximo = [(470, 400, 163, 30), pygame.image.load(diretorio_imagens + "Interacao/Proximo_MOFF.png"),                                                                      pygame.image.load(diretorio_imagens + "Interacao/Proximo_MON.png")]
        Fonte = pygame.font.Font(diretorio_imagens + "Font/AbyssinicaSIL-R.ttf", 40)
        Transparencia = screen.blit(pygame.image.load(diretorio_imagens + "Interacao/Transparencia_menu.png"),(0, 0))
        if Numero_fase <= 9:
            Transparencia 
            Nivel_finalizado = Fonte.render("Nivel Finalizado", 1, (115, 115, 115))
    
            i = len(self.Lista_pontuacao) - 1

            Print_nometempo = Fonte.render("Tempo: ", 1, (115, 115, 115))
            Print_nomedano = Fonte.render("Dano: ", 1, (115, 115, 115))
            Print_nomepontuacao = Fonte.render("Pontuacao: ", 1, (115, 115, 115))

            Print_tempo = Fonte.render("%.3f" %(self.Lista_pontuacao[i][0]), 1, (115, 115, 115))
            Print_dano = Fonte.render(str(self.Lista_pontuacao[i][1]), 1, (115, 115, 115))
            Print_pontuacao = Fonte.render(str(self.Lista_pontuacao[i][2]), 1, (115, 115, 115))
        
            screen.blit(Nivel_finalizado, (230, 170))    
                
            screen.blit(Print_tempo, (350, 250))
            screen.blit(Print_dano, (310, 300))
            screen.blit(Print_pontuacao, (410, 350))

            screen.blit(Print_nometempo, (200, 250))
            screen.blit(Print_nomedano, (200, 300))
            screen.blit(Print_nomepontuacao, (200, 350))

        
            if Rect(Proximo[0]).collidepoint(pygame.mouse.get_pos()):
                
                screen.blit(Proximo[2], (Proximo[0][0], Proximo[0][1]))
                if pygame.mouse.get_pressed()[0] and event.type == 5:
                    pygame.mouse.set_pos((0, 0))
                    Numero_fase += 1
                    self.virtual_x = cenario.Fases["Fase_" + str(Numero_fase)]["Virtual_x"]
                    self.virtual_y = cenario.Fases["Fase_" + str(Numero_fase)]["Virtual_y"]
                    self.angle = cenario.Fases["Fase_" + str(Numero_fase)]["Angulo_inicial"]
                    self.velocidade = cenario.Fases["Fase_" + str(Numero_fase)]["Velocidade_inicial"] 
                    self.movimenta = True
    
            else:
                screen.blit(Proximo[1], (Proximo[0][0], Proximo[0][1]))

        #Se nou houver mais fases mostra a tela de Game_over
        else:

            Game_data.Game_data_write(1, 0, 0, 0, 2, 0) 
            Transparencia
            Pontuacao_total = abs(self.Total_pontos - self.Pontuacao_fase) 
            Print_fimdejogo = Fonte.render("FIM DE JOGO", 1, (115, 115, 115))
            Print_nometempo = Fonte.render("Tempo total: ", 1, (115, 115, 115))
            Print_nomedano = Fonte.render("Dano total: ", 1, (115, 115, 115))
            Print_nomepontuacao = Fonte.render("Pontuacao total: ", 1, (115, 115, 115))

            Print_tempo = Fonte.render("%.3f" %(self.Total_tempo), 1, (115, 115, 115))
            Print_dano = Fonte.render(str(self.Total_dano), 1, (115, 115, 115))
            Print_pontuacao = Fonte.render(str(Pontuacao_total), 1, (115, 115, 115))
            
            screen.blit(Print_fimdejogo, (280, 170))

            screen.blit(Print_tempo, (440, 250))
            screen.blit(Print_dano, (410, 300))
            screen.blit(Print_pontuacao, (500, 350))

            screen.blit(Print_nometempo, (200, 250))
            screen.blit(Print_nomedano, (200, 300))
            screen.blit(Print_nomepontuacao, (200, 350))

            self.virtual_x, self.virtual_y =  9000, 9000
            if Rect(Proximo[0]).collidepoint(pygame.mouse.get_pos()):
                
                screen.blit(Proximo[2], (Proximo[0][0], Proximo[0][1]))
                if pygame.mouse.get_pressed()[0] and event.type == 5:

                    pygame.mouse.set_pos((0, 0))
                    if Pontuacao_total > 0 and (Pontuacao_total > ranking.Ultimo_colocado()[1] or ranking.Ultimo_colocado()[0] < 10):
                        Nome = ranking.Inserir_nome(screen, Fonte)
                        if Nome:
                            ranking.Inserir_recorde(Nome, Pontuacao_total)
    
                    return False 
            else:
                screen.blit(Proximo[1], (Proximo[0][0], Proximo[0][1]))

        return True 


#Loop principal do jogo
class Jogo: 

    global Numero_fase

    #Carregar os sons dos botoes
    def __init__(self):
        self.Botao_menu = [(20, 530, 40, 40), pygame.image.load(diretorio_imagens + "Interacao/Pause_MOFF.png"),
                                          pygame.image.load(diretorio_imagens + "Interacao/Pause_MON.png")]
        self.Botao_loja = [(90, 538, 40, 40), pygame.image.load(diretorio_imagens + "Botoes/Compras_MOFF.png"),
                                          pygame.image.load(diretorio_imagens + "Botoes/Compras_MON.png")]

        self.Som_mouse = [None]
        self.Reproduzir = [True]

    #Interagir com o menu informando a fase atual
    def Obter_nivel(self):
        return Game_data.Game_data_read()[0]
        #return Numero_fase

    #Definir a fase
    def Definir_nivel(self, fase):
        global Numero_fase
        Numero_fase = fase
       
    #Rodar o jogo
    def Iniciar(self,Tela_menu, Tela_jogo, Tela_cheia_on, game_data, Volume):

        Pausa_img = pygame.image.load(diretorio_imagens + "Interacao/Transparencia_pausa.png")
        pygame.mixer.music.load("Botoes_menu/Sons/Som_jogo.wav"),
        Sons_jogo = [pygame.mixer.Sound(DA + "Botoes_menu/Sons/Mouse_ON.wav"), 
                     pygame.mixer.Sound(DA + "Botoes_menu/Sons/Mouse_click.wav")]
        Sons_jogo[0].set_volume(Volume)
        Sons_jogo[1].set_volume(Volume)
        if Volume > .1: pygame.mixer.music.set_volume(.1)
        else: pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play(-1)
        carro = Carro(Game_data.Game_data_read()) 
        Numero_fase = Game_data.Game_data_read()[0]
        pygame.init()
        Tamanho_tela_x = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_tela"][0]
        Tamanho_tela_y = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_tela"][1]

        clock = pygame.time.Clock()
        Tela_pausa = [False]

        #Tela_cheia ON/OFF 
        if Tela_cheia_on:
            
            screen= pygame.display.set_mode((Tamanho_tela_x, Tamanho_tela_y), FULLSCREEN|HWSURFACE|DOUBLEBUF)
        else:
            screen= pygame.display.set_mode((Tamanho_tela_x, Tamanho_tela_y), HWSURFACE|DOUBLEBUF)

     
     

        while True:
            
            carro.Volume_sons = Volume
            Numero_fase = Game_data.Game_data_read()[0]

            Tamanho_mapa_x = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_mapa"][0]
            Tamanho_mapa_y = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_mapa"][1]
            Tamanho_tela_x = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_tela"][0]
            Tamanho_tela_y = cenario.Fases["Fase_" + str(Numero_fase)]["Tamanho_tela"][1]

            clock.tick_busy_loop(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                             
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Tela_pausa[0] = True



            camera = Camera(0, 0, Tamanho_mapa_x - Tamanho_tela_x, Tamanho_mapa_y - Tamanho_tela_y)
            pygame.display.set_caption(str(clock.get_fps()))
            background = cenario.Fases["Fase_" + str(Numero_fase)]["Imagem_fase"].convert()
            pygame.event.pump()
            key = list(pygame.key.get_pressed())
            carro.Movimentacao(key)
            camera.center_on(carro.virtual_x, carro.virtual_y)
            screen.blit(background, (-camera.x, -camera.y))
            
            #Mostra Cenario do jogo
            if Tela_jogo:
                Tela_menu, Tela_jogo = carro.draw(screen, camera, event)
                carro.Botoes_jogo(screen, camera)
                #mouse.Possibilidade_click(Sons_jogo, self.Som_mouse, self.Reproduzir, Volume)
            if mouse.Verifica_click(screen, event, self.Botao_menu)[1] and Numero_fase != 10:
                pygame.mixer.stop()
                Tela_menu = True
                Tela_jogo = False

            #Mostra cenario da loja
            if mouse.Verifica_click(screen, event, self.Botao_loja)[1] and Numero_fase != 10:
                pygame.mixer.stop()
                carro.Altera_itens_loja(loja.Menu_loja(screen, event, carro.Itens_loja()))

            #Mostra tela de pausa
            if Tela_pausa[0]:
                screen.blit(Pausa_img, (0, 0))
                pygame.display.flip() 
                carro.Pausar_jogo(screen, Tela_pausa, Pausa_img)


            #Volta pro menu
            if Tela_menu:
                pygame.mixer.music.stop()
                return Tela_menu, Tela_jogo

            #Salvar jogo, Atualizar tela

            carro.Escrever_dados()
            pygame.display.flip()
            screen.fill(0)
            clock.tick(60)

