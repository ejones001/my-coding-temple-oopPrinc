class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

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

    def add_expense(self, expense_amount):
        if expense_amount >= 0:
            if self.__expenses + expense_amount <= self.__allocated_budget:
                self.__expenses += expense_amount
                print("Expense added successfully.")
            else:
                print("Error: Expense exceeds allocated budget.")
        else:
            print("Error: Expense amount should be a positive number.")

    def get_remaining_budget(self):
        return self.__allocated_budget - self.__expenses

    def display_category_summary(self):
        print("Category Name:", self.__category_name)
        print("Allocated Budget:", self.__allocated_budget)
        print("Remaining Budget:", self.get_remaining_budget())


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
