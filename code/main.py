import pygame
import logging
from time import sleep, perf_counter
from tkinter import Tk
from setup import teleportlevel1, height, width, notelevel1
from level import TeleportLevel, NoteLevel, BassNoteLevel

# Main class


class Game:
    def __init__(self):
        # Class which includes all variables
        pygame.init()
        pygame.display.set_caption("Music Ascension")
        
        # logging
        submit_game = False
        if submit_game:
            logging.basicConfig(level= logging.INFO, format='%(message)s')
        elif not submit_game:
            logging.basicConfig(level= logging.DEBUG, format='main.py\n%(message)s')

        # Screen
        self.SCREEN = pygame.display.set_mode((width, height))
        self.level = TeleportLevel(teleportlevel1, self.SCREEN, 1)

        # Background
        self.frontPage = pygame.image.load("../resources/frontpage.png")
        self.levelBackground = pygame.image.load("../resources/background.jpg")
        self.inf_mode_img = pygame.image.load("../resources/infinite.png")
        self.startButtonImage = pygame.image.load("../resources/start.png")
        self.creditsButtonImage = pygame.image.load("../resources/credits.png")
        self.nextButtonImage = pygame.image.load("../resources/next3.png")
        self.beginnerMap = pygame.image.load("../resources/beginner_map.png")
        self.beginnerTopicsCovered = pygame.image.load("../resources/beginnertopics.png")
        self.beginnerImage = pygame.image.load("../resources/beginner.png")
        self.informationPage1 = pygame.image.load("../resources/NDNotes.jpg")
        self.NDhow2play = pygame.image.load("../resources/NDdirections.png")
        self.playButton = pygame.image.load("../resources/play.png")
        self.work_in_progress = pygame.image.load("../resources/WorkInProgress.jpg")
        self.backImage = pygame.image.load("../resources/back3.png")
        self.button = pygame.image.load("../resources/copybutton3.png")
        self.pizzaNotes1 = pygame.image.load("../resources/treble_notes.png")
        self.pizzaplaynotes = pygame.image.load("../resources/pizza_notes.png")
        self.creditsImage = pygame.image.load("../resources/creditsbackground.png")
        self.musicbutton = pygame.image.load("../resources/musicbutton.png")
        self.helpbutton = pygame.image.load("../resources/help2.png")
        self.NDbackground = pygame.image.load("../resources/NDbackground2.png")
        self.helpbg = pygame.image.load("../resources/help_bg.jpg")

        # Variables
        self.startGame = False
        self.infClicked = False
        self.creditsClicked = False
        self.beginnerClicked = False
        self.choosebeginnerlevel = False
        self.getCoordinates = False
        self.notes_1 = False
        self.duration_notes_1 = False
        self.level1picked = False
        self.level2picked = False
        self.level3picked = False
        self.informationPage2 = False
        self.DurationStage2 = False
        self.infclicked = False
        self.pizzaMan3 = False
        self.metronome_counter = False
        self.copied = False
        self.pizzaInfo2 = False
        self.noteBoolean1= True
        self.noteBoolean2 = False
        self.noteBoolean3 = False
        self.NDaudioBool = False
        self.helpbool = False
        self.done = False
        self.homeMusic = True
        self.sleepCounter1 = 0
        self.sleepCounter2 = 0
        self.sleepCounter3 = 0
        self.sleepCounter4 = 0
        self.sleepCounter5 = 0
        self.sleepCounter6 = 0
        self.nextCounter = 0
        self.nextCounter2 = 0
        self.completecounter = 0
        self.counter = 0
        self.creditsCounter = 0
        self.home_music_counter = 0
        self.start = 0
        self.end = 0
        # rects
        self.beginnerRect = pygame.Rect(600-self.beginnerImage.get_width()/2, 50, self.beginnerImage.get_width(), self.beginnerImage.get_height())
        self.startRect = pygame.Rect(540, 200, self.startButtonImage.get_width(), self.startButtonImage.get_height())
        self.infRect = pygame.Rect(600-self.inf_mode_img.get_width()/2, 400, self.inf_mode_img.get_width(), self.inf_mode_img.get_height())
        self.creditsButton = pygame.Rect(530, 300, self.creditsButtonImage.get_width(), self.creditsButtonImage.get_height())
        self.nextButton = pygame.Rect(width-self.nextButtonImage.get_width(), height-self.nextButtonImage.get_height(), self.nextButtonImage.get_width(), self.nextButtonImage.get_height())
        self.noteDurationStage1 = pygame.Rect(28, 341, 139, 188)
        self.noteDurationStage2 = pygame.Rect(225, 340, 135, 185)
        self.quarternoteAudio = pygame.Rect(461, 65, self.playButton.get_width(), self.playButton.get_height())
        self.wholenoteAudio = pygame.Rect(461, 330, self.playButton.get_width(), self.playButton.get_height())
        self.halfnoteAudio = pygame.Rect(1038, 65, self.playButton.get_width(), self.playButton.get_height())
        self.eighthnoteAudio = pygame.Rect(1038, 330, self.playButton.get_width(), self.playButton.get_height())
        self.level3 = pygame.Rect(400, 340, 140, 215)
        self.pizza_man_2 = pygame.Rect(605, 340, 140, 215)
        self.NDstage3 = pygame.Rect(830, 340, 140, 215)
        self.pizza_man_3 = pygame.Rect(1015, 340, 140, 215)
        self.backRect = pygame.Rect(0, height-self.backImage.get_height(), self.backImage.get_width(), self.backImage.get_height())
        self.copyClipboard = pygame.Rect(600-self.button.get_width()/2, height/2-100, self.button.get_width(), self.button.get_width())
        self.musichitbox = pygame.Rect(0, height-self.musicbutton.get_height(), self.musicbutton.get_width(), self.musicbutton.get_height())
        self.helpRect = pygame.Rect(width-self.helpbutton.get_width(), 0, self.helpbutton.get_width(), self.helpbutton.get_height())

        self.WHITE = (255, 255, 255)

    def run(self):
        logging.info('Hello and Welcome to Music Ascension!\nIf you cannot see the full window, please change your screen scale to 100%\
            \nTo see how, please check out our README.md file')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start = perf_counter()
                        self.done = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.end = perf_counter()
                        self.done = True
                        logging.debug(round(self.end - self.start, 1))

            if self.homeMusic:
                while not pygame.mixer.Channel(4).get_busy():
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound("../resources/backgroundmusic3.wav"))
                    pygame.mixer.Channel(4).set_volume(10)
            
            if not self.homeMusic:
                pygame.mixer.Channel(4).stop()

            self.SCREEN.fill(0)
            self.SCREEN.blit(self.frontPage, (0, 0))
            self.SCREEN.blit(self.startButtonImage, (540, 200))
            self.SCREEN.blit(self.creditsButtonImage, (530, 300))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.startRect.collidepoint(event.pos):
                    sleep(0.2)
                    self.startGame = True
                if self.creditsButton.collidepoint(event.pos):
                    self.creditsClicked = True

            if self.startGame:
                self.SCREEN.fill(0)
                self.SCREEN.blit(self.levelBackground, (0, 0))
                self.SCREEN.blit(self.beginnerImage,(600-self.beginnerImage.get_width()/2, 50))
                self.SCREEN.blit(self.inf_mode_img, (600-self.inf_mode_img.get_width()/2, 400, self.inf_mode_img.get_width(), self.inf_mode_img.get_height()))
                self.SCREEN.blit(self.musicbutton, (0, height-self.musicbutton.get_height()))

            if not self.startGame:
                if self.creditsClicked:
                    self.homeMusic = False
                    self.SCREEN.fill(self.WHITE)
                    self.SCREEN.blit(self.creditsImage, (0, 0))
                    self.SCREEN.blit(self.button, self.copyClipboard)
                    self.SCREEN.blit(self.backImage, self.backRect)
                    while not pygame.mixer.music.get_busy():
                        pygame.mixer.music.load("../resources/backgroundmusic2.wav")
                        pygame.mixer.music.play()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.backRect.collidepoint(event.pos):
                            self.creditsClicked = False
                            self.copied = False
                            self.homeMusic = True
                            self.creditsCounter = 0
                            self.sleepCounter3 = 0
                            pygame.mixer.music.stop()
                        if self.copyClipboard.collidepoint(event.pos) and self.creditsCounter == 1:
                            clipboard = Tk()
                            clipboard.withdraw()
                            clipboard.clipboard_clear()
                            clipboard.clipboard_append('https://docs.google.com/document/d/1THAizjwlYdVoINJjOBudmcoIM79gEhlbue3cjW5E7r0/edit?usp=sharing')
                            clipboard.update()
                            clipboard.destroy()
                            logging.debug("Copied to clipboard")
                            self.copied = True
                            
                    if event.type == pygame.MOUSEBUTTONDOWN and self.creditsCounter != 1 and self.copyClipboard.collidepoint(event.pos):
                        self.creditsCounter = 1

                    if self.copied:
                        copiedtext = (pygame.font.Font("../resources/PressStart2P.ttf", 40)).render('Link copied to Clipboard', True, (0, 0, 255))
                        self.SCREEN.blit(copiedtext, (600-copiedtext.get_width()/2, height/2+200))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.startGame:
                    if self.beginnerRect.collidepoint(event.pos):
                        self.beginnerClicked = True
                    elif self.infRect.collidepoint(event.pos):
                        self.infClicked = True
                        self.level1picked = True
                        logging.debug("e")


            if self.startGame:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.musichitbox.collidepoint(event.pos) and not self.helpbool:
                        logging.debug("Music Button Clicked")
                        if self.homeMusic and not self.beginnerClicked:
                            if self.home_music_counter == 0:
                                self.home_music_counter+=1
                                self.homeMusic = False
                                logging.debug("Music is Sine waves ", self.home_music_counter)
                                pygame.time.delay(200)
                        elif not self.homeMusic:
                            if self.home_music_counter == 1:
                                self.home_music_counter-=1
                                self.homeMusic = True
                                logging.debug("Chaos Theory is fluid mechanics ", self.home_music_counter)
                                pygame.time.delay(200)

                if self.beginnerClicked:
                    self.SCREEN.fill(self.WHITE)
                    self.SCREEN.blit(self.beginnerTopicsCovered, (0, 0))
                    self.SCREEN.blit(self.nextButtonImage, self.nextButton)
                    self.SCREEN.blit(self.backImage, self.backRect)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            self.choosebeginnerlevel = True
                        if self.backRect.collidepoint(event.pos):
                            self.beginnerClicked = False

                if self.choosebeginnerlevel:
                    self.SCREEN.blit(self.beginnerMap, (0, 0))
                    self.SCREEN.blit(self.helpbutton, self.helpRect)
                    while self.sleepCounter5 == 0:
                        sleep(0.3)
                        self.sleepCounter5+=1

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.noteDurationStage1.collidepoint(event.pos):
                            self.notes_1 = True
                        elif self.noteDurationStage2.collidepoint(event.pos):
                            self.duration_notes_1 = True
                        elif self.level3.collidepoint(event.pos):
                            self.pizzaMan3 = True
                        elif self.NDstage3.collidepoint(event.pos):
                            self.pizzaMan3 = True
                        elif self.pizza_man_2.collidepoint(event.pos):
                            self.pizzaMan3 = True
                        elif self.pizza_man_3.collidepoint(event.pos):
                            self.pizzaMan3 = True
                        elif self.helpRect.collidepoint(event.pos):
                            self.helpbool = True
                            self.sleepCounter6 == 0
                
                if self.helpbool:
                    self.SCREEN.fill(0)
                    self.SCREEN.blit(self.helpbg, (0, 0))
                    self.SCREEN.blit(self.backImage, self.backRect)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.backRect.collidepoint(event.pos):
                            self.helpbool = False
                            while self.sleepCounter6 == 0:
                                pygame.time.delay(250)
                                self.sleepCounter6+=1

                if self.DurationStage2:
                    self.SCREEN.blit(self.work_in_progress, (0, 0))
                    self.SCREEN.blit(self.backImage, self.backRect)
                    # Insert Code to call stage 2 of note duration
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.backRect.collidepoint(event.pos):
                            self.DurationStage2 = False

                if self.infclicked:
                    self.notes_1 = True

                if self.pizzaMan3:
                    self.SCREEN.blit(self.work_in_progress, (0, 0))
                    self.SCREEN.blit(self.backImage, self.backRect)
                    # Insert code to call stage 3 of pizza man minigame
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.backRect.collidepoint(event.pos):
                            self.pizzaMan3 = False
                
                if self.notes_1:
                    self.SCREEN.blit(self.pizzaNotes1, (0, 0))
                    self.SCREEN.blit(self.nextButtonImage, self.nextButton)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.choosebeginnerlevel:
                                self.pizzaInfo2 = True
                                while self.sleepCounter4 == 0:
                                    sleep(0.2)
                                    self.sleepCounter4 = 1
                
                if self.pizzaInfo2:
                    self.SCREEN.fill(0)
                    self.SCREEN.blit(self.pizzaplaynotes, (0, 0))
                    self.SCREEN.blit(self.nextButtonImage, self.nextButton)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.choosebeginnerlevel and self.nextCounter2 == 1:
                                self.level1picked = True
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.nextCounter2 == 0:
                                self.nextCounter2 = 1

                if self.duration_notes_1:
                    self.SCREEN.fill(self.WHITE)
                    self.SCREEN.blit(self.informationPage1, (0, 0))
                    self.SCREEN.blit(self.playButton, self.quarternoteAudio)
                    self.SCREEN.blit(self.playButton, self.wholenoteAudio)
                    self.SCREEN.blit(self.playButton, self.halfnoteAudio)
                    self.SCREEN.blit(self.playButton, self.eighthnoteAudio)
                    self.SCREEN.blit(self.nextButtonImage, self.nextButton)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            self.informationPage2 = True

                        elif self.quarternoteAudio.collidepoint(event.pos):
                            self.homeMusic = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/quarter_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.wholenoteAudio.collidepoint(event.pos):
                            self.homeMusic = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/whole_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.halfnoteAudio.collidepoint(event.pos):
                            self.homeMusic = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/half_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.eighthnoteAudio.collidepoint(event.pos):
                            self.homeMusic = False
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("../resources/eighth_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                if self.informationPage2:
                    self.SCREEN.blit(self.NDhow2play, (0, 0))
                    self.SCREEN.blit(self.nextButtonImage, self.nextButton)
                    if self.sleepCounter1 == 0:
                        sleep(0.2)
                        self.sleepCounter1 = 1

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.nextCounter == 1:
                                logging.debug(f"Next Counter: {self.nextCounter}")
                                self.level2picked = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.nextCounter == 0:
                                self.nextCounter+=1
                            
                if self.level1picked and self.counter == 0:
                    print("ww")
                    if self.infClicked:
                        self.level = NoteLevel(notelevel1, self.SCREEN, self.level.stage, infmode=True)
                    elif not self.infClicked:
                        self.level = NoteLevel(notelevel1, self.SCREEN, self.level.stage)
                    self.counter = 1

                if self.level1picked:
                    self.homeMusic = False
                    self.SCREEN.fill("black")
                    self.level.run()
                    if self.level.reset and self.level.stagefinished:
                        self.completecounter += 1
                        if self.completecounter >= 20:
                            self.level.run()
                            self.level = NoteLevel(notelevel1, self.SCREEN, self.level.stage)
                            self.completecounter = 0
                    elif self.level.chain:
                        self.level1picked = False
                        self.notes_1 = False
                        self.counter = 0
                    if self.level.back2 == True:
                        self.level1picked = False
                        self.level3picked = False
                        self.notes_1 = False
                        self.pizzaInfo2 = False
                        self.level.back2 = False
                        self.level.settingsClicked2 = False
                        self.counter = 0
                        self.level.backgroundmusic = True
                        self.homeMusic = True
                        self.infClicked = False
                        pygame.mixer.music.stop()

                if self.level2picked and self.counter == 0:
                    self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    self.counter = 1

                if self.level2picked:
                    self.homeMusic = False
                    self.level.playMetronome = True
                    self.SCREEN.fill("black")
                    self.SCREEN.blit(self.NDbackground, (0, 0))
                    try:
                        self.level.run(self.end-self.start)
                    except:
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                        self.level2picked = False
                        self.informationPage2 = False
                        self.duration_notes_1 = False
                        self.counter = 0
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                    if self.level.reset and self.level.stagefinished:
                        self.level.run(self.end-self.start)
                        while self.sleepCounter2 == 0:
                            sleep(1)
                            self.sleepCounter2 = 1
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    elif self.level.reset:
                        self.level = TeleportLevel(teleportlevel1, self.SCREEN, self.level.stage)
                    elif self.level.back:
                        self.level2picked = False
                        self.informationPage2 = False
                        self.duration_notes_1 = False
                        self.counter = 0
                        self.DurationStage2 = False
                        self.level3clicked = False
                        self.pizzaMan3 = False
                        self.level.playMetronome = False
                        self.homeMusic = True
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                        pygame.mixer.Channel(3).stop()
                    if not pygame.mixer.Channel(0).get_busy():
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('../resources/drum3.wav'))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.level.settings.collidepoint(event.pos):
                            self.level.settingsClicked = True
                    
                if self.level3picked and self.counter == 0:
                    self.level = BassNoteLevel(notelevel1, self.SCREEN, self.level.stage, True)
                    self.counter = 1
                    logging.debug("e")

                if self.level3picked:
                    self.homeMusic = False
                    self.SCREEN.fill("black")
                    self.level.run()
                    if self.level.reset and self.level.stagefinished:
                        self.completecounter += 1
                        if self.completecounter >= 20:
                            self.level.run()
                            self.level = BassNoteLevel(notelevel1, self.SCREEN, self.level.stage)
                            self.completecounter = 0
                    elif self.level.chain:
                        self.level3picked = False
                        self.notes_1 = False
                        self.counter = 0
                    if self.level.back2 == True:
                        self.level3picked = False
                        self.notes_1 = False
                        self.pizzaInfo2 = False
                        self.level.back2 = False
                        self.level.settingsClicked2 = False
                        self.counter = 0
                        self.level.backgroundmusic = True
                        self.homeMusic = True
                        pygame.mixer.music.stop()

            # Update Screen
            pygame.display.update()
            if self.done:
                self.start = 0
                self.end = 0

if Game().run == False:
    pygame.mixer.music.stop()
    pygame.quit()
    exit(0)
   

if __name__ == '__main__':
    Game().run()