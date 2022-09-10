import pygame, time, random
from setup import height


class TeleportPlayer(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.animation_speed = 0.15
        self.image = pygame.image.load("../resources/player.png")
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
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
        self.counter = True
        self.delta = 0
        self.correctnote = False
        self.level_note = "G"

    def set_image(self):

        image = self.image
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def input(self, delta):
        keys = pygame.key.get_pressed()
        self.delta = delta
        self.direction.x = 0

        if keys[pygame.K_c]:
            self.level_note = "C"
            while not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midC.wav"))
        elif keys[pygame.K_d]:
            self.level_note = "D"
            while not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midD.wav"))
        elif keys[pygame.K_e]:
            self.level_note = "E"
            while not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midE.wav"))
        elif keys[pygame.K_f]:
            self.level_note = "F"
            while not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midF.wav"))
        elif keys[pygame.K_g]:
            self.level_note = "G"
            while not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midG.wav"))
        elif keys[pygame.K_a]:
            self.level_note = "A"
            while not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midA.wav"))
        elif keys[pygame.K_b]:
            self.level_note = "B"
            while not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midB.wav"))

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
        elif 0.4 <= self.delta < 0.6 and self.correctnote:
            print("0.5")
            self.direction.y -= 32
            self.rect.y += self.direction.y
            self.direction.y += 32
            self.direction.x += 16
        elif 0.6 <= self.delta < 0.9:
            print("mission failed, we'll get e'm next time")
        elif 0.9 <= self.delta < 1.1 and self.correctnote:
            print("1")
            self.direction.y -= 64
            self.rect.y += self.direction.y
            self.direction.y += 64
            self.direction.x += 24
        elif 1.1 <= self.delta < 1.4:
            print("mission failed, we'll get e'm next time")
        elif 1.4 <= self.delta < 1.6 and self.correctnote:
            print("1.5")
            self.direction.y -= 96
            self.rect.y += self.direction.y
            self.direction.y += 96
            self.direction.x += 32
        elif 1.6 <= self.delta < 1.9:
            print("mission failed, we'll get e'm next time")
        elif 1.9 <= self.delta < 2.1 and self.correctnote:
            print("2")
            self.direction.y -= 128
            self.rect.y += self.direction.y
            self.direction.y += 128
            self.direction.x += 40
        elif 2.1 <= self.delta < 2.9:
            print("mission failed, we'll get e'm next time")
        elif 2.9 <= self.delta < 3.1 and self.correctnote:
            print("3")
            self.direction.y -= 192
            self.rect.y += self.direction.y
            self.direction.y += 192
            self.direction.x += 48
        elif 3.1 <= self.delta < 3.9:
            print("mission failed, we'll get e'm next time")
        elif 3.9 <= self.delta < 4.1 and self.correctnote:
            print("4")
            self.direction.y -= 256
            self.rect.y += self.direction.y
            self.direction.y += 256
            self.direction.x += 56
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
        self.image = pygame.image.load("../resources/player.png")
        self.rect_image = pygame.image.load("../resources/hitbox.png")
        self.rect = self.image.get_rect(center=self.pos)
        self.ready = False
        self.start = time.time()
        self.chain = False
        self.delivered = False
        self.coins = 0
        self.difficulty_time = 10
        
    def input(self):
        keys = pygame.key.get_pressed()

        if not self.counter:
            time.sleep(0.1)
            self.counter = True
        elif keys[pygame.K_UP] and self.counter and not self.ready and self.pos[1]-48 > 0:
            print("hi")
            self.pos = (self.pos[0], self.pos[1]-48)
            self.counter = False
        elif keys[pygame.K_DOWN] and self.counter and not self.ready and self.pos[1]+114 < height:
            self.pos = (self.pos[0], self.pos[1]+48)
            self.counter = False
        elif keys[pygame.K_SPACE]:
            self.ready = True
            if self.pos[1] == 720:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midC.wav"))
            if self.pos[1] == 672:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midD.wav"))
            if self.pos[1] == 624:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midE.wav"))
            if self.pos[1] == 576:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midF.wav"))
            if self.pos[1] == 528:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midG.wav"))
            if self.pos[1] == 480:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midA.wav"))
            if self.pos[1] == 432:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/midB.wav"))
            if self.pos[1] == 384:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/highC.wav"))
            if self.pos[1] == 336:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/highD.wav"))
            if self.pos[1] == 288:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/highE.wav"))
            if self.pos[1] == 240:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/highF.wav"))
            if self.pos[1] == 192:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/highG.wav"))
            if self.pos[1] == 144:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/highA.wav"))
            if self.pos[1] == 96:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/highB.wav"))
            if self.pos[1] == 48:
                while not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("../resources/maxC.wav"))
    
    def set_image(self):
        image = self.image
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
    
    def find_note(self):
        noteY = [720, 672, 624, 576, 528, 480, 432, 384, 336, 288, 240, 192, 144, 96, 48]
        notes = ["Mid C", "Mid D", "Mid E", "Mid F", "Mid G", "Mid A", "Mid B", "Hi C", "Hi D", "Hi E", "Hi F", "Hi G", "Hi A", "Hi B", "Max C"]

        self.note = notes[noteY.index(self.pos[1])]
                    
    def update(self):
        self.find_note()
        pos = self.pos
        self.input()
        self.update_status()
        self.set_image()
        if self.pos != pos:
            self.rect = self.image.get_rect(center=self.pos)
        if self.ready:
            self.direction.x = 1
        else:
            self.direction.x = 0
        self.end = time.time()
        if self.end - self.start >= self.difficulty_time:
            self.ready = True
        if self.end - self.start >= 100:
            self.chain = True
