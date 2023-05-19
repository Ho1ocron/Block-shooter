import pygame


def draw(screen, now_block, mouse_pose):
    if now_block == '1':
        surfase = pygame.Surface((100, 30))
        mouse_pose = (mouse_pose[0] - 50, mouse_pose[1] - 15)
        surfase.fill('cyan')
    if now_block == '2':
        surfase = pygame.Surface((30, 100))
        mouse_pose = (mouse_pose[0] - 15, mouse_pose[1] - 50)
        surfase.fill('cyan')
    if now_block == '3':
        surfase = pygame.Surface((100, 30))
        mouse_pose = (mouse_pose[0] - 50, mouse_pose[1] - 15)
        surfase.fill('red')
    if now_block == '4':
        surfase = pygame.Surface((30, 100))
        mouse_pose = (mouse_pose[0] - 15, mouse_pose[1] - 50)
        surfase.fill('red')
    if now_block == '5':
        surfase = pygame.Surface((100, 30))
        mouse_pose = (mouse_pose[0] - 50, mouse_pose[1] - 15)
        surfase.fill('green')
    if now_block == '6':
        surfase = pygame.Surface((30, 100))
        mouse_pose = (mouse_pose[0] - 15, mouse_pose[1] - 50)
        surfase.fill('green')
    if now_block == '7':
        surfase = pygame.Surface((100, 30))
        mouse_pose = (mouse_pose[0] - 50, mouse_pose[1]-+ 15)
        surfase.fill('gray')
    if now_block == '8':
        surfase = pygame.Surface((30, 100))
        mouse_pose = (mouse_pose[0] - 15, mouse_pose[1] - 50)
        surfase.fill('gray')
    if now_block == '9':
        mouse_pose = (mouse_pose[0] - 50, mouse_pose[1] - 20)
        surfase = pygame.transform.scale(pygame.image.load('GameFiles\Finish_line.png'), (100, 40))
    if now_block == '0':
        mouse_pose = (mouse_pose[0] - 20, mouse_pose[1] - 50)
        surfase = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('GameFiles\Finish_line.png'),
                                                                 (100, 40)), 90)
    elif now_block == 'money':
        mouse_pose = (mouse_pose[0] - 5, mouse_pose[1] - 5)
        surfase = pygame.Surface((15, 15))
        surfase.fill('yellow')
    surfase.set_alpha(150)
    print(1, now_block)
    screen.blit(surfase, mouse_pose)
