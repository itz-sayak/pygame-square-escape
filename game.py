import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Game")

# Set font
font = pygame.font.SysFont(None, 30)

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set game variables
player_size = 50
player_pos = [screen_width / 2, screen_height - 2 * player_size]
enemy_size = 50
enemy_pos = [random.randint(0, screen_width - enemy_size), 0]
enemy_list = [enemy_pos]
speed = 10
score = 0

# Set clock
clock = pygame.time.Clock()

# Define functions
def create_enemy():
    x = random.randint(0, screen_width - enemy_size)
    y = 0
    enemy_list.append([x, y])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, black, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_pos(enemy_list):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < screen_height:
            enemy_pos[1] += speed
        else:
            enemy_list.pop(idx)
            global score
            score += 1

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

# Start game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x, y]

    # Update game variables
    update_enemy_pos(enemy_list)
    if len(enemy_list) < 10:
        create_enemy()
    if collision_check(enemy_list, player_pos):
        game_over = True
        break
    score_text = "Score: " + str(score)
    score_display = font.render(score_text, True, black)

    # Draw objects
    screen.fill(white)
    draw_enemies(enemy_list)
    pygame.draw.rect(screen, black, (player_pos[0], player_pos[1], player_size, player_size))
    screen.blit(score_display, (10, 10))

    # Update screen
    pygame.display.update()

    # Set frame rate
    clock.tick(30)

# Game over screen
game_over_text = "Game Over!"
game_over_display =font.render(game_over_text, True, black)
screen.blit(game_over_display, (screen_width/2 - 75, screen_height/2 - 15))
pygame.display.update()

# Wait for 2 seconds
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()
quit()
