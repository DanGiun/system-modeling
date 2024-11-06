import random


class RatingSystem:
    def __init__(self, base_rating: int = 100, delta: int = 50):
        self.base_rating = base_rating
        self.delta = delta

    def game_logic(self, player_rating: int, opponent_rating: int) -> str:
        """
        Функция отвечает за определение победы и поражения в зависимости от рейтинга игроков
        :param player_rating: значение рейтинга отслеживаемого в модели игрока
        :param opponent_rating: значение рейтинга сгенерированного оппонента
        :return: возвращается значение результата матча
        """
        if abs(player_rating - opponent_rating) < self.delta // 5:
            return "tie"
        elif player_rating - opponent_rating < 0:
            return "lose"
        else:
            return "win"

    def rating_update(self, game_result: str):
        """
        Функция обновляет рейтинг игрока в зависимости от результата матча
        :param game_result: параметр - результат матча
        :return: Функция ничего не возвращает
        """
        if game_result == "lose":
            self.base_rating -= self.delta // 4
        elif game_result == "win":
            self.base_rating += self.delta // 4

    def iteration(self, trace: bool = True):
        """
        Функция симулирует одну итерацию, включающую в себя генерацию оппонента, симуляцию игры и изменение рейтинга
        :param trace: переменная отвечает за включение/открючение вывода данных о рейтинге до игры и после
        :return: Функция ничего не возвращает
        """
        if trace:
            print("rating before game:", self.base_rating)
        low_lim = self.base_rating - self.delta if self.base_rating - self.delta >= 0 else 0
        high_lim = self.base_rating + self.delta
        new_opponent = random.randint(low_lim, high_lim)
        game_result = self.game_logic(self.base_rating, new_opponent)
        self.rating_update(game_result)
        if trace:
            print("rating after game: ", self.base_rating)

    def game(self, matches, trace: bool = True):
        """
        Функция выполняет итерацию заданное количество матчей
        :param matches: количество матчей
        :param trace: переменная отвечает за включение/открючение вывода номера итерации,
        а также красиво оформленного рейтинга
        :return: Функция ничего не возвращает
        """
        for i in range(matches):
            if trace:
                print("iteration number", i+1)
                print("---------------------------")
            self.iteration(trace)
            if trace:
                print("---------------------------")

    def current_rating(self) -> int:
        """
        Функция позволяет выводить рейтинг
        :return: Возвращает текущее значение рейтинга
        """
        return self.base_rating
