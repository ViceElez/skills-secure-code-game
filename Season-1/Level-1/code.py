'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

MAX_CUMULATIVE_PRICE = 1e6
Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    balance=Decimal('0.00')
    expense=Decimal('0.00')

    for item in order.items:
        if item.type == 'payment':
            balance += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is not int or item.quantity <= 0:
                return "Invalid item quantity: %s" % item.quantity
            expense += Decimal(str(item.amount)) * int(item.quantity)
        else:
            return "Invalid item type: %s" % item.type
    if expense > MAX_CUMULATIVE_PRICE or balance > MAX_CUMULATIVE_PRICE:
        return "Total amount payable for an order exceeded"

    if balance - expense != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, balance - expense)
    else:
        return "Order ID: %s - Full payment received!" % order.id