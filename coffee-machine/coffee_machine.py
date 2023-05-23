# A simple coffee machine in python
# milk measured in milliliters
# water measured in milliliters
# coffee measured in grams
# Base amounts per cup of coffee

class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550

    def refill_supplies(self):
        self.water += int(input("Write how many ml of water you want to add: "))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans you want to add:"))
        self.cups += int(input("Write how many disposable cups you want to add:"))

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def current_supplies(self):
        print(f"""The coffee machine has:
    {self.water} ml of water
    {self.milk} ml of milk
    {self.coffee} g of coffee beans
    {self.cups} disposable cups
    ${self.money} of money
    """)

    def can_make_coffee(self, coffee_choice):
        if coffee_choice == "espresso":
            if self.water - 250 < 0:
                print("Sorry, not enough water")
            elif self.coffee - 16 < 0:
                print("Sorry not enough coffee")
            elif self.cups - 1 < 0:
                print("Sorry not enough cups")
            else:
                return True
        elif coffee_choice == "latte":
            if self.water - 350 < 0:
                print("Sorry, not enough water")
            elif self.coffee - 20 < 0:
                print("Sorry not enough coffee")
            elif self.milk - 75 < 0:
                print("Sorry not enough milk")
            elif self.cups - 1 < 0:
                print("Sorry not enough cups")
            else:
                return True
        elif coffee_choice == "cappuccino":
            if self.water - 200 < 0:
                print("Sorry, not enough water")
            elif self.coffee - 12 < 0:
                print("Sorry not enough coffee")
            elif self.milk - 100 < 0:
                print("Sorry not enough milk")
            elif self.cups - 1 < 0:
                print("Sorry not enough cups")
            else:
                return True

    def make_coffee(self, coffee_choice):
        # espresso consumes 250 water, 16 coffee, 1 cup and adds 4 dollars
        # latte consumes 350 water, 75 milk, 20 coffee and adds 7 dollars
        if coffee_choice == "espresso":
            if self.can_make_coffee(coffee_choice):
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
        elif coffee_choice == "latte":
            if self.can_make_coffee(coffee_choice):
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
        elif coffee_choice == "cappuccino":
            if self.can_make_coffee(coffee_choice):
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")

    def coffe_menu(self):
        coffe_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffe_choice == "1":
            self.make_coffee("espresso")
        elif coffe_choice == "2":
            self.make_coffee("latte")
        elif coffe_choice == "3":
            self.make_coffee("cappuccino")
        elif coffe_choice == "back":
            return


