from car import Car, ElectricCar

my_leaf = ElectricCar('Nissan', 'Leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_mustang = Car('Ford', 'Mustang', 2024)
print(my_mustang.get_descriptive_name())
