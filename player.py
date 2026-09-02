#Alana Melo Costa Diniz
#Gabrielly Emanuelly Pereira Dias

import pygame

pygame.mixer.init()

fila = []
pilha = []
tocando_agora = "Nenhuma"

def ver_biblioteca():
    with open("Biblioteca.txt", "r") as biblioteca:
        i = 1
        for linha in biblioteca:
            nome, mp3  = (linha.strip().split(" \ "))
            print(i, nome)
            i += 1

    print(" ")


def adicionar_na_fila(musica):
        with open("Biblioteca.txt", "r") as biblioteca:
            linhas = biblioteca.readlines()
            
            if musica == 0 or musica > len(linhas):
                print("Número de música invalido")

            else:
                nome, mp3 = linhas[musica-1].strip().split(" \ ")
                fila.append((nome, mp3))

def ver_fila():
    if fila:
        for i in range(len(fila)):
            print(fila[i][0])

    else:
        print("A fila de musicas está vazia...")

    print(" ")

def tocar_proxima():
    global tocando_agora

    if fila:
        if tocando_agora != "Nenhuma":
            pilha.append(tocando_agora)

        tocando_agora = fila.pop(0)
        pygame.mixer.music.stop()
        pygame.mixer.music.load(tocando_agora[1])
        pygame.mixer.music.play()

    else:
        print("A fila de musica está vazia...")
        if tocando_agora != "Nenhuma":
                pilha.append(tocando_agora)
                tocando_agora = "Nenhuma"
                pygame.mixer.music.stop()

    

def voltar():
    global tocando_agora
    if pilha:
        tocando_agora = pilha.pop()
        pygame.mixer.music.load(tocando_agora[1])
        pygame.mixer.music.play()

    else:
        print("O historico está vazio...")
        if tocando_agora != "Nenhuma":
                tocando_agora = "Nenhuma"
                pygame.mixer.music.stop()

def ver_historico():
    if pilha:
        for i in range(len(pilha)):
            print(pilha[i][0])

    else:
        print("O historico está vazio...")

    print(" ")

opcao = -1

while opcao != 0:
    with open("Constantes.txt", "r") as menu:
        print(menu.readline().strip())
        if tocando_agora == "Nenhuma":
            print(menu.readline().strip(), tocando_agora)
        else:
            print(menu.readline().strip(), tocando_agora[0])

        for linha in menu:
            print(linha.strip())

        opcao = int(input())

        if opcao == 1:
            ver_biblioteca()

        elif opcao == 2:
            ver_biblioteca()
            n = int(input('Digite o número da música:'))
            adicionar_na_fila(n)

        elif opcao == 3:
            ver_fila()

        elif opcao == 4:
            tocar_proxima()

        elif opcao == 5:
            voltar()

        elif opcao == 6:
            ver_historico()