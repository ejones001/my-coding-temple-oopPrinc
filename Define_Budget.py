class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget


category = BudgetCategory("Food", 500)
print(category.__category_name)  # This will result in an AttributeError
