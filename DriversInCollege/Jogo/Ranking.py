import pygame, sys
from pygame.locals import *

class Menu_ranking:
    def __init__(self, diretorio_rank):
        self.diretorio_rank = diretorio_rank

    def Imprime_tela(self, surface):
        self.surface = surface
        Fonte = pygame.font.Font("Font/AbyssinicaSIL-R.ttf", 20)
        Rank = open(self.diretorio_rank + "Ranking/Ranking.txt", "r")
        Rank = Rank.readlines()
        surface.blit(pygame.image.load("Imagens/Menu.png"), (0, 0))
        surface.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0)) 
        surface.blit(pygame.image.load("Imagens/Nome_ranking.png"), (300, 150))   
        Cord_x = 250
        Cord_y = 200        
        for colocado in range(len(Rank)):
            if colocado % 2 == 0:
                Rank_print = Fonte.render("%d - %s%s" %(colocado/2 + 1, Rank[colocado], "-" * (20 - len(Rank[colocado]))), 1, (80, 80, 80))
                Cord_y += 30
            else:

                Rank_print = Fonte.render(Rank[colocado], 1, (80, 80, 80))
                Cord_x += 250
            surface.blit(Rank_print, (Cord_x, Cord_y))
            Cord_x = 250
            self.ultimo_colocado = colocado


    def Ultimo_colocado(self):
        Rank = open(self.diretorio_rank + "Ranking/Ranking.txt", "r")
        Rank = Rank.readlines()
        if len(Rank) > 0:
            return len(Rank), int(Rank[-1])
        else:
            return len(Rank), 0

    def Inserir_recorde(self, Nome, Pontuacao):
        Ranking = open(self.diretorio_rank + "Ranking/Ranking.txt", "r")
        Linhas_ranking = Ranking.readlines()
        for pontos in range(1, 11, 2):
            try:
                if Pontuacao > int(Linhas_ranking[pontos]):
                    if len(Linhas_ranking) < 10:
                        Linhas_ranking.insert(pontos - 1, Nome + "\n" + str(Pontuacao) + "\n")
                        Ranking = open(self.diretorio_rank + "Ranking/Ranking.txt", "w")
                        Ranking.writelines(Linhas_ranking)
                        Ranking.close()
                        break
                    else:
                        Linhas_ranking.insert(pontos - 1, Nome + "\n" + str(Pontuacao) + "\n")
                        Linhas_ranking.pop(-1)
                        Linhas_ranking.pop(-1)
                        Ranking = open(self.diretorio_rank + "Ranking/Ranking.txt", "w")
                        Ranking.writelines(Linhas_ranking)
                        Ranking.close()
                        break
                elif pontos == 9 and len(Linhas_ranking) < 10:
                    Linhas_ranking.append(Nome + "\n" + str(Pontuacao) + "\n") 
                    Ranking = open(self.diretorio_rank + "Ranking/Ranking.txt", "w")
                    Ranking.writelines(Linhas_ranking)
                    Ranking.close()
                    break
            except:
                Linhas_ranking.append(Nome + "\n" + str(Pontuacao) + "\n") 
                Ranking = open(self.diretorio_rank + "Ranking/Ranking.txt", "w")
                Ranking.writelines(Linhas_ranking)
                Ranking.close()
                break
    

    def Inserir_nome(self, screen, Fonte):
        Submeter = [(500, 400, 130, 30), pygame.image.load(self.diretorio_rank + "Ranking/Submeter_MON.png"),
                        pygame.image.load(self.diretorio_rank + "Ranking/Submeter_MOFF.png")]

        Cancelar = [(160, 400, 130, 30), pygame.image.load(self.diretorio_rank + "Ranking/Cancelar_MON.png"),
                        pygame.image.load(self.diretorio_rank + "Ranking/Cancelar_MOFF.png")]
        Nome = []
        while True:
            
            screen.blit(pygame.image.load("Imagens/Menu.png"), (0, 0)) 
            screen.blit(pygame.image.load("Imagens/Transparencia_nome.png"), (0, 0)) 
            #screen.blit(pygame.image.load(diretorio), (0, 0))

            Digite_nome = Fonte.render("Digite seu nome:", 1, (115, 115, 115))
            screen.blit(Digite_nome, (250, 200))

            Imprime_nome = Fonte.render("".join(Nome), 1, (115, 115, 115))
            screen.blit(Imprime_nome, (260, 280))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if len(Nome) < 12:
                        if 97 <= event.key <= 122:
                            Letra = pygame.key.name(event.key)
                            Nome += Letra
                        elif event.key == 32:
                            Nome.append(" ")
                    if event.key == 8 and len(Nome) > 0:
                        Nome.pop()
                    if event.key == 13:
                        return "".join(Nome)
            if Rect(Submeter[0]).collidepoint(pygame.mouse.get_pos()) and len(Nome) > 0:
                screen.blit(Submeter[1], (Submeter[0][0], Submeter[0][1]))
                if pygame.mouse.get_pressed()[0] and event.type == 5:
                    return "".join(Nome)
            else:
                if len(Nome) > 0:
                    screen.blit(Submeter[2], (Submeter[0][0], Submeter[0][1]))
            if Rect(Cancelar[0]).collidepoint(pygame.mouse.get_pos()):
                screen.blit(Cancelar[1], (Cancelar[0][0], Cancelar[0][1]))
                if pygame.mouse.get_pressed()[0]:
                    return False
            else:
                screen.blit(Cancelar[2], (Cancelar[0][0], Cancelar[0][1]))


            pygame.display.update()
                
    def Reset_ranking(self):
        Ranking = open(self.diretorio_rank + "Ranking/Ranking.txt", "w")
        Ranking.writelines([])
        Ranking.close()
