import pygame
from itertools import cycle
from sys import exit
from time import sleep, perf_counter
from tkinter import Tk
from setup import teleportlevel1, height, width, notelevel1
from level import TeleportLevel, NoteLevel, BassNoteLevel


# Main class

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Music Ascension")
        
        # Screen
        self.screen = pygame.display.set_mode((width, height))
        self.level = TeleportLevel(teleportlevel1, self.screen, 1)

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
        self.COPIED_TEXT = pygame.image.load("../resources/copied.png")
        self.MUSIC_IMAGE = pygame.image.load("../resources/musicbutton.png")
        self.HELP_IMAGE = pygame.image.load("../resources/help2.png")
        self.NOTE_DURATION_BG = pygame.image.load("../resources/NDbackground2.png")
        self.HELP_BG = pygame.image.load("../resources/helpbg.png")

        # Variables
        # Booleans
        self.start_game = False
        self.adv_clicked = False
        self.credits_clicked = False
        self.off_credits = False
        self.beginner_clicked = False
        self.choose_beginner_lvl = False
        self.pizza_notes = False
        self.note_duration_notes = False
        self.level_1_picked = False
        self.level_2_picked = False
        self.level_3_picked = False
        self.inf_clicked = False
        self.note_duration_notes_2 = False
        self.adv_map = False
        self.note_duration_lvl_2 = False
        self.pizza_level_3 = False
        self.copied = False
        self.pizza_notes_2 = False
        self.note_duration_audio = False
        self.help_bool = False
        self.done = False
        self.home_music = True
        # integers
        self.sleep_counter_1 = 0
        self.sleep_counter_2 = 0
        self.sleep_counter_3 = 0
        self.sleep_counter_4 = 0
        self.sleep_counter_5 = 0
        self.next_counter = 0
        self.next_counter_2 = 0
        self.complete_counter = 0
        self.counter = 0
        self.credits_counter = 0
        self.home_musiccounter = 0
        self.start = 0
        self.end = 0
        # Constants
        self.BEGINNER_RECT = pygame.Rect(600-self.BEGINNER_IMAGE.get_width()/2, 50, self.BEGINNER_IMAGE.get_width(), self.BEGINNER_IMAGE.get_height())
        self.START_RECT = pygame.Rect(540, 200, self.START_BUTTON_IMAGE.get_width(), self.START_BUTTON_IMAGE.get_height())
        self.ADV_RECT = pygame.Rect(600-self.ADV_IMAGE.get_width()/2, 400, self.ADV_IMAGE.get_width(), self.ADV_IMAGE.get_height())
        self.CREDITS_RECT = pygame.Rect(530, 300, self.CREDITS_IMAGE.get_width(), self.CREDITS_IMAGE.get_height())
        self.NEXT_RECT = pygame.Rect(width-self.NEXT_IMAGE.get_width(), height-self.NEXT_IMAGE.get_height(), self.NEXT_IMAGE.get_width(), self.NEXT_IMAGE.get_height())
        self.NOTE_DURATION_LVL_1_RECT = pygame.Rect(28, 341, 139, 188)
        self.NOTE_DURATION_LVL_2_RECT = pygame.Rect(225, 340, 135, 185)
        self.EIGHTH_RECT = pygame.Rect(1038, 330, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.QUARTER_RECT = pygame.Rect(461, 65, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.HALF_RECT = pygame.Rect(1038, 65, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.WHOLE_RECT = pygame.Rect(461, 330, self.PLAY_IMAGE.get_width(), self.PLAY_IMAGE.get_height())
        self.LVL_3_RECT = pygame.Rect(400, 340, 140, 215)
        self.PIZZA_LVL_2_RECT = pygame.Rect(605, 340, 140, 215)
        self.INF_RECT = pygame.Rect(830, 340, 140, 215)
        self.PIZZA_LVL_3_RECT = pygame.Rect(1015, 340, 140, 215)
        self.BACK_RECT = pygame.Rect(0, height-self.BACK_IMAGE.get_height(), self.BACK_IMAGE.get_width(), self.BACK_IMAGE.get_height())
        self.COPY_RECT = pygame.Rect(600-self.COPY_BUTTON_IMAGE.get_width()/2, height/2-100, self.COPY_BUTTON_IMAGE.get_width(), self.COPY_BUTTON_IMAGE.get_width())
        self.MUSIC_RECT = pygame.Rect(0, height-self.MUSIC_IMAGE.get_height(), self.MUSIC_IMAGE.get_width(), self.MUSIC_IMAGE.get_height())
        self.HELP_RECT = pygame.Rect(width-self.HELP_IMAGE.get_width(), 0, self.HELP_IMAGE.get_width(), self.HELP_IMAGE.get_height())
        self.WHITE_COLOR = (255, 255, 255)

    def run(self):
        for _ in cycle((1, 1)):
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
                        print(round(self.end - self.start, 1))

            if self.home_music:
                while not pygame.mixer.Channel(4).get_busy():
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound("../resources/backgroundmusic3.wav"))
                    pygame.mixer.Channel(4).set_volume(10)
            
            if not self.home_music:
                pygame.mixer.Channel(4).stop()

            self.screen.fill(0)
            self.screen.blit(self.FRONT_PAGE, (0, 0))
            self.screen.blit(self.START_BUTTON_IMAGE, (540, 200))
            self.screen.blit(self.CREDITS_IMAGE, (530, 300))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.START_RECT.collidepoint(event.pos):
                    self.start_game = True
                    sleep(0.5)
                    self.off_credits = True
                if self.CREDITS_RECT.collidepoint(event.pos):
                    self.credits_clicked = True

            if self.start_game:
                self.screen.fill(0)
                self.screen.blit(self.LVL_BG, (0, 0))
                self.screen.blit(self.BEGINNER_IMAGE,(600-self.BEGINNER_IMAGE.get_width()/2, 50))
                self.screen.blit(self.ADV_IMAGE, (600-self.ADV_IMAGE.get_width()/2, 400, self.ADV_IMAGE.get_width(), self.ADV_IMAGE.get_height()))
                self.screen.blit(self.MUSIC_IMAGE, (0, height-self.MUSIC_IMAGE.get_height()))

            if not self.off_credits:
                if self.credits_clicked:
                    self.home_music = False
                    self.screen.fill(self.WHITE_COLOR)
                    self.screen.blit(self.CREDITS_BG, (0, 0))
                    self.screen.blit(self.COPY_BUTTON_IMAGE, self.COPY_RECT)
                    self.screen.blit(self.BACK_IMAGE, self.BACK_RECT)
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
                            print("Copied to clipboard")
                            self.copied = True
                            
                    if event.type == pygame.MOUSEBUTTONDOWN and self.credits_counter != 1 and self.COPY_RECT.collidepoint(event.pos):
                        self.credits_counter = 1

                    if self.copied:
                        copiedtext = (pygame.font.Font("../resources/PressStart2P.ttf", 40)).render('Link copied to Clipboard', True, (0, 0, 255))
                        self.screen.blit(copiedtext, (600-copiedtext.get_width()/2, height/2+200))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_game:
                    if self.ADV_RECT.collidepoint(event.pos):
                        self.adv_clicked = True
                    if self.BEGINNER_RECT.collidepoint(event.pos):
                        self.beginner_clicked = True

            if self.start_game and not self.adv_clicked:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.MUSIC_RECT.collidepoint(event.pos) and not self.help_bool:
                        print("Music Button Clicked")
                        if self.home_music and not self.beginner_clicked:
                            if self.home_musiccounter == 0:
                                self.home_musiccounter+=1
                                self.home_music = False
                                print("Music is Sine waves ", self.home_musiccounter)
                                pygame.time.delay(200)
                        elif not self.home_music:
                            if self.home_musiccounter == 1:
                                self.home_musiccounter-=1
                                self.home_music = True
                                print("Chaos Theory is fluid mechanics ", self.home_musiccounter)
                                pygame.time.delay(200)

                if self.adv_clicked:
                    self.screen.fill(self.WHITE_COLOR)
                    advTopicsText = pygame.font.SysFont(None, 40)
                    advTopicsText = advTopicsText.render('Topics Covered: ', True, 0)
                    self.screen.blit(advTopicsText, (0, 0))
                    advTopicsText2 = pygame.font.SysFont(None, 40)
                    advTopicsText2 = advTopicsText2.render('Dynamics and Articulation', True, 0)
                    self.screen.blit(advTopicsText2, (0, 50))
                    advTopicsText3 = pygame.font.SysFont(None, 40)
                    advTopicsText3 = advTopicsText3.render('Time Signatures', True, 0)
                    self.screen.blit(advTopicsText3, (0, 100))
                    self.screen.blit(self.NEXT_IMAGE, self.NEXT_RECT)
                    self.screen.blit(self.BACK_IMAGE, self.BACK_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            self.adv_map = True
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.adv_clicked = False

                if self.beginner_clicked:
                    self.screen.fill(self.WHITE_COLOR)
                    self.screen.blit(self.BEGINNER_TOPIC_IMAGE, (0, 0))
                    self.screen.blit(self.NEXT_IMAGE, self.NEXT_RECT)
                    self.screen.blit(self.BACK_IMAGE, self.BACK_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            self.choose_beginner_lvl = True
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.beginner_clicked = False

                if self.adv_map:
                    self.screen.fill("white")
                    self.screen.blit(self.ADV_MAP_IMAGE, (0, 0))
                    self.screen.blit(self.BACK_IMAGE, self.BACK_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.adv_clicked = False
                            self.adv_map = False

                if self.choose_beginner_lvl:
                    self.screen.blit(self.BEGINNER_MAP_IMAGE, (0, 0))
                    self.screen.blit(self.HELP_IMAGE, self.HELP_RECT)
                    while self.sleep_counter_4 == 0:
                        sleep(0.3)
                        self.sleep_counter_4+=1

                if event.type == pygame.MOUSEBUTTONDOWN and self.choose_beginner_lvl:
                    if self.NOTE_DURATION_LVL_1_RECT.collidepoint(event.pos):
                        self.pizza_notes = True
                    elif self.NOTE_DURATION_LVL_2_RECT.collidepoint(event.pos):
                        self.note_duration_notes = True
                    elif self.LVL_3_RECT.collidepoint(event.pos):
                        self.level_3_picked = True
                    elif self.INF_RECT.collidepoint(event.pos):
                        self.inf_clicked = True
                    elif self.PIZZA_LVL_2_RECT.collidepoint(event.pos):
                        print("Warning: File May Glitch.\nThis game is not finsished yet")
                        self.level_3_picked = True
                    elif self.PIZZA_LVL_3_RECT.collidepoint(event.pos):
                        self.pizza_level_3 = True
                    elif self.HELP_RECT.collidepoint(event.pos):
                        self.help_bool = True
                        self.sleep_counter_5 == 0
                
                if self.help_bool:
                    self.screen.fill(0)
                    self.screen.blit(self.HELP_BG, (0, 0))
                    self.screen.blit(self.BACK_IMAGE, self.BACK_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.help_bool = False
                            while self.sleep_counter_5 == 0:
                                pygame.time.delay(250)
                                self.sleep_counter_5+=1

                if self.note_duration_lvl_2:
                    self.screen.blit(self.ADV_MAP_IMAGE, (0, 0))
                    self.screen.blit(self.BACK_IMAGE, self.BACK_RECT)
                    # Insert Code to call stage 2 of note duration
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.note_duration_lvl_2 = False

                if self.inf_clicked:
                    self.level_1_picked = True
                    self.level.inf_mode = True

                if self.pizza_level_3:
                    self.screen.blit(self.ADV_MAP_IMAGE, (0, 0))
                    self.screen.blit(self.BACK_IMAGE, self.BACK_RECT)
                    # Insert code to call stage 3 of pizza man minigame
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_RECT.collidepoint(event.pos):
                            self.pizza_level_3 = False
                
                if self.pizza_notes:
                    self.screen.blit(self.PIZZA_NOTES_IMG, (0, 0))
                    self.screen.blit(self.NEXT_IMAGE, self.NEXT_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.choose_beginner_lvl:
                                self.pizza_notes_2 = True
                                while self.sleep_counter_3 == 0:
                                    sleep(0.2)
                                    self.sleep_counter_3 = 1
                
                if self.pizza_notes_2:
                    self.screen.fill(0)
                    self.screen.blit(self.PIZZA_NOTES_IMG_2, (0, 0))
                    self.screen.blit(self.NEXT_IMAGE, self.NEXT_RECT)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.choose_beginner_lvl and self.next_counter_2 == 1:
                                self.level_1_picked = True
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.next_counter_2 == 0:
                                self.next_counter_2 = 1

                if self.note_duration_notes:
                    self.screen.fill(self.WHITE_COLOR)
                    self.screen.blit(self.NOTE_DURATION_NOTES_IMG, (0, 0))
                    self.screen.blit(self.PLAY_IMAGE, self.QUARTER_RECT)
                    self.screen.blit(self.PLAY_IMAGE, self.WHOLE_RECT)
                    self.screen.blit(self.PLAY_IMAGE, self.HALF_RECT)
                    self.screen.blit(self.PLAY_IMAGE, self.EIGHTH_RECT)
                    self.screen.blit(self.NEXT_IMAGE, self.NEXT_RECT)

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
                    self.screen.blit(self.NOTE_DURATION_NOTES_IMG_2, (0, 0))
                    self.screen.blit(self.NEXT_IMAGE, self.NEXT_RECT)
                    if self.sleep_counter_1 == 0:
                        sleep(0.2)
                        self.sleep_counter_1 = 1

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.next_counter == 1:
                                print(f"Next Counter : {self.next_counter}")
                                self.level_2_picked = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.NEXT_RECT.collidepoint(event.pos):
                            if self.next_counter == 0:
                                self.next_counter+=1
                            
                if self.level_1_picked and self.counter == 0:
                    self.level = NoteLevel(notelevel1, self.screen, self.level.stage)
                    self.counter = 1

                if self.level_1_picked:
                    self.home_music = False
                    self.screen.fill("black")
                    self.level.run()
                    if self.level.reset and self.level.stage_finished:
                        self.complete_counter += 1
                        if self.complete_counter >= 20:
                            self.level.run()
                            self.level = NoteLevel(notelevel1, self.screen, self.level.stage)
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
                    self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
                    self.counter = 1

                if self.level_2_picked:
                    self.home_music = False
                    self.level.play_metronome = True
                    self.screen.fill("black")
                    self.screen.blit(self.NOTE_DURATION_BG, (0, 0))
                    try:
                        self.level.run(self.end-self.start)
                    except:
                        self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
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
                        self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
                    elif self.level.reset:
                        self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
                        if self.level.play_metronome:
                            if not pygame.mixer.Channel(0).get_busy():
                                pygame.mixer.Channel(0).play(pygame.mixer.Sound('../resources/metronome.wav'))
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
                    
                    if self.level.play_metronome:
                        if not pygame.mixer.Channel(0).get_busy():
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound('../resources/metronome.wav'))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.level.SETTINGS_RECT.collidepoint(event.pos):
                            self.level.settings_clicked = True
                    
                if self.level_3_picked and self.counter == 0:
                    self.level = BassNoteLevel(notelevel1, self.screen, self.level.stage, True)
                    self.counter = 1
                    print("e")

                if self.level_3_picked:
                    self.home_music = False
                    self.screen.fill("black")
                    self.level.run()
                    if self.level.reset and self.level.stage_finished:
                        self.complete_counter += 1
                        if self.complete_counter >= 20:
                            self.level.run()
                            self.level = BassNoteLevel(notelevel1, self.screen, self.level.stage)
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

            # Update Screen
            pygame.display.update()
            if self.done:
                self.start = 0
                self.end = 0
                
if __name__ == '__main__':
    Game().run()
