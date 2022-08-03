import pygame
import sys
import time


class Game:
    def __init__(self):
        # Class which includes all variables

        pygame.init()

        # Screen
        self.width, self.height = 1200, 704
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        # Background
        self.background1 = pygame.image.load("MyImages/App2022/App Images (1).jpg")
        self.gameOver = pygame.image.load("MyImages/App2022/youwin.png").convert_alpha()
        self.levelBackground = pygame.image.load("MyImages/App2022/RandomBackground(ReplaceImageLater).jpg")
        self.intermediateImage = pygame.image.load("MyImages/App2022/IntermediateImage.jpg")
        self.startButtonImage = pygame.image.load("MyImages/App2022/StartButton.png")
        self.creditsButtonImage = pygame.image.load("MyImages/App2022/CreditsButton.png")
        self.nextButtonImage = pygame.image.load("MyImages/App2022/NextButton.png")
        self.beginnerMap = pygame.image.load("MyImages/App2022/BeginnerMap.jpg")
        self.beginnerTopicsCovered = pygame.image.load("MyImages/App2022/TopicsCoveredBeginnerLevelReplacement.jpg")
        self.beginnerImage = pygame.image.load("MyImages/App2022/UpdatedBeginnerImage.png")

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
        self.beginnerRect = pygame.Rect(600-self.beginnerImage.get_width()/2, 50, self.beginnerImage.get_width(), self.beginnerImage.get_height())
        self.area = pygame.Rect(540, 200, self.startButtonImage.get_width(), self.startButtonImage.get_height())
        self.intermediateRect = pygame.Rect(600-self.intermediateImage.get_width()/2, 400, self.intermediateImage.get_width(),
                                            self.intermediateImage.get_height())
        self.creditsButton = pygame.Rect(530, 300, self.creditsButtonImage.get_width(),
                                         self.creditsButtonImage.get_height())
        self.nextButton = pygame.Rect(898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height())
        self.noteDurationStage1 = pygame.Rect(540, 310, 75, 75)
        self.noteDurationStartRect = pygame.Rect(898, 582, self.nextButtonImage.get_width(),
                                                 self.nextButtonImage.get_height())
        print(self.intermediateImage.get_width(), ' ', self.intermediateImage.get_height())

    def run(self):
        while 1:
            # The code that runs the program
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Reset Screen
            self.screen.fill(0)
            # Fills the background
            self.screen.blit(self.background1, (0, 0))
            # Start Button
            # screen.fill((0, 0, 255), rect=(210, 160, 220, 100))
            self.screen.blit(self.startButtonImage, (540, 200))
            # Credits Button
            # screen.fill(0, rect=(200, 275, creditsButtonImage.get_width(), creditsButtonImage.get_height()))
            self.screen.blit(self.creditsButtonImage, (530, 300))
            # Checks if START is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.area.collidepoint(event.pos):
                    self.startGame = True
                    print('START Button Clicked')
                    time.sleep(0.5)
                    self.levelConfirm = True
                    self.offCreditButton = True
                if self.creditsButton.collidepoint(event.pos):
                    self.creditsClicked = True
                    # print('Credits Button CLicked')
            if self.startGame:
                # Background
                self.screen.fill(0)
                self.screen.blit(self.levelBackground, (0, 0))
                # Beginner  image
                self.screen.blit(self.beginnerImage, (600-self.beginnerImage.get_width()/2, 50))
                # Intermediate Image
                self.screen.blit(self.intermediateImage,
                                 (600-self.intermediateImage.get_width()/2, 400, self.intermediateImage.get_width(), self.intermediateImage.get_height()))
                # Advanced
                pass
            if not self.offCreditButton:
                if self.creditsClicked:
                    self.screen.fill((255, 255, 255))
                    creditsText = pygame.font.SysFont(None, 30)
                    creditsText = creditsText.render('Credits:', True, 0)
                    creditsText2 = (pygame.font.SysFont(None, 30)).render('Insert Image Credits Here', True, 100)
                    self.screen.blit(creditsText, (0, 0))
                    self.screen.blit(creditsText2, (0, 100))
                    # Back Button
                    self.screen.fill(0, rect=(0, 480, 200, 123))
            # If intermediateImage clicked, change screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.levelConfirm:
                    if self.intermediateRect.collidepoint(event.pos):
                        self.interClicked = True
                        # print("Intermediate Button Clicked")
                    if self.beginnerRect.collidepoint(event.pos):
                        self.beginnerClicked = True
                        # print("Beginner Button Clicked")
            if self.levelConfirm:
                if self.interClicked:
                    self.screen.fill((255, 255, 255))
                    # Topics Covered (Text)
                    interTopicsText = pygame.font.SysFont(None, 40)
                    interTopicsText = interTopicsText.render('Topics Covered: ', True, 0)
                    self.screen.blit(interTopicsText, (0, 0))
                    # Dynamics and Articulations
                    interTopicsText2 = pygame.font.SysFont(None, 40)
                    interTopicsText2 = interTopicsText2.render('Dynamics and Articulation', True, 0)
                    self.screen.blit(interTopicsText2, (0, 50))
                    # Time Signatures
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
                # If Next is clicked for the beginner level
                if self.nextClicked:
                    self.screen.blit(self.beginnerMap, (0, 0))
                    # print('Next Button Clicked')
                    self.chooseBeginnerLevel = True
                    # self.screen.fill(0, rect=(540, 310, 75, 75))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.noteDurationStage1.collidepoint(event.pos):
                        self.stageChooser = True
                if self.stageChooser:
                    # Fills the screen with the information needed to learn about note duration
                    self.screen.fill((255, 255, 255))
                    # It is preferable if it is an image instead of typed out
                    title = (pygame.font.SysFont(None, 40)).render('Notes', True, 0)
                    self.screen.blit(title, (0, 0))
                    self.screen.blit(self.nextButtonImage,
                                     (898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height()))
                    pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.noteDurationStartRect.collidepoint(event.pos):
                            # Call the note duration minigame file
                            pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

            # Update Screen
            pygame.display.flip()


game = Game()
game.run()
