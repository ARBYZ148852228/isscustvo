from all_colors import *
import random
import time

# Инициализация PyGame
pygame.init()
size = (1280, 720)

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('Discoteca')
FPS = 30  # Устанавливаем частоту кадров
clock = pygame.time.Clock()
running = True

COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA,
          GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE,
          MAROON, TEAL, SILVER, GOLD]

# Количество кругов
NUM_CIRCLES = 10

# Массивы для хранения информации о кругах
circle_positions = []
circle_sizes = []
circle_colors = []

# Генерация начальных параметров кругов
for _ in range(NUM_CIRCLES):
    circle_positions.append((random.randint(0, size[0]), random.randint(0, size[1])))
    circle_sizes.append(random.randint(20, 100))
    circle_colors.append(random.choice(COLORS))

# Определяем начальный цвет фона
BACKGROUND = random.choice(COLORS)

last_update_time = time.time()
update_interval = 3  # Интервал обновления в секундах

# Загружаем музыкальную дорожку
pygame.mixer.music.load('soundtrack.mp3')  # Замените на путь к вашему музыкальному файлу
pygame.mixer.music.play(loops=-1)  # Начинаем воспроизведение музыки в бесконечном цикле

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()
    if current_time - last_update_time >= update_interval:
        # Обновляем параметры кругов
        for i in range(NUM_CIRCLES):
            circle_positions[i] = (random.randint(0, size[0]), random.randint(0, size[1]))
            circle_sizes[i] = random.randint(20, 100)
            circle_colors[i] = random.choice(COLORS)

        # Обновляем цвет фона
        BACKGROUND = random.choice(COLORS)

        # Сохраняем время последнего обновления
        last_update_time = current_time

    # Заполняем фон выбранным цветом
    screen.fill(BACKGROUND)

    # Рисуем круги
    for i in range(NUM_CIRCLES):
        pygame.draw.circle(screen, circle_colors[i], circle_positions[i], circle_sizes[i])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()