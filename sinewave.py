import pygame
from math import pi
from numpy import linspace, sin
pygame.init()
clock = pygame.time.Clock()
shadow = (192, 192, 192)
black = (0, 0, 0)
white = (255,255,255)
lightblue = (0, 0, 255)
screen = pygame.display.set_mode((700,530))
screen.fill(white)
pygame.display.set_caption('Sine wave')
done = False
x_start = 20
y_start = 250
x_r = linspace(0, 4*pi, 200)
y_r = sin(x_r) * (-1)
k = 0
text = pygame.font.SysFont('times new roman', 25)
y_label = text.render('y', 1, black)
x_label = text.render('x', 1, black)
zero = text.render('0', 1, black)
pi = text.render('π', 1, black)
mpi = text.render('-π', 1, black)
x_1 = text.render('1', 1, black)
x_m1 = text.render('-1', 1, black)
degree_180 = text.render('180', 1, black)
degree_m180 = text.render('-180', 1, black)
for i in range(30,671,80):
	pygame.draw.line(screen, shadow, (i,60), (i,440)) # y-grid rectangle
for i in range(60,441,95):
	pygame.draw.line(screen, shadow, (20,i), (680,i)) # x-grid rectangle
pygame.draw.line(screen, black, (350,20), (350,440)) # y-axis	
pygame.draw.line(screen, black, (20,250), (680,250)) # x-axis
pygame.draw.polygon(screen, black, [[330, 20], [350, 0], [370, 20]]) # y-axis arrow
pygame.draw.polygon(screen, black, [[680, 230], [700, 250], [680, 270]]) # x-axis arrow
screen.blit(degree_180, (490,485))
screen.blit(degree_m180, (160,485))
screen.blit(pi, (503,445))
screen.blit(mpi, (175,445))
screen.blit(x_m1, (1,425))
screen.blit(x_1, (5,45))
screen.blit(zero, (5,235))
screen.blit(zero, (345,445))
screen.blit(x_label, (660,250))
screen.blit(y_label, (330,20))
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	if k < (len(x_r)-1):
		start_pos = (x_start+x_r[k]/x_r[-1]*660,y_start+y_r[k]*190)
		end_pos = (x_start+x_r[k+1]/x_r[-1]*660,y_start+y_r[k+1]*190)
		k+=1
		pygame.draw.line(screen, lightblue, start_pos, end_pos, 3)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()