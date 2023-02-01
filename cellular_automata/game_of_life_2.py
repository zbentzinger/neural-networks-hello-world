from dataclasses import dataclass
import pygame
import numpy as np
import time
import random


@dataclass
class Colors:
    background: tuple
    grid: tuple
    die_next: tuple
    alive_next: tuple


def update_window(screen, cells, size, colors, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive_cells = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        color = colors.background if cells[row, col] == 0 else colors.alive_next

        if cells[row, col] == 1:
            if alive_cells < 2 or alive_cells > 3:
                if with_progress:
                    color = colors.die_next
            elif 2 <= alive_cells <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = colors.alive_next
        else:
            if alive_cells == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = colors.alive_next
            
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1 , size - 1))
    
    return updated_cells



if __name__ == "__main__":
    colors = Colors(
        background=(10, 10, 10), 
        grid=(40, 40, 40), 
        die_next=(170, 170, 170), 
        alive_next=(255, 255, 255)
    )

    size = 10

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    cells =  np.zeros((60, 80))
    screen.fill(colors.grid)
    
    update_window(screen, cells, size, colors=colors)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update_window(screen, cells, size, colors=colors)
                    pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                cells[mouse_pos[1] // size, mouse_pos[0] // size] = 1
                update_window(screen, cells, size, colors=colors)
                pygame.display.update()

        screen.fill(colors.grid)

        if running:
            cells = update_window(screen, cells, size, colors=colors, with_progress=True)
            pygame.display.update()
        
        time.sleep(0.001)
