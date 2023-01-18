import random
import json
from push_info import load_data, load_prices


def conv_nice_view(number):
    if number // 1000000000 > 0:
        number = str(round((number / 1000000000), 3))
        return (number + ' billions')
    elif number // 1000000 > 0:
        number = str(round((number / 1000000), 3))
        return (number + ' millions')
    else:
        return str(number)


def find_the_best_fails_collect(item_name, check_lev, tests=10000):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_stone_price = items_prices['Black_Stone_Armor']

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    crons_amount = item_settings['crons_amount']
    item_grade = item_settings['item_grade']
    soft_cap_fails = item_settings['soft_cap_fails']
    auction_price = item_settings['auction_price']
    use_the_same_item = item_settings['use_the_same_item']

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Armor_(White_Blue_Yellow_Grade)'][str(check_lev)]

    report = []
    all_fails_we_got = {}
    dis_price = 100000
    stone_amount = {20: 33, 30: 84}
    searsh_valks = {20: 0, 30: 0, 40: 0}
    blacksmiths_secret_book = {20: 1000000, 30: 4000000, 40: 10000000}
    for valks in range(20, 41, 10):
        report.append(
            f'\nTry to collect 10 advices of valks +{valks}:')
        attempt = 0
        lost_durability = 0
        spent_black_stones = 0
        spent_secrets_books = 0
        decrease_level = 0
        while attempt < tests:
            attempt += 1
            begin_lev = check_lev
            fails = 0
            while begin_lev == check_lev:
                spent_black_stones += 1
                chance = ((one_fail[str(fails)])*100)
                if 1 <= random.randint(1, 10000) <= chance:
                    decrease_level += 1
                    fails = 0
                    begin_lev += 1
                else:
                    lost_durability += 5
                    fails += 1
                    if fails == valks:
                        searsh_valks[valks] += 1
                        begin_lev += 1
                        spent_secrets_books += 1
        number = 0
        count_to_get_ten_valsk = 0
        while count_to_get_ten_valsk < 10:
            number += 1
            count_to_get_ten_valsk += searsh_valks[valks] / tests
        average_black_stones = int((spent_black_stones / tests) * number)
        report.append(f'Spent {average_black_stones} black stones (Armor)'
                      f'= {conv_nice_view(average_black_stones * black_stone_price)} silver')
        average_bought_items = int((decrease_level / tests) * number)
        report.append(f'Decreased level +15 back to +14 of reblath helmet {average_bought_items} times'
                      f'= {conv_nice_view(average_bought_items * dis_price)} silver')
        spent_items_for_dur = int(((lost_durability / 10) / tests) * number)
        report.append(f'Used {spent_items_for_dur} reblath helmet '
                      f'= {conv_nice_view(spent_items_for_dur * stuff_price)} silver')
        spent_for_books = blacksmiths_secret_book[valks]
        report.append(
            f'Spent to buy 10 blacksmiths secret book = {conv_nice_view(spent_for_books)} silver')
        full_expenses = (average_black_stones * black_stone_price
                         + average_bought_items * dis_price + spent_items_for_dur * stuff_price + spent_for_books)
        report.append(
            f'FULL EXPENSES = {conv_nice_view(full_expenses)} silver')
        if valks == 20 or valks == 30:
            report.append(f'Compare to get +{valks} fails to buy stones '
                          f'= {conv_nice_view(stone_amount[valks] * black_stone_price * 10)} silver')

    return report
