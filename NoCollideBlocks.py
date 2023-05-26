import pygame


all_sprites = pygame.sprite.Group()
sprites_to_save = []

class Wall1(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('cyan')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def update(self, xy, delete=False, save=False):
        if delete:
            collision = self.rect.collidepoint(*xy)
            if collision:
                self.kill()
            return
        self.rect.center = (self.rect.center[0] - xy[0], self.rect.center[1] - xy[1])
        if save:
            self.save_map()

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('1', *self.rect.center))


class Wall2(Wall1):
    def __init__(self, xy):
        Wall1.__init__(self, xy)
        self.image = pygame.Surface((30, 100))
        self.image.fill('cyan')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('2', *self.rect.center))


class SlowFlor1(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('3', *self.rect.center))


class SlowFlor2(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 100))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('4', *self.rect.center))


class SpeedFlor1(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('5', *self.rect.center))


class SpeedFlor2(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 100))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('6', *self.rect.center))


class MobileWall1(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('gray')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('7', *self.rect.center))


class MobileWall2(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 100))
        self.image.fill('gray')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('8', *self.rect.center))


class FinishFlor1(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('GameFiles\Finish_line.png'), (100, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('9', *self.rect.center))


class FinishFlor2(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('GamEFiles\Finish_line.png'),
                                                                    (100, 40)), 90)
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('0', *self.rect.center))


class Money(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def save_map(self):
        global sprites_to_save
        sprites_to_save.append(('Money', *self.rect.center))


def load_map(data):
    for i in data:
        type = str(i[1])
        coordinates = (i[2], i[3])
        if type == '1':
            block = Wall1(coordinates)
        elif type == '2':
            block = Wall2(coordinates)
        elif type == '3':
            block = SlowFlor1(coordinates)
        elif type == '4':
            block = SlowFlor2(coordinates)
        elif type == '5':
            block = SpeedFlor1(coordinates)
        elif type == '6':
            block = SpeedFlor2(coordinates)
        elif type == '7':
            block = MobileWall1(coordinates)
        elif type == '8':
            block = MobileWall2(coordinates)
        elif type == '9':
            block = FinishFlor1(coordinates)
        elif type == '0':
            block = FinishFlor2(coordinates)
        else:
            block = Money(coordinates)
        all_sprites.add(block)


def save_map():
    all_sprites.update((0, 0), save=True)
    return sprites_to_save


def create_sprite(coordinates, type):
    if type == '1':
        block = Wall1(coordinates)
    elif type == '2':
        block = Wall2(coordinates)
    elif type == '3':
        block = SlowFlor1(coordinates)
    elif type == '4':
        block = SlowFlor2(coordinates)
    elif type == '5':
        block = SpeedFlor1(coordinates)
    elif type == '6':
        block = SpeedFlor2(coordinates)
    elif type == '7':
        block = MobileWall1(coordinates)
    elif type == '8':
        block = MobileWall2(coordinates)
    elif type == '9':
        block = FinishFlor1(coordinates)
    elif type == '0':
        block = FinishFlor2(coordinates)
    else:
        block = Money(coordinates)
    all_sprites.add(block)


def update_sprites(coordinates):
    all_sprites.update(coordinates)


def draw_sprites(screen):
    all_sprites.draw(screen)


def delete_sprites(coordinates):
    all_sprites.update(coordinates, delete=True)
