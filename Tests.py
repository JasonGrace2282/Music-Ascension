import pygame
import time

# from pygame.locals import *
# import math
# import random
# import sys
# import pygame as pg

# Screen

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Background
background1 = pygame.image.load("MyImages/App2022/AppImagesFirstPage.jpg").convert_alpha()
gameOver = pygame.image.load("resources/BB_Resources/resources/images/youwin.png").convert_alpha()
forest = pygame.image.load("MyImages/App2022/Forest.png")
intermediateImage = pygame.image.load("MyImages/App2022/IntermediateImage.jpg")
startButtonImage = pygame.image.load("MyImages/App2022/StartButton.png")
creditsButtonImage = pygame.image.load("MyImages/App2022/CreditsButton.png")

# Variables
running = 1
startGame = False
interClicked = False
creditsClicked = False
closeStartButton = False
backButton = False
area = pygame.Rect(210, 160, startButtonImage.get_width(), startButtonImage.get_height())
intermediateRect = pygame.Rect(220, 225, intermediateImage.get_width(), intermediateImage.get_height())
creditsButton = pygame.Rect(200, 275, creditsButtonImage.get_width(), creditsButtonImage.get_height())
levelConfirm = False
# startButton = pygame.Rect(210)
# Other Code
while running:
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            running = 0
            pygame.quit()
            exit(0)
    # Reset Screen
    screen.fill(0)
    # Fills the background
    screen.blit(background1, (0, 0))
    # Start Button
    # screen.fill((0, 0, 255), rect=(210, 160, 220, 100))
    screen.blit(startButtonImage, (210, 160))
    # Credits Button
    # screen.fill(0, rect=(200, 275, creditsButtonImage.get_width(), creditsButtonImage.get_height()))
    screen.blit(creditsButtonImage, (200, 275))
    # Checks if START is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if area.collidepoint(event.pos):
            startGame = True
            print('START Button Clicked')
            levelConfirm = True
        if creditsButton.collidepoint(event.pos):
            creditsClicked = True
            print('Credits Button CLicked')
    if startGame:
        time.sleep(0.2)
        # Background
        screen.fill(0)
        screen.blit(forest, (0, 0))
        # Beginner text
        screen.fill((0, 255, 0), rect=(220, 50, 200, 124))
        beginnerText = pygame.font.SysFont(None, 50)
        beginnerText = beginnerText.render('Beginner', True, 0)
        screen.blit(beginnerText, (220, 50))
        # Intermediate Image
        screen.fill(0, (220, 225, intermediateImage.get_width(), intermediateImage.get_height()))
        screen.blit(intermediateImage, (220, 225, intermediateImage.get_width(), intermediateImage.get_height()))
        # Advanced
        pass
    if creditsClicked:
        screen.fill((255, 255, 255))
        creditsText = pygame.font.SysFont(None, 30)
        creditsText = creditsText.render('Credits:', True, 0)
        creditsText2 = (pygame.font.SysFont(None, 30)).render('Insert Image Credits Here', True, 100)
        screen.blit(creditsText, (0, 0))
        screen.blit(creditsText2, (0, 100))
        # Back Button
        screen.fill(0, rect=(0, 480, 200, 123))
    # If intermediateImage clicked, change screen
    if event.type == pygame.MOUSEBUTTONDOWN:
        if intermediateRect.collidepoint(event.pos):
            interClicked = True
            print("Intermediate Button Clicked")
    if levelConfirm:
        if interClicked:
            screen.fill((255, 255, 255))
            # Topics Covered (Text)
            interTopicsText = pygame.font.SysFont(None, 40)
            interTopicsText = interTopicsText.render('Topics Covered: ', True, 0)
            screen.blit(interTopicsText, (0, 0))
            # Dynamics and Articulations
            interTopicsText2 = pygame.font.SysFont(None, 40)
            interTopicsText2 = interTopicsText2.render('Dynamics and Articulation', True, 0)
            screen.blit(interTopicsText2, (0, 50))
            # Time Signatures
            interTopicsText3 = pygame.font.SysFont(None, 40)
            interTopicsText3 = interTopicsText3.render('Time Signatures', True, 0)
            screen.blit(interTopicsText3, (0, 100))
    # Update Screen
    pygame.display.flip()
