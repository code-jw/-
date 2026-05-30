import pygame
import sys

pygame.init()

tile_size = 64
rows = 7
cols = 10
width = cols * tile_size
height = rows * tile_size+60
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('미로 탈출 - 2일차')
clock = pygame.time.Clock()
font = pygame.font.SysFont('malgungothic',28)
small_font = pygame.font.SysFont('malgungothic',24)
curr = 0
#pygame.mixer.init()
#pygame.mixer.music.load("asset\\sound\\donut.mp3")
#pygame.mixer.music.play(-1)

maps = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 2],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
]
lastmap = 2
maze = maps[curr]
player_row = 1
player_col = 1
move_count = 0
total_score = 0
clear_game = False

wall_img = pygame.image.load("asset\\image\\vnfmsqur.png")
floor_img = pygame.image.load('asset\\image\\gkdisqur.png')
player_img = pygame.image.load('asset\\image\\jaekyonge.jpg')
goal_img = pygame.image.load('asset\\image\\tkdwk.png')

wall_img = pygame.transform.scale(wall_img, (tile_size,tile_size))
floor_img = pygame.transform.scale(floor_img, (tile_size,tile_size))
player_img = pygame.transform.smoothscale(player_img, (tile_size,tile_size))
goal_img = pygame.transform.scale(goal_img, (tile_size,tile_size))
player_img = pygame.transform.rotate(player_img, 270)


def draw_maze():
    for row in range(rows):
        for col in range(cols):
            x = col * tile_size
            y = row * tile_size+60

            if maze[row][col] == 1:
                screen.blit(wall_img, (x, y))

            else:
                screen.blit(floor_img, (x, y))

            if maze[row][col] == 2:
                screen.blit(goal_img, (x, y))


def draw_player():
    x = player_col * tile_size
    y = player_row * tile_size+60
    screen.blit(player_img, (x, y))


def move_player(dx, dy):
    global player_row, player_col, clear_game,curr,maze,move_count

    next_row = player_row + dy
    next_col = player_col + dx
    if 0 <= next_row < 7 and 0<=next_col<10:
        if maze[next_row][next_col] != 1:
            player_row = next_row
            player_col = next_col
            move_count += 1

        if maze[player_row][player_col] == 2:
            if curr != lastmap:
                curr += 1
                maze = maps[curr]
                player_row = 1
                player_col = 1
                move_count = 0
                draw_maze()
                draw_player()
            else:
                clear_game = True
def getscore():
    score = 100 - move_count
    return score
def draw_hud():
    stage_text = small_font.render(f"스테이지: {curr+1}", True, (255,255,255))
    move_text = small_font.render(f"이동 횟수: {move_count}", True, (255, 255, 255))
    score_text = small_font.render(f"점수: {total_score}", True, (255, 255, 255))
    screen.blit(stage_text,(10,15))
    screen.blit(move_text, (220, 15))
    screen.blit(score_text, (470, 15))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

        elif event.type == pygame.KEYDOWN and not clear_game:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)


            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)

            elif event.key == pygame.K_UP:
                move_player(0, -1)

            elif event.key == pygame.K_DOWN:
                move_player(0, 1)

    screen.fill((0,0,0))
    draw_maze()
    draw_player()
    total_score = getscore()
    draw_hud()
    if clear_game:
        text = font.render("도착! 미로를 탈출함", True, (255, 0, 0))
        screen.blit(text, (180, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()