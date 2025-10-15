import pygame
import random
import time

# Inițializăm Pygame
pygame.init()

random.seed(42)

# Configurarea culorilor și ferestrei
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Algorithm Visualizer')

# Generarea unui vector aleator
vector = [random.randint(1, 500) for _ in range(33)]
reset = vector.copy()
print("Vector inițial:", vector)

black = (0, 0, 0)
red = (255, 0, 0)

font = pygame.font.SysFont('Arial', 30)
text = 'Enter - Start Sorting   Space - Pause Sorting   R - Reset (While paused)'
text_surface = font.render(text, True, black)  # Cream o suprafață pentru text
text_rect = text_surface.get_rect(center=(600, 100))  # Poziția centrului textului


running = True

def bubbleSortVis(arr):
    drawElements(vector, 100)
    n = len(arr)
    # Parcurgem fiecare element al array-ului
    for i in range(0, n):
        if handlePauseOrReset(): return False
        # Ultimele i elemente sunt deja sortate
        for j in range(0, n - i - 1):
            # Desenăm elementele înainte de comparație
            drawElements(arr, j)  # Evidențiem elementele care se compară
            if handlePauseOrReset(): return False
            # Compară elementele adiacente
            if arr[j] > arr[j + 1]:
                # Schimbă elementele dacă sunt în ordine greșită
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Desenăm elementele după fiecare schimbare
                drawElements(arr, j)  # Redesenăm elementele pentru a arăta schimbarea
    drawElements(vector, 100)
    running = False
    return True

def drawElements(array, j):
    screen.fill(background_colour)  # Curăță ecranul
    screen.blit(text_surface, text_rect)
    rect_width = 25  # Lățimea fiecărui dreptunghi
    for i in range(len(array)):
        color = black  # Culoarea implicită
        # Evidențiem elementele care se compară doar dacă arr[j] < arr[j + 1]
        if i == j or i == j + 1:
            color = red
        # Poziția pe axa X
        rect_x = 100 + i * (rect_width + 5)  # Adaugă 5 pixeli între dreptunghiuri
        # Poziția pe axa Y este setată astfel încât dreptunghiurile să pornească de la bază
        rect_height = array[i]  # Scara pentru înălțime
        rect_y = 850 - rect_height  # Lasă 50 pixeli sus pentru margine
        pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height))  # Desenează dreptunghiul
    pygame.display.flip()  # Actualizăm ecranul
    time.sleep(0.1)  # Întârziere pentru a vizualiza schimbarea

def handlePauseOrReset():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = True
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.KEYDOWN:
                            if pause_event.key == pygame.K_SPACE:
                                paused = False  # Exit pause mode
                            elif pause_event.key == pygame.K_r:
                                return True
                        if pause_event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            return


drawElements(vector, 100)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not bubbleSortVis(vector):
                    vector = reset.copy()
                    drawElements(vector, 100)

pygame.quit()