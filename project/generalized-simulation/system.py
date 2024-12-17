import random
from lcg import SimpleLCG


class RatingSystem:
    def __init__(self, delta: int = 50):
        self.delta = delta

    def game_logic(self, player_rating: int, opponent_rating: int, trace: bool = True) -> str:
        """
        Функция отвечает за определение победы и поражения в зависимости от рейтинга игроков
        :param player_rating: значение рейтинга отслеживаемого в модели игрока
        :param opponent_rating: значение рейтинга сгенерированного оппонента
        :param trace: переменная отвечает за включение/открючение вывода данных
        :return: возвращается значение результата матча
        """
        if abs(player_rating - opponent_rating) < self.delta // 5:
            if trace:
                print("players have same rating")
            lcg = SimpleLCG(random.random())
            number = int(lcg.random_uniform_int(1, 10))
            if 1 <= number < 3:
                return "lose"
            elif 3 <= number < 9:
                return "tie"
            elif 9 <= number <= 10:
                return "win"
        elif player_rating - opponent_rating < 0:
            if trace:
                print("opponent has higher rating")
            lcg = SimpleLCG(random.random())
            number = int(lcg.random_uniform_int(1, 10))
            if 1 <= number < 7:
                return "lose"
            elif 7 <= number < 9:
                return "tie"
            elif 9 <= number <= 10:
                return "win"
        else:
            if trace:
                print("player has higher rating")
            lcg = SimpleLCG(random.random())
            number = int(lcg.random_uniform_int(1, 10))
            if 1 <= number < 3:
                return "lose"
            elif 3 <= number < 5:
                return "tie"
            elif 5 <= number <= 10:
                return "win"

    def rating_update(self, rating, game_result: str) -> int:
        """
        Функция обновляет рейтинг игрока в зависимости от результата матча
        :param rating: рейтинг игрока
        :param game_result: параметр - результат матча
        :return: Функция ничего не возвращает
        """
        if game_result == "lose":
            rating -= self.delta // 4
            return rating
        elif game_result == "win":
            rating += self.delta // 4
            return rating
        else:
            return rating

    def iteration(self, rating, trace: bool = True) -> int:
        """
        Функция симулирует одну итерацию, включающую в себя генерацию оппонента, симуляцию игры и изменение рейтинга
        :param rating: рейтинг игрока
        :param trace: переменная отвечает за включение/открючение вывода данных о рейтинге до игры и после
        :return: Функция ничего не возвращает
        """
        if trace:
            print("rating before game:", rating)
        low_lim = rating - self.delta if rating - self.delta >= 0 else 0
        high_lim = rating + self.delta
        new_opponent = random.randint(low_lim, high_lim)
        game_result = self.game_logic(rating, new_opponent, trace)
        new_rating = self.rating_update(rating, game_result)
        if trace:
            print("rating after game: ", new_rating)
        return new_rating

    def game(self, rating, matches, trace: bool = True) -> int:
        """
        Функция выполняет итерацию заданное количество матчей
        :param rating: рейтинг игрока
        :param matches: количество матчей
        :param trace: переменная отвечает за включение/открючение вывода номера итерации,
        а также красиво оформленного рейтинга
        :return: Функция ничего не возвращает
        """
        curr_rating = rating
        for i in range(0, matches):
            if trace:
                print("iteration number", i + 1)
                print("---------------------------")
            curr_rating = self.iteration(curr_rating, trace)
            if trace:
                print("---------------------------")
        return curr_rating

    def matchmaking(self, players_data: list, trace: bool = True) -> list:
        """
        Функиця моделирует игровые сессии каждого из игроков
        :param players_data: данные игроков
        :param trace: переменная отвечает за включение/открючение вывода
        :return: возвращает обновленные данные игроков
        """
        new_rating = []
        for i in players_data:
            temp = i
            new_rate = self.game(rating=i[1], matches=i[2], trace=trace)
            new_rating.append([temp[0], new_rate])
        return new_rating

    @staticmethod
    def current_rating(players_data: list):
        """
        Функция позволяет выводить рейтинг
        """
        print(players_data)
