import pygame, random
width = 800
height = 600
black = (0,0,0)
white = (255,255,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(  ( width, height ) )
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/nave.png").convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.centerx = width // 2
		self.rect.bottom = height - 10
		self.speed_x = 0
		self.shield = 100

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.left < 0:
			self.rect.left = 0

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/meteorito.png").convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange( width - self.rect.width)
		self.rect.y = random.randrange( -100, -40)
		self.speedy = random.randrange(1, 10) 
		self.speedx = random.randrange(-5, 5) 

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 25:
				self.rect.x = random.randrange( width - self.rect.width)
				self.rect.y = random.randrange( -100, -40)
				self.speedy = random.randrange(1, 10) 	

background = pygame.image.load("assets/background.png").convert()


all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
for i in range(8):
	meteor = Meteor()
	all_sprites.add(meteor)
	meteor_list.add(meteor)

running = True
while running:
	clock.tick(60)
	for event  in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	all_sprites.update()

	screen.blit(background, [0,0])

	all_sprites.draw(screen)

	pygame.display.flip()
pygame.quit()
