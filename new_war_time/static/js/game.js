import pygame_sdl2 as pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 50)
    pygame.display.flip()