from .freebie import Freebie

class Company:
    all = []

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year
        Company.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name

    @property
    def founding_year(self):
        return self._founding_year

    @founding_year.setter
    def founding_year(self, year):
        if isinstance(year, int):
            self._founding_year = year  

    def freebies(self):
        return [freebie for freebie in Freebie.all if freebie.company == self]

    def devs(self):
        return list(set(freebie.dev for freebie in self.freebies()))     

    @classmethod
    def oldest_company(cls):
        return min(cls.all, key=lambda company: company.founding_year)
    
    def give_freebie(self, dev, item_name, value):
        Freebie(dev, self, item_name, value)    

    def __repr__(self):
        return f'<Company name={self.name} founding year={self.founding_year} />'