import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 120

pygame.init()
pygame.mixer.init()

# load
ICON = pygame.image.load('./assets/textures/icon.png')
MENU_SOUND = pygame.mixer.music.load('./assets/sounds/flash_gordon_theme.mp3')
LASER = pygame.mixer.Sound('./assets/sounds/laser.wav')
COLLISION = pygame.mixer.Sound('./assets/sounds/collision.wav')
MAYDAY = pygame.mixer.Sound('./assets/sounds/mayday.wav')
BACKGROUND = pygame.image.load('./assets/textures/background.png')
START = pygame.image.load('./assets/textures/start.png')
CONSOLE = pygame.image.load('./assets/textures/console.png')
GAME_OVER = pygame.image.load('./assets/textures/game_over.png')
STARS0 = pygame.image.load('./assets/textures/stars0.png')
STARS1 = pygame.image.load('./assets/textures/stars1.png')
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
ENEMY0 = pygame.image.load('./assets/textures/enemy0.png')
ENEMY1 = pygame.image.load('./assets/textures/enemy1.png')
ENEMY2 = pygame.image.load('./assets/textures/enemy2.png')
ENEMY3 = pygame.image.load('./assets/textures/enemy3.png')
enemies = [0]*5
rescue_points_copy = [(80, 460), (85, 535), (115, 410), (260, 480), (330, 505),
                 (380, 405), (530, 430), (535, 510), (560, 485), (660, 460), (710, 435)]
rescue_points = rescue_points_copy.copy()
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
# variables
score = 0
highscore = 0
lives = 3
XS0, YS0 = 360, 200
XIS0, YIS0 = 395, 485
xs, ys = XS0, YS0
xis, yis = XIS0, YIS0
star_x, star_y = 185, 0
SPACESHIP_VEL = 0.15
SPACESHIP_ICON_VEL = 0.02
enemy_vel = 0.11
SHOT_VEL = 1.3
press = 0
playing = False
right_side = True
enemy_spawn = False
spawn_time = False
enemies_alive = False
shooting = False
recover = False
mouse_pressed = True
shot_time, pause_time = False, False
enemy_x = [0]*5
ENEMY_WIDTH = ENEMY1.get_width()
ENEMY_HEIGHT = ENEMY1.get_height()
SPACESHIP_WIDTH = SPACESHIP.get_width()
SPACESHIP_HEIGHT = SPACESHIP.get_height()
tornado = [((200,400), ['O','E'][random.randint(0,1)]), ((575,400), ['O','E'][random.randint(0,1)])][random.randint(0,1)]
tornado_dt = 30
tornado_move_time = 0
tornado_spawn = False
paused = False
message_sent = True

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 85, 212)
BROWN = (155, 83, 30)
PURPLE = (170, 0, 210)
ORANGE = (255, 170, 42)

# functions
def intersects(x1, y1, w1, h1, x2, y2, w2, h2):
    return not (x1+w1 < x2 or x1 > x2+w2 or y1 > y2+h2 or y1+h1 < y2)

def draw_score(score, x, y):
    for idx, val in enumerate(score):
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
        screen.blit(number, (x+35*idx, y))

def reset():
    global lives, score, xs, ys, xis, yis, rescue_points, star_x, star_y, right_side, enemy_spawn, enemy_vel, spawn_time, enemies_alive, shooting, recover, tornado, tornado_spawn, tornado_dt, message_sent
    lives, score = 3, 0
    xs, ys = XS0, YS0
    xis, yis = XIS0, YIS0
    rescue_points = rescue_points_copy.copy()
    star_x, star_y = 185, 0
    right_side = True
    enemy_spawn = False
    enemy_vel = 0.11
    spawn_time = False
    enemies_alive = False
    shooting = False
    recover = False
    tornado = [((200,400), ['O','E'][random.randint(0,1)]), ((575,400), ['O','E'][random.randint(0,1)])][random.randint(0,1)]
    tornado_spawn, tornado_dt = False, 30
    message_sent = True

# game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Flash Gordon")
pygame.display.set_icon(ICON)
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
anima = pygame.time.get_ticks()

# game loop
running = True
while running:
    dt = clock.tick(FPS)

    # events
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if not mouse_pressed and pygame.mouse.get_pressed()[0]:
        if 70 <= mouse_x <= 112 and 13 <= mouse_y <= 55:
            reset()
        elif 688 <= mouse_x <= 730 and 13 <= mouse_y <= 55:
            if paused:
                pygame.mixer.music.rewind()
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()
            paused = not paused
    mouse_pressed = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if playing:
        if lives > 0:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                new_ys = ys - SPACESHIP_VEL * dt
                if new_ys >= 85:
                    ys = new_ys
                new_yis = yis - SPACESHIP_ICON_VEL * dt
                if not MAP_MATRIX[int(new_yis-350)//25][int(xis)//25] and not MAP_MATRIX[int(new_yis-350)//25][int(xis+9)//25]:
                    yis = new_yis
                    star_y = (star_y + 0.005 * dt)%2
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                new_ys = ys + SPACESHIP_VEL * dt
                if new_ys <= 355 - SPACESHIP.get_height():
                    ys = new_ys
                new_yis = yis + SPACESHIP_ICON_VEL * dt
                if not MAP_MATRIX[int(new_yis-350+4)//25][int(xis)//25] and not MAP_MATRIX[int(new_yis-350+4)//25][int(xis+9)//25]:
                    yis = new_yis
                    star_y = (star_y - 0.005 * dt)%2
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                new_xs = xs - SPACESHIP_VEL * dt * 1.5
                if new_xs > 45:
                    xs = new_xs
                new_xis = xis - SPACESHIP_ICON_VEL * dt * 1.5
                if not MAP_MATRIX[int(yis-350)//25][int(new_xis)//25] and not MAP_MATRIX[int(yis-350+4)//25][int(new_xis)//25]:
                    xis = new_xis
                    star_x += SPACESHIP_VEL * 2 * dt
                right_side = False
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                new_xs = xs + SPACESHIP_VEL * dt * 1.5
                if new_xs <= 755 - SPACESHIP.get_width():
                    xs = new_xs
                new_xis = xis + SPACESHIP_ICON_VEL * dt * 1.5
                if not MAP_MATRIX[int(yis-350)//25][int(new_xis+9)//25] and not MAP_MATRIX[int(yis-350+4)//25][int(new_xis+9)//25]:
                    xis = new_xis
                    star_x -= SPACESHIP_VEL * 2 * dt
                right_side = True
            if keys[pygame.K_SPACE] and not shooting and not shot_time:
                LASER.play()
                shooting = True
                shot_y = ys + SPACESHIP_HEIGHT / 2 + 1.5
                if right_side:
                    shot_x = xs + SPACESHIP_WIDTH + 5
                    shot_dir = 1
                else:
                    shot_x = xs - 35
                    shot_dir = -1
            shot_time = keys[pygame.K_SPACE]
        
        # update
        if xis > 774:
            xis = 16
        if xis < 16:
            xis = 774
        if yis > 574:
            yis = 372
        if yis < 372:
            yis = 574
        if rescue_points != []:
            for idx, (rx, ry) in enumerate(rescue_points):
                if intersects(xis, yis, 10, 5, rx, ry, RESCUE.get_width(), RESCUE.get_height()):
                    del rescue_points[idx]
                    enemy_spawn = True
                    break
        else:
            if not spawn_time and not enemies_alive:
                rescue_points = rescue_points_copy.copy()
                xs, ys = XS0, YS0
                xis, yis = XIS0, YIS0
                enemy_vel += 0.02
                tornado_spawn = False
                tornado_dt -= 2
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
        
        if int(star_y):
            stars = STARS1
        else:
            stars = STARS0
        spaceship_pos = (xs, ys)
        
        # tornado
        while pygame.time.get_ticks() - tornado_move_time >= tornado_dt:
            tornado_move_time += tornado_dt
            (tornado_pos, tornado_dir) = tornado
            tor_x, tor_y = tornado_pos
            if lives > 0:
                if not intersects(tor_x+9, tor_y+4, 27-20, 27-10, xis, yis, 10, 5):
                    if tor_x%25==0 and tor_y%25==0:
                        if tornado_dir in ('N', 'S'):
                            if MAP_MATRIX[int(tor_y-350-25)//25][int(tor_x)//25] and tornado_dir == 'N' or tor_y <= 375:
                                tornado_dir = 'S'
                            if MAP_MATRIX[int(tor_y-350+25)//25][int(tor_x)//25] and tornado_dir == 'S' or tor_y >= 550:
                                tornado_dir = 'N'
                            if not MAP_MATRIX[int(tor_y-350)//25][int(tor_x-25)//25] and xis < tor_x:
                                tornado_dir = 'O'
                            if not MAP_MATRIX[int(tor_y-350)//25][int(tor_x+25)//25] and xis > tor_x:
                                tornado_dir = 'E'
                        else:
                            if MAP_MATRIX[int(tor_y-350)//25][int(tor_x-25)//25] and tornado_dir == 'O' or tor_x <= 25:
                                tornado_dir = 'E'
                            if MAP_MATRIX[int(tor_y-350)//25][int(tor_x+25)//25] and tornado_dir == 'E' or tor_x >= 750:
                                tornado_dir = 'O'
                            if not MAP_MATRIX[int(tor_y-350-25)//25][int(tor_x)//25] and yis < tor_y:
                                tornado_dir = 'N'
                            if not MAP_MATRIX[int(tor_y-350+25)//25][int(tor_x)//25] and yis > tor_y:
                                tornado_dir = 'S'

                    if tornado_dir == 'O':
                        tor_x -= 0.5
                    elif tornado_dir == 'E':
                        tor_x += 0.5
                    elif tornado_dir == 'N':
                        tor_y -= 0.5
                    elif tornado_dir == 'S':
                        tor_y += 0.5
                    
                    tornado = ((tor_x, tor_y), tornado_dir)
                elif not tornado_spawn:
                    tornado_spawn = True
                    tor_enemies = [1]*4
                    tor_enemies_info = [([0, 1],[775, -1])[random.randint(0,1)] for _ in range(4)]

        # render
        screen.fill(BLACK)
    
        # ecra cima
        for i in range(2):
            screen.blit(stars, ((i*432+star_x)%865 - 90, 80))
        if shooting:
            pygame.draw.rect(screen, PURPLE, (shot_x, shot_y, 30, 5), 0)
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
                enemy_x[idx] += enemy_vel * dt * (-1) ** enemy_direction[idx]
                if enemy_x[idx] < 25-ENEMY_WIDTH or enemy_x[idx] > 775:
                    enemy_types[idx] = 0
                if shooting and enemy_types[idx] != 0 and intersects(shot_x, shot_y, 30, 5, enemy_x[idx], 88+60*idx, ENEMY_WIDTH, ENEMY_HEIGHT):
                    score += 3
                    shooting = False
                    enemy_types[idx] = 0
                if not recover and enemy_types[idx] != 0 and intersects(xs, ys, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, enemy_x[idx], 88+60*idx, ENEMY_WIDTH, ENEMY_HEIGHT):
                    COLLISION.play()
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
        if tornado_spawn:
            dead_tor = 0
            for idx, enemy in enumerate(tor_enemies):
                tor_enemies_info[idx][0] += enemy_vel * 1.75 * dt * tor_enemies_info[idx][1]
                if tor_enemies_info[idx][0] < 0 or tor_enemies_info[idx][0] > 775:
                    tor_enemies[idx] = 0
                if shooting and tor_enemies[idx] != 0 and intersects(shot_x, shot_y, 30, 5, tor_enemies_info[idx][0], 120+60*idx, 35, 20):
                    score += 1
                    shooting = False
                    tor_enemies[idx] = 0
                if not recover and tor_enemies[idx] != 0 and intersects(xs, ys, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, tor_enemies_info[idx][0], 120+60*idx, 35, 20):
                    COLLISION.play()
                    lives -= 1
                    tor_enemies[idx] = 0
                    recover = True
                    recover_time = pygame.time.get_ticks()
                    blink = 0
                if enemy:
                    if tor_enemies_info[idx][1] == 1:
                        screen.blit(ENEMY0, (tor_enemies_info[idx][0], 120+60*idx))
                    else:
                        screen.blit(pygame.transform.flip(ENEMY0, True, False), (tor_enemies_info[idx][0], 120+60*idx))
                else:
                    dead_tor += 1
            if dead_tor == 4:
                tornado_spawn = False
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
        if lives <= 0:
            if not pygame.mixer.get_busy() and message_sent:
                MAYDAY.play()
                message_sent = False
            if score > highscore:
                highscore = score
            screen.blit(GAME_OVER, (25, 75))
            draw_score('%03d'%score, 245, 245)
            draw_score('%03d'%highscore, 620, 245)
    
        # ecra baixo
        for row in range(10):
            for col in range(32):
                if MAP_MATRIX[row][col]:
                    pygame.draw.rect(screen, BROWN, (25*col, 350+25*row, 25, 25), 0)
        pygame.draw.rect(screen, ORANGE, (tornado[0][0], tornado[0][1], 25, 25), 0)
        for x, y in rescue_points:
            screen.blit(RESCUE, (x, y))
        pygame.draw.rect(screen, BLUE, (xis, yis, 10, 5), 0)
        pygame.draw.rect(screen, WHITE, (0, 365, 800, 10), 0)
    else:
        if keys[pygame.K_RETURN]:
            playing = True
            tornado_move_time = pygame.time.get_ticks()
            BACK_MUSIC = pygame.mixer.music.load('./assets/sounds/vultans_theme.mp3')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
        screen.blit(BACKGROUND, (25, 75))
        if pygame.time.get_ticks() > anima:
            press += 1
            anima += 960
        if press % 2:
                screen.blit(START, (265, 410))

    # consola
    screen.blit(CONSOLE, (0, 0))
    for idx in range(lives):
        screen.blit(HEARTH, (275+45*idx, 15))
    draw_score('%03d'%score, 425, 15)

    pygame.display.flip()

pygame.quit()
