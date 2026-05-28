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


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25.0)
    print("Height updated: 25cm")

    rose.set_age(30)
    print("Age updated: 30 days")
    print()

    rose.set_height(-10.5)
    rose.set_age(-5)

    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
