class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.age: int = 0

    def grow(self, cm: float) -> None:
        self.height += cm

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        formatted_height = round(self.height, 1)
        print(f"{self.name}: {formatted_height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age = 30
    initial_height = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age_one_day()
        rose.show()

    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
