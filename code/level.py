import pygame, sys, time
from tiles import Tile
from setup import tilesize, width, height
from player import TeleportPlayer, NotePlayer
import random


class TeleportLevel():
    def __init__(self, level_data, surface, stage):


        # level setup
        self.display_surface = surface
        self.stage = stage
        self.setup_level(level_data)
        self.h_shift = 0
        self.v_shift = 0
        self.current_x = 0
        self.player_on_ground = False

        self.note_text = None
        self.gameover = pygame.image.load("resources/gameover.png")
        self.restartImage = pygame.image.load("resources/next.png")
        self.mainmenuImage = pygame.image.load("resources/next.png")
        self.settingsImage = pygame.image.load("resources/next.png")
        self.restart = pygame.Rect(0, 0, self.restartImage.get_width(), self.restartImage.get_height())
        self.mainmenu = pygame.Rect(0, self.restartImage.get_height(), self.mainmenuImage.get_width(), self.mainmenuImage.get_height())
        self.settings = pygame.Rect(100, 0, self.settingsImage.get_width(), self.settingsImage.get_height())
        self.settingsClicked = False
        self.stagefinished = False
        self.reset = False
        self.back = False
        self.complete = False
        self.note = "G"

    def on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        pos = (0, 640)

        last = False
        index = 0

        for info in layout[self.stage-1]:
            if info[0] == 0.5:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 128
                pos = (offset+pos[0], pos[1]-32)
                tile = Tile(pos, (tilesize, tilesize), info[1], last)

                self.tiles.add(tile)
                last = False

            if info[0] == 1:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 192

                pos = (offset+pos[0], pos[1]-64)
                tile = Tile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False
            
            if info[0] == 1.5:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 256
                pos = (offset+pos[0], pos[1]-96)
                tile = Tile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False
                
            if info[0] == 2:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 320
                pos = (offset+pos[0], pos[1]-128)
                tile = Tile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False
            
            if info[0] == 3:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 384
                pos = (offset+pos[0], pos[1]-192)
                tile = Tile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False
            
            if info[0] == 4:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 448
                pos = (offset+pos[0], pos[1]-256)
                tile = Tile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False
        
        player_sprite = TeleportPlayer((192, 512), self.display_surface)
        self.player.add(player_sprite)

    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x


        if player_x < width/2 and direction_x < 0:
            self.h_shift = 8
            player.speed = 0
        elif player_x > width/2:
            self.h_shift = -8
            player.speed = 0
        elif player_y < height/4:
            self.v_shift = 4

        else:
            self.h_shift = 0
            self.v_shift = 0
            player.speed = 8

    def detect_collisions(self, delta):

        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.is_last:
                    self.stage += 1
                    self.stagefinished = True
                    sprite.is_last = False
                note = pygame.font.SysFont(None, 30)
                self.note_text = note.render(self.note, True, (255, 255, 255))
                if self.note == sprite.note:
                    self.player.sprite.correctnote = True
                else:
                    self.player.sprite.correctnote = False
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling

        
    def run(self, delta):
        # tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.tiles.draw(self.display_surface)
        self.scroll()

        # player
        self.player.update(delta, self.h_shift)
        self.note = self.player.sprite.level_note
        self.detect_collisions(delta)
        self.on_ground()
        self.player.draw(self.display_surface)

        # conditions
        if self.stagefinished:
            self.reset = True

        if self.note_text != None:
            self.display_surface.blit(self.note_text, (0, 0))
        
        self.display_surface.blit(self.settingsImage, (100, 0))

        if self.settingsClicked:
            self.display_surface.blit(self.gameover, (0, 0))
            self.display_surface.blit(self.restartImage, (0, 0))
            self.display_surface.blit(self.mainmenuImage, (0, self.restartImage.get_height()))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart.collidepoint(event.pos):
                        print("why")
                        self.reset = True
                    if self.mainmenu.collidepoint(event.pos):
                        print("no u")
                        self.back = True

        if self.player.sprite.rect.topleft[1] > height:
            self.display_surface.blit(self.gameover, (0, 0))
            self.display_surface.blit(self.restartImage, (0, 0))
            self.display_surface.blit(self.mainmenuImage, (0, self.restartImage.get_height()))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart.collidepoint(event.pos):
                        print("why")
                        self.reset = True
                    if self.mainmenu.collidepoint(event.pos):
                        print("no u")
                        self.back = True
                    
class NoteLevel(TeleportLevel):
    def __init__(self, level_data, surface, stage):
        super().__init__(level_data, surface, stage)
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        noteY = [77, 127, 177, 227, 277, 327, 377.77777, 427, 477]

        pos = (0, 100)
        for i in range(1, 6):
            tile = Tile(pos, (9000, 20), "G", False)
            self.tiles.add(tile)
            pos = (pos[0], pos[1]+100)
        for i in range(43):
            yResult = random.choice(noteY)
            emtoinaldmage = Tile((400+i*200, yResult), (64, 64), "G", False)
            self.tiles.add(emtoinaldmage)

        player_sprite = NotePlayer((192, 377.7777777), self.display_surface)
        self.player.add(player_sprite)
    
    def detect_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
    
    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x

        if player_x < width/4 and direction_x < 0:
            self.h_shift = 8
            player.speed = 0
        elif player_x > width - width/4 and direction_x > 0:
            self.h_shift = -8
            player.speed = 0
        elif player_y < height/4:
            self.v_shift = 4
        else:
            self.h_shift = 0
            self.v_shift = 0
            player.speed = 8
    
    def run(self, delta):

        # level tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.tiles.draw(self.display_surface)
        self.scroll()

        # player
        self.player.update()
        self.detect_collisions()
        self.on_ground()
        self.player.draw(self.display_surface)
