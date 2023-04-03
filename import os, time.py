import os, time

def start(word_count, min_len=6, max_len=8):
    words = []
    os.system('cls')

    print(f"Введите слова ({word_count} по {min_len}-{max_len} букв)")
    for i in range(word_count):
        words.append(input(f'Введите слово №{i + 1}: '))
    for i in range(len(words)):
        if len(words[i]) > max_len or len(words[i]) < min_len:
            print(f'Кажется в слове {i + 1} букв больше или меньше нужного\n\tДавай по новой')
            time.sleep(2)
            start(word_count)
    print(words)
    words_list = words
    ans = int(input('Номер задания: '))
    if ans == 1:
        print("Поменять местами слова с максимальной и минимальной длиной при условии, что такие слова единственные")
        max_word = max(words_list)
        min_word = min(words_list)
        print(f'Максимальная длина у слова: {max_word}')
        print(f'Минимальная длина у слова: {min_word}')
        if words_list.count(max_word) == 1 and words_list.count(min_word) == 1:
            max_index = words_list.index(max_word)
            min_index = words_list.index(min_word)
            words_list[max_index] = min_word
            words_list[min_index] = max_word
        print(words_list)
    elif ans == 2:
        print("Заменить окончания (последние два символа) на 'ая' в словах, длина которых равна 5 ")
        for i in range(len(words_list)):
            if len(words_list[i]) == 5:
                words_list[i] = words_list[i][:3:1] + 'ая'
        print(words_list)
    elif ans == 3:
        print("Поменять местами слово, начинающееся на 'a', со словом, оканчивающимся на 'я', при условии, что такие слова существуют и являются единственными")
        wordA = []
        wordB = []
        for i in words_list:
            if i[-1:] == 'я':
                wordB = i
            if i[0] == 'а':
                wordA = i
        if len(wordA) == 1 and len(wordB) == 1:
            words_list[words_list.index(wordA)] = wordB
            words_list[words_list.index(wordB)] = wordA
        print(words_list)
    elif ans == 4:
        print("Удалить последние 3 символа из слов, начинающихся на 'a' ")
        for i in range(len(words_list)):
            if words_list[i][0] == "а":
                words_list[i] = words_list[i][:len(words_list[i])-3]
        print(words_list)
    elif ans == 5:
        print("Удалить первые 3 символа из слов, оканчивающихся на 'ие' ")
        for i in range(len(words_list)):
            if words_list[i][-2:] == "ие":
                words_list[i] = words_list[i][3:]
        print(words_list)
    elif ans == 6:
        print("Дополнить символом '*' слова, имеющие длину меньше максимальной по варианту задания, до максимальной ")
        for i in range(len(words_list)):
            if len(words_list[i]) < max_len:
                words_list[i] += (max_len - len(words_list[i])) * '*'
        print(words_list)
    elif ans == 7:
        print("Заменить первые 3 символа слов, имеющих выбранную длину, на символ '*' ")
        lenW = int(input('Длинна для замены: '))
        for i in range(len(words_list)):
            if len(words_list[i]) == lenW:
                words_list[i] = '***' + words_list[i][3:]
        print(words_list)
    elif ans == 8:
        print("Удалить все символы 'а' из слов, длина которых равна выбранной ")
        lenW = int(input('Длинна для удаления: '))
        for i in range(len(words_list)):
            if len(words_list[i]) == lenW:
                words_list[i] = words_list[i].replace('а', '')
        print(words_list)
    elif ans == 9:
        print("Заменить все символы 'a' на 'd' в словах, длина которых меньше выбранной ")
        lenW = int(input('Длинна для замены: '))
        for i in range(len(words_list)):
            if len(words_list[i]) < lenW:
                words_list[i] = words_list[i].replace('а', 'd')
        print(words_list)
    elif ans == 10:
        print("Заменить первые строчные буквы на заглавные в каждом слове, длина которого больше выбранной ")
        lenW = int(input('Длинна для upper: '))
        for i in range(len(words_list)):
            if len(words_list[i]) > lenW:
                words_list[i] = words_list[i].title()
        print(words_list)
    elif ans == 11:
        print("Вставить пробел после первых 2-х символов в слова, имеющие длину, на 1 меньше максимальной по варианту задания ")
        for i in range(len(words_list)):
            if len(words_list[i]) == max_len - 1:
                words_list[i] = words_list[0:2:1] + ' ' + words_list[i][2:]
        print(words_list)
    elif ans == 12:
        print("Заменить первую строчную букву на заглавную в словах, имеющих выбранную длину ")
        lenW = int(input('Длинна для upper: '))
        for i in range(len(words_list)):
            if len(words_list[i]) == lenW:
                words_list[i] = words_list[i].title()
        print(words_list)
    elif ans == 13:
        print("Вставить пробел перед последними 2-мя символами в слова, имеющие минимальную по варианту задания длину ")
        for i in range(len(words_list)):
            if len(words_list[i]) == min_len:
                words_list[i] = words_list[i][0:len(words_list[i])-2] + ' ' + words_list[i][-2::1]
        print(words_list)
    
while 1:
    input('\tНажмите Enter')
    start(5)
    