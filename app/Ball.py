########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Ball Class for Pong                                                  #
#                                                                      #
# Created on 2016-12-27                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants import *   # Constants File
import pygame                # For GUI
import random                # For choosing ball velocity

########################################################################
#                                                                      #
#                              BALL CLASS                              #
#                                                                      #
########################################################################

class Ball(object):
    def __init__(self, screen, appDirectory : str):
        self.screen       = screen   # Main screen
        self.appDirectory = appDirectory

        # Ball attributes
        self.image      = pygame.image.load(self.appDirectory + \
                                           "/images/ball.png")
        self.diameter   = BALL_RADIUS * TWO
        self.offScreen  = [False, False]
        self.collided   = False
        self.frameCount = 0

        # Initial ball setup
        self.centerBall()
        self.setInitialVelocity()

    # Method gets collided boolean
    def getCollided(self):
        return self.collided

    # Method sets collided boolean
    def setCollided(self, value : bool):
        self.collided = value

    # Method returns Ball's X value
    def getX(self):
        return self.X

    # Method returns Ball's Y value
    def getY(self):
        return self.Y

    # Method increments speed
    def incrementSpeed(self):
        if (self.xVel < 0):
            self.xVel = self.xVel - .5
        else:
            self.xVel = self.xVel + .5

        if (self.yVel < 0):
            self.yVel = self.yVel - .5
        else:
            self.yVel = self.yVel + .5

    # Method returns offSCreen
    def getOffScreen(self):
        return self.offScreen

    # Method resets offScreen array
    def resetOffScreen(self):
        self.offScreen = [False, False]
        
    # Method centers ball with random velocity
    def centerBall(self):
        self.X = SCREEN_RESOLUTION[WIDTH]  / TWO - BALL_RADIUS
        self.Y = SCREEN_RESOLUTION[HEIGHT] / TWO - BALL_RADIUS

    # Method sets velocity of ball
    def setInitialVelocity(self):
        # Seed velocities
        self.xVel = 0
        self.yVel = 0
        
        # Random velocity
        while (self.xVel == 0):
            self.xVel = (round(random.random() - .05, 1) + 1) * TWO
        while (self.yVel == 0):
            self.yVel = (round(random.random() - .05, 1) + 1) * TWO

        # Negative X?
        negX = random.randint(1, 100)
        if (negX > 50):
            self.xVel = self.xVel * -1

        # Negative Y?
        negY = random.randint(1, 100)
        if (negY > 50):
            self.yVel = self.yVel * -1

    # Method draws ball object
    def drawBall(self):
        self.screen.blit(self.image, (self.X, self.Y))
        self.X = self.X + self.xVel
        self.Y = self.Y + self.yVel

    # Method update ball object
    def update(self):
        # If ball collided with paddle, reverse x
        if (self.collided):
            self.xVel = self.xVel * -1
            self.collided = False
            
        # If ball goes off left or right, recenter and choose new
        # Velocity
        elif ((self.X <= 0 or self.X >= SCREEN_RESOLUTION[WIDTH] - \
                                     self.diameter) and \
              self.collided == False):
            # Handle scoring array
            if (self.X <= 0):
                self.offScreen[PLAYER] = True
            elif (self.X >= SCREEN_RESOLUTION[WIDTH] - self.diameter):
                self.offScreen[COMPUTER] = True

            # Re-center ball and choose new velocity
            self.speed = 2
            self.centerBall()
            self.setInitialVelocity()

        # If ball goes off top or bottom, reverse y velocity
        elif (self.Y <= 0 or self.Y >= SCREEN_RESOLUTION[HEIGHT] - \
                                     self.diameter):
            self.yVel = self.yVel * -1

        # Draw ball
        self.drawBall()
