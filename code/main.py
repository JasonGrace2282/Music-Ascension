import pygame, sys, time
from setup import *
from level import Level


class Game:
    def __init__(self):
        # Class which includes all variables
        pygame.init()

        # Screen
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.level = Level(level1, self.screen)

        # Background
        self.background1 = pygame.image.load("resources/frontpage.jpg")
        self.gameOver = pygame.image.load("resources/youwin.png").convert_alpha()
        self.levelBackground = pygame.image.load("resources/LevelBackground.png")
        self.intermediateImage = pygame.image.load("resources/FinalIntermediateImage.png")
        self.startButtonImage = pygame.image.load("resources/start.png")
        self.creditsButtonImage = pygame.image.load("resources/credits.png")
        self.nextButtonImage = pygame.image.load("resources/next.png")
        self.beginnerMap = pygame.image.load("resources/beginnerMap.jpg")
        self.beginnerTopicsCovered = pygame.image.load("resources/beginnertopics.jpg")
        self.beginnerImage = pygame.image.load("resources/FinalBeginnerImage.png")
        self.metronome = pygame.mixer.Sound("resources/Metronome.mp3")

        # Variables
        self.startGame = False
        self.interClicked = False
        self.creditsClicked = False
        self.offCreditButton = False
        self.backButton = False
        self.levelConfirm = False
        self.beginnerClicked = False
        self.nextClicked = False
        self.chooseBeginnerLevel = False
        self.getCoordinates = False
        self.boolean = False
        self.stageChooser = False
        self.level1picked = False
        self.counter = False
        self.informationPage2 = False
        self.nextCounter = 0
        self.metronome.set_volume(0.1)
        self.beginnerRect = pygame.Rect(600 - self.beginnerImage.get_width() / 2, 50, self.beginnerImage.get_width(),
                                        self.beginnerImage.get_height())
        self.area = pygame.Rect(540, 200, self.startButtonImage.get_width(), self.startButtonImage.get_height())
        self.intermediateRect = pygame.Rect(600 - self.intermediateImage.get_width() / 2, 400,
                                            self.intermediateImage.get_width(), self.intermediateImage.get_height())
        self.creditsButton = pygame.Rect(530, 300, self.creditsButtonImage.get_width(),
                                         self.creditsButtonImage.get_height())
        self.nextButton = pygame.Rect(898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height())
        self.noteDurationStage1 = pygame.Rect(540, 310, 75, 75)
        self.noteDurationStartRect = pygame.Rect(898, 582, self.nextButtonImage.get_width(),
                                                 self.nextButtonImage.get_height())

        self.start = 0
        self.end = 0
        self.done = False

    def run(self):
        while 1:
            # The code that runs the program
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
                self.screen.blit(self.beginnerImage, (600 - self.beginnerImage.get_width() / 2, 50))
                self.screen.blit(self.intermediateImage, (
                    600 - self.intermediateImage.get_width() / 2, 400, self.intermediateImage.get_width(),
                    self.intermediateImage.get_height()))

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

                    if self.informationPage2:
                        self.screen.fill(0)
                        self.screen.blit(self.nextButtonImage,
                                         (
                                         898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height()))

                    if self.nextClicked:
                        self.screen.blit(self.beginnerMap, (0, 0))
                        self.chooseBeginnerLevel = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.noteDurationStage1.collidepoint(event.pos):
                        if self.nextCounter:
                            self.stageChooser = True
                        else:
                            self.informationPage2 = True
                            self.nextCounter = True

                if self.stageChooser:
                    self.screen.fill((255, 255, 255))
                    # It is preferable if it is an image instead of typed out
                    title = (pygame.font.SysFont(None, 40)).render('Notes', True, 0)
                    self.screen.blit(title, (0, 0))
                    self.screen.blit(self.nextButtonImage,
                                     (898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height()))
                    pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.stageChooser:
                            if self.noteDurationStartRect.collidepoint(event.pos):
                                self.level1picked = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

                if self.level1picked:
                    self.screen.fill("black")
                    self.level.run(self.end - self.start)
                
                if self.level1picked and self.counter == False:
                    #run metronome
                    self.counter = True
                
                if not self.level1picked and self.counter == True:
                    #turn off metronome
                    self.counter = False
            

                """if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())"""

            # Update Screen
            pygame.display.update()
            if self.done:
                self.start = 0
                self.end = 0


game = Game()
game.run()
