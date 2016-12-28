########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Paddle Class for Pong                                                #
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
import pygame               # For GUI
import random               # For choosing paddle velocity
import math                 # For collision detection

########################################################################
#                                                                      #
#                             PADDLE CLASS                             #
#                                                                      #
########################################################################

class Paddle(object):
    ballHint = "Ball Object"
    
    def __init__(self, screen, appDirectory : str, x : int, y :int,
                 player : int):
        self.screen       = screen   # Main screen
        self.appDirectory = appDirectory
        self.player       = player   # 0: Player, 1: Computer

        # Paddle attributes
        self.image    = pygame.image.load(self.appDirectory + \
                                          "/images/paddle.png")
        self.X        = x
        self.Y        = y
        self.speed    = 1
        self.collided = False

    # Method sets collided
    def setCollided(self, value : bool):
        self.collied = value

    # Method resets speed
    def resetSpeed(self):
        self.speed = 1

    # Method increments speed
    def incrementSpeed(self):
        self.speed = self.speed + .3

    # Method draws paddle
    def drawPaddle(self):
        self.screen.blit(self.image, (self.X, self.Y))

    # Method handles player move
    def playerMove(self, y : int):
        if (y <= (PADDLE_HEIGHT / TWO)):
            self.Y = 0
        elif (y >= SCREEN_RESOLUTION[HEIGHT] - (PADDLE_HEIGHT / TWO)):
            self.Y = SCREEN_RESOLUTION[HEIGHT] - PADDLE_HEIGHT
        else:
            self.Y = y - (PADDLE_HEIGHT / TWO)

    # Method handles computer move
    def computerMove(self, y : int):
        # Decide paddle velocity
        velocity = random.randint(2, 6) + self.speed
        if (self.Y > y):
            velocity = velocity * -1        

        # Move paddle
        if (y >= (self.Y + PADDLE_HEIGHT) or y <= self.Y):
            if (self.Y <= 0 and velocity < 0):
                self.Y = 0
            elif (self.Y >= SCREEN_RESOLUTION[HEIGHT] - PADDLE_HEIGHT and \
                  velocity > 0):
                self.Y = SCREEN_RESOLUTION[HEIGHT] - PADDLE_HEIGHT
            else:
                self.Y = velocity + self.Y

    # Method detects collision with ball
    def collidedWith(self, ball : ballHint):
        self.collided = False   # Assume no collision
        
        # Store ball attribute
        ballDiameter = BALL_RADIUS * TWO
        ballX        = ball.getX()
        ballY        = ball.getY()

        # Player paddle collision
        if (ballX <= PADDLE_WIDTH and \
            ballY >= self.Y and ballY <= self.Y + PADDLE_HEIGHT and \
            self.player == PLAYER):
            self.collided = True

        # Computer paddle collision
        elif (ballX >= (SCREEN_RESOLUTION[WIDTH] - PADDLE_WIDTH - \
                        ballDiameter) and \
            ballY >= self.Y and ballY <= self.Y + PADDLE_HEIGHT and \
            self.player == COMPUTER):
            self.collided = True
        
        # Return collision boolean
        return self.collided

    # Method updates paddle
    def update(self):
        self.drawPaddle()
