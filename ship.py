import pygame

class Ship:
	"""Classe para cuidar da espaçonave"""
	
	def __init__(self, ai_game):
		"""inicializa a espaçonave e define a posição inicial"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		#sobe a imagem da espaçonave e obtem seu rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		
		#começa cada espaçonave nova no centro inferior da tela
		self.rect.midbottom = self.screen_rect.midbottom
		
		# flag de movimento
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""atualiza a posicao da nave com base na flag de movimento"""
		if self.moving_right:
			self.rect.x += 1 
		if self.moving_left:
			self.rect.x -= 1 
		
	def blitme(self):
		""" desenha a espaçonave em sua localização atual """
		self.screen.blit(self.image, self.rect)
		
	
