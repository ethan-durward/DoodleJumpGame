import pygame, random

class GameObject(pygame.sprite.Sprite):
    def __init__(self,x,y,img_path):
        super().__init()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        self.rect = self.rect.move(self.rand_xd*self.speed, self.rand_yd*self.speed)


class StationaryPlatform:
    def __init__(self, screen_rect):
        rand_x = random.randint(100, screen_rect.width)
        rand_y = random.randint(100,screen_rect.width)
        super().__init__(rand_x, rand_y, "stationary_platform.png")

class MovingPlatform:
    def __init__(self, screen_rect):
        rand_x = random.randint(100, screen_rect.width)
        rand_y = random.randint(100,screen_rect.width)
        super().__init__(rand_x, rand_y, "moving_platform.png")
        self.speed = 2

class Character:
    def __init__(self, screen_rect):
        super().__init__(screen_rect.centerx, screen_rect.centery, "character.png")
        self.speed = 5
        self.acceleration = 2
