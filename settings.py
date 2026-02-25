
class Settings:
	""" Classe para armazenar as configurações do jogo """
	def __init__(self):
		"""Inicializa as configurações do jogo"""
		#configurações da tela
		self.screen_width = 1200
		self.screen_heigth = 800
		self.bg_color = (230, 230, 230)
		
		#configurações da espaçonave
		self.ship_speed = 1.5
		
		#configurações dos projeteis
		self.bullet_speed = 2.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		
