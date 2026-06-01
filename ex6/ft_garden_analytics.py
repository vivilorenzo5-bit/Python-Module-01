class Plant:

    class Stats:

        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    def __init__(
            self,
            name: str = "Unknown plant",
            height: float = 0.0,
            age: int = 0
            ) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._stats: Plant.Stats = Plant.Stats()

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

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    def grow(self, cm: float) -> None:
        self._height += cm
        self._stats.increment_grow()

    def age_one_day(self) -> None:
        self._age += 1
        self._stats.increment_age()

    def show(self) -> None:
        formatted_height = round(self._height, 1)
        print(f"{self._name}: {formatted_height}cm, {self._age} days old")
        self._stats.increment_show()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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

    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def increment_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self) -> None:
        formatted_height = round(self._height, 1)
        formatted_diameter = round(self._trunk_diameter, 1)
        print(f"Tree {self._name} now produces a shade of "
              f"{formatted_height}cm long and {formatted_diameter}cm wide.")
        if isinstance(self._stats, Tree.TreeStats):
            self._stats.increment_shade()

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
        self._nutritional_value: float = 0.0

    def grow(self, cm: float) -> None:
        super().grow(cm)
        self._nutritional_value += 0.5

    def age_one_day(self) -> None:
        super().age_one_day()
        self._nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {int(self._nutritional_value)}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_plant_stats(plant: Plant) -> None:
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(8.0)
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    for _ in range(20):
        sunflower.age_one_day()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_plant_stats(anonymous)


if __name__ == "__main__":
    main()
