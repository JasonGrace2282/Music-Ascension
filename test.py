from itertools import cycle
from time import perf_counter
import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 790))
counter = 0
run = True
start = perf_counter()
while run:
    print(counter)
    counter+=1
    if counter == 1000000:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
middle = perf_counter()
for i in cycle((1, 1)):
    print(counter)
    counter+=1
    if counter == 2000000:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
end = perf_counter()
print(f'For loop: {end-middle}')
print(f'While Loop: {middle-start}')

