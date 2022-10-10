import pygame
import logging as lg
from time import sleep, perf_counter
from tkinter import Tk
from setup import teleportlevel1, height, width, notelevel1
from level import TeleportLevel, NoteLevel, BassNoteLevel

# Main class

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        pygame.display.set_caption("Music Ascension")

        # logging
        lg.basicConfig(level=lg.DEBUG)
        
        # Screen
        self.SCREEN = pygame.display.set_mode((width, height))
        self.level = TeleportLevel(teleportlevel1, self.SCREEN, 1)

        # Background/Constants
        self.FRONT_PAGE = pygame.image.load("../resources/frontpage.png")
        self.LVL_BG = pygame.image.load("../resources/background.jpg")
        self.ADV_IMAGE = pygame.image.load("../resources/Advanced.png")
        self.START_BUTTON_IMAGE = pygame.image.load("../resources/start.png")
        self.CREDITS_IMAGE = pygame.image.load("../resources/credits.png")
        self.NEXT_IMAGE = pygame.image.load("../resources/next3.png")
        self.BEGINNER_MAP_IMAGE = pygame.image.load("../resources/beginnermap.png")
        self.BEGINNER_TOPIC_IMAGE = pygame.image.load("../resources/beginnertopics.png")
        self.BEGINNER_IMAGE = pygame.image.load("../resources/beginner.png")
        self.NOTE_DURATION_NOTES_IMG = pygame.image.load("../resources/NDNotes.jpg")
        self.NOTE_DURATION_NOTES_IMG_2 = pygame.image.load("../resources/NDdirections.png")
        self.PLAY_IMAGE = pygame.image.load("../resources/play.png")
        self.ADV_MAP_IMAGE = pygame.image.load("../resources/WorkInProgress.jpg")
        self.BACK_IMAGE = pygame.image.load("../resources/back3.png")
        self.COPY_BUTTON_IMAGE = pygame.image.load("../resources/copybutton3.png")
        self.PIZZA_NOTES_IMG = pygame.image.load("../resources/treble_notes.png")
        self.PIZZA_NOTES_IMG_2 = pygame.image.load("../resources/pizza_notes.png")
        self.CREDITS_BG = pygame.image.load("../resources/creditsbackground.png")
        self.MUSIC_IMAGE = pygame.image.load("../resources/musicbutton.png")
        self.HELP_IMAGE = pygame.image.load("../resources/help2.png")
        self.NOTE_DURATION_BG = pygame.image.load("../resources/NDbackground2.png")
        self.HELP_BG = pygame.image.load("../resources/helpbg.png")

        # Variables

        # Booleans
        booleans = [False]*23+[True]
        self.start_game, self.adv_clicked, self.credits_clicked, self.off_credits, self.beginner_clicked, self.choose_beginner_lvl, self.pizza_notes, \
            self.note_duration_notes, self.level_1_picked, self.level_2_picked, self.level_3_picked, self.level_4_picked, self.inf_clicked, \
                self.note_duration_notes_2, self.adv_map, self.note_duration_lvl_2, self.pizza_level_3, self.copied, self.pizza_notes_2, \
                    self.note_duration_audio, self.help_bool, self.done, self.bass, self.home_music = booleans

        # integers
        zero = [0]*13
        self.sleep_counter_1, self.sleep_counter_2, self.sleep_counter_3, self.sleep_counter_4, self.sleep_counter_5, self.next_counter, self.next_counter_2,\
            self.complete_counter, self.counter, self.credits_counter, self.home_music_counter, self.start, self.end = zero
        
        # Constants
        self.BEGINNER_RECT = pygame.Rect(600-self.BEGINNER_IMAGE.get_width()/2, 50, self.BEGINNER_IMAGE.get_width(), self.BEGINNER_IMAGE.get_height())
        self.START_RECT = pygame.Rect(540, 200, self.START_BUTTON_IMAGE.get_width(), self.START_BUTTON_IMAGE.get_height())
        self.INF_RECT = pygame.Rect(600-self.ADV_IMAGE.get_width()/2, 400, self.ADV_IMAGE.get_width(), self.ADV_IMAGE.get_height())
        self.CREDITS_RECT = pygame.Rect(530, 300, self.CREDITS_IMAGE.get_width(), self.CREDITS_IMAGE.get_height())
        self.NEXT_RECT = pygame.Rect(width-self.NEXT_IMAGE.get_width(), height-self.NEXT_IMAGE.get_height(), self.NEXT_IMAGE.get_width(), self.NEXT_IMAGE.get_height())
        self.LVL_1_RECT = pygame.Rect(28, 341, 139, 188)
        self.LVL_2_RECT = pygame.Rect(225, 340, 135, 185)
        self.EIGHTH_RECT = pygame.Rect(1038, 330, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.QUARTER_RECT = pygame.Rect(461, 65, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.HALF_RECT = pygame.Rect(1038, 65, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.WHOLE_RECT = pygame.Rect(461, 330, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.LVL_3_RECT = pygame.Rect(830, 340, 140, 215)
        self.LVL_4_RECT = pygame.Rect(1015, 340, 140, 215)
        self.BACK_RECT = pygame.Rect(0, height-self.BACK_IMAGE.get_height(), self.BACK_IMAGE.get_width(), self.BACK_IMAGE.get_height())
        self.COPY_RECT = pygame.Rect(600-self.COPY_BUTTON_IMAGE.get_width()/2, height/2-100, self.COPY_BUTTON_IMAGE.get_width(), self.COPY_BUTTON_IMAGE.get_width())
        self.MUSIC_RECT = pygame.Rect(0, height-self.MUSIC_IMAGE.get_height(), self.MUSIC_IMAGE.get_width(), self.MUSIC_IMAGE.get_height())
        self.HELP_RECT = pygame.Rect(width-self.HELP_IMAGE.get_width(), 0, self.HELP_IMAGE.get_width(), self.HELP_IMAGE.get_height())
        self.WHITE_COLOR = (255, 255, 255)

    def main(self):
        lg.info(f"\nHello and Welcome to Music Ascension! To enjoy the full game, please change your screen scale to 100% through Settings->Display->Scale and Layout.\
        \nThe dimensions of this window are {width}x{height}\nThis game is not finished yet, so some features may not work. Read the README.md file for more info.")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start = perf_counter()
                        self.done = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.end = perf_counter()
                        self.done = True
                        lg.debug(round(self.end - self.start, 1))

            if self.home_music:
                while not pygame.mixer.Channel(4).get_busy():
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound("../resources/backgroundmusic3.wav"))
                    pygame.mixer.Channel(4).set_volume(10)
            else:
                pygame.mixer.Channel(4).stop()

            self.SCREEN.fill(0)
            self.SCREEN.blit(self.FRONT_PAGE, (0, 0))
            self.SCREEN.blit(self.START_BUTTON_IMAGE, (540, 200))
            self.SCREEN.blit(self.CREDITS_IMAGE, (530, 300))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.START_RECT.collidepoint(event.pos):
                    self.start_game = True
                    sleep(0.5)
                    self.off_credits = True
                if self.CREDITS_RECT.collidepoint(event.pos):
                    self.credits_clicked = True

            if self.start_game:
                self.SCREEN.fill(0)
                self.SCREEN.blit(self.LVL_BG, (0, 0))
                self.SCREEN.blit(self.BEGINNER_IMAGE,(600-self.BEGINNER_IMAGE.get_width()/2, 50))
                self.SCREEN.blit(self.ADV_IMAGE, (600-self.ADV_IMAGE.get_width()/2, 400, self.ADV_IMAGE.get_width(), self.ADV_IMAGE.get_height()))
                self.SCREEN.blit(self.MUSIC_IMAGE, (0, height-self.MUSIC_IMAGE.get_height()))

            if not self.off_credits:
                if self.credits_clicked:
                    self.home_music = False
                    self.SCREEN.fill(self.WHITE_COLOR)
                    self.SCREEN.blit(self.CREDITS_BG, (0, 0))
                    self.SCREEN.blit(self.COPY_BUTTON_IMAGE, self.COPY_RECT)
                    self.SCREEN.blit(self.BACK_IMAGE, self.BACK_RECT)
                    while not pygame.mixer.music.get_busy():
                        pygame.mixer.music.load("../resources/backgroundmusic2.wav")
                        pygame.mixer.music.play()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.credits_clicked = False
                            self.copied = False
                            self.home_music = True
                            self.credits_counter = 0
                            pygame.mixer.music.stop()
                        if self.COPY_RECT.collidepoint(event.pos) and self.credits_counter == 1:
                            clipboard = Tk()
                            clipboard.withdraw()
                            clipboard.clipboard_clear()
                            clipboard.clipboard_append('https://docs.google.com/document/d/1THAizjwlYdVoINJjOBudmcoIM79gEhlbue3cjW5E7r0/edit?usp=sharing')
                            clipboard.update()
                            clipboard.destroy()
                            lg.info("Copied to clipboard")
                            self.copied = True
                            
                    if event.type == pygame.MOUSEBUTTONDOWN and self.credits_counter != 1 and self.COPY_RECT.collidepoint(event.pos):
                        self.credits_counter = 1

                    if self.copied:
                        copiedtext = (pygame.font.Font("../resources/PressStart2P.ttf", 40)).render('Link copied to Clipboard', True, (0, 0, 255))
                        self.SCREEN.blit(copiedtext, (600-copiedtext.get_width()/2, height/2+200))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_game:
                    if self.BEGINNER_RECT.collidepoint(event.pos):
                        self.beginner_clicked = True
                    elif self.INF_RECT.collidepoint(event.pos):
                        self.inf_clicked = True
                        self.level_1_picked = True
                        self.level.inf_mode = True
                        lg.debug("e")              

            if self.start_game:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.MUSIC_RECT.collidepoint(event.pos) and not self.help_bool:
                        lg.debug("Music Button Clicked")
                        if self.home_music and not self.beginner_clicked:
                            if self.home_music_counter == 0:
                                self.home_music_counter+=1
                                self.home_music = False
                                lg.debug("Music is Sine waves ", self.home_music_counter)
                                pygame.time.delay(200)
                        elif not self.home_music:
                            if self.home_music_counter == 1:
                                self.home_music_counter-=1
                                self.home_music = True
                                lg.debug("Chaos Theory is fluid mechanics ", self.home_music_counter)
                                pygame.time.delay(200)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.NEXT_RECT.collidepoint(event.pos):
                        self.adv_map = True
                    if self.BACK_RECT.collidepoint(event.pos):
                        self.adv_clicked = False

                if self.beginner_clicked:
                    self.SCREEN.fill(self.WHITE_COLOR)
                    self.SCREEN.blit(self.BEGINNER_TOPIC_IMAGE, (0, 0))
                    self.SCREEN.blit(self.NEXT_IMAGE, self.NEXT_RECT)
                    self.SCREEN.blit(self.BACK_IMAGE, self.BACK_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            self.choose_beginner_lvl = True
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.beginner_clicked = False

                if self.adv_map:
                    self.SCREEN.fill("white")
                    self.SCREEN.blit(self.ADV_MAP_IMAGE, (0, 0))
                    self.SCREEN.blit(self.BACK_IMAGE, self.BACK_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.adv_clicked = False
                            self.adv_map = False

                if self.choose_beginner_lvl:
                    self.SCREEN.blit(self.BEGINNER_MAP_IMAGE, (0, 0))
                    self.SCREEN.blit(self.HELP_IMAGE, self.HELP_RECT)
                    while self.sleep_counter_4 == 0:
                        sleep(0.3)
                        self.sleep_counter_4+=1

                if event.type == pygame.MOUSEBUTTONDOWN and self.choose_beginner_lvl:
                    if self.LVL_1_RECT.collidepoint(event.pos):
                        self.pizza_notes = True
                        self.bass = False
                        lg.debug("1")
                    elif self.LVL_2_RECT.collidepoint(event.pos):
                        self.note_duration_notes = True
                        self.bass = False
                        lg.debug("2")
                    elif self.LVL_3_RECT.collidepoint(event.pos):
                        self.pizza_notes = True
                        self.bass = True
                        lg.debug("3")
                    elif self.LVL_4_RECT.collidepoint(event.pos):
                        self.note_duration_notes = True
                        self.bass = True
                        lg.debug("4")
                    elif self.HELP_RECT.collidepoint(event.pos):
                        self.help_bool = True
                        self.sleep_counter_5 == 0
                        lg.debug("w")
                
                if self.pizza_notes:
                    self.SCREEN.blit(self.PIZZA_NOTES_IMG, (0, 0))
                    self.SCREEN.blit(self.NEXT_IMAGE, self.NEXT_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.choose_beginner_lvl:
                                self.pizza_notes_2 = True
                                while self.sleep_counter_3 == 0:
                                    sleep(0.2)
                                    self.sleep_counter_3 = 1
                
                if self.pizza_notes_2:
                    self.SCREEN.fill(0)
                    self.SCREEN.blit(self.PIZZA_NOTES_IMG_2, (0, 0))
                    self.SCREEN.blit(self.NEXT_IMAGE, self.NEXT_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.choose_beginner_lvl and self.next_counter_2 == 1:
                                if self.bass:
                                    self.level_3_picked = True
                                else:
                                    self.level_1_picked = True
                            if self.next_counter_2 == 0:
                                self.next_counter_2 = 1
                
                if self.note_duration_notes:
                    self.SCREEN.fill(self.WHITE_COLOR)
                    self.SCREEN.blit(self.NOTE_DURATION_NOTES_IMG, (0, 0))
                    self.SCREEN.blit(self.PLAY_IMAGE, self.QUARTER_RECT)
                    self.SCREEN.blit(self.PLAY_IMAGE, self.WHOLE_RECT)
                    self.SCREEN.blit(self.PLAY_IMAGE, self.HALF_RECT)
                    self.SCREEN.blit(self.PLAY_IMAGE, self.EIGHTH_RECT)
                    self.SCREEN.blit(self.NEXT_IMAGE, self.NEXT_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            self.note_duration_notes_2 = True

                        elif self.QUARTER_RECT.collidepoint(event.pos):
                            self.home_music = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/quarter_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.WHOLE_RECT.collidepoint(event.pos):
                            self.home_music = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/whole_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.HALF_RECT.collidepoint(event.pos):
                            self.home_music = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/half_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.EIGHTH_RECT.collidepoint(event.pos):
                            self.home_music = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/eighth_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                if self.note_duration_notes_2:
                    self.SCREEN.blit(self.NOTE_DURATION_NOTES_IMG_2, (0, 0))
                    self.SCREEN.blit(self.NEXT_IMAGE, self.NEXT_RECT)
                    if self.sleep_counter_1 == 0:
                        sleep(0.2)
                        self.sleep_counter_1 = 1

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.next_counter == 1:
                                if self.bass:
                                    self.level_4_picked = True
                                else:
                                    self.level_2_picked = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.next_counter == 0:
                                self.next_counter+=1
                            
                if self.help_bool:
                    self.SCREEN.fill(0)
                    self.SCREEN.blit(self.HELP_BG, (0, 0))
                    self.SCREEN.blit(self.BACK_IMAGE, self.BACK_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.help_bool = False
                            while self.sleep_counter_5 == 0:
                                pygame.time.delay(250)
                                self.sleep_counter_5+=1                    
               
                if self.level_1_picked and self.counter == 0:
                    self.level = NoteLevel(notelevel1, self.SCREEN, self.level.stage)
                    self.counter = 1

                if self.level_1_picked:
                    self.home_music = False
                    self.SCREEN.fill("black")
                    self.level.run()
                    if self.level.reset and self.level.stage_finished:
                        self.complete_counter += 1
                        if self.complete_counter >= 20:
                            self.level.run()
                            self.level = NoteLevel(notelevel1, self.SCREEN, self.level.stage)
                            self.complete_counter = 0
                    elif self.level.chain:
                        self.level_1_picked = False
                        self.pizza_notes = False
                        self.counter = 0
                    if self.level.back2 == True:
                        self.level_1_picked = False
                        self.pizza_notes = False
                        self.pizza_notes_2 = False
                        self.level.back2 = False
                        self.level.settings_clicked2 = False
                        self.counter = 0
                        self.level.background_music = True
                        self.home_music = True
                        pygame.mixer.music.stop()

                if self.level_2_picked and self.counter == 0:
                    self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    self.counter = 1

                if self.level_2_picked:
                    self.home_music = False
                    self.level.play_metronome = True
                    self.SCREEN.fill("black")
                    self.SCREEN.blit(self.NOTE_DURATION_BG, (0, 0))
                    try:
                        self.level.run(self.end-self.start)
                    except:
                        lg.error(f'self.end-self.start failed. self.end-self.start={self.end-self.start}')
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                        self.level_2_picked = False
                        self.note_duration_notes_2 = False
                        self.note_duration_notes = False
                        self.counter = 0
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                    if self.level.reset and self.level.stage_finished:
                        self.level.run(self.end-self.start)
                        while self.sleep_counter_2 == 0:
                            sleep(1)
                            self.sleep_counter_2 = 1
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    elif self.level.reset:
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    elif self.level.back:
                        self.level_2_picked = False
                        self.note_duration_notes_2 = False
                        self.note_duration_notes = False
                        self.counter = 0
                        self.note_duration_lvl_2 = False
                        self.inf_clicked = False
                        self.LVL_3_RECTclicked = False
                        self.pizza_level_3 = False
                        self.level.play_metronome = False
                        self.home_music = True
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                        pygame.mixer.Channel(3).stop()

                    if not pygame.mixer.Channel(0).get_busy():
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('../resources/drum3.wav'))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.level.SETTINGS_RECT.collidepoint(event.pos):
                            self.level.settings_clicked = True
                    
                if self.level_3_picked and self.counter == 0:
                    self.level = BassNoteLevel(notelevel1, self.SCREEN, self.level.stage, True)
                    self.counter = 1
                    lg.debug('e')

                if self.level_3_picked:
                    self.home_music = False
                    self.SCREEN.fill("black")
                    self.level.run()
                    if self.level.reset and self.level.stage_finished:
                        self.complete_counter += 1
                        if self.complete_counter >= 20:
                            self.level.run()
                            self.level = BassNoteLevel(notelevel1, self.SCREEN, self.level.stage)
                            self.complete_counter = 0
                    elif self.level.chain:
                        self.level_3_picked = False
                        self.pizza_notes = False
                        self.counter = 0
                    if self.level.back2 == True:
                        self.level_3_picked = False
                        self.pizza_notes = False
                        self.pizza_notes_2 = False
                        self.level.back2 = False
                        self.level.settings_clicked2 = False
                        self.counter = 0
                        self.home_music = True
                        pygame.mixer.music.stop()
                
                if self.level_4_picked and self.counter == 0:
                    self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    self.counter = 1

                if self.level_4_picked:
                    self.home_music = False
                    self.level.play_metronome = True
                    self.SCREEN.fill("black")
                    self.SCREEN.blit(self.NOTE_DURATION_BG, (0, 0))
                    try:
                        self.level.run(self.end-self.start)
                    except:
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                        self.level_2_picked = False
                        self.note_duration_notes_2 = False
                        self.note_duration_notes = False
                        self.counter = 0
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                    if self.level.reset and self.level.stage_finished:
                        self.level.run(self.end-self.start)
                        while self.sleep_counter_2 == 0:
                            sleep(1)
                            self.sleep_counter_2 = 1
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    elif self.level.reset:
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    elif self.level.back:
                        self.level_2_picked = False
                        self.note_duration_notes_2 = False
                        self.note_duration_notes = False
                        self.counter = 0
                        self.note_duration_lvl_2 = False
                        self.inf_clicked = False
                        self.LVL_3_RECTclicked = False
                        self.pizza_level_3 = False
                        self.level.play_metronome = False
                        self.home_music = True
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                        pygame.mixer.Channel(3).stop()
                    
                    if not pygame.mixer.Channel(0).get_busy():
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('../resources/drum3.wav'))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.level.SETTINGS_RECT.collidepoint(event.pos):
                            self.level.settings_clicked = True

            # Update Screen
            pygame.display.update()
            if self.done:
                self.start = 0
                self.end = 0
                
if __name__ == '__main__':
    Game().main()