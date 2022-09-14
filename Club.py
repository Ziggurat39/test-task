import random
import time

names = {1: "Никита", 2: "Валера", 3: "Женя", 4: "Аркаша"}
genders = {1: "мальчик", 2: "девочка"}
practice = {1: "любит", 2: "может", 3: "умеет"}
genres = {1: "РНБ", 2: "Электрохаус", 3: "Поп-музыка"}
current_track = ""
my_list = []
arr = []


def set_random_track():
    global current_track
    current_track = genres[random.randint(1, 3)]


def add_my_track():
    global my_list
    choice = int(input("Введите жанр трека, где:\n1 - РНБ\n2 - Электрохаус\n3 - Поп-музыка\nВыбор: "))
    if choice in genres:
        my_list.append(genres[choice])
    else:
        print("Некорректный ввод")


def set_my_track():
    global current_track
    if len(my_list) == 0:
        print("Список треков пуст")
    else:
        current_track = my_list[0]
        my_list.pop(0)


def see_my_list():
    global my_list
    print("Треклист содержит:", my_list)


def add_dancer(n):
    for i in range(n):
        points = []
        for j in range(3):
            points.append(random.randint(0, 1))
        arr.append(Dancer(random.randint(1, 4), random.randint(1, 2), random.randint(1, 3), points))
        points.clear()
        time.sleep(0.1)
        print("Добавлен новый посетитель...")
    return arr


def remove_dancer(array, index):
    array.pop(index)


def get_stats():
    print("Запрошены досье гостей...")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    for i in range(len(arr)):
        print(f'{i}, {arr[i].name}, {arr[i].sex}, {arr[i].skill}, {arr[i].points}')
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


def club_run():
    print("Добро пожаловать в клуб 'PYTHON 3'")
    set_random_track()
    while True:
        print("-------------------------------------------------------------")
        print(f'Сейчас в клубе играет {current_track}, тем временем:')
        for i in range(len(arr)):
            print(arr[i])
        print("--------МЕНЮ--------")
        c = int(input(
            "1 - случайная песня, 2 - следующая песня по моему списку, 3 - добавить песню в список, 4 - просмотр списка, 5 - удалить гостя, 6 - добавить гостя, 7 - получить статы, 10 - выход\nВыбор: "))
        if c == 1:
            print("Продолжаем...")
            set_random_track()
        elif c == 2:
            set_my_track()
        elif c == 3:
            add_my_track()
        elif c == 4:
            see_my_list()
        elif c == 5:
            remove_dancer(arr, int(input("Какой индекс удалить? - ")))
        elif c == 6:
            add_dancer(1)
        elif c == 7:
            get_stats()
        elif c == 10:
            print("Клуб закрывается...")
            break


class Dancer:
    def __init__(self, name_num, sex_num, prc_num, array):
        self.name = names[name_num]
        self.sex = genders[sex_num]
        self.skill = practice[prc_num]
        self.points = []  # 0 - хип-хоп, 1 - электроданс, 2 - поп
        self.points.extend(array)

    def time_to_dance(self):
        global current_track
        if current_track == "РНБ" and self.points[0] == 1:
            return f'покачиванет телом вперед и назад, ноги в полу-присяде, руки согнуты в локтях, головой вперед-назад'
        elif current_track == "Электрохаус" and self.points[1] == 1:
            return f'покачивает туловищем вперед-назад, почти нет движения головой, круговые движения - вращения руками, ноги двигаются в ритме'
        elif current_track == "Поп-музыка" and self.points[2] == 1:
            return f'делает плавные движения туловищем, руками, ногами и головой'
        else:
            return f'пьет водку в баре'

    def __str__(self):
        return f'Посетитель {self.name} ({self.sex}), {self.skill} танцевать, и поскольку сейчас играет {current_track}, то {self.name} {self.time_to_dance()}'
