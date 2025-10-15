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
green = (0, 255, 0)

font = pygame.font.SysFont('Arial', 30)
text = 'Enter - Start Sorting   Space - Pause Sorting   R - Reset (While paused)'
text_surface = font.render(text, True, black)  # Cream o suprafață pentru text
text_rect = text_surface.get_rect(center=(600, 100))  # Poziția centrului textului


running = True

def insertionSortVis(arr):
    # Parcurgem fiecare element din vector, începând cu al doilea
    for i in range(1, len(arr)):
        key = arr[i]# Elementul curent de inserat în subarray-ul sortat
        j = i - 1
        # Mutăm elementele mai mari decât `key` cu o poziție în față
        while j >= 0 and arr[j] > key:
            if handlePauseOrReset(): return False
            drawElements(arr,i,j)
            arr[j + 1] = arr[j]
            drawElements(arr,i,j+1)
            j -= 1

        # Inserăm `key` în poziția corectă
        arr[j + 1] = key
        drawElements(arr,j + 1, 100)
    drawElements(arr,100, 100)
    running = False
    return True

def drawElements(array, i, j):
    screen.fill(background_colour)  # Curăță ecranul
    screen.blit(text_surface, text_rect)
    rect_width = 25  # Lățimea fiecărui dreptunghi
    for k in range(len(array)):
        color = black  # Culoarea implicită
        if k == i:
            color = red
        elif k == j:
            color = green
        # Poziția pe axa X
        rect_x = 100 + k * (rect_width + 5)  # Adaugă 5 pixeli între dreptunghiuri
        # Poziția pe axa Y este setată astfel încât dreptunghiurile să pornească de la bază
        rect_height = array[k]  # Scara pentru înălțime
        rect_y = 850 - rect_height  # Lasă 50 pixeli sus pentru margine
        pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height))  # Desenează dreptunghiul
    pygame.display.flip()  # Actualizăm ecranul
    time.sleep(0.01)  # Întârziere pentru a vizualiza comparația


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

drawElements(vector, 100, 100)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not insertionSortVis(vector):
                    vector = reset.copy()
                    drawElements(vector, 100, 100)

pygame.quit()