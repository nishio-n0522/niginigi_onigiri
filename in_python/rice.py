class RiceType:
    Koshihikari: str = "so_tasty"

class Rice:
    def __init__(self, rice_type: RiceType) -> None:
        self.rice_type = rice_type