from extras import MENU, resources

class machine():
    
    def cash(self, product):
        print("Please insert a coin")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        
        user_amount = (quarters * 0.25) + (dimes * 0.1) + ( nickles * 0.05) + (pennies * 0.01)
        value = MENU[product]
        if user_amount < value["cost"]:
            return False
        else:
            resources["money"] += value["cost"]
            change = user_amount - value["cost"]
            return change
            
            
    def resources_maths(self, product):
        if product == "espresso":
            if resources["water"] >= 50:
                if resources["coffee"] >= 18:
                    return True
                else:
                    return False
            else:
                return False
        #for latte    
        elif  product == "latte":
            if resources["water"] >= 200:
                if resources["coffee"] >= 24:
                    if resources["milk"] >= 150:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
            
        elif product == "cappuccino":
            if resources["water"] >= 250:
                if resources["coffee"] >= 24:
                    if resources["milk"] >= 100:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False  
            
                  
    def serve(self, product):
        print(f"Here is your {product} ☕, Enjoy!!!")
        value = MENU[product]
        key = value["ingredients"]
        
        if "water" in key:
            resources["water"] -= key["water"]
        if "milk" in key:
            resources["milk"] -= key["milk"]
        if "coffee" in key:
            resources["coffee"] -= key["coffee"]
            
        
    def prompt(self, user_input):
        if user_input == "off":
            return False
        
        elif user_input == "resources":
                
            water = resources["water"]
            milk = resources["milk"]
            coffee = resources["coffee"]
            cash = resources["money"]
            
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${cash}")
                
                
                
                
        else:
            if self.resources_maths(user_input) == True:
                cash = self.cash(user_input)
                if cash == False:
                    print("Your money is not enough")
                else:
                    print(f"Have your change of ${cash}")
                    self.serve(user_input)
                    
                    
                    
            else:
                print(f"There are not enough ingredients to make your {user_input}")
                
            
        
        
def main():
    on = True
    while on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        engine = machine()
        if engine.prompt(user_input) ==  False:
            on = False
            
if __name__ == '__main__':
    main()