import pygame
import logging
from random import randint, choice
from tiles import TeleportTile, NoteTile
from setup import tilesize, width, height
from player import TeleportPlayer, NotePlayer


class TeleportLevel():
    def __init__(self, level_data, surface, stage):

        pygame.mixer.init()

        # level setup
        self.DISPLAY_SURFACE = surface
        self.stage = stage
        self.note_text = None
        self.complete = False
        self.note = "G"
        self.setup_level(level_data)
        self.h_shift = 0
        self.v_shift = 0
        self.current_x = 0
        self.musicCounter = 0
        self.player_on_ground = False

        # logging
        logging.basicConfig(level= logging.DEBUG, format='level.py\n%(message)s')

        self.background4Settings = pygame.image.load("../resources/blank.jpg")
        self.restartImage = pygame.image.load("../resources/retry2.png")
        self.mainmenuImage = pygame.image.load("../resources/quit2.png")
        self.settingsImage = pygame.image.load("../resources/menubutton2.png")
        self.backImage = pygame.image.load("../resources/back2.png")
        self.musicbutton = pygame.image.load("../resources/musicbutton.png")
        self.pizzaWin = pygame.image.load("../resources/pizza_delivered.png")
        self.coins = pygame.image.load("../resources/coins.png")
        self.pizzaBackground = pygame.image.load("../resources/trebleclef.png")
        self.pizzaBackground2 = pygame.image.load("../resources/bassclef.png")
        self.starbackground = pygame.image.load("../resources/starbg.png")
        self.stageimage = pygame.image.load("../resources/stagefinished.png")
        self.helpimage = pygame.image.load("../resources/help2.png")
        self.helpbg = pygame.image.load("../resources/pizza_notes.png")
        self.exitSettings = pygame.Rect(0, 0, self.restartImage.get_width(), self.restartImage.get_height())
        self.exitSettings2 = pygame.Rect(0, 0, self.backImage.get_width(), self.backImage.get_height())
        self.restart = pygame.Rect(0, self.restartImage.get_height(), self.backImage.get_width(), self.backImage.get_height())
        self.middle_restart = pygame.Rect(width/2-self.restartImage.get_width()/2, 350-self.restartImage.get_height()/2, self.backImage.get_width(), self.backImage.get_height())
        self.mainmenu = pygame.Rect(0, self.restartImage.get_height()+self.backImage.get_height(), self.mainmenuImage.get_width(), self.mainmenuImage.get_height())
        self.mainmenu2 = pygame.Rect(0, self.backImage.get_height(), self.mainmenuImage.get_width(), self.mainmenuImage.get_height())
        self.middle_mainmenu = pygame.Rect(width/2-self.mainmenuImage.get_width()/2, 450-self.mainmenuImage.get_height()/2, self.mainmenuImage.get_width(), self.mainmenuImage.get_height())
        self.settings = pygame.Rect(100, 0, self.settingsImage.get_width(), self.settingsImage.get_height())
        self.settings2 = pygame.Rect(1200-self.settingsImage.get_width()-self.helpimage.get_width(), 0, self.settingsImage.get_width(), self.settingsImage.get_height())
        self.musicRect2 = pygame.Rect(0, self.backImage.get_height()+self.mainmenuImage.get_height(), self.musicbutton.get_width(), self.musicbutton.get_height())
        self.pizzaFinishedMenu = pygame.Rect(1200-self.settingsImage.get_width(), 790-self.settingsImage.get_height(), self.settingsImage.get_width(), self.settingsImage.get_height())
        self.metronomeRect = pygame.Rect(0, self.restartImage.get_height()+self.backImage.get_height()+self.mainmenuImage.get_height(), self.musicbutton.get_width(), self.musicbutton.get_height())
        self.helpRect = pygame.Rect(width-self.helpimage.get_width(), 0, self.helpimage.get_width(), self.helpimage.get_height())
        self.backbuttonRect = pygame.Rect(0, height-self.backImage.get_height(), self.backImage.get_width(), self.backImage.get_height())
        self.helpbool = False
        self.settingsClicked = False
        self.settingsClicked2 = False
        self.stagefinished = False
        self.backgroundmusic = True
        self.reset = False
        self.back = False
        self.back2 = False
        self.back3 = False
        self.spaceclicked = False
        self.playMetronome = True
        self.wrongcounter = 0
        self.staff = pygame.sprite.GroupSingle()
        self.stagetimer = 0
        self.WHITE = (255, 255, 255)
        if self.stage == 1:
            self.staff.add(NoteTile((35, 100), (266, 937), False, True, "../resources/beginnerstaff.png"))
        elif self.stage == 2:
            self.staff.add(NoteTile((35, 100), (266, 937), False, True, "../resources/odetojoystaff.png"))
        elif self.stage == 3:
            self.staff.add(NoteTile((35, 100), (266, 937), False, True, "../resources/wheelsstaff.png"))
        elif self.stage == 4:
            self.staff.add(NoteTile((35, 100), (266, 937), False, True, "../resources/twinklestaff.png"))
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

        try:
            for info in layout[self.stage-1]:
                if info[0] == 0.5:
                    index += 1
                    if len(layout[self.stage-1]) == index:
                        last = True
                    offset = 128
                    pos = (offset+pos[0], pos[1]-32)
                    tile = TeleportTile(pos, (tilesize, tilesize), info[1], last, True, "../resources/island2.png")

                    self.tiles.add(tile)
                    last = False

                if info[0] == 1:
                    index += 1
                    if len(layout[self.stage-1]) == index:
                        last = True
                    offset = 192

                    pos = (offset+pos[0], pos[1]-64)
                    tile = TeleportTile(pos, (tilesize, tilesize), info[1], last, True, "../resources/island2.png")
                    self.tiles.add(tile)
                    last = False

                if info[0] == 1.5:
                    index += 1
                    if len(layout[self.stage-1]) == index:
                        last = True
                    offset = 256
                    pos = (offset+pos[0], pos[1]-96)
                    tile = TeleportTile(pos, (tilesize, tilesize), info[1], last, True, "../resources/island2.png")
                    self.tiles.add(tile)
                    last = False

                if info[0] == 2:
                    index += 1
                    if len(layout[self.stage-1]) == index:
                        last = True
                    offset = 320
                    pos = (offset+pos[0], pos[1]-128)
                    tile = TeleportTile(pos, (tilesize, tilesize), info[1], last, True, "../resources/island2.png")
                    self.tiles.add(tile)
                    last = False

                if info[0] == 3:
                    index += 1
                    if len(layout[self.stage-1]) == index:
                        last = True
                    offset = 384
                    pos = (offset+pos[0], pos[1]-192)
                    tile = TeleportTile(pos, (tilesize, tilesize), info[1], last, True, "../resources/island2.png")
                    self.tiles.add(tile)
                    last = False

                if info[0] == 4:
                    index += 1
                    if len(layout[self.stage-1]) == index:
                        last = True
                    offset = 448
                    pos = (offset+pos[0], pos[1]-256)
                    tile = TeleportTile(pos, (tilesize, tilesize), info[1], last, True, "../resources/island2.png")
                    self.tiles.add(tile)
                    last = False

            player_sprite = TeleportPlayer((192, 512), self.DISPLAY_SURFACE)
            self.player.add(player_sprite)

        except:
            self.complete = True

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
        elif player_y < height/2:
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
                note = pygame.font.Font("../resources/PressStart2P.ttf", 40)
                self.note_text = note.render(f'{self.player.sprite.level_note}', True, self.WHITE)
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top + 50
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

                if sprite.note == self.player.sprite.level_note:
                    self.player.sprite.correctnote = True
                else:
                    self.player.sprite.correctnote = False

            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling

    def run(self, delta):
        # tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.tiles.draw(self.DISPLAY_SURFACE)
        self.staff.update(self.h_shift, "x")
        self.staff.draw(self.DISPLAY_SURFACE)
        self.scroll()

        # player
        self.player.update(delta, self.h_shift)
        self.detect_collisions(delta)
        self.on_ground()
        self.player.draw(self.DISPLAY_SURFACE)

        # conditions
                
        if self.stagefinished:
            self.reset = True

        if self.note_text != None:
            self.DISPLAY_SURFACE.blit(self.note_text, (width/2-self.note_text.get_width()/2, 200))
        
        self.DISPLAY_SURFACE.blit(self.settingsImage, (100, 0))

        if self.settingsClicked:
            self.DISPLAY_SURFACE.blit(self.background4Settings, (0, 0))
            self.DISPLAY_SURFACE.blit(self.background4Settings, (0, self.background4Settings.get_height()))
            self.DISPLAY_SURFACE.blit(self.background4Settings, (0, 2*self.background4Settings.get_height()))
            self.DISPLAY_SURFACE.blit(self.backImage, (0, 0))
            self.DISPLAY_SURFACE.blit(self.restartImage, (0, 100))
            self.DISPLAY_SURFACE.blit(self.mainmenuImage, (0, self.restartImage.get_height()+self.backImage.get_height()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart.collidepoint(event.pos):
                        logging.debug("reset")
                        self.reset = True
                        pygame.mixer.Channel(3).stop()
                    if self.mainmenu.collidepoint(event.pos):
                        logging.debug("main menu")
                        self.back = True
                        pygame.mixer.music.stop()
                    if self.exitSettings.collidepoint(event.pos):
                        logging.debug("settings exited")
                        self.settingsClicked = False

        if self.player.sprite.rect.topleft[1] > height:
            self.DISPLAY_SURFACE.blit(self.restartImage, self.middle_restart)
            self.DISPLAY_SURFACE.blit(self.mainmenuImage, self.middle_mainmenu)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.middle_restart.collidepoint(event.pos):
                        logging.debug("reset")
                        self.reset = True
                        pygame.mixer.Channel(3).stop()
                    if self.middle_mainmenu.collidepoint(event.pos):
                        logging.debug("main menu")
                        self.back = True
                        pygame.mixer.music.stop()
        

class NoteLevel(TeleportLevel):
    def __init__(self, level_data, surface, stage, bass=False, infmode = False):
        self.WHITE = (255, 255, 255)
        self.coins_needed = [30, (300, 10)]
        self.ledger = pygame.sprite.GroupSingle()
        self.house = pygame.sprite.GroupSingle()
        self.old_house = pygame.sprite.GroupSingle()
        self.barrier = pygame.sprite.GroupSingle()
        super().__init__(level_data, surface, stage)
        self.chain = False
        self.draw_old = True
        self.draw = True
        self.draw_ledger = False
        self.counter = 0
        self.counterclock = False
        self.playerdelivered = False
        self.playercoins = 0
        self.level_data = level_data
        self.bass = bass
        self.infmode = infmode


    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        player_sprite = NotePlayer((192, 528), self.DISPLAY_SURFACE)
        self.player.add(player_sprite)
        try:
            self.player.sprite.difficulty_time = layout[self.stage-1]
        except:
            self.complete = True

        self.randomize_note()

    def detect_collisions(self):
        player = self.player.sprite
        player.rect.centerx += player.direction.x * player.speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.wrongcounter = 0

        # logging.debug(f'self.note: {self.note}\nself.player.sprite.note: {self.player.sprite.note}')
        if self.note == self.player.sprite.note:
            if self.house.sprite.rect.colliderect(player.rect):
                self.draw_old = False
                self.playerdelivered = True
                if self.coincounter == 0:
                    self.player.sprite.coins = self.playercoins + randint(5, 8)
                    self.playercoins = self.player.sprite.coins
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound('../resources/correct.wav'))
                    self.coincounter = 1
                    self.wrongcounter = 1
                    logging.debug(f'Coins: {self.player.sprite.coins}')
            else:
                self.coincounter = 0
                self.player.sprite.coins = self.playercoins

        if not self.infmode:
            if self.playercoins >= self.coins_needed[0]:
                if self.stagetimer <= 50:
                    self.stagetimer += 1
                    self.DISPLAY_SURFACE.blit(self.stageimage, (0, 0))
                    logging.debug("Feynman is cool ", self.stagetimer)
                else:
                    self.stagetimer = 0
                    self.stage += 1
                    self.stagefinished = True
                    self.reset = True
                    self.playercoins = 0
                    self.DISPLAY_SURFACE.blit(self.pizzaBackground, (0, 0))

        if self.barrier.sprite.rect.colliderect(player.rect):
            self.counterclock = True
            self.old_house.add(self.house.sprite)
            if self.wrongcounter == 0:
                wrong_audiofile = pygame.mixer.Sound('../resources/wrong2.wav')
                wrong_audiofile.set_volume(0.2)
                pygame.mixer.Channel(3).play(wrong_audiofile)
            self.randomize_note()

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
        notes = ["Mid C", "Mid D", "Mid E", "Mid F", "Mid G", "Mid A", "Mid B", "High C", "High D", "High E", "High F", "High G", "High A", "High B", "Max C"]

        note = choice(notes)
        font = pygame.font.Font("../resources/PressStart2P.ttf", 35)
        smallfont = pygame.font.Font("../resources/PressStart2P.ttf", 28)
        self.font3 = pygame.font.Font("../resources/PressStart2P.ttf", 35)
        coins_left = self.coins_needed[0]-self.player.sprite.coins
        self.coins_needed_text = smallfont.render(f'Coins needed: {coins_left}', True, self.WHITE)
        self.note_text = font.render(f'Find {note}', True, self.WHITE)
        self.noteselected_text = font.render("Find ", True, self.WHITE)
        self.note = note
        self.coin_text = font.render(str(self.player.sprite.coins), True, self.WHITE)

        self.player.sprite.pos = (self.player.sprite.rect.centerx, self.player.sprite.rect.centery)

        yResult = noteY[notes.index(note)]
        house = NoteTile((self.player.sprite.pos[0] + 1200, yResult), (64, 64), True, True, "../resources/house.png")
        self.house.add(house)
        barrier = NoteTile((self.house.sprite.pos[0], 0), (1, 704), False, False)
        self.barrier.add(barrier)

    def run(self):
        # background
        self.DISPLAY_SURFACE.blit(self.starbackground, (0, 0))

        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spaceclicked = True
                    self.wrongcounter = 0
                    # logging.debug(f'self.spaceclicked = {self.spaceclicked}\nself.wrongcounter = {self.wrongcounter}')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.settings2.collidepoint(event.pos):
                    self.settingsClicked2 = True
                    logging.debug("settings clicked")
                elif self.helpRect.collidepoint(event.pos):
                    self.helpbool = True
                elif self.backbuttonRect.collidepoint(event.pos):
                    if self.helpbool:
                        self.helpbool = False
                if self.settingsClicked2:
                    if self.mainmenu2.collidepoint(event.pos):
                        logging.debug("main menu")
                        self.back2 = True
                        pygame.mixer.music.stop()
                    elif self.exitSettings2.collidepoint(event.pos):
                        logging.debug("settings exited")
                        self.settingsClicked2 = False
                    elif self.musicRect2.collidepoint(event.pos):
                        if self.backgroundmusic:
                            if self.musicCounter == 0:
                                self.musicCounter+=1
                                self.backgroundmusic = False
                                logging.debug("Physics ", self.musicCounter)
                        elif not self.backgroundmusic:
                            if self.musicCounter == 1:
                                self.musicCounter-=1
                                self.backgroundmusic = True
                                logging.debug("Feynman is cool ", self.musicCounter)
        
        if self.backgroundmusic:
            while not pygame.mixer.music.get_busy():
                pygame.mixer.music.load("../resources/backgroundmusic.wav")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()

        elif not self.backgroundmusic:
            pygame.mixer.music.stop()

        self.DISPLAY_SURFACE.blit(self.pizzaBackground, (0, 0))

        if self.settingsClicked2:
            self.DISPLAY_SURFACE.blit(self.backImage, (0, 0))
            self.DISPLAY_SURFACE.blit(self.mainmenuImage, (0, self.backImage.get_height()))
            self.DISPLAY_SURFACE.blit(self.musicbutton, (0, self.backImage.get_height()+self.mainmenuImage.get_height()))

        # level tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.house.update(self.h_shift, "x")
        self.barrier.update(self.h_shift, "x")
        self.tiles.draw(self.DISPLAY_SURFACE)
        self.house.draw(self.DISPLAY_SURFACE)
        self.DISPLAY_SURFACE.blit(self.settingsImage, self.settings2)
        self.DISPLAY_SURFACE.blit(self.helpimage, self.helpRect)

        if self.old_house != None and self.draw_old:
            self.old_house.update(self.h_shift, "x")
            self.old_house.draw(self.DISPLAY_SURFACE)
        elif not self.draw_old:
            self.draw_old = True
        self.scroll()

        # player
        self.player.update()
        self.detect_collisions()
        self.on_ground()

        if self.draw:
            self.player.draw(self.DISPLAY_SURFACE)
            if not self.infmode:
                self.DISPLAY_SURFACE.blit(self.coins_needed_text, self.coins_needed[1])
            if self.note_text != None:
                self.DISPLAY_SURFACE.blit(self.note_text, (700-self.note_text.get_width()/2, 200))
            if self.coin_text != None:
                self.DISPLAY_SURFACE.blit(self.coins, (self.settingsImage.get_width(), 0))
                self.DISPLAY_SURFACE.blit(self.coin_text, (self.settingsImage.get_width()+self.coins.get_width(), 0))

            
            if self.player.sprite.rect.topleft[1] == 672:
                tile = NoteTile((self.player.sprite.rect.topleft[0]-18+24, self.player.sprite.rect.topleft[1]+22+24), (96, 20), False, False)
                tile.add(self.ledger)
                self.draw_ledger = True
            elif self.player.sprite.rect.topleft[1] == 96:
                tile = NoteTile((self.player.sprite.rect.topleft[0]-18+24, self.player.sprite.rect.topleft[1]+22+24), (96, 20), False, False)
                tile.add(self.ledger)
                self.draw_ledger = True
            elif self.player.sprite.rect.topleft[1] == 48:
                tile = NoteTile((self.player.sprite.rect.topleft[0]-18+24, self.player.sprite.rect.topleft[1]+22+24+48), (96, 20), False, False)
                tile.add(self.ledger)
                self.draw_ledger = True
            elif self.player.sprite.rect.topleft[1] == 0:
                tile = NoteTile((self.player.sprite.rect.topleft[0]-18+24, self.player.sprite.rect.topleft[1]+22+24), (96, 20), False, False)
                tile.add(self.ledger)
                self.draw_ledger = True
            else:
                self.draw_ledger = False

            if not self.player.sprite.ready and self.draw_ledger:
                self.ledger.draw(self.DISPLAY_SURFACE)
        
        if self.counterclock:
            self.counter += 1
            if self.counter >= 20:
                player_sprite = NotePlayer((self.player.sprite.pos), self.DISPLAY_SURFACE)
                self.player.add(player_sprite)
                self.counterclock = False
                self.counter = 0
                self.player.update()
                self.player.sprite.difficulty_time = self.level_data[self.stage-1]
                if not self.playerdelivered:
                    self.player.sprite.delivered = True
                    self.player.update()
                    self.playerdelivered = False

        if self.complete:
            self.counter += 1
            if self.counter >= 20:
                self.DISPLAY_SURFACE.blit(self.pizzaWin, (0, 0))
                self.DISPLAY_SURFACE.blit(self.settingsImage, (1200-self.settingsImage.get_width(), 790-self.settingsImage.get_height()))
                self.draw = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.pizzaFinishedMenu.collidepoint(event.pos):
                            self.back2 = True
                            pygame.mixer.music.stop()
                            
        if self.stage <= 1 and not self.bass:
            if self.player.sprite.pos[1] == 720:
                note_helper = self.font3.render("Mid C", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 672:
                note_helper = self.font3.render("Mid D", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 624:
                note_helper = self.font3.render("Mid E", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 576:
                note_helper = self.font3.render("Mid F", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 528:
                note_helper = self.font3.render("Mid G", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 480:
                note_helper = self.font3.render("Mid A", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 432:
                note_helper = self.font3.render("Mid B", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 384:
                note_helper = self.font3.render("High C", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 336:
                note_helper = self.font3.render("High D", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 288:
                note_helper = self.font3.render("High E", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 240:
                note_helper = self.font3.render("High F", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 192:
                note_helper = self.font3.render("High G", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 144:
                note_helper = self.font3.render("High A", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 96:
                note_helper = self.font3.render("High B", True, self.WHITE)
                highB = 932-note_helper.get_width()
                if self.spaceclicked:
                    logging.debug("highB changed")
                    highB = 850-note_helper.get_width()
                self.DISPLAY_SURFACE.blit(note_helper, (highB, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 48:
                note_helper = self.font3.render("Max C", True, self.WHITE)
                maxC = 900-note_helper.get_width()
                if self.spaceclicked:
                    logging.debug("maxC changed")
                    maxC = 850-note_helper.get_width()
                self.DISPLAY_SURFACE.blit(note_helper, (maxC, self.player.sprite.pos[1]))
        
        if self.stage <= 1 and self.bass:
            if self.player.sprite.pos[1] == 720:
                note_helper = self.font3.render("Min C", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 672:
                note_helper = self.font3.render("Min D", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 624:
                note_helper = self.font3.render("Min E", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 576:
                note_helper = self.font3.render("Min F", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 528:
                note_helper = self.font3.render("Min G", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 480:
                note_helper = self.font3.render("Min A", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 432:
                note_helper = self.font3.render("Min B", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 384:
                note_helper = self.font3.render("Low C", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 336:
                note_helper = self.font3.render("Low D", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 288:
                note_helper = self.font3.render("Low E", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 240:
                note_helper = self.font3.render("Low F", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 192:
                note_helper = self.font3.render("Low G", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 144:
                note_helper = self.font3.render("Low A", True, self.WHITE)
                self.DISPLAY_SURFACE.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 96:
                note_helper = self.font3.render("Low B", True, self.WHITE)
                lowB = 932-note_helper.get_width()
                if self.spaceclicked:
                    logging.debug("lowB changed")
                    lowB = 850-note_helper.get_width()
                self.DISPLAY_SURFACE.blit(note_helper, (lowB, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 48:
                note_helper = self.font3.render("Mid C", True, self.WHITE)
                midC = 900-note_helper.get_width()
                if self.spaceclicked:
                    logging.debug("midC changed")
                    midC = 850-note_helper.get_width()
                self.DISPLAY_SURFACE.blit(note_helper, (midC, self.player.sprite.pos[1]))
        
        if self.helpbool:
            self.DISPLAY_SURFACE.blit(self.helpbg, (0, 0))
            self.DISPLAY_SURFACE.blit(self.backImage, self.backbuttonRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

class BassNoteLevel(NoteLevel):
    def __init__(self, level_data, surface, stage, bass):
        super().__init__(level_data, surface, stage, bass)
    
    def randomize_note(self):
        noteY = [78, 128, 178, 228, 278, 328, 378, 428, 478]

        """pos = (0, 100)
        for i in range(1, 6):
            tile = NoteTile(pos, (9000, 20), "G", False)
            self.tiles.add(tile)
            pos = (pos[0], pos[1]+100"""

        noteY = [698, 650, 602, 554, 506, 458, 410, 362, 314, 266, 218, 170, 122, 74, 26]
        notes = ["Min C", "Min D", "Min E", "Min F", "Min G", "Min A", "Min B", "Low C", "Low D", "Low E", "Low F", "Low G", "Low A", "Low B", "Mid C"]

        note = choice(notes)
        font = pygame.font.Font("../resources/PressStart2P.ttf", 35)
        self.font3 = pygame.font.Font("../resources/PressStart2P.ttf", 35)
        self.note = note
        self.coin_text = font.render(str(self.player.sprite.coins), True, self.WHITE)
        self.note_text = font.render(f'Find {note}', True, self.WHITE)

        self.player.sprite.pos = (self.player.sprite.rect.centerx, self.player.sprite.rect.centery)

        yResult = noteY[notes.index(note)]
        house = NoteTile((self.player.sprite.pos[0] + 1200, yResult), (64, 64), True, True, "../resources/house.png")
        self.house.add(house)
        barrier = NoteTile((self.house.sprite.pos[0], 0), (1, 704), False, False)
        self.barrier.add(barrier)