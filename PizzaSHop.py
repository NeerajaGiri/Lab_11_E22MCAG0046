#NeerajaGiri
#46
from geek_pizza import *
from chicago_pizza import *
from sicillian_pizza import *
from new_york_style_pizza import *
from thickcrust import *
from thincrust import *
from mozzarellacheese import *
from parmesancheese import *
from provolenecheese import *
from reggianocheese import *
from barbecue import *
from marinarasauce import *
from plumsauce import *
from pumpkin import *


class Main(Pizza):
    def _init_(self):
        self.total_cost = None
        self.pizza_details = None

    def main(self):
        c = 2
        while c:
            print("0. Exit")
            print("1. Select Pizza")
            print("2. Select Dough")
            print("3. Select Cheese")
            print("4. Select Sauce")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print("1. Greek Pizza")
                print("2. Chicago Pizza")
                print("3. New York Style Pizza")
                print("4. Sicilian Pizza")
                pizza = int(input("Enter Type of Pizza:"))
                if pizza == 1:
                    pizza_choice = ChicagoPizza()
                    p = pizza_choice.get_basePrice()
                    p1 = "Greek Pizza"
                    print("Greek Pizza: ", pizza_choice.get_basePrice())
                    c = 2
                if pizza == 2:
                    pizza_choice = ChicagoPizza()
                    p = pizza_choice.get_basePrice()
                    p1 = "Chicago Pizza"
                    print("Chicago Pizza: ", pizza_choice.get_basePrice())
                    c = 2
                if pizza == 3:
                    pizza_choice = NewYorkStylePizza()
                    p = pizza_choice.get_basePrice()
                    p1 = "New York Style Pizza"
                    print("New York Style Pizza: ",
                          pizza_choice.get_basePrice())
                    c = 2
                if pizza == 4:
                    pizza_choice = SicilianPizza()
                    p = pizza_choice.get_basePrice()
                    p1 = "Sicilian Pizza"
                    print("Sicilian Pizza: ", pizza_choice.get_basePrice())
                    c = 2
                elif c == 2:
                    print("1. ThickCrust Dough")
                    print("2. ThinCrust Dough")
                    dough = int(input("Enter Type of Dough:"))
                    if dough == 1:
                        dough_choice = ThinkCrustDough(100)
                        d = dough_choice.get_cost()
                        d1 = "Thick Crust Dough"
                        print("Thick Crust: ", dough_choice.get_cost())
                        c = 3
                    elif dough == 2:
                        dough_choice = ThinCrustDough(125)
                        d = dough_choice.get_cost()
                        d1 = "Thin Crust Dough"
                        print("Thin Crust: ", dough_choice.get_cost())
                        c = 3
                    elif c == 3:
                        print(c)
                        print("1. Mozzarella Cheese")
                        print("2. Parmesan Cheese")
                        print("3. Provolone Cheese")
                        print("4. Reggaino Cheese")
                        cheese = int(input("Enter Type of Cheese:"))
                        if cheese == 1:
                            cheese_choice = MozzarellaCheese(100)
                            ch = cheese_choice.get_cost()
                            print("Mozzarella Cheese: ",
                                  cheese_choice.get_cost())
                            ch1 = "Mozzarella Cheese"
                            c = 4
                        if cheese == 2:
                            cheese_choice = ParmesanCheese(150)
                            ch = cheese_choice.get_cost()
                            ch1 = "Parmesan Cheese"
                            print("Parmesan Cheese: ",
                                  cheese_choice.get_cost())
                            c = 4
                        if cheese == 3:
                            cheese_choice = ProvoloneCheese(200)
                            ch = cheese_choice.get_cost()
                            ch1 = "Provolone Cheese"
                            print("Provolone Cheese: ",
                                  cheese_choice.get_cost())
                            c = 4
                        if cheese == 4:
                            cheese_choice = ReggainoCheese(250)
                            ch = cheese_choice.get_cost()
                            ch1 = "Reggaino Cheese"
                            print("Reggaino Cheese: ",
                                  cheese_choice.get_cost())
                            c = 4
                        elif c == 4:
                            print("1. Barbecue Sauce")
                            print("2. Marinara Sauce")
                            print("3. PlumTomato Sauce")
                            print("4. Pumpkin Sauce")
                            sauce = int(input("Enter Type of Sauce:"))
                            if sauce == 1:
                                sauce_choice = BarbecueSauce(100)
                                sauce = sauce_choice.get_cost()
                                sauce1 = "Barbecue Sauce"
                                print("Barbecue Sauce: ",
                                      sauce_choice.get_cost())
                            if sauce == 2:
                                sauce_choice = MarinaraSauce(150)
                                sauce = sauce_choice.get_cost()
                                sauce1 = "Marinara Sauce"
                                print("Marinara Sauce: ",
                                      sauce_choice.get_cost())
                            if sauce == 3:
                                sauce_choice = PlumTomatoSauce(200)
                                sauce = sauce_choice.get_cost()
                                sauce1 = "PlumTomato Sauce"
                                print("PlumTomato Sauce: ",
                                      sauce_choice.get_cost())
                            if sauce == 4:
                                sauce_choice = PumpkinSauce(250)
                                sauce = sauce_choice.get_cost()
                                sauce1 = "Pumpkin Sauce"
                                print("Pumpkin Sauce: ",
                                      cheese_choice.get_cost())
                            total_cost = p+d+ch+sauce
                            self.total_cost = float(total_cost)
                            pizza_details = f"Pizza: {p1}, Dough: {d1}, Cheese: {ch1},Sauce: {sauce1}"
                            self.pizza_details = pizza_details
                            # return float(total_cost), pizza_details
            elif choice == 2 or 3 or 4:
                choice = 1
            elif choice == 0:
                print("Exiting")
                break
            elif choice > 4:
                print("Invalid Option")

    def calculateCost(self):
        return self.total_cost

    def displayDetails(self):
        return self.pizza_details


m = Main()
m.main()
print("Total Cost:", m.calculateCost())
print("Pizza Details:", m.displayDetails())