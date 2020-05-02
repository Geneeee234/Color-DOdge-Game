#COLOR DODGE GAME
import pygame
import random
import sys

pygame.init()
pygame.font.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
silver = (192, 192, 192)

clock = pygame.time.Clock()

wall = list(range(10))
walls_x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
walls_y = 30

win_h = 500
win_w = 300

player_x = win_w // 2
player_y = win_h - 32

score = 0
my_font = pygame.font.SysFont("monospace", 30)

speed = 3

window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("COLOR DODGE GAME")
class box:
    def __init__(self, size, color, x, y):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
    def left(self):
        if self.x - self.size >= 0:
             return self.x - self.size
        else:
            return self.x
    def right(self, win_w):
        if self.x + self.size < win_w:
            return self.x + self.size
        else:
            return self.x

def color_walls(path_color):
    wall_color = path_color
    while wall_color == path_color:
        wall_color = random.randint(1, 3)
    return wall_color

def wall_creation(wall, wall_color, walls_x, walls_y):
    if wall_color == 1:
        for index in range(len(wall)):
            wall[index] = box(30, blue, walls_x[index], walls_y)
        return wall
    elif wall_color == 2:
        for index in range(len(wall)):
            wall[index] = box(30, red, walls_x[index], walls_y)
        return wall
    else:
        for index in range(len(wall)):
            wall[index] = box(30, green, walls_x[index], walls_y)
        return wall

def path_create(wall, player):
    paths = []
    while len(paths) != 3:
        path = random.randint(0, 9)
        if path not in paths:
            paths.append(path)
    for index in paths:
        wall[index].color = player.color
    return wall

def chk_color_collision(wall, player):
    if wall.color != player.color and player.x == wall.x:
        return True
    else:
        return False

def collission(wall, player):
    def chk_list(wall_coordinates, player, wall):
        if wall_coordinates >= player.x:
            return True
        else:
            return False
    def chk_list2(wall_coordinates, player, wall):
        if wall_coordinates >= player.y:
            return True
        else:
            return False
    def chk_list3(wall_coordinates, player, wall):
        if wall_coordinates < player.x + player.size:
            return True
        else:
            return False
    def chk_list4(wall_coordinates, player, wall):
        if wall_coordinates < player.y + player.size:
            return True
        else:
            return False
    def chk_list5(wall_coordinates, player, wall):
        if player.x >= wall_coordinates:
            return True
        else:
            return False
    def chk_list6(wall_coordinates, player, wall):
        if player.y >= wall_coordinates:
            return True
        else:
            return False
    def chk_list7(wall_coordinates, player, wall):
        if player.x < wall_coordinates + player.size:
            return True
        else:
            return False
    def chk_list8(wall_coordinates, player, wall):
        if player.y < wall_coordinates + player.size:
            return True
        else:
            return False
    pl = []
    wall_x = []
    y = []
    for i in range(len(wall)):
        pl.append(player)
        wall_x.append(wall[i].x)
        y.append(wall[i].y)
    walls_y = y
    print(walls_y)
    print(pl)
    print(walls_x)
    if (any(list(map(chk_list, walls_x, pl, wall))) and any(list(map(chk_list3, walls_x, pl, wall))) and any(list(map(chk_color_collision,wall, pl)))) or (any(list(map(chk_list5, walls_x, pl, wall))) and any(list(map(chk_list7, walls_x, pl, wall)))and any(list(map(chk_color_collision, wall, pl)))):
        if(any(list(map(chk_list2, walls_y, pl, wall))) and any(list(map(chk_list4, walls_y, pl, wall)))and any(list(map(chk_color_collision,wall, pl)))) or (any(list(map(chk_list6, walls_y, pl, wall))) and any(list(map(chk_list8, walls_y, pl, wall)))and any(list(map(chk_color_collision, wall, pl)))):
            return True
    return False


if random.randint(1, 3) == 1:
    path_color = 1
    player = box(30, blue, player_x, player_y)
elif random.randint(1, 3) == 2:
    path_color = 2
    player = box(30, red, player_x, player_y)
else:
    path_color = 3
    player = box(30, green, player_x, player_y)

wall_color = color_walls(path_color)
wall = wall_creation(wall, wall_color, walls_x, walls_y)
wall = path_create(wall, player)

run = True

while run:
    window.fill(silver)
    if collission(wall, player):
        print("=" * 100)
        print("Score: ", score)
        print("=" * 100)
        run = False

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x = player.left()
            elif event.key == pygame.K_RIGHT:
                player.x = player.right(win_w)

    pygame.draw.rect(window, player.color, (player.x, player.y, player.size, player.size))
    for i in range(10):
        pygame.draw.rect(window, wall[i].color, (wall[i].x, wall[i].y, wall[i].size, wall[i].size))

        if wall[i].y >= 30 and wall[i].y <= win_h:
            wall[i].y += speed
        elif wall[i].y >= win_h:
            score += 20
            speed = speed + (3 - int(speed * 0.2))
            if random.randint(1, 3) == 1:
                path_color = 1
                player = box(30, blue, player_x, player_y)
            elif random.randint(1, 3) == 2:
                path_color = 2
                player = box(30, red, player_x, player_y)
            else:
                path_color = 3
                player = box(30, green, player_x, player_y)

            wall_color = color_walls(path_color)
            wall = wall_creation(wall, wall_color, walls_x, walls_y)
            wall = path_create(wall, player)

    text = "Score: " + str(score)
    score_text = my_font.render(text, 1, black)
    window.blit(score_text, (win_w / 4, 0))
    clock.tick(30)
    pygame.display.update()

# BY REYES EUGENE