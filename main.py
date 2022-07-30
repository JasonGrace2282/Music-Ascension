import pygame, sys, time


class Game():
    def __init__(self):

        pygame.init()

        # Screen
        self.width, self.height = 640, 480
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        # Background
        self.background1 = pygame.image.load("MyImages/App2022/AppImagesFirstPage.jpg").convert_alpha()
        self.gameOver = pygame.image.load("MyImages/App2022/youwin.png").convert_alpha()
        self.forest = pygame.image.load("MyImages/App2022/Forest.png")
        self.intermediateImage = pygame.image.load("MyImages/App2022/IntermediateImage.jpg")
        self.startButtonImage = pygame.image.load("MyImages/App2022/StartButton.png")
        self.creditsButtonImage = pygame.image.load("MyImages/App2022/CreditsButton.png")

        # Variables
        self.startGame = False
        self.interClicked = False
        self.creditsClicked = False
        self.closeStartButton = False
        self.backButton = False
        self.area = pygame.Rect(210, 160, self.startButtonImage.get_width(), self.startButtonImage.get_height())
        self.intermediateRect = pygame.Rect(220, 225, self.intermediateImage.get_width(), self.intermediateImage.get_height())
        self.creditsButton = pygame.Rect(200, 275, self.creditsButtonImage.get_width(), self.creditsButtonImage.get_height())
        self.levelConfirm = False

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
            self.screen.blit(self.startButtonImage, (210, 160))
            # Credits Button
            # screen.fill(0, rect=(200, 275, creditsButtonImage.get_width(), creditsButtonImage.get_height()))
            self.screen.blit(self.creditsButtonImage, (200, 275))
            # Checks if START is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.area.collidepoint(event.pos):
                    self.startGame = True
                    print('START Button Clicked')
                    self.levelConfirm = True
                if self.creditsButton.collidepoint(event.pos):
                    self.creditsClicked = True
                    print('Credits Button CLicked')
            if self.startGame:
                time.sleep(0.2)
                # Background
                self.screen.fill(0)
                self.screen.blit(self.forest, (0, 0))
                # Beginner text
                self.screen.fill((0, 255, 0), rect=(220, 50, 200, 124))
                beginnerText = pygame.font.SysFont(None, 50)
                beginnerText = beginnerText.render('Beginner', True, 0)
                self.screen.blit(beginnerText, (220, 50))
                # Intermediate Image
                self.screen.fill(0, (220, 225, self.intermediateImage.get_width(), self.intermediateImage.get_height()))
                self.screen.blit(self.intermediateImage, (220, 225, self.intermediateImage.get_width(), self.intermediateImage.get_height()))
                # Advanced
                pass
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
                if self.intermediateRect.collidepoint(event.pos):
                    self.interClicked = True
                    print("Intermediate Button Clicked")
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
            # Update Screen
            pygame.display.flip()

game = Game()
game.run()


