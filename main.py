import pygame
import os
from constants import *

# needed to remove annoing ALSA sound driver errors. Pulse is the sound server of choice, I guess
# sound driver/server can be confirmed by running >echo $PULSE_SERVER< (shoud see output if it's pulse)
os.environ['SDL_AUDIODRIVER'] = 'pulse'

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
