import pygame, random
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 9

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

    move = False

    dx, dy = 0, 0 # movement direction
    direction_changed = False # prevent reverse movement

    snakes = [] # the snake (player)
    foods = [] # the foods
    foods.append(Food(screen))
 
    snakes.append(Snake(screen, (9 * 50, 6 * 50,), GREEN))


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                # controlling the direction
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_ESCAPE:
                    running = False
                #if not direction_changed:
                if event.key == K_LEFT and dx != 1 and not direction_changed:
                    start = True
                    dx, dy = -1, 0
                    direction_changed = True
                elif event.key == K_RIGHT and dx != -1 and not direction_changed:
                    start = True
                    dx, dy = 1, 0
                    direction_changed = True
                elif event.key == K_UP and dy != 1 and not direction_changed:
                    start = True
                    dx, dy = 0, -1
                    direction_changed = True
                elif event.key == K_DOWN and dy != -1 and not direction_changed:
                    start = True
                    dx, dy = 0, 1
                    direction_changed = True

        screen.fill(BLACK)

        draw_map(screen)

        for snake in snakes: # drawing the snakes
            snake.draw_rect()

        for food in foods:
            food.draw_food()

        ate_food = False
        if start: # moving the snake head
            new_head = Snake(screen, (snakes[0].pos[0] + (50 * dx), snakes[0].pos[1] + (50 * dy)), GREEN)
            snakes.insert(0, new_head)
            direction_changed = False

            for food in foods:
                #check if the snakes head collide with the food
                if snakes[0].pos[0] == food.posx and snakes[0].pos[1] == food.posy:
                    #remove the current food and add the snakes length before add another food
                    foods.remove(food)
                    foods.append(Food(screen))
                    ate_food = True
                    break
            
            if not ate_food:
                snakes.pop()
            
            #init the rule (walls)
            if snakes[0].rect.x < 0 or snakes[0].rect.x >= WIDTH:   
                running = False
            if snakes[0].rect.y < 0 or snakes[0].rect.y >= HEIGHT:
                running = False

            for snake in snakes[1:]: #lose if the head collide with its body
                if snakes[0].rect.colliderect(snake.rect):
                    running = False
            

        pygame.display.update()
        clock.tick(FPS) # fps

def main():
    screen = init()
    game_loop(screen)
    
    pygame.quit()

if __name__ == "__main__":
    main()
