import forca
import adivinhaco

print('**********************************')
print('****Escolha o Jogo****************')
print('**********************************')

print('(1) Forca (2) Adivinhação')

jogo = int(input('Qual o jogo? '))

if (jogo == 1):
    print('Jogando Forca')
    forca.jogar()


elif (jogo == 2):
    print('Jogando Adivinhação')
    adivinhaco.jogar()

