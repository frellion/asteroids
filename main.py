# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	print("Starting Asteroids!")
	#print(f"Screen width: {SCREEN_WIDTH}")
	#print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	#player setup
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		player.update(dt)
		screen.fill(pygame.Color("black"))
		player.draw(screen)
		pygame.display.flip()
		dt = (clock.tick(60)/1000)


if __name__ == "__main__":
	main()
