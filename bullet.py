import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Classe para gerenciar os projeteis das naves"""
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		
		# cria um bullet rect em (0, 0) em seguida define a posição correta
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		
		# armazena a posicao do projetil como um float
		self.y = float(self.rect.y)
		
	def update(self):
		"""Desloca o projetil verticalmente na tela"""
		#atualiza a posicao exata do projetil
		self.y -= self.settings.bullet_speed
		#atualiza a posicao do rect
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Desenha o projetil na tela"""
		pygame.draw.rect(self.screen, self.color, self.rect) 
		
		
