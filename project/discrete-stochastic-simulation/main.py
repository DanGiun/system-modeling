from system import RatingSystem


def main():
    game = RatingSystem(1000)
    print(game.current_rating())
    game.game(100, trace=False)
    print(game.current_rating())


if __name__ == '__main__':
    main()
