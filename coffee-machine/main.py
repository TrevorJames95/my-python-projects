import coffee_machine

if __name__ == '__main__':
    action = "start"
    coffee_machine = coffee_machine.CoffeeMachine()
    while action != "exit":
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            coffee_machine.coffe_menu()
        elif action == "fill":
            coffee_machine.refill_supplies()
        elif action == "take":
            coffee_machine.take_money()
        elif action == "remaining":
            coffee_machine.current_supplies()

