import pygame


def draw(screen, now_block, mouse_pose):
    if now_block == '1':
        surfase = pygame.Surface((100, 30))
        surfase.fill('cyan')
    if now_block == '2':
        surfase = pygame.Surface((30, 100))
        surfase.fill('cyan')
    if now_block == '3':
        surfase = pygame.Surface((100, 30))
        surfase.fill('red')
    if now_block == '4':
        surfase = pygame.Surface((30, 100))
        surfase.fill('red')
    if now_block == '5':
        surfase = pygame.Surface((100, 30))
        surfase.fill('green')
    if now_block == '6':
        surfase = pygame.Surface((30, 100))
        surfase.fill('green')
    if now_block == '7':
        surfase = pygame.Surface((100, 30))
        surfase.fill('gray')
    if now_block == '8':
        surfase = pygame.Surface((30, 100))
        surfase.fill('gray')
    if now_block == '9':
        surfase = pygame.transform.scale(pygame.image.load('GameFiles\Finish_line.png'), (100, 40))
    if now_block == '0':
        surfase = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('GameFiles\Finish_line.png'),
                                                                 (100, 40)), 90)
    elif now_block == 'money':
        surfase = pygame.Surface((15, 15))
        surfase.fill('yellow')
    surfase.get_rect().center = (mouse_pose[0], mouse_pose[1])
    surfase.set_alpha(150)
    screen.blit(surfase, mouse_pose)
