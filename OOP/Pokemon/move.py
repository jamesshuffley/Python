class Move:
    def __init__(self, name, move_type, power):
        self.name = name
        self.move_type = move_type
        self.power = power


if __name__ == "__main__":
    flamethrower = Move(
        name="Flamethrower",
        move_type="Fire",
        power=100
    )
    print(flamethrower)
    print(type(flamethrower))
    print(flamethrower.power)
