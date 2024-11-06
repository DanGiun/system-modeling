from system import RatingSystem


def main():
    game = RatingSystem(1000)
    game.current_rating()
    game.game(20, False)
    game.current_rating()


if __name__ == '__main__':
    main()
