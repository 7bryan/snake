import pygame, random
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 10

WIDTH, HEIGHT = 1000, 700
SCREEN_SIZE = (WIDTH, HEIGHT)

def draw_map(screen): # drawing the grid
    for i in range(14): # the y coordinate
        for j in range(20): # the x coordinate
            pygame.draw.rect(screen, RED, (j * 50, i * 50, 50, 50), 1)

class Snake: # the individual snake object for snakes
    def __init__(self, screen, pos, color):
        self.screen = screen
        self.pos = pos
        self.color = color
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Food():
    def __init__(self, screen):
        self.screen = screen
        self.posx = random.randint(0, 19) * 50
        self.posy = random.randint(0, 13) * 50
        self.rect = pygame.Rect(self.posx, self.posy, 50, 50)

    def draw_food(self):
        pygame.draw.rect(self.screen, BLUE, self.rect, 10)


def init():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    return screen

def game_loop(screen):
    running = True
    clock = pygame.time.Clock()
    start = False

    dx, dy = 0, 0 # movement direction

    snakes = [] # the snake (player)
    foods = []
    foods.append(Food(screen))

    for i in range(5):
        snakes.append(Snake(screen, (i * 50, i * 50,), GREEN))


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                # controlling the direction
                if event.key == pygame.K_LEFT:
                    if not start:
                        start = True
                    if dx == 0:
                        dx -= 1
                        dy = 0
                    elif dx == -1:
                        ...
                    elif dx == 1:
                        ...
                    else:
                        dx *= -1
                        dy = 0
                elif event.key == pygame.K_UP:
                    if not start:
                        start = True
                    if dy == 0:
                        dy -= 1
                        dx = 0
                    elif dy == -1:
                        ...
                    elif dy == 1:
                        ...
                    else:
                        dy *= -1
                        dx = 0
                elif event.key == pygame.K_RIGHT:
                    if not start:
                        start = True
                    if dx == 0:
                        dx += 1
                        dy = 0
                    elif dx == 1:
                        ...
                    elif dx == -1:
                        ...
                    else:
                        dx *= -1
                        dy = 0
                elif event.key == pygame.K_DOWN:
                    if not start:
                        start = True
                    if dy == 0:
                        dy += 1
                        dx = 0
                    elif dy == 1:
                        ...
                    elif dy == -1:
                        ...
                    else:
                        dy *= -1
                        dx = 0

        screen.fill(BLACK)

        draw_map(screen)

        for snake in snakes: # drawing the snakes
            snake.draw_rect()

        for food in foods:
            food.draw_food()

        if start: # moving the snake head
            snakes.insert(0, Snake(screen, (snakes[0].pos[0] + (50 * dx), snakes[0].pos[1] + (50 * dy)), GREEN))
            for food in foods:
                #check if the snakes head collide with the food
                if snakes[0].pos[0] == food.posx and snakes[0].pos[1] == food.posy:
                    #remove the current food and add the snakes length before add another food
                    foods.remove(food)
                    foods.append(Food(screen))
                else: #else, move the snakes normally
                    snakes.pop()
            

        pygame.display.update()
        clock.tick(FPS) # fps

def main():
    screen = init()
    game_loop(screen)
    
    pygame.quit()

if __name__ == "__main__":
    main()
