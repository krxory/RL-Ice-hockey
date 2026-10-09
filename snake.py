import pygame

pygame.init()
screen = pygame.display.set_mode((1300, 800))
clock = pygame.time.Clock()
running = True
center = screen.get_rect().center
dt=0

class Paddle():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 550
        self.height = 120
        self.width = 25
        self.cooldown = 0.8

    def move(self, dx, dy, dt, slow):
        if slow:
            speed = self.speed * 0.3
            self.x += dx * speed * dt
            self.y += dy * speed * dt

        else:
            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

p1 = Paddle(200, center[1], (139, 128, 0))
p2 = Paddle(1100, center[1], (48, 25, 62))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("gray")
    dt = clock.tick(240) / 1000

    border = pygame.draw.rect(screen, "black", (90, 25 ,1120 , 750), 5)
    goalLeft = pygame.draw.rect(screen, "yellow", (0, center[1] - 250 // 2, 95, 250))
    goalRight = pygame.draw.rect(screen, "purple", (1205, center[1] - 250 // 2, 95, 250))

    keys = pygame.key.get_pressed()

    dx1 = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    dy1 = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
    slow1 = keys[pygame.K_LSHIFT]
    dash1 = keys[pygame.K_e]

    dx2 = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    dy2 = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    slow2 = keys[pygame.K_RSHIFT]
    dash2 = keys[pygame.K_QUESTION]

    p1.move(dx1, dy1, dt, slow1)
    p2.move(dx2, dy2, dt, slow2)
    p1.draw(screen)
    p2.draw(screen)





    pygame.display.flip()
pygame.quit()