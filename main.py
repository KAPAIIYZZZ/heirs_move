class Field:
    def __init__(self):
        self.massive = []
    def render(self, size, character_list):
        self.massive = [[0] * size for i in range(size)]
        for x in range(len(character_list)):
            self.massive[character_list[x].point.x][character_list[x].point.y] = character_list[x].mark
        for i in range(0, len(self.massive)):
            for j in range(0, len(self.massive[i])):
                print(self.massive[i][j], end=' ')
            print()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Character:
    def __init__(self, point, mark):
        self.point = point
        self.mark = mark
    def move(self, direction, size):
        if direction == 'w':
            if self.point.x - 1 < 0:
                print('Игрок выходит за пределы поля')
            else:
                self.point.x -= 1
        elif direction == 'd':
            if self.point.y + 1 >= size:
                print('Игрок выходит за пределы поля')
            else:
                self.point.y += 1
        elif direction == 's':
            if self.point.x + 1 >= size:
                print('Игрок выходит за пределы поля')
            else:
               self.point.x += 1
        elif direction == 'a':
            if self.point.y - 1 < 0:
                print('Игрок выходит за пределы поля')
            else:
               self.point.y -= 1
        else:
            print('Неверная команда')

class Character2(Character):
    def __init__(self, point, mark):
        super().__init__(point,mark)

def main():
    size = int(input('Введите размер поля: '))
    field = Field()
    print('Введите координаты 1 игрока')
    x1 = int(input('x: '))
    y1 = int(input('y: '))
    if x1 < 0 or y1 < 0 or x1 >=size or y1 >= size:
        print('Неверные координаты')
    print('Введите координаты 2 игрока')
    x2 = int(input('x: '))
    y2 = int(input('y: '))
    if x2 < 0 or y2 < 0 or x2 >=size or y2 >= size:
        print('Неверные координаты')
    else:
        character_list = []
        character1 = Character(Point(x1,y1), 1)
        character2 = Character2(Point(x2, y2), 2)
        character_list.append(character1)
        character_list.append(character2)
        field.render(size, character_list)
        while True:
            stop = input('Введите + если хотите передвинуть игроков, - если хотите завершить ')
            if stop == '+':
                gamer = input('Введите какого игрока вы хотите передвинуть 1 или 2 ')
                direction = input('Введите направление движения:\nw - вверх, d - вправо, s - вниз, a - влево\n')
                if gamer == '1':
                    character_list[0].move(direction, size)
                    field.render(size, character_list)
                elif gamer == '2':
                    character_list[1].move(direction, size)
                    field.render(size, character_list)
                else:
                    print('Неправильное значение')
            elif stop == '-':
                break
            else:
                print('Erorr')
main()