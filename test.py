from time import perf_counter
import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 790))
counter = 0
my_list = [0]
run = True
start = perf_counter()
while run:
    print(counter)
    counter+=1
    if counter == 10000:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
middle = perf_counter()
for i in my_list:
    print(counter)
    counter+=1
    my_list.append(i+1)
    if counter == 20000:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
end = perf_counter()
print(f'For loop: {end-middle}')
print(f'While Loop: {middle-start}')

