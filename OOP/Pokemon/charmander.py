from pokemon import Pokemon
from move import Move


class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
            name="Charmander",
            poke_type="Fire",
            hp=7,
            attack=9,
            defence=5
        )
        self.moves.append(Move(
            "Scratch",
            "Normal",
            10
        ))
        self.moves.append(Move(
            "Growl",
            "Normal",
            0
        ))


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(
            name="Pikachu",
            poke_type="Electric",
            hp=6,
            attack=6,
            defence=6
        )
        self.moves.append(Move(
            "Thundershock",
            "Electic",
            20
        ))
        self.moves.append(Move(
            "Tail Whip",
            "Normal",
            0
        ))


char = Charmander()

# print(char.type)
# print(char.hp)
# for move in char.moves:
#     print(f"{move.name} ({move.type}): {move.power}")

result = char.use_move("Scratch")

print(result)

pika = Pikachu()

result = pika.use_move("Thundershock")

print(result)
