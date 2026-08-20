import pygame
pygame.init()

screen = pygame.display.set_mode((1200,800))

pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

full_surface = pygame.image.load('ground_sky.jpg')

x = 50
y = 50 
width = 40
heigh = 40
vel = 5

run = True
while run:
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(full_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
    

pygame.quit()