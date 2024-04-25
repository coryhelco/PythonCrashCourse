#!/usr/bin/env python3.11

class Restaurant:
    """ A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.num_served = number_served

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"The name of the restaurant is {self.name}.")
        print(f"The restaurant serves {self.type} cuisine.")

    def open_restaurant(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now open!")

    def set_number_served(self, number_served):
        """Set the number of customers served."""
        self.num_served = number_served
    
    def increment_number_served(self, customers_served):
        """Increment the number of customers served."""
        self.num_served += customers_served

class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self):
        """Display the flavors available."""
        print("The following flavors are available:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def pick_flavor(self, flavor):
        """Pick a flavor."""
        self.flavor = flavor
        print(f"You have picked {self.flavor}.")


restaurant = Restaurant("Helco's Tavern", "American")
restaurant.describe_restaurant()
restaurant.open_restaurant()

ice_cream_stand = IceCreamStand("Helco's Ice Cream Stand", "Ice Cream", ["strawberry", "vanilla", "chocolate"])
ice_cream_stand.display_flavors()
ice_cream_stand.pick_flavor("strawberry")

print(f"\n{restaurant.name} is a {restaurant.type} restaurant.")
print(f"{restaurant.name} has served {restaurant.num_served} customers.")

restaurant.set_number_served(12)
#restaurant.num_served = 55
print(f"{restaurant.name} has served {restaurant.num_served} customers.")

restaurant.increment_number_served(10)
print(f"{restaurant.name} has served {restaurant.num_served} customers.")

