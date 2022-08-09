import pygame

class TeleportPlayer(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.animation_speed = 0.15
        self.image = pygame.image.load("../resources/player.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = pos

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # player status
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.start = 0
        self.end = 0
        self.counter = 0
        self.delta = 0
    
    def set_image(self):
        
        image = self.image
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
        
        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        
        
    def input(self, delta):
        keys = pygame.key.get_pressed()
        self.delta = delta
        self.direction.x = 0

        self.teleport()

    def update_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > self.gravity:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def teleport(self):
        if self.delta <= 0:
            pass
        elif 0.1 <= self.delta < 0.4:
            print("mission failed, we'll get e'm next time")
        elif 0.4 <= self.delta < 0.6:
            print("0.5")
            self.direction.y -= 32
            self.rect.y += self.direction.y
            self.direction.y += 32
            self.direction.x += 24
        elif 0.6 <= self.delta < 0.9:
            print("mission failed, we'll get e'm next time")
        elif 0.9 <= self.delta < 1.1:
            print("1")
            self.direction.y -= 64
            self.rect.y += self.direction.y
            self.direction.y += 64
            self.direction.x += 24
        elif 1.1 <= self.delta < 1.4:
            print("mission failed, we'll get e'm next time")
        elif 1.4 <= self.delta < 1.6:
            print("1.5")
            self.direction.y -= 64
            self.rect.y += self.direction.y
            self.direction.y += 64
            self.direction.x += 32
        elif 1.6 <= self.delta < 1.9:
            print("mission failed, we'll get e'm next time")
        elif 1.9 <= self.delta < 2.1:
            print("2")
            self.direction.y -= 128
            self.rect.y += self.direction.y
            self.direction.y += 128
            self.direction.x += 24
        elif 2.1 <= self.delta < 2.9:
            print("mission failed, we'll get e'm next time")
        elif 2.9 <= self.delta < 3.1:
            print("3")
            self.direction.y -= 128
            self.rect.y += self.direction.y
            self.direction.y += 128
            self.direction.x += 32
        elif 3.1 <= self.delta < 3.9:
            print("mission failed, we'll get e'm next time")
        elif 3.9 <= self.delta < 4.1:
            print("4")
            self.direction.y -= 256
            self.rect.y += self.direction.y
            self.direction.y += 256
            self.direction.x += 32
        elif self.delta > 4.1:
            print("mission failed, we'll get e'm next time")
    
    def update(self, delta, shift):
        self.input(delta)
        self.update_status()
        self.set_image()
        self.rect.x += shift

class NotePlayer(TeleportPlayer):
    def __init__(self, pos, surface):
        super().__init__(pos, surface)
    
    def input(self, delta):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.pos = (self.pos[0], self.pos[1]-100)
        elif keys[pygame.K_DOWN]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0