from app.piece import Piece

class Rook(Piece):

    def __init__(self, color: str, tile_width: float, tile_heigth: float) -> None:
        self.img_path = f"/imgs/{color}_rook.png"
        super().__init__(color, tile_width, tile_heigth, self.img_path)

    # def get_valid_moves(self, board, pos):
    #     moves = []
    #     x, y = pos
    #     for i in range(x + 1, 8):
    #         if board[i][y] == 0:
    #             moves.append((i, y))
    #         else:
    #             if board[i][y].color != self.color:
    #                 moves.append((i, y))
    #             break
    #     for i in range(x - 1, -1, -1):
    #         if board[i][y] == 0:
    #             moves.append((i, y))
    #         else:
    #             if board[i][y].color != self.color:
    #                 moves.append((i, y))
    #             break
    #     for i in range(y + 1, 8):
    #         if board[x][i] == 0:
    #             moves.append((x, i))
    #         else:
    #             if board[x][i].color != self.color:
    #                 moves.append((x, i))
    #             break
    #     for i in range(y - 1, -1, -1):
    #         if board[x][i] == 0:
    #             moves.append((x, i))
    #         else:
    #             if board[x][i].color != self.color:
    #                 moves.append((x, i))
    #             break
    #     return moves