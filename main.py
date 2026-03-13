import pygame
print('Setup Start')
pygame.init()

pygame.init()
window = pygame.display.set_mode(size =(800, 600))
print('Setup End')

print('Loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # system exit
            quit()

