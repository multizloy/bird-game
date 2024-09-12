import pygame
from pipe import Pipe
from bird import Bird
from game import GameIndicator
from settings import WIDTH, HEIGHT, pipe_size, pipe_gap, pipe_pair_sizes
import random


class World:

    def __init__(self, screen: pygame.display) -> None:
        """
        Initialize World object.

        Args:
            screen (pygame.display): A pygame display surface to draw on.

        """
        self.screen = screen
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.5
        self.current_pipe = None
        self.pipes = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self._generate_world()
        self.playing = False
        self.game_over = False
        self.passed = False
        self.game = GameIndicator(screen)

    def _add_pipe(self):
        """
        Adds a new pipe when the last pipe added has moved past the desired horizontal space.

        The new pipe is created with a random size and added to the sprite group.
        """
        pipe_pair_size = random.choice(pipe_pair_sizes)
        top_pipe_height = pipe_pair_size[0] * pipe_size
        bottom_pipe_height = pipe_pair_size[1] * pipe_size
        top_pipe = Pipe(
            (WIDTH, 0 - (bottom_pipe_height + pipe_gap)), pipe_size, HEIGHT, True
        )
        bottom_pipe = Pipe(
            (WIDTH, top_pipe_height + pipe_gap), pipe_size, HEIGHT, False
        )
        self.pipes.add(top_pipe)
        self.pipes.add(bottom_pipe)
        self.current_pipe = top_pipe

    def _generate_world(self):
        """
        Generates the game world by adding the first pipe and the player
        """
        self._add_pipe()
        bird = Bird((WIDTH // 2 - pipe_size, HEIGHT // 2 - pipe_size), 30)
        self.player.add(bird)

    def _scroll_x(self):
        """
        Scroll the game world's x axis at a constant rate when the game is playing.

        If the game is not playing, the x axis is not scrolled.
        """
        if self.playing:
            self.world_shift = -6
        else:
            self.world_shift = 0

    def _apply_gravity(self, player: Bird):
        """
        Applies gravity to the given player by adding the gravity constant to
        its vertical direction, and then adding that direction to its y position.

        This should be called every frame, regardless of whether the game is
        playing or not.
        """
        if self.playing or self.game_over:
            player.direction.y += self.gravity
            player.rect.y += player.direction.y

    def _handle_collisions(self):
        """
        Checks for collisions between the player and the pipes, and the player
        and the ground.

        If the player collides with either the pipes or the ground, the game
        is over. Otherwise, if the player passes the current pipe, the player's
        score is incremented and the passed flag is set to True.

        """
        bird = self.player.sprite
        if (
            pygame.sprite.groupcollide(self.player, self.pipes, False, False)
            or bird.rect.bottom >= HEIGHT
            or bird.rect.top <= 0
        ):
            self.playing = False
            self.game_over = True
        else:
            bird = self.player.sprite
            if bird.rect.x >= self.current_pipe.rect.centerx:
                bird.score += 1
                self.passed = True

    def update(self, player_event = None):
        """
        Updates the game state.

        Checks for collisions with the pipes and the ground, applies gravity to
        the player, and updates the player's position. If the player has jumped
        and the game is not over, increments the player's score and sets the
        passed flag to True. If the player is not playing, shows the game's
        instructions.

        Args:
            player_event (str): The event triggered by the player. Possible
                values are "jump" and "restart".
        """
        if self.current_pipe.rect.centerx <= (WIDTH //2) - pipe_size:
            self._add_pipe()
        
        self.pipes.update(self.world_shift)
        self.pipes.draw(self.screen)
        
        self._apply_gravity(self.player.sprite)
        self._scroll_x()
        self._handle_collisions()
        
        if player_event == "jump" and not self.game_over:
            player_event = True
        elif player_event == "restart":
            self.game_over = False
            self.pipes.empty()
            self.player.empty()
            self.player.score = 0
            self._generate_world()
        else:
            player_event = False
        if not self.playing:
            self.game.instructions()
        
        self.player.update(player_event)
        self.player.draw(self.screen)
        self.game.show_score(self.player.sprite.score)