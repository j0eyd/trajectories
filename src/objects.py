import pygame
import random
from constants import *

#random color
def getRandCol():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#modify the speed of an object based on a pull vector
def pullSpeed(modified, pull):
	modified.x += pull.x/60
	modified.y += pull.y/60

#fundamental properties of objec
class object():
	def __init__(self, surface, pos = pygame.Vector2(0, 0),
			  speed = pygame.Vector2(0, 0), color = getRandCol()):
		self.surface = surface
		self.pos = pos
		self.speed = speed
		self.color = color
	
	def updatePos(self):
		self.pos.x += self.speed.x/60
		self.pos.y += self.speed.y/60

#object + radius
class circle():
	def __init__(self, surface, radius, pos = pygame.Vector2(0, 0),
			  speed = pygame.Vector2(0, 0), color = getRandCol()):
		self.o = object(surface, pos, speed, color)
		self.radius = radius
	
	def draw(self):
		pygame.draw.circle(self.o.surface, self.o.color, self.o.pos, self.radius)
	
	def updatePosScreen(self):
		outXright = (self.o.pos.x + self.radius > SCREEN_WIDTH)
		outXleft = (self.o.pos.x - self.radius < 0)
		outYdown = (self.o.pos.y + self.radius > SCREEN_HEIGHT)
		outYup = (self.o.pos.y - self.radius < 0)
		if (not outXright and not outXleft and not outYdown and not outYup):
			self.o.updatePos()
		elif (outXright):
			ratio = (SCREEN_WIDTH - (self.o.pos.x + self.radius)) / self.o.speed.x
			self.o.pos.x = SCREEN_WIDTH - self.radius
			self.o.speed.x *= -BOUNCE_DAMP
			self.o.pos.y += self.o.speed.y/60
		# For outXleft
		elif outXleft:
			ratio = (self.o.pos.x - self.radius) / abs(self.o.speed.x)
			self.o.pos.x -= self.radius
			self.o.speed.x *= -BOUNCE_DAMP
			self.o.pos.y += self.o.speed.y / 60

		# For outYdown
		elif outYdown:
			ratio = (SCREEN_HEIGHT - (self.o.pos.y + self.radius)) / self.o.speed.y
			self.o.pos.y += SCREEN_HEIGHT - self.radius
			self.o.speed.y *= -BOUNCE_DAMP
			self.o.pos.x += self.o.speed.x / 60

		# For outYup
		else :
			ratio = (self.o.pos.y - self.radius) / abs(self.o.speed.y)
			self.o.pos.y -= (ratio - 0.5) * abs(self.o.speed.y) + self.radius
			self.o.speed.y *= -BOUNCE_DAMP
			self.o.pos.x += self.o.speed.x / 60