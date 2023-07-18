import pygame

import game
from constants import width, height, frame_rate, load_text


def main():
    # Some initialization stuff.
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    load_text()

    board = game.empty_board()
    state = game.RED_TURN

    while True:
        # Update the state and check if we should exit the app.
        state, done = game.update(state, board)
        if done:
            break

        # Draw the state to the screen.
        game.draw(state, board, screen)

        # Wait a bit.
        clock.tick(frame_rate)

    pygame.quit()


if __name__ == "__main__":
    main()
