import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH = 800
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пианино")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Высота клавиш
KEY_HEIGHT = 200

# Количество октав и клавиш в октаве
OCTAVES = 4
KEYS_IN_OCTAVE = 12


# Функция для рисования клавиш
def draw_keys():
    key_width = WIDTH // KEYS_IN_OCTAVE // OCTAVES  # Ширина клавиши
    for octave in range(OCTAVES):
        for key in range(KEYS_IN_OCTAVE):
            # Определяем позицию клавиши
            x = octave * KEYS_IN_OCTAVE * key_width + key * key_width

            # Рисуем белую клавишу
            pygame.draw.rect(WINDOW, WHITE, (x, HEIGHT - KEY_HEIGHT, key_width, KEY_HEIGHT))

            # Рисуем черные клавиши
            if key in [1, 3, 6, 8, 10]:  # Позиции черных клавиш
                black_key_x = x + key_width * 2 / 3  # Позиция черной клавиши
                pygame.draw.rect(WINDOW, BLACK,
                                 (black_key_x, HEIGHT - KEY_HEIGHT * 0.6, key_width / 3, KEY_HEIGHT * 0.6))


# Основной цикл программы
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Заполнение фона
        WINDOW.fill(BLACK)

        # Рисуем клавиши
        draw_keys()

        # Обновляем экран
        pygame.display.flip()


# Запуск программы
if __name__ == "__main__":
    main()
