class SimpleLCG:
    def __init__(self, seed):
        self.m = 2**31 - 1  # Модуль
        self.a = 1103515245  # Коэффициент
        self.c = 12345  # Приращение
        self.state = seed  # Начальное значение (семя)

    def next(self):
        # Генерация следующего числа
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random_uniform_int(self, a, b):
        # Генерация случайного целого числа в диапазоне [a, b]
        random_number = self.next() % (b - a + 1) + a
        return random_number
