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


category = BudgetCategory("Food", 500)
print(category.get_remaining_budget())  # Output: 500

category.add_expense(100)
print(category.get_remaining_budget())  # Output: 400

category.add_expense(450)  # Output: Error: Expense exceeds allocated budget.
print(category.get_remaining_budget())  # Output: 400 (unchanged)

category.add_expense(-50)  # Output: Error: Expense amount should be a positive number.
print(category.get_remaining_budget())  # Output: 400 (unchanged)
