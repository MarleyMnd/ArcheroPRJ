import pygame
import sys


# Flower class
class Flower(pygame.sprite.Sprite):
    """To animate the flower."""

    def __init__(self, pos_x, pos_y):
        """Initialize the array with the flower's sprites."""

        super().__init__()

        self.sprites_flower = []

        # Initialize sprites one by one and put them in the sprites array
        self.sprites_flower.append(pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower0.png").convert_alpha())
        self.sprites_flower.append(pygame.image.load("PNJ/flower/PNJ_flower1/sprite_flower1.png").convert_alpha())

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_flower[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_flower):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_flower[int(self.actual_sprite)]

# Zombie class
class Zombie(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_zombie = []

        # Initialize sprites one by one and put them in the sprites array
        self.sprites_zombie.append(pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie0.png").convert_alpha())
        self.sprites_zombie.append(pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie1.png").convert_alpha())
        self.sprites_zombie.append(pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie2.png").convert_alpha())
        self.sprites_zombie.append(pygame.image.load("PNJ/zombie/zombie_hand/sprite_zombie3.png").convert_alpha())

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_zombie[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_zombie):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_zombie[int(self.actual_sprite)]


# Spider class
class Spider(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_spider = []

        # Initialize sprites one by one and put them in the sprites array
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider00.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider01.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider02.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider03.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider04.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider05.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider06.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider07.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider08.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider09.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider10.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider11.png").convert_alpha())
        self.sprites_spider.append(pygame.image.load("PNJ/spider/spider/sprite_spider12.png").convert_alpha())

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_spider[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_spider):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_spider[int(self.actual_sprite)]


# Bee class
class Bee(pygame.sprite.Sprite):
    """To animate the bee."""
    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_bee = []

        # Initialize sprites one by one and put them in the sprites array
        self.sprites_bee.append(pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee0.png").convert_alpha())
        self.sprites_bee.append(pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee1.png").convert_alpha())
        self.sprites_bee.append(pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee2.png").convert_alpha())
        self.sprites_bee.append(pygame.image.load("PNJ/bee/beep beep the bee/sprite_bee3.png").convert_alpha())

        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_bee[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_bee):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_bee[int(self.actual_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Screen/Window parameter
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flower GIF animation")


# Creating sprites and form a group with them for the FLOWER
moving_sprites_flower = pygame.sprite.Group()
flower = Flower(425, 270)
moving_sprites_flower.add(flower)

# Creating sprites and form a group with them for the ZOMBIE
moving_sprites_zombie = pygame.sprite.Group()
zombie = Zombie(400, -60)
moving_sprites_zombie.add(zombie)

# Creating sprites and form a group with them for the SPIDER
moving_sprites_spider = pygame.sprite.Group()
spider = Spider(800, 50)
moving_sprites_spider.add(spider)

# Creating sprites and form a group with them for the BEE
moving_sprites_bee = pygame.sprite.Group()
bee = Bee(150, 200)
moving_sprites_bee.add(bee)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Shut down the pygame library
            pygame.quit()
            # Exit the program
            sys.exit()

    # We need to draw the elements:
    # - Screen color
    screen.fill((214, 159, 126))

    # - Draw the sprites
    moving_sprites_flower.draw(screen)
    moving_sprites_zombie.draw(screen)
    moving_sprites_spider.draw(screen)
    moving_sprites_bee.draw(screen)

    # - Update the displayed sprites
    moving_sprites_flower.update(0.02)
    moving_sprites_zombie.update(0.05)
    moving_sprites_spider.update(0.15)
    moving_sprites_bee.update(0.5)

    # - Update what is displayed on the screen
    pygame.display.flip()
    clock.tick(60)
