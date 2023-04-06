from ball import Ball
from random import randint

"""
    Ищет границы последоватедльности
    из одинаковых шаров возле индекса (target)
"""

def find_bounds(a: list, target: int) -> (int, int):  # TODO покрыть тестами
    left, right = target, target
    for i in range(target + 1, len(a)):
        if a[i].color == a[target].color:
            right += 1
        else:
            break
    for i in range(target - 1, 0, -1):
        if a[i].color == a[target].color:
            left -= 1
        else:
            break
    return left, right



class Sequence:
    arr = []

    def generate(self, screen):
        i = randint(0, 3)
        if i == 1:
            ball = Ball(screen, "r")
        elif i == 2:
            ball = Ball(screen, "g")
        elif i == 3:
            ball = Ball(screen, "b")
        else:
            ball = Ball(screen, "y")
        self.push(ball)


    def push(self, ball: Ball) -> None:
        self.arr.append(ball)

    def insert(self, ball: Ball, pos: int) -> None:
        self.arr.insert(pos, ball)
        l, r = find_bounds(self.arr, pos)
        if r - l + 1 >= 3:
            self.knock(l, r)

    def knock(self, left: int, right: int):
        del self.arr[left:right + 1]

    def move(self):
        for i in self.arr:
            i.rect.move_ip(0, 40)

    def draw(self):
        for i in self.arr:
            i.draw()