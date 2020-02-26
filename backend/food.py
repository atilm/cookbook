
class Food():
    def __init__(self, name, kcal):
        self.id = None
        self.name = name
        self.kcal = kcal

    def to_dict(self):
        return { 'id' : self.id, 'name' : self.name, 'kcal' : self.kcal }