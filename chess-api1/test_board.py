import pytest

from board import Board, InvalidField, InvalidFigure


def test_board_queen():
    board = Board("queen", "A1")
    available_moves = board.list_available_moves()
    assert "A2" in available_moves


def test_board_king():
    board = Board("king", "A1")
    available_moves = board.list_available_moves()
    assert "A2" in available_moves


def test_board_rook():
    board = Board("rook", "A1")
    available_moves = board.list_available_moves()
    assert "A2" in available_moves


def test_board_knight():
    board = Board("knight", "A1")
    available_moves = board.list_available_moves()
    assert "B3" in available_moves


def test_board_bishop():
    board = Board("bishop", "A1")
    available_moves = board.list_available_moves()
    assert "B2" in available_moves


def test_board_pawn():
    board = Board("pawn", "A2")
    available_moves = board.list_available_moves()
    assert "A3" in available_moves


def test_board_to_short_fields():
    with pytest.raises(InvalidField):
        Board("king", "A")


def test_board_to_long_fields():
    with pytest.raises(InvalidField):
        Board("king", "A111")


def test_board_invalid_first_field_letter():
    with pytest.raises(InvalidField):
        Board("king", "X1")


def test_board_invalid_secound_field_letter():
    with pytest.raises(InvalidField):
        Board("king", "A0")


def test_board_invalid_figure():
    with pytest.raises(InvalidFigure):
        Board("kinggg", "A1")


def test_board_invalid_destination_field_letter():
    with pytest.raises(InvalidField):
        board = Board("queen", "A1")
        board.validate_move("B9")


def test_board_validate_move_queen():
    board = Board("queen", "A1")
    assert board.validate_move("A2")


def test_board_invalidate_move_quenn():
    board = Board("queen", "A1")
    assert not board.validate_move("B8")


def test_board_validate_move_king():
    board = Board("king", "A1")
    assert board.validate_move("A2")


def test_board_invalidate_move_king():
    board = Board("king", "A1")
    assert not board.validate_move("B8")


def test_board_validate_move_rook():
    board = Board("rook", "B2")
    assert board.validate_move("C2")


def test_board_invalidate_move_rook():
    board = Board("rook", "B2")
    assert not board.validate_move("C3")


def test_board_validate_move_bishop():
    board = Board("bishop", "B2")
    assert board.validate_move("C3")


def test_board_invalidate_move_bishop():
    board = Board("bishop", "B2")
    assert not board.validate_move("C2")


def test_board_validate_move_knight():
    board = Board("knight", "B2")
    assert board.validate_move("C4")


def test_board_invalidate_move_knight():
    board = Board("knight", "B2")
    assert not board.validate_move("C2")


def test_board_validate_move_pawn():
    board = Board("pawn", "B2")
    assert board.validate_move("B3")


def test_board_invalidate_move_pawn():
    board = Board("knight", "B2")
    assert not board.validate_move("C2")
