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
from decimal import *

MAX_ITEM_AMOUNT = 1e6
TOTAL_MAX_PAYABLE = 1e5


Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    payments = Decimal(0)
    expenses = Decimal(0)

    for item in order.items:
        if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
            if item.type == 'payment':
                payments += Decimal(str(item.amount))
            elif item.type == 'product' and type(item.quantity) is int:
                expenses += Decimal(str(item.amount)) * item.quantity
            else:
                return "Invalid item type: %s" % item.type

    if abs(payments) > TOTAL_MAX_PAYABLE or expenses > TOTAL_MAX_PAYABLE:
        return 'Total amount payable for an order exceeded'

    net = payments - expenses
    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id