
class Ingredient():
    def __init__(self, name, kcal):
        self.id = None
        self.name = name
        self.kcal = kcal

    def to_dict(self):
        return { 'name' : self.name, 'kcal' : self.kcal }