import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	""" Classe geral para gerenciar ativos e comportamentos do jogo """
	
	def __init__(self):
		"""Inicia a classe e cria os recursos do jogo"""
		pygame.init()
		self.relogio = pygame.time.Clock()
		self.settings = Settings()

		# TELA CHEIA
		#self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = self.screen.get_rect().height

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
		pygame.display.set_caption("Alien Invasion")
		
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
				
	def run_game(self):
		"""Inicia o loop principal do jogo"""
		while True :
			self._check_events()
			self.ship.update()
			self.bullets.update()
			
			#descarta os projeteis que desapareceram da tela
			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
			#verificar na tela os numeros de projeteis e se estão diminuindo
			#print(len(self.bullets))
			
			self._update_screen()
			self.relogio.tick(60)
	
	
	def _check_events(self):
		""" responde as teclas pressionadas"""
		#observa os eventos do mouse e teclado
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
				
	
	def _check_keydown_events(self, event):
		"""responde ao pressionar uma tecla"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullets()
	
	def _check_keyup_events(self, event):
		"""responde ao soltar a tecla pressionada"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
	
	
	def _fire_bullets(self):
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)
	
				
	def _update_screen(self):
		""" atualiza as imagens da tela e muda para a tela nova"""
		#redesenha a tela a cada passagem pelo loop
		self.screen.fill(self.settings.bg_color)
		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet() 
		
		self.ship.blitme()
		#deixa a tela desenhada mais recente possivel
		pygame.display.flip()
		
	
if __name__ == '__main__':
	#Cria uma instancia do jogo e executa o jogo
	ai = AlienInvasion()
	ai.run_game()
