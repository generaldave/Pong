########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# init Class for Pong                                                  #
#                                                                      #
# Created on 2016-12-27                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Constants import *   # Constants File
from   Paddle    import *   # Paddle Class
from   Ball      import *   # Ball Class
from   Score     import *   # Score Class
import pygame               # For GUI

########################################################################
#                                                                      #
#                              INIT CLASS                              #
#                                                                      #
########################################################################

class init(object):
    def __init__(self, appDirectory : str):
        self.appDirectory = appDirectory

        # Initialize pygame
        pygame.init()
        self.background = pygame.image.load(self.appDirectory + \
                                            "/images/background.png")

        # Set collision count to 0
        self.collisionCount = 0

        # Call method to set up GUI
        self.setupGUI()

        # Call method to run app
        self.runApp()

    # Method set up GUI
    def setupGUI(self):
        # Screen attributes
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)
        pygame.display.set_caption("Pong")
        self.clock  = pygame.time.Clock()      # Frames per second
        self.mouse  = pygame.mouse.get_pos()   # Mouse position

        # GUI Objects
        y = SCREEN_RESOLUTION[HEIGHT] / TWO - 40
        self.ball           = Ball(self.screen, self.appDirectory)
        self.playerScore    = Score(self.screen, 145, 20)
        self.computerScore  = Score(self.screen, 470, 20)
        self.playerPaddle   = Paddle(self.screen, self.appDirectory, \
                                    0, y, PLAYER)
        self.computerPaddle = Paddle(self.screen, self.appDirectory, \
                                    630, y, COMPUTER)

    # Method runs app
    def runApp(self):
        run = True
        while run:
            self.mouse = pygame.mouse.get_pos()   # Mouse position

            # Handle Quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Move paddles
            self.playerPaddle.playerMove(self.mouse[1])
            self.computerPaddle.computerMove(self.ball.getY())

            # Detect collision
            if (self.playerPaddle.collidedWith(self.ball) or \
                self.computerPaddle.collidedWith(self.ball)):
                self.ball.setCollided(True)
                self.collisionCount = self.collisionCount + 1

                # After 3 collisions, speed up ball and 
                # computer paddle
                if (self.collisionCount % 3 == 0):
                    self.ball.incrementSpeed()
                    self.computerPaddle.incrementSpeed()

            # Handles scoring
            offScreen = self.ball.getOffScreen()
            if (True in offScreen and not self.ball.getCollided()):
                if (offScreen[PLAYER]):
                    self.computerScore.increment()
                elif (offScreen[COMPUTER]):
                    self.playerScore.increment()
                self.ball.resetOffScreen()
                self.computerPaddle.resetSpeed()

            # Update app
            self.screen.blit(self.background, ORIGIN)
            self.playerPaddle.update()
            self.computerPaddle.update()
            self.ball.update()
            self.playerPaddle.update()
            self.computerPaddle.update()
            self.playerScore.update()
            self.computerScore.update()
            pygame.display.update()
            self.clock.tick(FPS)

        # Quit game cleanly
        pygame.quit()
