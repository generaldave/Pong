########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Score Class for Pong                                                 #
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

########################################################################
#                                                                      #
#                             SCORE CLASS                              #
#                                                                      #
########################################################################

class Score(object):
    def __init__(self, screen, x : int, y : int):
        self.screen = screen   # Main screen

        # Initialize font
        pygame.font.init()
        self.font = pygame.font.SysFont("Helvetica", FONT_SIZE)

        # Text attributes
        self.color = WHITE
        self.score = "0"
        self.X     = x
        self.Y     = y

    # Method increments score
    def increment(self):
        self.score = str(int(self.score) + 1)

    # Method draws text
    def drawText(self):
        self.text = self.font.render(self.score, \
                                     True,       \
                                     self.color)
        self.screen.blit(self.text, (self.X, self.Y))

    # Method updates score
    def update(self):
        self.drawText()
        
