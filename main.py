# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	print("Starting Asteroids!")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	#Group setup
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	#player setup
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	#asteroidfield setup
	asteroidField = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


		screen.fill(pygame.Color("black"))
		#can run update() on Group
		updatable.update(dt)
		#drawable objects must  be looped through
		for item in drawable:
			item.draw(screen)
		for asteroid in asteroids:
			if asteroid.is_collision(player):
				sys.exit("Game Over!")
			for shot in shots:
				if asteroid.is_collision(shot):
					shot.kill()
					asteroid.kill()
		pygame.display.flip()
		dt = (clock.tick(60)/1000)


if __name__ == "__main__":
	main()
