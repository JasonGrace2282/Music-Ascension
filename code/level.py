import pygame
from sys import exit
from random import randint, choice
from tiles import TeleportTile, NoteTile
from setup import tilesize, width, height
from player import TeleportPlayer, NotePlayer


class TeleportLevel():
    def __init__(self, level_data, surface, stage):

        pygame.mixer.init()

        # level setup and unique variables
        self.display_surface = surface
        self.stage = stage
        self.note_text = None
        self.note = "G"
        self.setup_level(level_data)
        self.staff = pygame.sprite.GroupSingle()

        #Constants
        #Images
        self.SETTINGS_BG_IMG = pygame.image.load("../resources/blank.jpg")
        self.RESTART_IMG = pygame.image.load("../resources/retry2.png")
        self.QUIT_IMG = pygame.image.load("../resources/quit2.png")
        self.SETTINGS_IMG = pygame.image.load("../resources/menubutton2.png")
        self.BACK_IMG = pygame.image.load("../resources/back2.png")
        self.MUSIC_IMG = pygame.image.load("../resources/musicbutton.png")
        self.PIZZA_WIN_IMG = pygame.image.load("../resources/pizza_delivered.png")
        self.COINS_IMG = pygame.image.load("../resources/coins.png")
        self.TREBLE_CLEF_IMG = pygame.image.load("../resources/trebleclef.png")
        self.BASS_CLEF_IMG = pygame.image.load("../resources/bassclef.png")
        self.GRADIENT_IMG = pygame.image.load("../resources/starbg.png")
        self.STAGE_FINISHED_IMG = pygame.image.load("../resources/pizza_delivered.png")
        self.HELP_IMG = pygame.image.load("../resources/help2.png")
        self.HELP_BG = pygame.image.load("../resources/pizza_notes.png")

        #Rects
        self.EXIT_SETTINGS_RECT = pygame.Rect(0, 0, self.RESTART_IMG.get_width(), self.RESTART_IMG.get_height())
        self.EXIT_SETTINGS_RECT2 = pygame.Rect(0, 0, self.BACK_IMG.get_width(), self.BACK_IMG.get_height())
        self.RESTART_RECT = pygame.Rect(0, self.RESTART_IMG.get_height(), self.BACK_IMG.get_width(), self.BACK_IMG.get_height())
        self.MIDDLE_RESTART_RECT = pygame.Rect(width/2-self.RESTART_IMG.get_width()/2, 350-self.RESTART_IMG.get_height()/2, self.BACK_IMG.get_width(), self.BACK_IMG.get_height())
        self.MAIN_MENU_RECT = pygame.Rect(0, self.RESTART_IMG.get_height()+self.BACK_IMG.get_height(), self.QUIT_IMG.get_width(), self.QUIT_IMG.get_height())
        self.MAIN_MENU_RECT2 = pygame.Rect(0, self.BACK_IMG.get_height(), self.QUIT_IMG.get_width(), self.QUIT_IMG.get_height())
        self.MIDDLE_MAIN_MENU_RECT = pygame.Rect(width/2-self.QUIT_IMG.get_width()/2, 450-self.QUIT_IMG.get_height()/2, self.QUIT_IMG.get_width(), self.QUIT_IMG.get_height())
        self.SETTINGS_RECT = pygame.Rect(100, 0, self.SETTINGS_IMG.get_width(), self.SETTINGS_IMG.get_height())
        self.SETTINGS_RECT2 = pygame.Rect(1200-self.SETTINGS_IMG.get_width()-self.HELP_IMG.get_width(), 0, self.SETTINGS_IMG.get_width(), self.SETTINGS_IMG.get_height())
        self.MUSIC_RECT = pygame.Rect(0, self.BACK_IMG.get_height()+self.QUIT_IMG.get_height(), self.MUSIC_IMG.get_width(), self.MUSIC_IMG.get_height())
        self.PIZZA_FINISHED_RECT = pygame.Rect(1200-self.SETTINGS_IMG.get_width(), 790-self.SETTINGS_IMG.get_height(), self.SETTINGS_IMG.get_width(), self.SETTINGS_IMG.get_height())
        self.HELP_RECT = pygame.Rect(width-self.HELP_IMG.get_width(), 0, self.HELP_IMG.get_width(), self.HELP_IMG.get_height())
        self.BACK_RECT = pygame.Rect(0, height-self.BACK_IMG.get_height(), self.BACK_IMG.get_width(), self.BACK_IMG.get_height())

        #colors
        self.WHITE_COLOR = (255, 255, 255)
        
        #Variables
        #Booleans
        self.complete = False
        self.player_on_ground = False
        self.help_bool = False
        self.inf_mode = False
        self.settings_clicked = False
        self.settings_clicked2 = False
        self.stage_finished = False
        self.reset = False
        self.back = False
        self.back2 = False
        self.back3 = False
        self.space_clicked = False
        self.background_music = True
        self.play_metronome = True

        #Integers
        self.wrong_counter = 0
        self.h_shift = 0
        self.v_shift = 0
        self.current_x = 0
        self.music_counter = 0
        self.stage_timer = 0

        if self.stage == 1:
            self.staff.add(NoteTile((35, 10), (266, 937), False, True, "../resources/beginnerstaff.png"))
        elif self.stage == 2:
            self.staff.add(NoteTile((35, 10), (266, 937), False, True, "../resources/odetojoystaff.png"))
        elif self.stage == 3:
            self.staff.add(NoteTile((35, 10), (266, 937), False, True, "../resources/wheelsstaff.png"))
        elif self.stage == 4:
            self.staff.add(NoteTile((35, 10), (266, 937), False, True, "../resources/twinklestaff.png"))

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
                    self.stage_finished = True
                    sprite.is_last = False
                note = pygame.font.Font("../resources/PressStart2P.ttf", 40)
                self.note_text = note.render(f'{self.player.sprite.level_note}', True, self.WHITE_COLOR)
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
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
        self.tiles.draw(self.display_surface)
        self.staff.update(self.h_shift, "x")
        self.staff.draw(self.display_surface)
        self.scroll()

        # player
        self.player.update(delta, self.h_shift)
        self.detect_collisions(delta)
        self.on_ground()
        self.player.draw(self.display_surface)

        # conditions
                
        if self.stage_finished:
            self.reset = True

        if self.note_text != None:
            self.display_surface.blit(self.note_text, (width/2-self.note_text.get_width()/2, 200))
        
        self.display_surface.blit(self.SETTINGS_IMG, (100, 0))

        if self.settings_clicked:
            self.display_surface.blit(self.SETTINGS_BG_IMG, (0, 0))
            self.display_surface.blit(self.SETTINGS_BG_IMG, (0, self.SETTINGS_BG_IMG.get_height()))
            self.display_surface.blit(self.SETTINGS_BG_IMG, (0, 2*self.SETTINGS_BG_IMG.get_height()))
            self.display_surface.blit(self.BACK_IMG, (0, 0))
            self.display_surface.blit(self.RESTART_IMG, (0, 100))
            self.display_surface.blit(self.QUIT_IMG, (0, self.RESTART_IMG.get_height()+self.BACK_IMG.get_height()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.RESTART_RECT.collidepoint(event.pos):
                        print("reset")
                        self.reset = True
                        pygame.mixer.Channel(3).stop()
                    if self.MAIN_MENU_RECT.collidepoint(event.pos):
                        print("main menu")
                        self.back = True
                        pygame.mixer.music.stop()
                    if self.EXIT_SETTINGS_RECT.collidepoint(event.pos):
                        print("SETTINGS_RECT exited")
                        self.settings_clicked = False

        if self.player.sprite.rect.topleft[1] > height:
            self.display_surface.blit(self.RESTART_IMG, self.MIDDLE_RESTART_RECT)
            self.display_surface.blit(self.QUIT_IMG, self.MIDDLE_MAIN_MENU_RECT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.MIDDLE_RESTART_RECT.collidepoint(event.pos):
                        print("reset")
                        self.reset = True
                        pygame.mixer.Channel(3).stop()
                    if self.MIDDLE_MAIN_MENU_RECT.collidepoint(event.pos):
                        print("main menu")
                        self.back = True
                        pygame.mixer.music.stop()


class NoteLevel(TeleportLevel):
    def __init__(self, level_data, surface, stage, bass=False):
        self.WHITE_COLOR = (255, 255, 255)
        self.COINS_IMG_needed = [30, (300, 10)]
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
        self.playerCOINS_IMG = 0
        self.level_data = level_data
        self.bass = bass


    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        player_sprite = NotePlayer((192, 528), self.display_surface)
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
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.wrong_counter = 0

        # print(f'self.note: {self.note}\nself.player.sprite.note: {self.player.sprite.note}')
        if self.note == self.player.sprite.note:
            if self.house.sprite.rect.colliderect(player.rect):
                self.draw_old = False
                self.playerdelivered = True
                if self.coincounter == 0:
                    self.player.sprite.coins = self.playerCOINS_IMG + randint(5, 8)
                    self.playerCOINS_IMG = self.player.sprite.coins
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound('../resources/correct.wav'))
                    self.coincounter = 1
                    self.wrong_counter = 1
                    print(f'Coins: {self.player.sprite.coins}')
            else:
                self.coincounter = 0
                self.player.sprite.coins = self.playerCOINS_IMG

        if not self.inf_mode:
            if self.playerCOINS_IMG >= self.COINS_IMG_needed[0]:
                if self.stage_timer <= 50:
                    self.stage_timer += 1
                    self.display_surface.blit(self.STAGE_FINISHED_IMG, (0, 0))
                    print("Feynman is cool ", self.stage_timer)
                else:
                    self.stage_timer = 0
                    self.stage += 1
                    self.stage_finished = True
                    self.reset = True
                    self.playerCOINS_IMG = 0
                    self.display_surface.blit(self.TREBLE_CLEF_IMG, (0, 0))

        if self.barrier.sprite.rect.colliderect(player.rect):
            self.counterclock = True
            self.old_house.add(self.house.sprite)
            if self.wrong_counter == 0:
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
        COINS_IMG_left = self.COINS_IMG_needed[0]-self.player.sprite.coins
        self.COINS_IMG_needed_text = smallfont.render(f'Coins needed: {COINS_IMG_left}', True, self.WHITE_COLOR)
        self.note_text = font.render(f'Find {note}', True, self.WHITE_COLOR)
        self.noteselected_text = font.render("Find ", True, self.WHITE_COLOR)
        self.note = note
        self.coin_text = font.render(str(self.player.sprite.coins), True, self.WHITE_COLOR)

        self.player.sprite.pos = (self.player.sprite.rect.centerx, self.player.sprite.rect.centery)

        yResult = noteY[notes.index(note)]
        house = NoteTile((self.player.sprite.pos[0] + 1200, yResult), (64, 64), True, True, "../resources/house.png")
        self.house.add(house)
        barrier = NoteTile((self.house.sprite.pos[0], 0), (1, 704), False, False)
        self.barrier.add(barrier)

    def run(self):
        # background
        self.display_surface.blit(self.GRADIENT_IMG, (0, 0))

        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.space_clicked = True
                    self.wrong_counter = 0
                    # print(f'self.space_clicked = {self.space_clicked}\nself.wrong_counter = {self.wrong_counter}')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.SETTINGS_RECT2.collidepoint(event.pos):
                    self.settings_clicked2 = True
                    print("SETTINGS_RECT clicked")
                elif self.HELP_RECT.collidepoint(event.pos):
                    self.help_bool = True
                elif self.BACK_RECT.collidepoint(event.pos):
                    if self.help_bool:
                        self.help_bool = False
                if self.settings_clicked2:
                    if self.MAIN_MENU_RECT2.collidepoint(event.pos):
                        print("main menu")
                        self.back2 = True
                        pygame.mixer.music.stop()
                    elif self.EXIT_SETTINGS_RECT2.collidepoint(event.pos):
                        print("SETTINGS_RECT exited")
                        self.settings_clicked2 = False
                    elif self.MUSIC_RECT.collidepoint(event.pos):
                        if self.background_music:
                            if self.music_counter == 0:
                                self.music_counter+=1
                                self.background_music = False
                                print("Physics ", self.music_counter)
                        elif not self.background_music:
                            if self.music_counter == 1:
                                self.music_counter-=1
                                self.background_music = True
                                print("Feynman is cool ", self.music_counter)
        
        if self.background_music:
            while not pygame.mixer.music.get_busy():
                pygame.mixer.music.load("../resources/backgroundmusic.wav")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()

        elif not self.background_music:
            pygame.mixer.music.stop()

        self.display_surface.blit(self.TREBLE_CLEF_IMG, (0, 0))

        if self.settings_clicked2:
            self.display_surface.blit(self.BACK_IMG, (0, 0))
            self.display_surface.blit(self.QUIT_IMG, (0, self.BACK_IMG.get_height()))
            self.display_surface.blit(self.MUSIC_IMG, (0, self.BACK_IMG.get_height()+self.QUIT_IMG.get_height()))

        # level tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.house.update(self.h_shift, "x")
        self.barrier.update(self.h_shift, "x")
        self.tiles.draw(self.display_surface)
        self.house.draw(self.display_surface)
        self.display_surface.blit(self.SETTINGS_IMG, self.SETTINGS_RECT2)
        self.display_surface.blit(self.HELP_IMG, self.HELP_RECT)

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

        if self.draw:
            self.player.draw(self.display_surface)
            if not self.inf_mode:
                self.display_surface.blit(self.COINS_IMG_needed_text, self.COINS_IMG_needed[1])
            if self.note_text != None:
                self.display_surface.blit(self.note_text, (700-self.note_text.get_width()/2, 200))
            if self.coin_text != None:
                self.display_surface.blit(self.COINS_IMG, (self.SETTINGS_IMG.get_width(), 0))
                self.display_surface.blit(self.coin_text, (self.SETTINGS_IMG.get_width()+self.COINS_IMG.get_width(), 0))

            
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
                self.ledger.draw(self.display_surface)
        
        if self.counterclock:
            self.counter += 1
            if self.counter >= 20:
                player_sprite = NotePlayer((self.player.sprite.pos), self.display_surface)
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
                self.display_surface.blit(self.PIZZA_WIN_IMG, (0, 0))
                self.display_surface.blit(self.SETTINGS_IMG, (1200-self.SETTINGS_IMG.get_width(), 790-self.SETTINGS_IMG.get_height()))
                self.draw = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.PIZZA_FINISHED_RECT.collidepoint(event.pos):
                            self.back2 = True
                            pygame.mixer.music.stop()
                            
        if self.stage <= 1 and not self.bass:
            if self.player.sprite.pos[1] == 720:
                note_helper = self.font3.render("Mid C", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 672:
                note_helper = self.font3.render("Mid D", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 624:
                note_helper = self.font3.render("Mid E", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 576:
                note_helper = self.font3.render("Mid F", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 528:
                note_helper = self.font3.render("Mid G", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 480:
                note_helper = self.font3.render("Mid A", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 432:
                note_helper = self.font3.render("Mid B", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 384:
                note_helper = self.font3.render("High C", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 336:
                note_helper = self.font3.render("High D", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 288:
                note_helper = self.font3.render("High E", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 240:
                note_helper = self.font3.render("High F", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 192:
                note_helper = self.font3.render("High G", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 144:
                note_helper = self.font3.render("High A", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 96:
                note_helper = self.font3.render("High B", True, self.WHITE_COLOR)
                highB = 932-note_helper.get_width()
                if self.space_clicked:
                    print("highB changed")
                    highB = 850-note_helper.get_width()
                self.display_surface.blit(note_helper, (highB, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 48:
                note_helper = self.font3.render("Max C", True, self.WHITE_COLOR)
                maxC = 900-note_helper.get_width()
                if self.space_clicked:
                    print("maxC changed")
                    maxC = 850-note_helper.get_width()
                self.display_surface.blit(note_helper, (maxC, self.player.sprite.pos[1]))
        
        if self.stage <= 1 and self.bass:
            if self.player.sprite.pos[1] == 720:
                note_helper = self.font3.render("Min C", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 672:
                note_helper = self.font3.render("Min D", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 624:
                note_helper = self.font3.render("Min E", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 576:
                note_helper = self.font3.render("Min F", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 528:
                note_helper = self.font3.render("Min G", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 480:
                note_helper = self.font3.render("Min A", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 432:
                note_helper = self.font3.render("Min B", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 384:
                note_helper = self.font3.render("Low C", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 336:
                note_helper = self.font3.render("Low D", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 288:
                note_helper = self.font3.render("Low E", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 240:
                note_helper = self.font3.render("Low F", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 192:
                note_helper = self.font3.render("Low G", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 144:
                note_helper = self.font3.render("Low A", True, self.WHITE_COLOR)
                self.display_surface.blit(note_helper, (956, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 96:
                note_helper = self.font3.render("Low B", True, self.WHITE_COLOR)
                lowB = 932-note_helper.get_width()
                if self.space_clicked:
                    print("lowB changed")
                    lowB = 850-note_helper.get_width()
                self.display_surface.blit(note_helper, (lowB, self.player.sprite.pos[1]))
            elif self.player.sprite.pos[1] == 48:
                note_helper = self.font3.render("Mid C", True, self.WHITE_COLOR)
                midC = 900-note_helper.get_width()
                if self.space_clicked:
                    print("midC changed")
                    midC = 850-note_helper.get_width()
                self.display_surface.blit(note_helper, (midC, self.player.sprite.pos[1]))
        
        if self.help_bool:
            self.display_surface.blit(self.HELP_BG, (0, 0))
            self.display_surface.blit(self.BACK_IMG, self.BACK_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

class BassNoteLevel(NoteLevel):
    def __init__(self, level_data, surface, stage, bass):
        super().__init__(level_data, surface, stage, bass)
        smallfont = pygame.font.Font("../resources/PressStart2P.ttf", 28)
        self.COINS_IMG_needed_text = smallfont.render(f'Coins needed: {COINS_IMG_left}', True, self.WHITE_COLOR)
    
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
        self.coin_text = font.render(str(self.player.sprite.coins), True, self.WHITE_COLOR)
        self.note_text = font.render(f'Find {note}', True, self.WHITE_COLOR)

        self.player.sprite.pos = (self.player.sprite.rect.centerx, self.player.sprite.rect.centery)

        yResult = noteY[notes.index(note)]
        house = NoteTile((self.player.sprite.pos[0] + 1200, yResult), (64, 64), True, True, "../resources/house.png")
        self.house.add(house)
        barrier = NoteTile((self.house.sprite.pos[0], 0), (1, 704), False, False)
        self.barrier.add(barrier)