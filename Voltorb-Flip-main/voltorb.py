from pygame import display, mixer, image, sprite
from game_tile import Tile
import pygame, levels

pygame.init()
# mixer.init()
# mixer.music.load(r"SFX\Raging Loop chime song.wav")



SCREEN_WIDTH = 790
SCREEN_HEIGHT = 590

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((82,162,111))

tiles = levels.convert_to_sprite(levels.set_board(3, 1, 6))

tiles.draw(screen)

# mixer.music.play(loops = -1, start=0.0, fade_ms=0)

# test_tile = Tile(0, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


# tiles = sprite.Group(test_tile)

tiles.draw(screen)

# test_tile.initTile(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# voltorb_tile = image.load(r"Assets\voltorb flip tile.png").convert()
# screen.blit(voltorb_tile, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
display.flip()



running = True

while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # get a list of all sprites that are under the mouse cursor

            for sprites in tiles:
                clicked_sprite = sprites.rect.collidepoint(pos)
                if clicked_sprite:
                    sprites.flip_tile(screen, display)

    