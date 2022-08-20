import numpy as np


def clean_expression(expression):
    return expression


def generate_expressions(expression, b):
    '''

    :param expression:
    :param b: a number
    :return:
    '''

    formulas = []

    if len(b) > 1:
        sub_formulas = generate_expressions(expression, [b[0]])
        for sub_formula in sub_formulas:
            formulas.append(generate_expressions(sub_formula, b[1:]))
    else:
        for operator in ['+', '-', '*', '/']:
            formula = '(' + str(expression) + ')' + operator + str(b[0])
            formulas.append(formula)

    return formulas


def get_permutation(l):
    if len(l) == 1:
        return l

    if len(l) == 2:
        return [l, [l[1], l[0]]]

    possible_permutations = []
    for a in l:
        sub_list = l.copy()
        sub_list.remove(a)
        possible_subpermutations = get_permutation(sub_list)
        possible_permutations += [[a] + sub for sub in possible_subpermutations]
    return possible_permutations


def get24(l: list):
    '''
    Get 24 using arithmetic operators in : (, ), +, -, x, /

    :param l: a list containing numbers from 1 to 9
    :return: a possible expression to get 24
    '''

    all_orders = get_permutation(l)
    formulas = []

    for order in all_orders:
        sub_list = order.copy()
        a = sub_list.pop(0)

        formulas.append(generate_expressions(a, sub_list))

    possible_answers = []
    for formula in list(np.concatenate(formulas).flat):
        if eval(formula) == 24:
            possible_answers.append(formula)
    if len(possible_answers) == 0:
        return "Impossible"
    return possible_answers


if __name__ == '__main__':
    l = [9, 9, 9, 4]

    answers = get24(l)
    print(answers)
