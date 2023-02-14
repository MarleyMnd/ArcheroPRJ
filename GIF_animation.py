import pygame
import sys


# Flower class
class Flower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.sprites = []

        self.sprites.append(pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower0.png").convert_alpha())
        self.sprites.append(pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower1.png").convert_alpha())

        self.actual_sprite = 0
        self.image = self.sprites[self.actual_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use 0.02 to slow down the animation because of the int casting at
        # line 30 will round it to the next integer -> 0.02 rounded to 1, 0.04 rounded to 1 etc.)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites[int(self.actual_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Screen/Window parameter
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flower GIF animation")


# Creating sprites and groups
moving_sprites = pygame.sprite.Group()
flower = Flower(425, 270)
moving_sprites.add(flower)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # We need to draw the elements:
    screen.fill((214, 159, 126))
    moving_sprites.draw(screen)
    moving_sprites.update(0.02)
    pygame.display.flip()
    clock.tick(60)
