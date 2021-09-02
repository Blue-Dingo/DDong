#####################################################################################
# 게임개발 기본 templete
import pygame
from random import *

from pygame.constants import KEYDOWN

# 필수초기화
pygame.init()

# 화면크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption("DDong")

# FPS
clock = pygame.time.Clock()
#####################################################################################


def GetEnemyX():
    return randint(0, background_width-enemy_width)


# 1. 사용자 게임 초기화 (배경, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load(
    "D:\\Documents\\coding\\phthon\\pygame_basic\\background.png")
background_width = background.get_rect().size[0]
background_height = background.get_rect().size[1]

character = pygame.image.load(
    "D:\\Documents\\coding\\phthon\\pygame_basic\\character.png")
character_width = character.get_rect().size[0]
character_height = character.get_rect().size[1]
character_x = background_width/2-character_width/2
character_y = background_height-character_height
character_speed = 1
character_to_x = 0


enemy = pygame.image.load(
    "D:\\Documents\\coding\\phthon\\pygame_basic\\enemy.png")
enemy_width = enemy.get_rect().size[0]
enemy_height = enemy.get_rect().size[1]
enemy_x = GetEnemyX()
enemy_y = 0
enemy_speed = 0.5


# 이벤트 루프
running = True
while running:

    dt = clock.tick(30)  # fps 설정

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 캐릭터 위치
    character_x += character_to_x * dt  # fps보정
    if character_x < 0:
        character_x = 0
    elif character_x > background_width - character_width:
        character_x = background_width - character_width

    # enemy 위치
    enemy_y += enemy_speed * dt  # fps보정
    if enemy_y > background_height:
        enemy_x = GetEnemyX()
        enemy_y = 0

    # 충돌처리를 위한 rect 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        running = False

    # 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x, character_y))
    screen.blit(enemy, (enemy_x, enemy_y))

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
