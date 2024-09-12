import pygame
from settings import WIDTH, HEIGHT

pygame.font.init()


class GameIndicator:
    def __init__(self, screen):
        """
        Initialize GameIndicator object.

        Parameters
        ----------
        screen : pygame.Surface
            The surface to draw the text onto.

        Attributes
        ----------
        screen : pygame.Surface
            The surface to draw the text onto.
        font : pygame.font.Font
            The font to use for rendering the score.
        inst_font : pygame.font.Font
            The font to use for rendering the instructions.
        color : pygame.Color
            The color to use for rendering the score.
        inst_color : pygame.Color
            The color to use for rendering the instructions.
        """
        self.screen = screen
        self.font = pygame.font.SysFont("Bauhaus 93", 60)
        self.inst_font = pygame.font.SysFont("Bauhaus 93", 30)
        self.color = pygame.Color("white")
        self.inst_color = pygame.Color("black")

    def show_score(self, int_score):
        
        """
        Show the current score of the bird on the screen.

        Parameters
        ----------
        int_score : int
            The current score of the bird.
        """

        bird_score = str(int_score)
        score = self.font.render(bird_score, True, self.color)
        self.screen.blit(score, (WIDTH // 2, 50))

    def instructions(self):
        
        """
        Show the instructions of the game on the screen.

        This function will display the instructions on the screen at the
        specified coordinates. The instructions are displayed in the specified
        color using the specified font.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        inst_text1 = "Press SPACE button to Jump,"
        inst_text2 = 'Press "R" Button to Restart Game.'
        ins1 = self.inst_font.render(inst_text1, True, self.inst_color)
        ins2 = self.inst_font.render(inst_text2, True, self.inst_color)
        self.screen.blit(ins1, (95, 400))
        self.screen.blit(ins2, (70, 450))
