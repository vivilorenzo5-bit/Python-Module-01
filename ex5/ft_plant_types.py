class Plant:
    def __init__(
            self,
            name: str = "Unknown plant",
            height: float = 0.0,
            age: int = 0
            ) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def grow(self, cm: float) -> None:
        self._height += cm

    def age_one_day(self) -> None:
        self._age += 1

    def show(self) -> None:
        formatted_height = round(self._height, 1)
        print(f"{self._name}: {formatted_height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str
            ) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._has_bloomed: bool = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        formatted_height = round(self._height, 1)
        formatted_diameter = round(self._trunk_diameter, 1)
        print(f"Tree {self._name} now produces a shade of "
              f"{formatted_height}cm long and {formatted_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        formatted_diameter = round(self._trunk_diameter, 1)
        print(f"Trunk diameter: {formatted_diameter}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str
            ) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def grow(self, cm: float) -> None:
        super().grow(cm)
        self._nutritional_value += 1

    def age_one_day(self) -> None:
        super().age_one_day()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}"
              f"Nutritional value: {self._nutritional_value}")
