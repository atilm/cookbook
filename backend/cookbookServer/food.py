
class Food:
    def __init__(self, name, kcal, seasonMonths):
        self.id = None
        self.name = name
        self.kcal = kcal
        self.seasonMonths = seasonMonths

    @classmethod
    def from_dict(cls, js):
        name = js['name']
        kcal = js['kcal']
        seasonMonths = []
        if 'seasonMonths' in js:
            seasonMonths = js['seasonMonths'] 

        obj = cls(name, kcal, seasonMonths)
        obj.id = js['id']
        return obj

    def to_dict(self):
        return { 
            'id' : self.id,
            'name' : self.name,
            'kcal' : self.kcal,
            'seasonMonths' : self.seasonMonths }