expression = "4 ** 9"


def expression_out(exp):
    operators = {'+': 'Plus ',
                 '-': 'Minus ',
                 '*': 'Times ',
                 '/': 'Divided By ',
                 '**': 'To The Power Of ',
                 '=': 'Equals ',
                 '!=': 'Does Not Equal '}
    nums = {'1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
            '10': 'Ten'}
    lst = exp.split(" ")
    if lst[1] in operators:
        return nums[lst[0]] + " " + operators[lst[1]] + nums[lst[2]]
    else:
        return "That's not an operator!"


print(expression_out(expression))
