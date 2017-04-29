from pygame.locals import * 
import pygame 
from os import path


#Get image directory
img_dir = path.join(path.dirname(__file__), 'images')
 
class Shopper:
	x = 44 #initial starting point
	y = 4
	speed = 10
 
	def moveRight(self):
		self.x = self.x + self.speed
 
	def moveLeft(self):
		self.x = self.x - self.speed
 
	def moveUp(self):
		self.y = self.y - self.speed
 
	def moveDown(self):
		self.y = self.y + self.speed
 
class Maze:
	def __init__(self):
		self.M = 100
		self.N = 100
		self.maze = [ 1,1,1,1,1,1,1,1,1,1,
			1,0,0,0,0,0,0,0,0,1,
			1,0,0,0,0,0,0,0,0,1,
			1,0,1,1,1,1,1,1,0,1,
			1,0,1,0,0,0,0,0,0,1,
			1,0,1,0,1,1,1,1,0,1,
			1,0,0,0,0,0,0,0,0,1,
			1,1,1,1,1,1,1,1,1,1 ]
 
	def draw(self,screen,image_surf):
		bx = 0
		by = 0
		for i in range(0,self.M*self.N):
			if self.maze[ bx + (by*self.M) ] == 1:
				screen.blit(image_surf,( bx * 44 , by * 44))
 
		bx = bx + 1
		if bx > self.M-1:
			bx = 0 
			by = by + 1
 
 
class Store:
	windowWidth = 945
	windowHeight = 600
	Shopper = 0
 
	def __init__(self):
		self._running = True
		self._screen = None
		self._image_surf = None
		self._block_surf = None
		self.Shopper = Shopper()
		self.maze = Maze()
 
	def on_init(self):
		pygame.init()
		self._screen = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
		pygame.display.set_caption('Target shopper')
		self._running = True
		self._image_surf = pygame.image.load(path.join(img_dir,"targetshopper.jpg")).convert()
		self._block_surf = pygame.image.load(path.join(img_dir,"block.png")).convert()
		self.grocery = pygame.image.load(path.join(img_dir,"grocery.png")).convert()	 
		self.home = pygame.image.load(path.join(img_dir,"homeimprove.png")).convert()       
		self.cards = pygame.image.load(path.join(img_dir,"cardsparty.png")).convert()       
		self.office = pygame.image.load(path.join(img_dir,"homeoffice.png")).convert()       		
		self.pharmacy = pygame.image.load(path.join(img_dir,"pharmacy.png")).convert() 
		self.petcare = pygame.image.load(path.join(img_dir,"petcare.png")).convert() 
		self.jewelry = pygame.image.load(path.join(img_dir,"jewelry.png")).convert() 
		self.mens = pygame.image.load(path.join(img_dir,"mens.png")).convert() 
		self.womens = pygame.image.load(path.join(img_dir,"womens.png")).convert() 
		self.personal = pygame.image.load(path.join(img_dir,"personal.png")).convert() 
		self.shoes = pygame.image.load(path.join(img_dir,"shoes.png")).convert() 
		self.boys = pygame.image.load(path.join(img_dir,"boys.png")).convert() 
		self.girls = pygame.image.load(path.join(img_dir,"girls.png")).convert() 
		self.electronics = pygame.image.load(path.join(img_dir,"electronics.png")).convert()
		self.toys = pygame.image.load(path.join(img_dir,"toys.png")).convert()
		self.dollar = pygame.image.load(path.join(img_dir,"dollar.png")).convert()
		self.target = pygame.image.load(path.join(img_dir,"target.png")).convert()

	def on_event(self, event):
		if event.type == QUIT:
			self._running = False
 
	def on_loop(self):
		pass
 
	def on_render(self):
		self._screen.fill((255,255,255))
		self._screen.blit(self._image_surf,(self.Shopper.x,self.Shopper.y))
		self._screen.blit(self.grocery, (20, 50))
		self._screen.blit(self.home, (517, 20))
		self._screen.blit(self.cards, (560, 360))
		self._screen.blit(self.office, (560, 265))
		self._screen.blit(self.pharmacy, (200, 290))
		self._screen.blit(self.jewelry, (350, 280))
		self._screen.blit(self.petcare, (460, 110))
		self._screen.blit(self.personal, (200, 390))
		self._screen.blit(self.womens, (212, 470))
		self._screen.blit(self.shoes, (480, 250))
		self._screen.blit(self.mens, (200, 200))
		self._screen.blit(self.girls, (200, 20))
		self._screen.blit(self.boys, (260, 15))
		self._screen.blit(self.toys, (320, 110))
		self._screen.blit(self.electronics, (320, 40))
		self._screen.blit(self.dollar, (620, 470))
		self._screen.blit(self.target, (720, 470))
		self.maze.draw(self._screen, self._block_surf)
		pygame.display.flip()
 
	def on_cleanup(self):
		pygame.quit()
 
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
 
		while( self._running ):
			pygame.event.pump()
			keys = pygame.key.get_pressed()
 
			if (keys[K_RIGHT]):
				self.Shopper.moveRight()
 
			if (keys[K_LEFT]):
				self.Shopper.moveLeft()
 
			if (keys[K_UP]):
				self.Shopper.moveUp()
 
			if (keys[K_DOWN]):
				self.Shopper.moveDown()
 
			if (keys[K_ESCAPE]):
				self._running = False
 
			self.on_loop()
			self.on_render()
		self.on_cleanup()
 
if __name__ == "__main__" :
	theStore = Store()
	theStore.on_execute()
