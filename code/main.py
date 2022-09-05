import pygame, sys, time, tkinter
from setup import *
from level import TeleportLevel, NoteLevel

# Main class


class Game:
    def __init__(self):
        # Class which includes all variables
        pygame.init()
        pygame.mixer.init()
        

        # Screen
        self.screen = pygame.display.set_mode((width, height))
        self.level = TeleportLevel(teleportlevel1, self.screen, 1)

        # Background
        self.frontPage = pygame.image.load("resources/frontpage.png")
        self.levelBackground = pygame.image.load("resources/background.jpg")
        self.AdvancedImage = pygame.image.load("resources/Advanced.png")
        self.startButtonImage = pygame.image.load("resources/start.png")
        self.creditsButtonImage = pygame.image.load("resources/credits.png")
        self.nextButtonImage = pygame.image.load("resources/next3.png")
        self.beginnerMap = pygame.image.load("resources/beginnermap2.png")
        self.beginnerTopicsCovered = pygame.image.load("resources/beginnertopics.png")
        self.beginnerImage = pygame.image.load("resources/beginner.png")
        self.informationPage1 = pygame.image.load("resources/NDNotes.jpg")
        self.NDhow2play = pygame.image.load("resources/NDdirections.png")
        self.playButton = pygame.image.load("resources/play.png")
        self.advMapImage = pygame.image.load("resources/WorkInProgress.jpg")
        self.backImage = pygame.image.load("resources/back2.png")
        self.button = pygame.image.load("resources/button.jpg")
        self.pizzaNotes1 = pygame.image.load("resources/treble_notes.png")
        self.pizzaPlay = pygame.image.load("resources/pizza_notes.png")
        self.pizzaBackground = pygame.image.load("resources/pizzaBackground.png")

        # Variables
        self.startGame = False
        self.advClicked = False
        self.creditsClicked = False
        self.offCreditButton = False
        self.levelConfirm = False
        self.beginnerClicked = False
        self.nextClicked = False
        self.chooseBeginnerLevel = False
        self.getCoordinates = False
        self.stageChooser = False
        self.stageChooser2 = False
        self.level1picked = False
        self.level2picked = False
        self.informationPage2 = False
        self.advancedMap = False
        self.DurationStage2 = False
        self.DurationStage3 = False
        self.pizzaMan2 = False
        self.pizzaMan3 = False
        self.metronome_counter = False
        self.copied = False
        self.pizzaInfo2 = False
        self.sleepCounter1 = 0
        self.sleepCounter2 = 0
        self.sleepCounter3 = 0
        self.sleepCounter4 = 0
        self.nextCounter = 0
        self.nextCounter2 = 0
        self.completecounter = 0
        self.counter = 0
        self.beginnerRect = pygame.Rect(600-self.beginnerImage.get_width()/2, 50, self.beginnerImage.get_width(), self.beginnerImage.get_height())
        self.startRect = pygame.Rect(540, 200, self.startButtonImage.get_width(), self.startButtonImage.get_height())
        self.advancedRect = pygame.Rect(600-self.AdvancedImage.get_width()/2, 400, self.AdvancedImage.get_width(), self.AdvancedImage.get_height())
        self.creditsButton = pygame.Rect(530, 300, self.creditsButtonImage.get_width(), self.creditsButtonImage.get_height())
        self.nextButton = pygame.Rect(width-self.nextButtonImage.get_width(), height-self.nextButtonImage.get_height(), self.nextButtonImage.get_width(), self.nextButtonImage.get_height())
        self.noteDurationStage1 = pygame.Rect(28, 341, 139, 188)
        self.noteDurationStage2 = pygame.Rect(225, 340, 135, 185)
        self.quarternoteAudio = pygame.Rect(461, 65, self.playButton.get_width(), self.playButton.get_height())
        self.wholenoteAudio = pygame.Rect(461, 330, self.playButton.get_width(), self.playButton.get_height())
        self.halfnoteAudio = pygame.Rect(1038, 65, self.playButton.get_width(), self.playButton.get_height())
        self.eighthnoteAudio = pygame.Rect(1038, 330, self.playButton.get_width(), self.playButton.get_height())
        self.NDstage2 = pygame.Rect(400, 340, 140, 215)
        self.pizza_man_2 = pygame.Rect(605, 340, 140, 215)
        self.NDstage3 = pygame.Rect(830, 340, 140, 215)
        self.pizza_man_3 = pygame.Rect(1015, 340, 140, 215)
        self.backRect = pygame.Rect(0, height-self.backImage.get_height(), self.backImage.get_width(), self.backImage.get_height())
        self.copyClipboard = pygame.Rect(0, height/2-100, self.button.get_width(), self.button.get_width())

        self.start = 0
        self.end = 0
        self.done = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start = time.time()
                        self.done = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.end = time.time()
                        self.done = True
                        print(self.end - self.start)

            self.screen.fill(0)
            self.screen.blit(self.frontPage, (0, 0))
            self.screen.blit(self.startButtonImage, (540, 200))
            self.screen.blit(self.creditsButtonImage, (530, 300))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.startRect.collidepoint(event.pos):
                    self.startGame = True
                    time.sleep(0.5)
                    self.levelConfirm = True
                    self.offCreditButton = True
                if self.creditsButton.collidepoint(event.pos):
                    self.creditsClicked = True

            if self.startGame:
                self.screen.fill(0)
                self.screen.blit(self.levelBackground, (0, 0))
                self.screen.blit(self.beginnerImage,(600-self.beginnerImage.get_width()/2, 50))
                self.screen.blit(self.AdvancedImage, (600-self.AdvancedImage.get_width()/2, 400, self.AdvancedImage.get_width(), self.AdvancedImage.get_height()))

            if not self.offCreditButton:
                if self.creditsClicked:
                    while self.sleepCounter3 == 0:
                        time.sleep(0.5)
                        self.sleepCounter3 = 1
                    self.screen.fill((255, 255, 255))
                    creditsText = pygame.font.SysFont(None, 30)
                    creditsText = creditsText.render('Credits:', True, 0)
                    creditsText2 = (pygame.font.SysFont(None, 30)).render('Click the button to copy', True, 100)
                    self.screen.blit(self.button, self.copyClipboard)
                    self.screen.blit(creditsText, (0, 0))
                    self.screen.blit(creditsText2, (0, 100))
                    self.screen.blit(self.backImage, self.backRect)
                    # self.screen.fill((255, 0, 0), self.copyClipboard)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.backRect.collidepoint(event.pos):
                            self.creditsClicked = False
                            self.copied = False
                        if self.copyClipboard.collidepoint(event.pos):
                            clipboard = tkinter.Tk()
                            clipboard.withdraw()
                            clipboard.clipboard_clear()
                            clipboard.clipboard_append('https://docs.google.com/document/d/1THAizjwlYdVoINJjOBudmcoIM79gEhlbue3cjW5E7r0/edit?usp=sharing')
                            clipboard.update()
                            clipboard.destroy()
                            print("Copied to clipboard")
                            self.copied = True

                    if self.copied:
                        text = (pygame.font.SysFont(None, 30)).render("Copied link to Clipboard", True, 0)
                        self.screen.blit(text, (600, 400))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.levelConfirm:
                    if self.advancedRect.collidepoint(event.pos):
                        self.advClicked = True
                    if self.beginnerRect.collidepoint(event.pos):
                        self.beginnerClicked = True

            if self.levelConfirm:
                if self.advClicked:
                    self.screen.fill((255, 255, 255))
                    advTopicsText = pygame.font.SysFont(None, 40)
                    advTopicsText = advTopicsText.render('Topics Covered: ', True, 0)
                    self.screen.blit(advTopicsText, (0, 0))
                    advTopicsText2 = pygame.font.SysFont(None, 40)
                    advTopicsText2 = advTopicsText2.render('Dynamics and Articulation', True, 0)
                    self.screen.blit(advTopicsText2, (0, 50))
                    advTopicsText3 = pygame.font.SysFont(None, 40)
                    advTopicsText3 = advTopicsText3.render('Time Signatures', True, 0)
                    self.screen.blit(advTopicsText3, (0, 100))
                    self.screen.blit(self.nextButtonImage, self.nextButton)
                    self.screen.blit(self.backImage, self.backRect)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            self.advancedMap = True
                        if self.backRect.collidepoint(event.pos):
                            self.advClicked = False

                if self.beginnerClicked:
                    self.screen.fill((255, 255, 255))
                    self.screen.blit(self.beginnerTopicsCovered, (0, 0))
                    self.screen.blit(self.nextButtonImage, self.nextButton)
                    self.screen.blit(self.backImage, self.backRect)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            self.nextClicked = True
                        if self.backRect.collidepoint(event.pos):
                            self.beginnerClicked = False

                if self.advancedMap:
                    self.screen.fill("white")
                    self.screen.blit(self.advMapImage, (0, 0))

                if self.nextClicked:
                    self.screen.blit(self.beginnerMap, (0, 0))
                    self.chooseBeginnerLevel = True

                if event.type == pygame.MOUSEBUTTONDOWN and self.chooseBeginnerLevel:
                    if self.noteDurationStage1.collidepoint(event.pos):
                        self.stageChooser = True
                    elif self.noteDurationStage2.collidepoint(event.pos):
                        self.stageChooser2 = True
                    elif self.NDstage2.collidepoint(event.pos):
                        self.DurationStage2 = True
                    elif self.NDstage3.collidepoint(event.pos):
                        self.DurationStage3 = True
                    elif self.pizza_man_2.collidepoint(event.pos):
                        self.pizzaMan2 = True
                    elif self.pizza_man_3.collidepoint(event.pos):
                        self.pizzaMan3 = True

                if self.DurationStage2:
                    self.screen.blit(self.advMapImage, (0, 0))
                    # Insert Code to call stage 2 of note duration

                if self.DurationStage3:
                    self.screen.blit(self.advMapImage, (0, 0))
                    # Insert Code to call stage 3 of note duration minigame

                if self.pizzaMan2:
                    self.screen.blit(self.advMapImage, (0, 0))
                    # Insert code for stage 2 of pizza man minigame

                if self.pizzaMan3:
                    self.screen.blit(self.advMapImage, (0, 0))
                    # Insert code to call stage 3 of pizza man minigame
                
                if self.stageChooser:
                    self.screen.blit(self.pizzaNotes1, (0, 0))
                    self.screen.blit(self.nextButtonImage, self.nextButton)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.chooseBeginnerLevel:
                                self.pizzaInfo2 = True
                                while self.sleepCounter4 == 0:
                                    time.sleep(0.2)
                                    self.sleepCounter4 = 1
                
                if self.pizzaInfo2:
                    self.screen.fill(0)
                    self.screen.blit(self.pizzaPlay, (0, 0))
                    self.screen.blit(self.nextButtonImage, self.nextButton)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.chooseBeginnerLevel and self.nextCounter2 == 1:
                                self.level1picked = True
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.nextCounter2 == 0:
                                self.nextCounter2 = 1

                if self.stageChooser2:
                    self.screen.fill((255, 255, 255))
                    self.screen.blit(self.informationPage1, (0, 0))
                    self.screen.blit(self.playButton, self.quarternoteAudio)
                    self.screen.blit(self.playButton, self.wholenoteAudio)
                    self.screen.blit(self.playButton, self.halfnoteAudio)
                    self.screen.blit(self.playButton, self.eighthnoteAudio)
                    self.screen.blit(self.nextButtonImage, self.nextButton)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            self.informationPage2 = True

                        elif self.quarternoteAudio.collidepoint(event.pos):
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("resources/quarter_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.wholenoteAudio.collidepoint(event.pos):
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("resources/whole_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                        elif self.halfnoteAudio.collidepoint(event.pos):
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("resources/half_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()
                                
                        elif self.eighthnoteAudio.collidepoint(event.pos):
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound("resources/eighth_note.mp3"))
                            elif pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).stop()

                if self.informationPage2:
                    self.screen.blit(self.NDhow2play, (0, 0))
                    self.screen.blit(self.nextButtonImage, self.nextButton)
                    while self.sleepCounter1 == 0:
                        time.sleep(0.2)
                        self.sleepCounter1 = 1

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.nextCounter == 1:
                                if self.chooseBeginnerLevel:
                                    self.level2picked = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.nextButton.collidepoint(event.pos):
                            if self.nextCounter != 1:
                                self.nextCounter = self.nextCounter + 1
                            
                if self.level1picked and self.counter == 0:
                    self.level = NoteLevel(notelevel1, self.screen, self.level.stage)
                    self.counter = 1

                if self.level1picked:
                    self.screen.fill("black")
                    self.screen.blit(self.pizzaBackground, (0, 0))
                    self.level.run()
                    if self.level.reset and self.level.stagefinished:
                        self.completecounter += 1
                        if self.completecounter >= 20:
                            self.level.run()
                            self.level = NoteLevel(notelevel1, self.screen, self.level.stage)
                            self.completecounter = 0
                    elif self.level.chain:
                        self.level1picked = False
                        self.stageChooser = False
                        self.counter = 0

                if self.level2picked and self.counter == 0:
                    self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('resources/metronome.mp3'))
                    self.counter = 1

                if self.level2picked:
                    self.screen.fill("black")
                    try:
                        self.level.run(self.end-self.start)
                    except:
                        self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
                        self.level2picked = False
                        self.informationPage2 = False
                        self.stageChooser2 = False
                        self.counter = 0
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                    if self.level.reset and self.level.stagefinished:
                        self.level.run(self.end-self.start)
                        while self.sleepCounter2 == 0:
                            time.sleep(1)
                            self.sleepCounter2 = 1
                        
                        self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
                    elif self.level.reset:
                        self.level = TeleportLevel(teleportlevel1, self.screen, self.level.stage)
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('resources/metronome.mp3'))
                    elif self.level.back:
                        self.level2picked = False
                        self.informationPage2 = False
                        self.stageChooser2 = False
                        self.counter = 0
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.level.settings.collidepoint(event.pos):
                            self.level.settingsClicked = True

            # Update Screen
            pygame.display.update()
            if self.done:
                self.start = 0
                self.end = 0


game = Game()
game.run()
