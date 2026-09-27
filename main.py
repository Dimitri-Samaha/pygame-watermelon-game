import pygame
import random
import numpy as np

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

VEL = 3

class Fruit:
    def __init__(self, game, lvl : int) -> None:
        self.game = game
        self.lvl = lvl
        self.dropped = False
        self.update()

    def drop(self):
        if self.pos[1]+self.radius+VEL < 522:
            self.pos = [self.pos[0], self.pos[1]+VEL]
        return

    def draw(self) -> None:
        pygame.draw.circle(self.game.WINDOW, self.color, self.pos, self.radius)
        return
    
    def draw_line(self) -> None:
       pygame.draw.line(self.game.WINDOW, (255, 255, 255), (self.pos[0], 190), (self.pos[0], 520), width=3)
       return 
    
    def check_circumference(self):
        theta = np.linspace(0, np.pi*2, 360)
        x = self.pos[0] + np.cos(theta)*self.radius
        y = self.pos[1] + np.sin(theta)*self.radius
        point_list = [[x[i], y[i]] for i in range(len(x))]
        return point_list
    
    def update(self):
        if self.lvl == 0:
            self.radius = 12
            self.color = BLUE
        elif self.lvl == 1:
            self.radius = 17
            self.color = RED
        elif self.lvl == 2:
            self.radius = 22
            self.color = GREEN
        
        if not self.dropped:
            if self.game.mousepos[0] > self.radius:
                if self.game.WIDTH-self.game.mousepos[0] < self.radius:
                    self.pos = self.game.WIDTH-self.radius, 190-self.radius
                else:
                    self.pos = self.game.mousepos[0], 190-self.radius
            else:
                self.pos = self.radius, 190-self.radius
            self.draw_line()
        else:
            self.cirumference = self.check_circumference()
            for fruit in self.game.fruits:
                for point in fruit.circumference:
                    pass
                    # nanani nanana
                
        self.draw()
        return 



class Game:
    def __init__(self) -> None:
        pass

    def generate_fruit(self):
        self.fruits.append(Fruit(self, random.randrange(0, 3)))
        return

    def check_fruits(self):
        if self.fruits[-1].dropped:
            self.generate_fruit()

    def main(self):
        # init
        pygame.init() 
        pygame.display.set_caption("Watermelon game")  # set window caption

        self.bg = pygame.image.load("images\\bg.jpg") 
        self.WIDTH, self.HEIGHT = self.bg.get_size()
        self.WIDTH, self.HEIGHT = (int(self.WIDTH*0.3), int(self.HEIGHT*0.3))
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGHT)) # Scale the image to your needed size
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) # create my window surface 

        clock = pygame.time.Clock() # set clock depending on fps
        FPS = 60

        self.mousepos = pygame.mouse.get_pos()
        self.fruits = [Fruit(self, 0)]

        menu = True
        # Create menu loop
        while menu:
            clock.tick(FPS)
            self.WINDOW.blit(self.bg, (0, 0))

            self.mousepos = pygame.mouse.get_pos()
            for fruit in self.fruits:
                fruit.update()

            self.check_fruits()
            
            # Listen for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if not self.fruits[-1].dropped:                   
                        self.fruits[-1].dropped = True
                    print(self.mousepos[1])
            pygame.display.update()

        return 



if __name__ == "__main__":
    game1 = Game()
    game1.main()
