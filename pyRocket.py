import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROCKET_WIDTH = 50
ROCKET_HEIGHT = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROCKET_SPEED = 5
ENEMY_SPEED = 3
ENEMY_SIZE = 50

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Rocket Game")

# Load images
background = pygame.image.load('Background.png')
rocket_image = pygame.image.load('Rocket.jpg')
rocket_image = pygame.transform.scale(rocket_image, (ROCKET_WIDTH, ROCKET_HEIGHT))

# Font for score
font = pygame.font.Font(None, 36)

# Rocket initial position
rocket_x = SCREEN_WIDTH // 4
rocket_y = SCREEN_HEIGHT // 4

# Enemy positions
enemies = []

def create_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
    enemy_y = -ENEMY_SIZE
    return [enemy_x, enemy_y]

# Initial score
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Update rocket position based on key presses
    if keys[pygame.K_LEFT]:
        rocket_x -= ROCKET_SPEED
    if keys[pygame.K_RIGHT]:
        rocket_x += ROCKET_SPEED
    if keys[pygame.K_UP]:
        rocket_y -= ROCKET_SPEED
    if keys[pygame.K_DOWN]:
        rocket_y += ROCKET_SPEED

    # Ensure the rocket stays within screen bounds
    rocket_x = max(0, min(rocket_x, SCREEN_WIDTH - ROCKET_WIDTH))
    rocket_y = max(0, min(rocket_y, SCREEN_HEIGHT - ROCKET_HEIGHT))

    # Move enemies
    for enemy in enemies:
        enemy[1] += ENEMY_SPEED
        # Check for collision with rocket
        if (rocket_x < enemy[0] < rocket_x + ROCKET_WIDTH or rocket_x < enemy[0] + ENEMY_SIZE < rocket_x + ROCKET_WIDTH) and \
           (rocket_y < enemy[1] < rocket_y + ROCKET_HEIGHT or rocket_y < enemy[1] + ENEMY_SIZE < rocket_y + ROCKET_HEIGHT):
            running = False  # End game if collision

    # Remove enemies that have moved off the screen
    enemies = [enemy for enemy in enemies if enemy[1] < SCREEN_HEIGHT]

    # Add new enemies
    if random.randint(0, 20) == 0:
        enemies.append(create_enemy())

    # Update score
    score += 1

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw the rocket
    screen.blit(rocket_image, (rocket_x, rocket_y))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE))

    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Game over screen
screen.fill(BLACK)
game_over_text = font.render('Game Over', True, WHITE)
score_text = font.render(f'Final Score: {score}', True, WHITE)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
screen.blit(score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
sys.exit()

