# class Dog:
#     def __init__(self, dog_name, colour):  # initialise to make sure the class is not changed in the future
#         self.animal_type = "canine"  # class variable
#         self.legs = 4
#         self.name = dog_name
#         self.colour = colour
#
#     def bark(self):  # method
#         return f"Woof! I am a {self.animal_type}"
#
#
# fido = Dog("Fido", "Black")  # instantiation = creating an INSTANCE of the class
# print(fido.animal_type)
# print(fido.bark())


# class Spartans:
#     def __init__(self, employee_id, first_name, last_name):
#         self.employee_id = employee_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.stream = "Data Engineering"
#         self.placement = "Home Office"
#
#
# james = Spartans("001", "James", "Shuffley")


class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.current_speed = 0

    def accelerate(self, speed_add):
        if self.current_speed + speed_add > self.top_speed:
            self.current_speed = self.top_speed
        else:
            self.current_speed += speed_add

    def brake(self, speed_subtract):
        if self.current_speed - speed_subtract < 0:
            self.current_speed = 0
        else:
            self.current_speed -= speed_subtract


davids_car = Car("Hyundai", "i20", 150)

davids_car.accelerate(60)
davids_car.brake(20)

print(davids_car.current_speed)

