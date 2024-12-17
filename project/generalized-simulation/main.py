from system import RatingSystem


def main():
    game = RatingSystem()
    players = [["test1", 1500, 50], ["test2", 1080, 20], ["test3", 2000, 30]]
    new = game.matchmaking(players, False)
    game.current_rating(new)


if __name__ == '__main__':
    main()
