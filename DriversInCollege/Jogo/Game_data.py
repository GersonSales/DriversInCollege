def Game_data_read():
    arquivo = open("Jogo/Game_data.txt", "r")
    arquivos = arquivo.readlines()
    arquivo.close()
    return (int(arquivos[0]), float(arquivos[1]), int(arquivos[2]), int(arquivos[3]), int(arquivos[4]), int(arquivos[5]))
def Game_data_write(fase, tempo, dano, pontos, Cor, Dano_fase):
    arquivo = open("Jogo/Game_data.txt", "w")
    arquivos = arquivo.writelines(["%d\n%f\n%d\n%d\n%d\n%d" %(fase, tempo, dano, pontos, Cor, Dano_fase)])
    arquivo.close()

