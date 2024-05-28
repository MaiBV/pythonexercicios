import pygame
import time

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Wait for a few seconds before exiting
time.sleep(10)

pygame.quit()
