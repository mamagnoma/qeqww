import random
import time
import curses

# инициализация экрана
screen = curses.initscr()
curses.noecho()
curses.curs_set(False)
screen.keypad(True)

# получить размер экрана
max_y, max_x = screen.getmaxyx()

# создать список букв
letters = []
while True:
    # создать новую букву с случайным символом и начальными координатами
    letter = {
        "char": chr(random.randint(65, 90)),
        "y": 0,
        "x": random.randint(0, max_x),
    }
    letters.append(letter)

    # отображение всех букв на экране
    screen.clear()
    for letter in letters:
        screen.addstr(int(letter["y"]), int(letter["x"]), letter["char"])

    # обновление экрана
    screen.refresh()

    # перемещение каждой буквы на одну единицу вниз
    for letter in letters:
        letter["y"] += 1

        # удаление буквы, если она достигла конца экрана
        if letter["y"] >= max_y:
            letters.remove(letter)

    # задержка на 0.1 секунды
    time.sleep(0.1)