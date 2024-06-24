# class Animal:
#     def make_sound(self, s):
#         print(s)
#         class Horse(Animal):
#           pass
#
#         pony = Horse()
#         print(pony.make_sound('igogo'))

# class Parents:
#     def parametres(self, hair, eyes):
#         print(hair, eyes)
#
#     class Son:(Parents):
#     pass
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor

# class Car:
#     @classmethod
#     def stop(cls):
#         print('Машина остановилась')

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
#
# rectangle = Rectangle(4, 5)
# print(rectangle.area)
#
# rectangle.width = 6
# print(rectangle.area)

# class Worker:
#     def __init__(self, name):
#         self.name = name
#
# class HRworker(Worker):
#     def __init__(self, name, job):
#         super().__init__(name)
#         self.job = job
#         @property
#         def user(self):
#             return self.name + self.job
#
class Player:
    def __init__(self, run):
        self.run = run

        class a(Player):
            def __init__(self, run, makingGoals):
                super().__init__(run)
                self.makingGoals = makingGoals

                class b(Player):
                    def __init__(self, run, defend):
                        super().__init__(run)
                        self.defend = defend

                        class c(Player):
                            def __init__(self, run, holding):
                                super().__init__(run)
                                self.holding = holding

                                class d(Player):
                                    def __init__(self, run, hands):
                                        super().__init__(run)
                                        self.hands = hands
