from dataclasses import dataclass
from typing import Optional

import pygame

frame_rate = 30

padding = 25
top_padding = 125
piece_size = 50
border_size = 25

rows = 6
columns = 7

width = 2 * padding + columns * piece_size + (columns + 1) * border_size
height = padding + top_padding + rows * piece_size + (rows + 1) * border_size

border_color = (0, 0, 255)
background_color = (255, 255, 255)
red_color = (255, 0, 0)
yellow_color = (255, 255, 0)


@dataclass
class Text:
    red_turn_text: Optional[pygame.Surface] = None
    yellow_turn_text: Optional[pygame.Surface] = None
    red_win_text: Optional[pygame.Surface] = None
    yellow_win_text: Optional[pygame.Surface] = None
    draw_text: Optional[pygame.Surface] = None
    number_texts: Optional[list[pygame.Surface]] = None


def resize_surface(surface: pygame.Surface, n: int):
    width = n * surface.get_width()
    height = n * surface.get_height()
    resized = pygame.Surface((width, height))
    old_pixels = pygame.PixelArray(surface.copy())
    pixels = pygame.PixelArray(resized)
    for x in range(width):
        for y in range(height):
            pixels[x, y] = old_pixels[x // n, y // n]  # type: ignore
    return pixels.surface.convert()


def load_scaled(path: str) -> pygame.Surface:
    white = (255, 255, 255)
    image = pygame.image.load(path)
    width, height = image.get_size()
    pixels = pygame.PixelArray(image)
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == white:  # type: ignore
                pixels[x, y] = text_color  # type: ignore
            else:
                pixels[x, y] = background_color  # type: ignore
    return resize_surface(pixels.surface, text_scale)


def load_text():
    text_holder.red_turn_text = load_scaled("text/red_turn.png")
    text_holder.yellow_turn_text = load_scaled("text/yellow_turn.png")
    text_holder.red_win_text = load_scaled("text/red_win.png")
    text_holder.yellow_win_text = load_scaled("text/yellow_win.png")
    text_holder.draw_text = load_scaled("text/draw.png")
    text_holder.number_texts = [load_scaled(f"text/{i}.png") for i in range(1, 8)]


text_color = 0xFF000000
text_scale = 4
text_holder = Text()
number_x_offset = 15
number_y_offset = 80
