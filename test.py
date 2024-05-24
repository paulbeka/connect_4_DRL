from game import Game

def test_victory_conditions():
    # Horizontal win for player 1
    game1 = Game(displayScreen=False)
    game1.board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0]
    ]
    assert game1.check_victory(game1.board) == 1

    # Vertical win for player 2
    game2 = Game(displayScreen=False)
    game2.board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0]
    ]
    assert game2.check_victory(game2.board) == 2

    # Diagonal win for player 1
    game3 = Game(displayScreen=False)
    game3.board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0],
        [1, 2, 1, 0, 0, 0],
        [2, 2, 2, 1, 0, 0],
        [2, 1, 2, 2, 1, 0]
    ]
    assert game3.check_victory(game3.board) == 1

    print("All tests passed!")
