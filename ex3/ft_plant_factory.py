class Plant:
    def __init__(
            self,
            name: str = "Unknown plant",
            height: float = 0.0,
            age: int = 0
            ) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def grow(self, cm: float) -> None:
        self.height += cm

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        formatted_height = round(self.height, 1)
        print(f"{self.name}: {formatted_height}cm, {self.age} days old")


def main() -> None:
    print("=== Plant Factory Showcase ===")

    rose = Plant("Rose", 25.0, 30)
    print("Created: ", end="")
    rose.show()

    oak = Plant("Oak", 200.0, 365)
    print("Created: ", end="")
    oak.show()

    cactus = Plant(height=5.0, age=90, name="Cactus")
    print("Created: ", end="")
    cactus.show()

    sunflower = Plant(age=45, name="Sunflower", height=80.0)
    print("Created: ", end="")
    sunflower.show()

    anonymous_plant = Plant()
    print("Created: ", end="")
    anonymous_plant.show()


if __name__ == "__main__":
    main()
