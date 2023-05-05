import pygame


class Wall1:
    def __init__(self, xy):
        self.image = pygame.Surface((100, 30))
        self.image.fill('cyan')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class Wall2(Wall1):
    def __init__(self, xy):
        Wall1.__init__(self, xy)
        self.image = pygame.Surface((30, 100))
        self.image.fill('cyan')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class SlowFlor1(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class SlowFlor2(SlowFlor1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 100))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class SpeedFlor1(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class SpeedFlor2(SpeedFlor1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 100))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class MobileWall1(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class MobileWall2(MobileWall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 100))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class FinishFlor1(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('Finish_line.png'), (100, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class FinishFlor2(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Finish_line.png'),
                                                                    (100, 40)), 90)
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class Money(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


def update_sprites():
    pass