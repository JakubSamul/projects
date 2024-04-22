import abc

CHESSBOARD = {
    "A8": 57,
    "B8": 58,
    "C8": 59,
    "D8": 60,
    "E8": 61,
    "F8": 62,
    "G8": 63,
    "H8": 64,
    "A7": 49,
    "B7": 50,
    "C7": 51,
    "D7": 52,
    "E7": 53,
    "F7": 54,
    "G7": 55,
    "H7": 56,
    "A6": 41,
    "B6": 42,
    "C6": 43,
    "D6": 44,
    "E6": 45,
    "F6": 46,
    "G6": 47,
    "H6": 48,
    "A5": 33,
    "B5": 34,
    "C5": 35,
    "D5": 36,
    "E5": 37,
    "F5": 38,
    "G5": 39,
    "H5": 40,
    "A4": 25,
    "B4": 26,
    "C4": 27,
    "D4": 28,
    "E4": 29,
    "F4": 30,
    "G4": 31,
    "H4": 32,
    "A3": 17,
    "B3": 18,
    "C3": 19,
    "D3": 20,
    "E3": 21,
    "F3": 22,
    "G3": 23,
    "H3": 24,
    "A2": 9,
    "B2": 10,
    "C2": 11,
    "D2": 12,
    "E2": 13,
    "F2": 14,
    "G2": 15,
    "H2": 16,
    "A1": 1,
    "B1": 2,
    "C1": 3,
    "D1": 4,
    "E1": 5,
    "F1": 6,
    "G1": 7,
    "H1": 8,
}


class Figure(metaclass=abc.ABCMeta):
    def __init__(self, current_field: str):
        self.current_field = current_field

    @abc.abstractmethod
    def list_available_moves(self) -> list[str]:
        pass

    def validate_move(self, dest: str) -> bool:
        return dest in self.list_available_moves()


class Queen(Figure):
    def list_available_moves(self) -> list[str]:
        moves = []
        step = ord(self.current_field[0]) - 65
        for i in range(-(step * 9), ((7 - step) * 9 + 1), 9):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        for i in range(-((7 - step) * 7), (step * 7 + 1), 7):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        rest = CHESSBOARD[self.current_field] % 8
        # moves left and right
        for i in range(-(rest - 1), (9 - rest)):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        # moves up and down
        for i in range(-56, 64, 8):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        moves_avaliable = {}
        for value in moves:
            if value in CHESSBOARD.values():
                for key in CHESSBOARD:
                    if CHESSBOARD[key] == value:
                        moves_avaliable[key] = CHESSBOARD[key]
        return list(moves_avaliable.keys())


class King(Figure):
    def list_available_moves(self) -> list[str]:
        moves = [
            CHESSBOARD[self.current_field] + 1,
            CHESSBOARD[self.current_field] - 1,
            CHESSBOARD[self.current_field] + 7,
            CHESSBOARD[self.current_field] + 8,
            CHESSBOARD[self.current_field] + 9,
            CHESSBOARD[self.current_field] - 7,
            CHESSBOARD[self.current_field] - 8,
            CHESSBOARD[self.current_field] - 9,
        ]
        moves_avaliable = {}
        for value in moves:
            if value in CHESSBOARD.values():
                for key in CHESSBOARD:
                    if CHESSBOARD[key] == value:
                        moves_avaliable[key] = CHESSBOARD[key]
        return list(moves_avaliable.keys())


class Rook(Figure):
    name = "Rook"

    def list_available_moves(self) -> list[str]:
        moves = []
        rest = CHESSBOARD[self.current_field] % 8
        # moves left and right
        for i in range(-(rest - 1), (9 - rest)):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        # moves up and down
        for i in range(-56, 64, 8):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        moves_avaliable = {}
        for value in moves:
            if value in CHESSBOARD.values():
                for key in CHESSBOARD:
                    if CHESSBOARD[key] == value:
                        moves_avaliable[key] = CHESSBOARD[key]
        return list(moves_avaliable.keys())


class Bishop(Figure):
    def list_available_moves(self) -> list[str]:
        moves = []
        step = ord(self.current_field[0]) - 65
        for i in range(-(step * 9), ((7 - step) * 9 + 1), 9):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        for i in range(-((7 - step) * 7), (step * 7 + 1), 7):
            if i == 0:
                continue
            moves.append(CHESSBOARD[self.current_field] + i)
        moves_avaliable = {}
        for value in moves:
            if value in CHESSBOARD.values():
                for key in CHESSBOARD:
                    if CHESSBOARD[key] == value:
                        moves_avaliable[key] = CHESSBOARD[key]
        return list(moves_avaliable.keys())


class Knight(Figure):
    def list_available_moves(self) -> list[str]:
        moves = []
        numbers = [-17, -15, -10, -6, 6, 10, 15, 17]
        for i in numbers:
            add = CHESSBOARD[self.current_field] + i
            moves.append(add)
        moves1 = {}
        ordd = ord(self.current_field[0])
        orddd = [ordd - 2, ordd - 1, ordd + 1, ordd + 2]
        for value in moves:
            if value in CHESSBOARD.values():
                for key in CHESSBOARD:
                    if CHESSBOARD[key] == value:
                        moves1[key] = CHESSBOARD[key]
        moves_avaliable = {}
        for key in moves1:
            if ord(key[0]) in orddd:
                moves_avaliable[key] = moves1[key]
        return list(moves_avaliable.keys())


class Pawn(Figure):
    def list_available_moves(self) -> list[str]:
        moves = []
        if self.current_field[1] == "2":
            moves.append(CHESSBOARD[self.current_field] + 8)
            moves.append(CHESSBOARD[self.current_field] + 16)
        elif self.current_field[1] == "1":
            pass
        else:
            moves.append(CHESSBOARD[self.current_field] + 8)
        moves_avaliable = {}
        for value in moves:
            if value in CHESSBOARD.values():
                for key in CHESSBOARD:
                    if CHESSBOARD[key] == value:
                        moves_avaliable[key] = CHESSBOARD[key]
        return list(moves_avaliable.keys())


class Figures:
    @staticmethod
    def get_figure(name: str, field: str) -> Figure:
        figures = {
            "queen": Queen,
            "rook": Rook,
            "pawn": Pawn,
            "bishop": Bishop,
            "king": King,
            "knight": Knight,
        }
        return figures[name](field)
