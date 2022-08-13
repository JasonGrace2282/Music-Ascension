import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions, note, last):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft = pos)
        self.note = note
        self.is_last = last
    
    def update(self, shift, plane):
        if plane == "x":
            self.rect.x += shift
        elif plane == "y":
            self.rect.y += shift