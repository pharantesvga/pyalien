import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	""" Classe geral para gerenciar ativos e comportamentos do jogo """
	
	def __init__(self):
		"""Inicia a classe e cria os recursos do jogo"""
		pygame.init()
		self.clock = pygame.time.Clock()
		self.settings = Settings()
				
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
		pygame.display.set_caption("Alien Invasion")
		
		self.ship = Ship(self)
		
			
	def run_game(self):
		"""Inicia o loop principal do jogo"""
		while True :
			self._check_events()
			self.ship.update()
			self._update_screen()
			self.clock.tick(60)
	
	
	def _check_events(self):
		""" responde as teclas pressionadas"""
		#observa os eventos do mouse e teclado
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = True
				if event.key == pygame.K_LEFT:
					self.ship.moving_left = True
			
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
					
				if event.key == pygame.K_LEFT:
					self.ship.moving_left = False
				
				
	def _update_screen(self):
		""" atualiza as imagens da tela e muda para a tela nova"""
		#redesenha a tela a cada passagem pelo loop
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		#deixa a tela desenhada mais recente possivel
		pygame.display.flip()
		
	
if __name__ == '__main__':
	#Cria uma instancia do jogo e executa o jogo
	ai = AlienInvasion()
	ai.run_game()
