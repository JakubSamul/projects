#!flask/bin/python
from flask import Flask

from board import Board, InvalidField, InvalidFigure

app = Flask(__name__)


@app.route("/api/v1/<string:figure>/<string:field>/")
def list_available_moves(figure: str, field: str):
    try:
        board = Board(figure, field)
    except InvalidFigure:
        return {}, 404
    except InvalidField:
        return {
            "availableMoves": [],
            "error": "Field does not exist.",
            "figure": figure,
            "currentField": field,
        }, 409
    valid = board.list_available_moves()
    if valid:
        return {
            "availableMoves": valid,
            "error": None,
            "figure": figure,
            "currentField": field,
        }


@app.route("/api/v1/<string:figure>/<string:field>/<string:dest>/")
def validate_move(figure: str, field: str, dest: str):
    try:
        board = Board(figure, field)
    except InvalidField:
        return {}, 409
    except InvalidFigure:
        return {}, 404
    try:
        valid = board.validate_move(dest)
    except InvalidField:
        return {}, 409
    if valid:
        return {
            "move": "valid",
            "figure": figure,
            "error": None,
            "currentField": field,
            "destField": dest,
        }
    else:
        return {
            "move": "invalid",
            "figure": figure,
            "error": "Current move is not permitted.",
            "currentField": field,
            "destField": dest,
        }


if __name__ == "__main__":
    app.run(debug=True)
