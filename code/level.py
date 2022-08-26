from turtle import back
from types import NoneType
import pygame
import sys
import random
from tiles import TeleportTile, NoteTile
from setup import tilesize, width, height
from player import TeleportPlayer, NotePlayer


class TeleportLevel():
    def __init__(self, level_data, surface, stage):


        # level setup
        self.display_surface = surface
        self.stage = stage
        self.note_text = None
        self.setup_level(level_data)
        self.h_shift = 0
        self.v_shift = 0
        self.current_x = 0
        self.player_on_ground = False

        self.background4Settings = pygame.image.load("resources/BlackBlank.jpg")
        self.restartImage = pygame.image.load("resources/retry2.png")
        self.mainmenuImage = pygame.image.load("resources/quit2.png")
        self.settingsImage = pygame.image.load("resources/menu.png")
        self.backImage = pygame.image.load("resources/back2.png")
        self.exitSettings = pygame.Rect(0, 0, self.restartImage.get_width(), self.restartImage.get_height())
        self.restart = pygame.Rect(0, self.restartImage.get_height(), self.backImage.get_width(), self.backImage.get_height())
        self.mainmenu = pygame.Rect(0, self.restartImage.get_height()+self.backImage.get_height(), self.mainmenuImage.get_width(), self.mainmenuImage.get_height())
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
                tile = TeleportTile(pos, (tilesize, tilesize), info[1], last)

                self.tiles.add(tile)
                last = False

            if info[0] == 1:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 192

                pos = (offset+pos[0], pos[1]-64)
                tile = TeleportTile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False

            if info[0] == 1.5:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 256
                pos = (offset+pos[0], pos[1]-96)
                tile = TeleportTile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False

            if info[0] == 2:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 320
                pos = (offset+pos[0], pos[1]-128)
                tile = TeleportTile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False

            if info[0] == 3:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 384
                pos = (offset+pos[0], pos[1]-192)
                tile = TeleportTile(pos, (tilesize, tilesize), info[1], last)
                self.tiles.add(tile)
                last = False

            if info[0] == 4:
                index += 1
                if len(layout[self.stage-1]) == index:
                    last = True
                offset = 448
                pos = (offset+pos[0], pos[1]-256)
                tile = TeleportTile(pos, (tilesize, tilesize), info[1], last)
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
            self.display_surface.blit(self.background4Settings, (0, 0))
            self.display_surface.blit(self.backImage, (0, 0))
            self.display_surface.blit(self.restartImage, (0, 100))
            self.display_surface.blit(
                self.mainmenuImage, (0, self.restartImage.get_height()+self.backImage.get_height()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart.collidepoint(event.pos):
                        print("reset")
                        self.reset = True
                    if self.mainmenu.collidepoint(event.pos):
                        print("main menu")
                        self.back = True
                    if self.exitSettings.collidepoint(event.pos):
                        self.settingsClicked = False

        if self.player.sprite.rect.topleft[1] > height:
            self.display_surface.blit(self.background4Settings, (0, 0))
            self.display_surface.blit(self.restartImage, (0, 0))
            self.display_surface.blit(
                self.mainmenuImage, (0, self.restartImage.get_height()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart.collidepoint(event.pos):
                        print("reset")
                        self.reset = True
                    if self.mainmenu.collidepoint(event.pos):
                        print("main menu")
                        self.back = True


class NoteLevel(TeleportLevel):
    def __init__(self, level_data, surface, stage):
        self.ledger = pygame.sprite.GroupSingle()
        self.house = pygame.sprite.GroupSingle()
        self.old_house = pygame.sprite.GroupSingle()
        self.barrier = pygame.sprite.GroupSingle()
        super().__init__(level_data, surface, stage)
        self.chain = False
        self.draw_old = True
        self.counter = 0
        self.counterclock = False
        self.playerdelivered = False
        self.playercoins = 0


    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        pos = (0, 240)
        for i in range(1, 6):
            tile = NoteTile(pos, (9000, 20), False, False)
            self.tiles.add(tile)
            pos = (pos[0], pos[1]+96)

        player_sprite = NotePlayer((192, 538), self.display_surface)
        self.player.add(player_sprite)

        self.randomize_note()

    def detect_collisions(self):
        player = self.player.sprite
        player.rect.centerx += player.direction.x * player.speed

        if self.house.sprite.rect.colliderect(player.rect):
            print("it worked")
            self.draw_old = False
            self.playerdelivered = True

            if self.coincounter == 0:
                self.player.sprite.coins = self.playercoins + 1
                self.playercoins = self.player.sprite.coins
                self.coincounter = 1
        else:
            self.coincounter = 0

        if self.barrier.sprite.rect.colliderect(player.rect):
            self.counterclock = True
            self.old_house.add(self.house.sprite)
            self.randomize_note()
            print(player.pos)

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
        else:
            self.h_shift = 0
            self.v_shift = 0
            player.speed = 8

    def randomize_note(self):
        noteY = [698, 650, 602, 554, 506, 458, 410, 362, 314, 266, 218, 170, 122, 74, 26]
        notes = ["MidC", "MidD", "MidE", "MidF", "MidG", "MidA", "MidB", "HiC", "HiD", "HiE", "HiF", "HiG", "HiA", "HiB", "MaxC"]

        note = random.choice(notes)
        font = pygame.font.SysFont(None, 30)
        self.note_text = font.render(note, True, (255, 255, 255))
        self.coin_text = font.render(str(self.player.sprite.coins), True, (255, 255, 255))

        self.player.sprite.pos = (self.player.sprite.rect.centerx, self.player.sprite.rect.centery)

        yResult = noteY[notes.index(note)]
        house = NoteTile((self.player.sprite.pos[0] + 1200, yResult), (64, 64), True, True, "resources/house.png")
        self.house.add(house)
        barrier = NoteTile((self.house.sprite.pos[0], 0), (1, 704), False, False)
        self.barrier.add(barrier)

    def run(self):

        # level tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.house.update(self.h_shift, "x")
        self.barrier.update(self.h_shift, "x")
        self.tiles.draw(self.display_surface)
        self.house.draw(self.display_surface)
        if self.old_house != None and self.draw_old:
            self.old_house.update(self.h_shift, "x")
            self.old_house.draw(self.display_surface)
        elif not self.draw_old:
            self.draw_old = True
        self.scroll()

        # player
        self.player.update()
        self.detect_collisions()
        self.on_ground()

        self.player.draw(self.display_surface)

        if self.note_text != None:
            self.display_surface.blit(self.note_text, (0, 0))
        if self.coin_text != None:
            self.display_surface.blit(self.coin_text, (1000, 0))

        if self.player.sprite.pos[1] == 578:
            tile = NoteTile((self.player.sprite.pos[0]-18, self.player.sprite.pos[1]+22), (100, 20), False, False)
            tile.add(self.ledger)
        elif self.player.sprite.pos[1] == 628:
            tile = NoteTile((self.player.sprite.pos[0]-18, self.player.sprite.pos[1]-28), (100, 20), False, False)
            tile.add(self.ledger)

        if not self.player.sprite.ready:
            self.ledger.draw(self.display_surface)
        
        if self.counterclock:
            self.counter += 1
            if self.counter >= 20:
                print(self.player.sprite.pos)
                player_sprite = NotePlayer((self.player.sprite.pos), self.display_surface)
                self.player.add(player_sprite)
                self.counterclock = False
                self.counter = 0
                self.player.update()
                if not self.playerdelivered:
                    self.player.sprite.delivered = True
                    self.player.update()
                    self.playerdelivered = False