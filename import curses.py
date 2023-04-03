import curses
import random
import time

# Инициализация экрана curses
screen = curses.initscr()

# Получаем размеры экрана
max_y, max_x = screen.getmaxyx()

# Задаем начальное положение шарика
ball_y = max_y // 2
ball_x = max_x // 2

# Задаем начальное направление движения шарика
direction_y = 1
direction_x = 1

# Задаем скорость шарика
speed = 0.05

# Отключаем отображение курсора
curses.curs_set(0)

# Бесконечный цикл для движения шарика
while True:
    # Очистка экрана перед рисованием шарика
    screen.clear()

    # Отрисовка шарика
    screen.addstr(int(ball_y), int(ball_x), "o")

    # Обновление экрана
    screen.refresh()

    # Задержка для создания эффекта анимации
    time.sleep(speed)

    # Вычисление нового положения шарика
    ball_y += direction_y
    ball_x += direction_x

    # Проверка столкновения шарика с границами экрана
    if ball_y >= max_y - 1 or ball_y <= 0:
        direction_y *= -1

    if ball_x >= max_x - 1 or ball_x <= 0:
        direction_x *= -1
        
 