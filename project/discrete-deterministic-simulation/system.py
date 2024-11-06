import random


class RatingSystem:
    def __init__(self, base_rating: int = 100):
        self.base_rating = base_rating
        self.delta = 50

    def game_logic(self, player_rating: int, opponent_rating: int) -> str:
        if abs(player_rating - opponent_rating) < self.delta // 5:
            return "tie"
        elif player_rating - opponent_rating < 0:
            return "lose"
        else:
            return "win"

    def rating_update(self, game_result: str):
        if game_result == "lose":
            self.base_rating -= self.delta // 4
        elif game_result == "win":
            self.base_rating += self.delta // 4

    def iteration(self, trace: bool = True):
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
        for i in range(matches):
            if trace:
                print("iteration number", i+1)
                print("---------------------------")
            self.iteration(trace)
            if trace:
                print("---------------------------")

    def current_rating(self) -> int:
        return self.base_rating
