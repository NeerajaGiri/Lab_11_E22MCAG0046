#NeerajaGiri
#46
class Pizza:
    def __init__(self, name, base_price):
        self.name = name
        self.sauce = None
        self.cheese = None
        self.dough = None
        self.base_price = base_price
        
    def add_sauce(self, sauce):
        self.sauce = sauce
        
    def add_cheese(self, cheese):
        self.cheese = cheese
        
    def add_dough(self, dough):
        self.dough = dough
        
    def calculate_cost(self):
        cost = self.base_price
        if self.sauce:
            cost += self.sauce.cost
        if self.cheese:
            cost += self.cheese.cost
        if self.dough:
            cost += self.dough.cost
        return cost
    
    def display_details(self):
        print(f"{self.name} pizza with {self.sauce}, {self.cheese}, {self.dough}. Total cost: {self.calculate_cost()}")
