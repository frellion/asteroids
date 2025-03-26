# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	print("Starting Asteroids!")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	#Group setup
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	#player setup
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


		screen.fill(pygame.Color("black"))
		#player.update(dt)
		#player.draw(screen)
		updatable.update(dt)
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = (clock.tick(60)/1000)


if __name__ == "__main__":
	main()
