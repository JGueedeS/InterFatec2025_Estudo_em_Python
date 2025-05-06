import os
import pygame
pygame.init()
print("Diretório atual:", os.getcwd())
pygame.mixer.music.load('../som.mp3')
pygame.mixer.music.play()
pygame.event.wait()
