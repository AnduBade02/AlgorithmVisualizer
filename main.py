import bubble_sort
import insertion_sort
import pygame
import random

pygame.init()

black = (0, 0, 0)

background_colour = (255, 255, 255)
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Algorithm Visualizer')

vector = [random.randint(1, 500) for _ in range(33)]
reset = vector.copy()
print("Vector inițial:", vector)

font = pygame.font.SysFont('Arial', 30)
text = 'B - Bubble Sort    I - Insertion Sort'
text_surface = font.render(text, True, black)  # Cream o suprafață pentru text
text_rect = text_surface.get_rect(center=(600, 400))  # Poziția centrului textului

screen.fill(background_colour)  # Curăță ecranul
screen.blit(text_surface, text_rect)
pygame.display.flip()
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bubble_sort.bubbleSortVis(vector)
                elif event.key == pygame.K_i:
                    insertion_sort.insertionSortVis(vector)