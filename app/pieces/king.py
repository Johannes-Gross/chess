from app.piece import Piece

class King(Piece):

    def __init__(self, color: str, tile_width: float, tile_heigth: float) -> None:
        self.img_path = f"/imgs/{color}_king.png"
        super().__init__(color, tile_width, tile_heigth, self.img_path)