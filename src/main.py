import sys

import pygame
import pygame.time as PyTime

import src
from RsSystem import game_system
from scene import RsScene
src.resolutions
if __name__ == "__main__":
    pygame.init()

    size = width, height = (640, 480)
    black = (0, 0, 0)
    screen = pygame.display.set_mode(resolutions)
    absolute_timer = PyTime.Clock()

    Scenes = game_system.Scenes
    Start_scene = RsScene()
    Scenes.append(Start_scene)

    Current_scene = Start_scene
    if not Current_scene:
        raise RuntimeError("No scene found")

    Current_scene.onAwake()
    while Current_scene.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass

        frame_time = absolute_timer.get_time()
        screen.fill(black)
        Current_scene.onUpdate(frame_time)
        Current_scene.onUpdateLater(frame_time)
        Current_scene.onDraw(frame_time)
        Current_scene.onGUI(frame_time)

        pygame.display.flip()
        absolute_timer.tick()
    Current_scene.onDestroy()

    if 0 < len(Scenes):
        Current_scene = Scenes.pop()

    print("Program is ended.")
