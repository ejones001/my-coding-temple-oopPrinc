class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_allocated_budget):
        if new_allocated_budget >= 0:
            self.__allocated_budget = new_allocated_budget
        else:
            print("Error: Budget should be a positive number.")


category = BudgetCategory("Food", 500)
print(category.get_category_name())  # Output: Food
print(category.get_allocated_budget())  # Output: 500

category.set_category_name("Entertainment")
category.set_allocated_budget(700)

print(category.get_category_name())  # Output: Entertainment
print(category.get_allocated_budget())  # Output: 700

category.set_allocated_budget(-100)  # Output: Error: Budget should be a positive number.
print(category.get_allocated_budget())  # Output: 700 (unchanged)
