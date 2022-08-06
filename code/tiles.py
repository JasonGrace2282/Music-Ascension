import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, shift, plane):
        if plane == "x":
            self.rect.x += shift
        elif plane == "y":  
            self.rect.y += shift