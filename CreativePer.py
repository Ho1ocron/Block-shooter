import pygame


def type_block(event):
    if event.key == pygame.K_1:
        return '1'
    if event.key == pygame.K_2:
        return '2'
    if event.key == pygame.K_3:
        return '3'
    if event.key == pygame.K_4:
        return '4'
    if event.key == pygame.K_5:
        return '5'
    if event.key == pygame.K_6:
        return '6'
    if event.key == pygame.K_7:
        return '7'
    if event.key == pygame.K_8:
        return '8'
    if event.key == pygame.K_9:
        return '9'
    if event.key == pygame.K_0:
        return '0'
    if event.key == pygame.K_q:
        return 'money'
