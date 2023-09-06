import csv
from models.dish import Dish

from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.menu_data = source_path
        self.dishes = self.recipe()

    def read_menu_base_data(self, path):
        with open(path) as file:
            csv_file = csv.DictReader(file)
            dishes = set()
            for item in csv_file:
                name = item["dish"]
                price = float(item["price"])
                dish = Dish(name, price)
                dishes.add(dish)
            return dishes

    def recipe(self):
        dishes = self.read_menu_base_data(self.menu_data)
        for dish in dishes:
            with open(self.menu_data) as file:
                csv_file = csv.DictReader(file)
                for item in csv_file:
                    if item["dish"] == dish.name:
                        dish.add_ingredient_dependency(
                            Ingredient(item["ingredient"]),
                            int(item["recipe_amount"]),
                        )
        return dishes


# {Dish('lasanha presunto', R$25.90, {'queijo mussarela': 15, 'tomate': 10,
# 'farinha de trigo': 10, 'sal': 5, 'água': 10, 'berinjela': 15}),
# Dish('lasanha berinjela', R$27.00, {'queijo mussarela': 15, 'tomate': 10,
# 'farinha de trigo': 10, 'sal': 5, 'água': 10, 'presunto': 15})}
