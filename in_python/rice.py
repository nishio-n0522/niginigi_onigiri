class RiceType:
    Koshihikari: str = "so_tasty"

class Rice:
    def __init__(self, rice_type: RiceType) -> None:
        self.rice_type = rice_type
        self.is_washed = False

    def wash_rice(self) -> None:
        self.is_washed = True
