import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, shift, plane):
        if plane == "x":
            self.rect.x += shift
        elif plane == "y":  
            self.rect.y += shift