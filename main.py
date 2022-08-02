import pygame
import sys
import time


class Game:
    def __init__(self):

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

        # Variables
        self.startGame = False
        self.interClicked = False
        self.creditsClicked = False
        self.offCreditButton = False
        self.backButton = False
        self.levelConfirm = False
        self.beginnerClicked = False
        self.nextClicked = False
        self.counter = 1
        self.beginnerRect = pygame.Rect(550, 50, 200, 124)
        self.area = pygame.Rect(540, 200, self.startButtonImage.get_width(), self.startButtonImage.get_height())
        self.intermediateRect = pygame.Rect(550, 400, self.intermediateImage.get_width(),
                                            self.intermediateImage.get_height())
        self.creditsButton = pygame.Rect(530, 300, self.creditsButtonImage.get_width(),
                                         self.creditsButtonImage.get_height())
        self.nextButton = pygame.Rect(898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height())

    def run(self):
        while True:
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
                    print('Credits Button CLicked')
            if self.startGame:
                # Background
                self.screen.fill(0)
                self.screen.blit(self.levelBackground, (0, 0))
                # Beginner text
                self.screen.fill((0, 255, 0), rect=(550, 50, 200, 124))
                beginnerText = pygame.font.SysFont(None, 50)
                beginnerText = beginnerText.render('Beginner', True, 0)
                self.screen.blit(beginnerText, (560, 50))
                # Intermediate Image
                self.screen.blit(self.intermediateImage,
                                 (550, 400, self.intermediateImage.get_width(), self.intermediateImage.get_height()))
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
                        print("Intermediate Button Clicked")
                    if self.beginnerRect.collidepoint(event.pos):
                        self.beginnerClicked = True
                        print("Beginner Button Clicked")
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
                    beginnerTopicsText = (pygame.font.SysFont(None, 40)).render('Topics Covered', True, 0)
                    self.screen.blit(beginnerTopicsText, (0, 0))
                    self.screen.blit(self.nextButtonImage,
                                     (898, 582, self.nextButtonImage.get_width(), self.nextButtonImage.get_height()))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.nextButton.collidepoint(event.pos):
                        self.nextClicked = True

                if self.nextClicked:
                    self.screen.fill(0)
                    if self.counter == 1:
                        print('Next Button Clicked')
                        self.counter -= 1
            # Update Screen
            pygame.display.flip()


game = Game()
game.run()
