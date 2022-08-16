import pygame, sys, time
from setup import *
from level import TeleportLevel, NoteLevel


class Game:
    def __init__(self):
        # Class which includes all variables
        pygame.init()

        # Screen
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.level = TeleportLevel(level1, self.screen, 1)

        # Background
        self.background1 = pygame.image.load("resources/frontpage.jpg")
        self.levelBackground = pygame.image.load("resources/background.png")
        self.intermediateImage = pygame.image.load("resources/intermediate.png")
        self.startButtonImage = pygame.image.load("resources/start.png")
        self.creditsButtonImage = pygame.image.load("resources/credits.png")
        self.nextButtonImage = pygame.image.load("resources/next.png")
        self.beginnerMap = pygame.image.load("resources/beginnermap.jpg")
        self.beginnerTopicsCovered = pygame.image.load("resources/beginnertopics.jpg")
        self.beginnerImage = pygame.image.load("resources/beginner.png")
        self.informationPage1 = pygame.image.load("resources/NDNotes.png")
        self.NDhow2play = pygame.image.load("resources/HowToPlayND.png")
        self.playButton = pygame.image.load("resources/Play.png")

        # Variables
        self.startGame = False
        self.interClicked = False
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
        self.counter = 0
        self.beginnerRect = pygame.Rect(600-self.beginnerImage.get_width()/2, 50, self.beginnerImage.get_width(), self.beginnerImage.get_height())
        self.startRect = pygame.Rect(540, 200, self.startButtonImage.get_width(), self.startButtonImage.get_height())
        self.intermediateRect = pygame.Rect(600-self.intermediateImage.get_width()/2, 400, self.intermediateImage.get_width(), self.intermediateImage.get_height())
        self.creditsButton = pygame.Rect(530, 300, self.creditsButtonImage.get_width(), self.creditsButtonImage.get_height())
        self.nextButton = pygame.Rect(898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height())
        self.noteDurationStage1 = pygame.Rect(28, 341, 139, 188)
        self.noteDurationStage2 = pygame.Rect(600, 100, 75, 75)
        self.noteDurationStartRect = pygame.Rect(898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height())

        self.start = 0
        self.end = 0
        self.done = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
            self.screen.blit(self.background1, (0, 0))
            self.screen.blit(self.startButtonImage, (540, 200))
            self.screen.blit(self.creditsButtonImage, (530, 300))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.area.collidepoint(event.pos):
                    self.startGame = True
                    print('START Button Clicked')
                    time.sleep(0.5)
                    self.levelConfirm = True
                    self.offCreditButton = True
                if self.creditsButton.collidepoint(event.pos):
                    self.creditsClicked = True

            if self.startGame:
                self.screen.fill(0)
                self.screen.blit(self.levelBackground, (0, 0))
                self.screen.blit(self.beginnerImage, (600-self.beginnerImage.get_width()/2, 50))
                self.screen.blit(self.intermediateImage, (600-self.intermediateImage.get_width()/2, 400, self.intermediateImage.get_width(), self.intermediateImage.get_height()))
            

            if not self.offCreditButton:
                if self.creditsClicked:
                    self.screen.fill((255, 255, 255))
                    creditsText = pygame.font.SysFont(None, 30)
                    creditsText = creditsText.render('Credits:', True, 0)
                    creditsText2 = (pygame.font.SysFont(None, 30)).render('Insert Image Credits Here', True, 100)
                    self.screen.blit(creditsText, (0, 0))
                    self.screen.blit(creditsText2, (0, 100))
                    self.screen.fill(0, rect=(0, 480, 200, 123))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.levelConfirm:
                    if self.intermediateRect.collidepoint(event.pos):
                        self.interClicked = True
                    if self.beginnerRect.collidepoint(event.pos):
                        self.beginnerClicked = True

            if self.levelConfirm:
                if self.interClicked:
                    self.screen.fill((255, 255, 255))
                    interTopicsText = pygame.font.SysFont(None, 40)
                    interTopicsText = interTopicsText.render('Topics Covered: ', True, 0)
                    self.screen.blit(interTopicsText, (0, 0))
                    interTopicsText2 = pygame.font.SysFont(None, 40)
                    interTopicsText2 = interTopicsText2.render('Dynamics and Articulation', True, 0)
                    self.screen.blit(interTopicsText2, (0, 50))
                    interTopicsText3 = pygame.font.SysFont(None, 40)
                    interTopicsText3 = interTopicsText3.render('Time Signatures', True, 0)
                    self.screen.blit(interTopicsText3, (0, 100))

                if self.beginnerClicked:
                    self.screen.fill((255, 255, 255))
                    self.screen.blit(self.beginnerTopicsCovered, (0, 0))
                    self.screen.blit(self.nextButtonImage,
                                     (898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height()))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.nextButton.collidepoint(event.pos):
                        self.nextClicked = True

                if self.nextClicked:
                    self.screen.blit(self.beginnerMap, (0, 0))
                    self.chooseBeginnerLevel = True

                if event.type == pygame.MOUSEBUTTONDOWN and self.chooseBeginnerLevel:
                    if self.noteDurationStage1.collidepoint(event.pos):
                        self.stageChooser = True
                    if self.noteDurationStage2.collidepoint(event.pos):
                        self.stageChooser2 = True

                if self.stageChooser:
                    self.screen.fill((255, 255, 255))
                    self.screen.blit(self.informationPage1, (0, 0))
                    self.screen.blit(self.playButton, (461,55))
                    self.screen.blit(self.playButton, (461,285))
                    self.screen.blit(self.playButton, (1038,55))
                    self.screen.blit(self.playButton, (1038,285))
                    self.screen.blit(self.nextButtonImage, (898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height()))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.noteDurationStartRect.collidepoint(event.pos):
                            self.level1picked = True
                
                if self.stageChooser2:
                    self.screen.fill((255, 255, 255))
                    title = (pygame.font.SysFont(None, 40)).render('Notes', True, 0)
                    self.screen.blit(title, (0, 0))
                    self.screen.blit(self.nextButtonImage, (898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height()))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.noteDurationStartRect.collidepoint(event.pos):
                            self.level2picked = True
                            
                if self.level1picked and self.counter == 0:
                    self.level = TeleportLevel(level1, self.screen, self.level.stage)
                    self.counter = 1

                if self.level1picked:
                    self.screen.fill("black")
                    self.level.run(self.end-self.start)
                    if self.level.reset and self.level.stagefinished:
                        self.level.run(self.end-self.start)
                        time.sleep(1)
                        self.level = TeleportLevel(level1, self.screen, self.level.stage)
                    elif self.level.reset:
                        self.level = TeleportLevel(level1, self.screen, self.level.stage)
                    elif self.level.back:
                        self.level1picked = False
                        self.stageChooser = False
                        self.counter = 0
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.level.settings.collidepoint(event.pos):
                            self.level.settingsClicked = True
                
                if self.level2picked and self.counter == 0:
                    self.level = NoteLevel(level1, self.screen, self.level.stage)
                    self.counter = 1
                
                if self.level2picked:
                    self.screen.fill("black")
                    self.level.run(self.end-self.start)

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                
            # Update Screen
            pygame.display.update()
            if self.done:
                self.start = 0
                self.end = 0


game = Game()
game.run()