from figures import Figure, Figures


class InvalidField(Exception):
    pass


class InvalidFigure(Exception):
    pass


class Board:
    def __init__(self, figure_name: str, field: str):
        self.field = self._validate_field(field)
        self.figure = self._validate_figure(figure_name, field)

    def list_available_moves(self) -> list[str]:
        return self.figure.list_available_moves()

    def validate_move(self, dest: str) -> bool:
        dest = self._validate_field(dest)
        return self.figure.validate_move(dest)

    def _validate_field(self, field: str) -> str:
        if len(field) != 2:
            raise InvalidField()
        if field[0] not in "ABCDEFGH":
            raise InvalidField()
        if field[1] not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            raise InvalidField()
        return field.upper()

    def _validate_figure(self, figure_name: str, field: str) -> Figure:
        try:
            return Figures.get_figure(figure_name, field)
        except KeyError:
            raise InvalidFigure()
