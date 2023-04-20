from pygame import display, mixer, image, mouse
import pygame

pygame.init()
mixer.init()
mixer.music.load(r"SFX\Raging Loop chime song.wav")


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((82,162,111))

mixer.music.play(loops = -1, start=0.0, fade_ms=0)

voltorb_tile = image.load(r"Assets\voltorb flip tile.png").convert()
screen.blit(voltorb_tile, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

display.flip()


running = True

while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            display.flip

    