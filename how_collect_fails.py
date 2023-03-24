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
    one_fail = item_settings['one_fail']

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Armor_(White_Blue_Yellow_Grade)'][str(check_lev)]

    report = []
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


def how_to_get_high_enh_chance(first_check_lev=15, tests=10000, second_check_lev=20,
                               first_item_name='RU_Green_Grade_Azwell_Longsword_Weapon',
                               second_item_name='Blackstar_Weapon_Longsword'):
    items_prices = load_prices()
    first_stuff_price = items_prices[first_item_name]
    second_stuff_price = items_prices[second_item_name]
    black_stone_price = items_prices['Black_Stone_Weapon']

    first_item_settings = load_data()[first_item_name]
    first_one_fail = first_item_settings['one_fail']
    second_item_settings = load_data()[second_item_name]
    second_one_fail = second_item_settings['one_fail']

    if first_one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        first_one_fail = item['Armor_(White_Blue_Yellow_Grade)'][str(
            first_check_lev)]
        # first_one_fail = item['RU_SERVER_WEAPON_(Green_Grade)'][str(
        #    first_check_lev)]

    if second_one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        second_one_fail = item['Weapons_(Black_Star)'][str(
            second_check_lev)]

    report = []
    report.append(
        f'\nIncrease chances to get +20 black star weapon:')
    attempt = 0
    lost_durability = 0
    spent_black_stones = 0
    passed_chance = []
    all_chance = {}
    fails_bs = 180
    dif_attempts = 0
    try_black_star = False
    while attempt < tests:
        attempt += 1
        dif_attempts += 1
        begin_lev = first_check_lev
        fails = 0
        count = 0
        while begin_lev == first_check_lev:
            spent_black_stones += 1
            if try_black_star:
                chance_bs = ((second_one_fail[str(fails_bs)])*100)
                if 1 <= random.randint(1, 10000) <= chance_bs:
                    print(f'we got bs! After {dif_attempts} cases')
                    dif_attempts = 0
                    try_black_star = False
                else:
                    print('LOSER AGAIN {dif_attempts} cases')
            else:
                chance = ((first_one_fail[str(fails)])*100)
                if 1 <= random.randint(1, 10000) <= chance:
                    fails = 0
                    begin_lev += 1
                    if len(passed_chance) >= 15:
                        if len(passed_chance) not in all_chance:
                            all_chance[len(passed_chance)] = 1
                        else:
                            all_chance[len(passed_chance)] += 1
                    passed_chance.clear()
                else:
                    count += 1
                    if count == 18:
                        passed_chance.append(1)
                        if len(passed_chance) == 4:
                            chance_bs = ((second_one_fail[str(fails_bs)])*100)
                            if 1 <= random.randint(1, 10000) <= chance_bs:
                                print(f'we got bs! After {dif_attempts} cases')
                                dif_attempts = 0
                                try_black_star = False
                            else:
                                print(f'LOSER! After {dif_attempts} cases')
                                try_black_star = True
                        count = 0
                    lost_durability += 5
                    fails += 1
    number = 0
    count_to_get_ten_valsk = 0
    # while count_to_get_ten_valsk < 10:
    #     number += 1
    #     count_to_get_ten_valsk += searsh_valks[valks] / tests
    # average_black_stones = int((spent_black_stones / tests) * number)
    # report.append(f'Spent {average_black_stones} black stones (Armor)'
    #               f'= {conv_nice_view(average_black_stones * black_stone_price)} silver')
    # average_bought_items = int((decrease_level / tests) * number)
    # report.append(f'Decreased level +15 back to +14 of reblath helmet {average_bought_items} times'
    #               f'= {conv_nice_view(average_bought_items * dis_price)} silver')
    # spent_items_for_dur = int(((lost_durability / 10) / tests) * number)
    # report.append(f'Used {spent_items_for_dur} reblath helmet '
    #               f'= {conv_nice_view(spent_items_for_dur * first_stuff_price)} silver')
    # spent_for_books = blacksmiths_secret_book[valks]
    # report.append(
    #     f'Spent to buy 10 blacksmiths secret book = {conv_nice_view(spent_for_books)} silver')
    # full_expenses = (average_black_stones * black_stone_price
    #                  + average_bought_items * dis_price + spent_items_for_dur * first_stuff_price + spent_for_books)
    # report.append(
    #     f'FULL EXPENSES = {conv_nice_view(full_expenses)} silver')
    # if valks == 20 or valks == 30:
    #     report.append(f'Compare to get +{valks} fails to buy stones '
    #                   f'= {conv_nice_view(stone_amount[valks] * black_stone_price * 10)} silver')

    # return report
    print(report)
    print(all_chance)
    print(passed_chance)


# how_to_get_high_enh_chance()
