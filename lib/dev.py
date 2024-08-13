from .freebie import Freebie

class Dev:
    all = []

    def __init__(self, name):
        self.name = name
        Dev.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name

    def freebies(self):
        return [freebie for freebie in Freebie.all if freebie.dev == self]

    def companies(self):
        return list(set(freebie.company for freebie in self.freebies()))

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies())

    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev

    def num_times_played(self, game):
        return sum(1 for freebie in self.freebies() if freebie.company == game)
    
    def __repr__(self):
        return f'<Dev name={self.name} />'
