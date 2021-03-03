import pygame
import sys
import os
import scene

pygame.init()

global Scene
Scene = scene.RsScene()

size = width, height = (640, 480)
black = (0, 0, 0)
screen = pygame.display.set_mode(size)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass

        screen.fill(black)
        pygame.display.flip()
