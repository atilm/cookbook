
class Food():
    def __init__(self, name, kcal):
        self.id = None
        self.name = name
        self.kcal = kcal

    @classmethod
    def fromJson(cls, js):
        name = js['name']
        kcal = js['kcal']
        obj = cls(name, kcal)
        obj.id = js['id']
        return obj

    def to_dict(self):
        return { 'id' : self.id, 'name' : self.name, 'kcal' : self.kcal }