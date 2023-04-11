import sys

from ball import Ball

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


# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)



class Sequence:
    def __init__(self, screen, path):
        self.screen = screen
        self.balls_arr = []
        self.path = path
        self.generate()

    def generate(self):
        self.push(Ball(screen=self.screen, x=int(self.path[0][0]),
                       y=int(self.path[0][1])))

    def push(self, ball: Ball) -> None:
        self.balls_arr.append(ball)

    def re_count(self, pos: int) -> None:
        for i in range(pos + 1):
            self.balls_arr[i].counter += 42

    def insert(self, ball: Ball, pos: int) -> None:
        ball.counter = self.balls_arr[pos].counter
        self.balls_arr.insert(pos, ball)
        l, r = find_bounds(self.balls_arr, pos)
        if r - l + 1 >= 3:
            self.knock(l, r)
        else:
            self.re_count(pos)

    def knock(self, left: int, right: int):
        del self.balls_arr[left:right + 1]
        for i in range(left):
            self.balls_arr[i].counter = self.balls_arr[left].counter + 41 * (i)

    def move(self):
        for ball in self.balls_arr:
            try:
                ball.move_ball(int(self.path[ball.counter][0]),
                               int(self.path[ball.counter][1]))
                ball.counter += 1
            except IndexError:
                sys.exit()

    def draw(self):
        for ball in self.balls_arr:
            ball.draw_ball()
