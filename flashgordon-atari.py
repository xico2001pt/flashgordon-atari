import pygame
import random

WIDTH = 800
HEIGHT = 600
fps = 30

# load
# ICON = pygame.image.load('./assets/textures/icon.png')
CONSOLE = pygame.image.load('./assets/textures/console.png')
HEARTH = pygame.image.load('./assets/textures/hearth.png')
ZERO = pygame.image.load('./assets/textures/zero.png')
ONE = pygame.image.load('./assets/textures/one.png')
TWO = pygame.image.load('./assets/textures/two.png')
THREE = pygame.image.load('./assets/textures/three.png')
FOUR = pygame.image.load('./assets/textures/four.png')
FIVE = pygame.image.load('./assets/textures/five.png')
SIX = pygame.image.load('./assets/textures/six.png')
SEVEN = pygame.image.load('./assets/textures/seven.png')
EIGHT = pygame.image.load('./assets/textures/eight.png')
NINE = pygame.image.load('./assets/textures/nine.png')
ENEMY_SPAWN1 = pygame.image.load('./assets/textures/enemy_spawn1.png')
ENEMY_SPAWN2 = pygame.image.load('./assets/textures/enemy_spawn2.png')
RESCUE = pygame.image.load('./assets/textures/rescue.png')
SHIELD = pygame.image.load('./assets/textures/shield.png')
SPACESHIP = pygame.image.load('./assets/textures/spaceship.png')
ENEMY1 = pygame.image.load('./assets/textures/enemy1.png')
ENEMY2 = pygame.image.load('./assets/textures/enemy2.png')
ENEMY3 = pygame.image.load('./assets/textures/enemy3.png')
score = 0
highscore = 0
lives = 3
enemies = [0] * 5
rescue_points = [(80, 460), (85, 535), (115, 410), (260, 480), (330, 505),
                 (380, 405), (530, 430), (535, 510), (560, 485), (660, 460), (710, 435)]
MAP_MATRIX = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
              [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# physics
XS0, YS0 = 360, 200
XIS0, YIS0 = 395, 485
xs, ys = XS0, YS0
xis, yis = XIS0, YIS0
SPACESHIP_VEL = 0.16
SPACESHIP_ICON_VEL = 0.025
ENEMY_VEL = 0.10
SHOT_VEL = 1.3
right_side = True
enemy_spawn = False
spawn_time = False
enemies_alive = False
shooting = False
recover = False
enemy_x = [0]*5
ENEMY_WIDTH = ENEMY1.get_width()
ENEMY_HEIGHT = ENEMY1.get_height()
SPACESHIP_WIDTH = SPACESHIP.get_width()
SPACESHIP_HEIGHT = SPACESHIP.get_height()

# definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 85, 212)
BROWN = (170, 100, 30)
YELLOW = (255, 255, 153)

# funções
def intersects(x1, y1, w1, h1, x2, y2, w2, h2):
    return not (x1+w1 < x2 or x1 > x2+w2 or y1 > y2+h2 or y1+h1 < y2)


# inicialização do jogo
pygame.init()
pygame.mixer.init()  # permite som
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Flash Gordon")
# pygame.display.set_icon(ICON)
clock = pygame.time.Clock()

# game loop
running = True
while running:
    dt = clock.tick(fps)

    # ler eventos
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if 70 <= mouse_x <= 110 and 15 <= mouse_y <= 55:
            running = False
        elif 660 <= mouse_x <= 725 and 15 <= mouse_y <= 55:
            if fps == 30:
                fps = 120
            else:
                fps = 30
        # IMPLEMENTAR RESET

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        new_ys = ys - SPACESHIP_VEL * dt
        if new_ys >= 85:
            ys = new_ys
        new_yis = yis - SPACESHIP_ICON_VEL * dt
        if not MAP_MATRIX[int(new_yis-350)//25][int(xis)//25] and not MAP_MATRIX[int(new_yis-350)//25][int(xis+9)//25]:
            yis = new_yis
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        new_ys = ys + SPACESHIP_VEL * dt
        if new_ys <= 355 - SPACESHIP.get_height():
            ys = new_ys
        new_yis = yis + SPACESHIP_ICON_VEL * dt
        if not MAP_MATRIX[int(new_yis-350+4)//25][int(xis)//25] and not MAP_MATRIX[int(new_yis-350+4)//25][int(xis+9)//25]:
            yis = new_yis
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        new_xs = xs - SPACESHIP_VEL * dt * 1.5
        if new_xs > 45:
            xs = new_xs
        new_xis = xis - SPACESHIP_ICON_VEL * dt * 1.5
        if not MAP_MATRIX[int(yis-350)//25][int(new_xis)//25] and not MAP_MATRIX[int(yis-350+4)//25][int(new_xis)//25]:
            xis = new_xis
        right_side = False
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        new_xs = xs + SPACESHIP_VEL * dt * 1.5
        if new_xs <= 755 - SPACESHIP.get_width():
            xs = new_xs
        new_xis = xis + SPACESHIP_ICON_VEL * dt * 1.5
        if not MAP_MATRIX[int(yis-350)//25][int(new_xis+9)//25] and not MAP_MATRIX[int(yis-350+4)//25][int(new_xis+9)//25]:
            xis = new_xis
        right_side = True
    if keys[pygame.K_SPACE] and shooting is False:
        shooting = True
        shot_y = ys + SPACESHIP_HEIGHT / 2 + 2
        if right_side:
            shot_x = xs + SPACESHIP_WIDTH + 5
            shot_dir = 1
        else:
            shot_x = xs - 35
            shot_dir = -1

    # atualizar
    if xis >= 775:
        xis = 15
    if xis < 15:
        xis = 775
    if yis >= 575:
        yis = 370
    if yis < 370:
        yis = 575
    if rescue_points != []:
        for idx, (rx, ry) in enumerate(rescue_points):
            if intersects(xis, yis, 10, 5, rx, ry, RESCUE.get_width(), RESCUE.get_height()):
                del rescue_points[idx]
                enemy_spawn = True
                break
    else:
        if spawn_time is False and enemies_alive is False:
            running = False # acrescentar reinicio
    if enemy_spawn:
        enemies_alive = False
        enemy_spawn = False
        enemy_types = [random.randint(1, 3) for _ in range(5)]
        enemy_direction = [random.randint(0, 1) for _ in range(5)]
        for idx, num in enumerate(enemy_types):
            enemies[idx] = num
        spawn_time = True
        next_frame = pygame.time.get_ticks()
        frame = 0
        enemy_xi = 420 - ENEMY_WIDTH
    
    if lives == 0:
        running = False
    if len(str(score))<3:
        str_score = '0'*(3-len(str(score)))+str(score)
    else:
        str_score = str(score)
    spaceship_pos = (xs, ys)

    # render
    screen.fill(BLACK)

    # ecra cima
    if shooting:
        pygame.draw.rect(screen, YELLOW, (shot_x, shot_y, 30, 5), 0)
        shot_x += SHOT_VEL * shot_dir * dt
        if shot_x < -10 or shot_x > 780:
            shooting = False
    if spawn_time:
        if pygame.time.get_ticks() > next_frame:
            frame = frame + 1
            next_frame += 300
        for i in range(5):
            enemy_x[i] = enemy_xi + (i*10)*(-1)**i
            if frame % 2:
                screen.blit(ENEMY_SPAWN2, (enemy_x[i], 88+60*i))
            else:
                screen.blit(ENEMY_SPAWN1, (enemy_x[i], 88+60*i))
        if frame == 4:
            spawn_time = False
            enemies_alive = True

    if enemies_alive:
        dead = 0
        for idx, enemy in enumerate(enemy_types):
            enemy_x[idx] += ENEMY_VEL * dt * (-1) ** enemy_direction[idx]
            if enemy_x[idx] < 25-ENEMY_WIDTH or enemy_x[idx] > 775:
                enemy_types[idx] = 0
            if shooting and enemy_types[idx] != 0 and intersects(shot_x, shot_y, 30, 5, enemy_x[idx], 88+60*idx, ENEMY_WIDTH, ENEMY_HEIGHT):
                score += 3
                shooting = False
                enemy_types[idx] = 0
            if not recover and enemy_types[idx] != 0 and intersects(xs, ys, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, enemy_x[idx], 88+60*idx, ENEMY_WIDTH, ENEMY_HEIGHT):
                lives -= 1
                enemy_types[idx] = 0
                recover = True
                recover_time = pygame.time.get_ticks()
                blink = 0
            if enemy == 0:
                dead += 1
            elif enemy == 1:
                screen.blit(ENEMY1, (enemy_x[idx], 88+60*idx))
            elif enemy == 2:
                screen.blit(ENEMY2, (enemy_x[idx], 88+60*idx))
            else:
                screen.blit(ENEMY3, (enemy_x[idx], 88+60*idx))
        if dead == 5:
            enemies_alive = False
    if recover:
        if pygame.time.get_ticks() > recover_time:
            blink += 1
            recover_time += 300
        if blink == 8:
            recover = False
        if blink % 2:
                screen.blit(SHIELD, (xs-5, ys-5))

    if right_side:
        screen.blit(SPACESHIP, spaceship_pos)
    else:
        screen.blit(pygame.transform.flip(SPACESHIP, True, False), spaceship_pos)

    # ecra baixo
    for row in range(10):
        for col in range(32):
            if MAP_MATRIX[row][col]:
                pygame.draw.rect(screen, BROWN, (25*col, 350+25*row, 25, 25), 0)
    for x, y in rescue_points:
        screen.blit(RESCUE, (x, y))
    pygame.draw.rect(screen, BLUE, (xis, yis, 10, 5), 0)
    pygame.draw.rect(screen, WHITE, (0, 365, 800, 10), 0)

    # consola
    screen.blit(CONSOLE, (0, 0))
    for idx in range(lives):
        screen.blit(HEARTH, (275+45*idx, 15))
    for idx, val in enumerate(str_score):
        if val == '0':
            number = ZERO
        elif val == '1':
            number = ONE
        elif val == '2':
            number = TWO
        elif val == '3':
            number = THREE
        elif val == '4':
            number = FOUR
        elif val == '5':
            number = FIVE
        elif val == '6':
            number = SIX
        elif val == '7':
            number = SEVEN
        elif val == '8':
            number = EIGHT
        else:
            number = NINE
        screen.blit(number, (425+35*idx, 15))

    pygame.display.flip()

pygame.quit()
