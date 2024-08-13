# from lib.dev import Dev
# from lib.company import Company

class Freebie:
    all = []

    def __init__(self, dev, company, item_name, value):
        self.dev = dev
        self.company = company
        self.item_name = item_name
        self.value = value
        Freebie.all.append(self)

    @property
    def dev(self):
        return self._dev

    @dev.setter
    def dev(self, new_dev):
        from lib.dev import Dev  # Import here
        if isinstance(new_dev, Dev):
            self._dev = new_dev

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, new_company):
        from lib.company import Company  # Import here
        if isinstance(new_company, Company):
            self._company = new_company

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, new_item_name):
        if isinstance(new_item_name, str):
            self._item_name = new_item_name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, int):
            self._value = new_value

    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'

    def __repr__(self):
        return f'<Dev dev={self.dev} Company company={self.company} Item item={self.item_name} Value value={self.value} />'    
