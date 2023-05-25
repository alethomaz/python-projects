import random


def jogar():

    imprimir_mensagem()
    palavra_secreta = pegando_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
 
    # enquanto não False e nao False:
    # enquanto True e True:
    # enquanto True
    while not enforcou and not acertou:
        print('jogando...')

        chute = input('Qual a letra? ').upper().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    print(f'Encontrei a letra {chute} na posição {index}')
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            print(f'Você pode errar somente mais {7 - erros} vezes')
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)
    if acertou:
        print('Você ganhou!!')
        imprime_mensagem_vencedor()
    else:
        print('Você perdeu!')
        imprime_mensagem_perdedor(palavra_secreta)
    print('Fim de jogo!')

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprimir_mensagem():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def pegando_palavra_secreta():

    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()

if __name__ == "__main__":
    # Para diferenciar um arquivo de executado e importado
    jogar()
