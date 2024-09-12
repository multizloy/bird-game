from os import walk
import pygame

WIDTH = 600
HEIGHT = 650

pipe_pair_sizes = [
    (1,7),
    (2,6),
    (3,5),
    (4,4),
    (5,3),
    (6,2),
    (7,1),
]
pipe_size = HEIGHT // 10
pipe_gap = (pipe_size * 2) + (pipe_size // 2)
ground_space =50

def import_sprite(path: str) -> pygame.Surface:

    """
    Import all images in a given path and return them as a list of Surfaces.

    Args:
        path (str): The path to the directory containing the images to be imported.

    Returns:
        list[pygame.Surface]: A list of all the images in the directory as Surfaces.
    """
    surface_list = []
    for _, __, img_files in walk(path):
        for img_file in img_files:
            full_path = f"{path}/{img_file}"
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)

    return surface_list