# any stack
# db optional
# CRUD->expense tracker
# 1. amount
# 2. date
# 3. cat. and sub_cat.
# 4. description
#
# get-> all expenses in a time interval (month, year)->tans and total
# get-> cat or sub cat
import datetime

def get_total(expense_list):
    total = 0
    for expense in expense_list.cost:
        total += expense.cost
        return total

