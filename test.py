import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка параметров окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Скруглённый прямоугольник с альфа-каналом")


def draw_rounded_rect(surface, color, rect, radius):
    """Рисует скруглённый прямоугольник с альфа-каналом."""
    # Создаем временную поверхность
    shape_surface = pygame.Surface(rect.size, pygame.SRCALPHA)

    # Рисуем закругленный прямоугольник на временной поверхности
    pygame.draw.rect(shape_surface, color, (0, 0, rect.width, rect.height), border_radius=radius)

    # Отображаем временную поверхность на основной
    surface.blit(shape_surface, rect.topleft)


# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона белым цветом
    screen.fill((255, 255, 255))

    # Параметры для отрисовки
    rect = pygame.Rect(100, 100, 200, 100)  # Позиция и размер прямоугольника
    color = (0, 128, 255, 128)  # Цвет с альфа-каналом (RGBA)
    radius = 20  # Радиус скругления

    # Рисуем скруглённый прямоугольник с альфа-каналом
    draw_rounded_rect(screen, color, rect, radius)

    # Обновляем экран
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()