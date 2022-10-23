import pygame
# pygame é um biblioteca para criação de games em python

print('===Desafio 021===')
pygame.init()  # iniciar(init)
pygame.mixer.music.load('Oceano.mp3')  # carregar musica importada
pygame.mixer.music.play()  # tocar musica escolhida
pygame.event.wait()  # pausar a musica


