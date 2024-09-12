import pygame
from settings import import_sprite


class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        """
        Initialize the Bird object.

        Args:
            pos (tuple): The starting position of the bird.
            size (int): The size of the bird.

        Attributes:
            frame_index (int): The index of the current frame of animation.
            animation_delay (int): The number of frames to wait before switching to the next frame.
            jump_move (int): The vertical speed of the bird when jumping.
            bird_img (list): A list of all the frames of animation for the bird.
            image (pygame.Surface): The current frame of animation.
            rect (pygame.Rect): The rectangle of the bird.
            mask (pygame.Mask): The mask of the bird.
            direction (pygame.math.Vector2): The direction of the bird.
            score (int): The score of the bird.
        """
        super().__init__()
        # bird basic info
        self.frame_index = 0
        self.animation_delay = 3
        self.jump_move = -9
        # bird animation
        self.bird_img = import_sprite("assets/character")
        self.image = self.bird_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)
        # bird status
        self.direction = pygame.math.Vector2(0, 0)
        self.score = 0

    # for bird's flying animation
    def _animate(self):
        """For bird's flying animation
        
        This method is used to animate the bird's flying effect by switching
        the surface of the bird between different sprites. The frame index is
        used to keep track of the current frame and the index of the current
        sprite. The sprite index is calculated based on the current frame index
        and the animation delay. The bird's mask is also updated after each
        frame change.
        """
        sprites = self.bird_img
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0

    # to make the bird fly higher
    def _jump(self):
        """Make the bird jump higher
        
        This method is used to make the bird jump higher by setting the y
        component of the direction vector to the jump move value. The jump move
        value is negative, so the bird will move up the screen.
        """
        self.direction.y = self.jump_move

    # updates the bird's overall state
    def update(self, is_jump):
        """Updates the bird's overall state
        
        This method is used to update the bird's overall state by making it
        jump and animate its flying effect. The is_jump parameter is used to
        determine whether the bird should jump or not. The method makes the bird
        jump by calling the _jump method if is_jump is True, and then animate
        the bird's flying effect by calling the _animate method.
        """
        if is_jump:
            self._jump()
        self._animate()
