o = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"


def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    new_order = ""
    for i in menu:
        count = order.count(i.lower())
        while count > 0:
            new_order = new_order + " " + i
            count -= 1
    return new_order[1:]


print(get_order(o))
