class RiceType:
    Koshihikari: str = "so_tasty"
    Akitakomachi: str = "nice"
    Yumepirika: str = "cute"

class OnigiriContents:
    Umeboshi: str = "very_sour"

class RiceBall:
    def __init__(self, rice_type: RiceType, contents: OnigiriContents = None) -> None:
        self.rice_type = rice_type
        self.contents = contents

class Rice:
    def __init__(self, rice_type: RiceType) -> None:
        self.rice_type = rice_type
        self.is_washed = False
        self.is_boiled = False

    def wash_rice(self) -> None:
        self.is_washed = True

    def boil_rice(self) -> None:
        self.is_boiled = True

    def press_rice_into_a_ball(self) -> RiceBall:
        return RiceBall(self.rice_type)