class RiceType:
    Koshihikari: str = "so_tasty"

class Rice:
    def __init__(self, rice_type: RiceType) -> None:
        self.rice_type = rice_type
        self.is_boiled = False

    def boil_rice(self):
        self.is_boiled = True