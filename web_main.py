import asyncio
import pygame
from settings import *
from sys import exit
from os.path import join

# components
from game import Game
from score import Score
from preview import Preview

from random import choice

class Main:
    def __init__(self):
        # general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

        # components
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

        # audio - make it optional for web compatibility
        try:
            self.music = pygame.mixer.Sound(join('sound', 'music.wav'))
            self.music.set_volume(0.05)
            self.music.play(-1)
        except (pygame.error, FileNotFoundError):
            print("Audio file not found or audio not supported, continuing without sound")
            self.music = None

        # running flag
        self.running = True

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    async def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # display 
            self.display_surface.fill(GRAY)
            
            # components - using original UI layout
            if not self.game.win:
                self.game.run()
                self.score.run()
                self.preview.run(self.next_shapes)
            else:
                self.game.run()
            
            # updating the game
            pygame.display.update()
            self.clock.tick(60)  # Set a specific FPS
            
            # This is crucial for web compatibility
            await asyncio.sleep(0)

        pygame.quit()

async def main():
    game = Main()
    await game.run()

if __name__ == '__main__':
    asyncio.run(main())
