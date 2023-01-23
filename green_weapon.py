import random
import math
import json
from push_info import load_data, load_prices


def find_fails_whithout_naderr(begin_lev, end_lev, tests, base_persent,
                               name_of_item, stuff_price,
                               one_fail, black_stone_price, con_black_stone_price,
                               max_fails):

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['WEAPON_(Green_Grade)']

    stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
    fails = [0, 0, 0, 0, 0, 0, 0, 10, 10, 15,
             15, 20, 30, 30, 30, 30, 30, 30, 30, 30]
    start_pos = 7
    finish_pos = end_lev - 1
    if begin_lev > 7:
        start_pos = begin_lev - 1
    report = []
    tests = 1000
    first_case = True
    best_result = 0
    data_best_result = []
    best_check_fail = 0
    best_attempt_price = 0
    while True:
        for test_fails in range(0, 31, 5):
            fails[start_pos] = test_fails
            attempt = 0
            spent_black_stones = 0
            spent_con_black_stones = 0
            lost_durability = 0
            total_expenses = 0
            while attempt < tests:
                attempt += 1
                collected_fails = 0
                temp_level = begin_lev
                changed_grade = True
                current_fails = 0
                while temp_level < end_lev:
                    if changed_grade:
                        current_fails = fails[temp_level]
                        if temp_level >= 7:
                            spent_black_stones += stone_amount[current_fails]
                    else:
                        current_fails = fails[temp_level] + collected_fails
                    if current_fails > max_fails[str(temp_level + 1)]:
                        current_fails = max_fails[str(temp_level + 1)]
                    chance = (
                        (one_fail[str(temp_level + 1)][str(current_fails)])*100)
                    if 1 <= random.randint(1, 10000) <= chance:
                        changed_grade = True
                        collected_fails = 0
                        if temp_level <= 14:
                            spent_black_stones += 1
                        else:
                            spent_con_black_stones += 1
                        temp_level += 1
                    else:
                        changed_grade = False
                        if temp_level == 15:
                            collected_fails += 2
                            spent_con_black_stones += 1
                            lost_durability += 10
                        elif temp_level == 16:
                            collected_fails += 3
                            spent_con_black_stones += 1
                            lost_durability += 10
                        else:
                            lost_durability += 5
                            spent_black_stones += 1
                            collected_fails += 1
            spent_black_stones /= tests
            spent_con_black_stones /= tests
            spent_items = int((int(lost_durability / 10)) / tests)
            report.append(f'For case: {fails}')
            temp_expenses = int(spent_black_stones) * black_stone_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {int(spent_black_stones)} black stones = {conv_nice_view(temp_expenses)} silver')
            temp_expenses = spent_con_black_stones * con_black_stone_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {spent_con_black_stones} concentrated black stones = {conv_nice_view(temp_expenses)} silver')
            temp_expenses = spent_items * stuff_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {spent_items} items = {conv_nice_view(temp_expenses)} silver')
            report.append(
                f'Total EXPENSES= {conv_nice_view(total_expenses)} silver')
            report.append('')
            if first_case == True:
                best_result = total_expenses
                first_case = False
            if total_expenses <= best_result:
                best_result = total_expenses
                data_best_result.clear()
                data_best_result.append(int(spent_black_stones))
                data_best_result.append(spent_con_black_stones)
                data_best_result.append(spent_items)
                data_best_result.append(total_expenses)
                data_best_result.append(fails.copy())
            if test_fails == 0:
                best_attempt_price = total_expenses
            if total_expenses <= best_attempt_price:
                best_attempt_price = total_expenses
                best_check_fail = test_fails
            print(f'ready {start_pos}, {test_fails}')
        if (start_pos == finish_pos) and (fails[start_pos] == 30):
            report.append('')
            report.append('The best case:')
            report.append(str(data_best_result))
            break
        fails[start_pos] = best_check_fail
        start_pos += 1
    # report = 'done'
    return report


def find_fails_with_naderr(begin_lev, end_lev, tests, base_persent,
                           name_of_item, stuff_price,
                           one_fail, black_stone_price):
    one_fail = unpack_one_fail(one_fail.copy(), base_persent)
    celiing_fail = get_failstack_ceiling(one_fail)
    stone_amount = {0: 0, 5: 5, 10: 12, 15: 21,
                    20: 33, 25: 53, 30: 84, 40: 0, 44: 0,
                    50: 0, 80: 0, 100: 0, 120: 0}

    def count_expenses(valkas_list):
        tests = 1000
        attempt = 0
        spent_items = 0
        spent_black_stones = 0
        nadera_level_1 = 2
        nadera_level_2 = 3
        nadera_level_3 = 4
        nadera_level_4 = 5
        while attempt < tests:
            attempt += 1
            temp_level = begin_lev
            collected_fails = 0
            increased_lev = True
            save_on_nedara_1 = 0
            save_on_nedara_2 = 0
            save_on_nedara_3 = 0
            save_on_nedara_4 = 0
            while temp_level != end_lev:
                spent_items += 1
                if temp_level == begin_lev:
                    spent_items += 1
                if (temp_level + 1 == nadera_level_1) and save_on_nedara_1 != 0:
                    fails = save_on_nedara_1
                    save_on_nedara_1 = 0
                elif (temp_level + 1 == nadera_level_2) and save_on_nedara_2 != 0:
                    fails = save_on_nedara_2
                    save_on_nedara_2 = 0
                elif (temp_level + 1 == nadera_level_3) and save_on_nedara_3 != 0:
                    fails = save_on_nedara_3
                    save_on_nedara_3 = 0
                elif (temp_level + 1 == nadera_level_4) and save_on_nedara_4 != 0:
                    fails = save_on_nedara_4
                    save_on_nedara_4 = 0
                elif increased_lev:
                    fails = valkas_list[temp_level]
                    spent_black_stones += stone_amount[valkas_list[temp_level]]
                else:
                    fails = collected_fails
                chance = ((one_fail[str(temp_level + 1)][fails])*100)
                if 1 <= random.randint(1, 10000) <= chance:
                    increased_lev = True
                    temp_level += 1
                    collected_fails = 0
                else:
                    increased_lev = False
                    collected_fails = fails + 1
                    if collected_fails > celiing_fail[temp_level]:
                        collected_fails = celiing_fail[temp_level]
                    if temp_level + 1 == nadera_level_1:
                        save_on_nedara_1 = collected_fails
                        increased_lev = True
                        collected_fails = 0
                    elif temp_level + 1 == nadera_level_2:
                        save_on_nedara_2 = collected_fails
                        increased_lev = True
                        collected_fails = 0
                    elif temp_level + 1 == nadera_level_3:
                        save_on_nedara_3 = collected_fails
                        increased_lev = True
                        collected_fails = 0
                    elif temp_level + 1 == nadera_level_4:
                        save_on_nedara_4 = collected_fails
                        increased_lev = True
                        collected_fails = 0
                    temp_level = begin_lev
        spent_items = int(spent_items / tests)
        spent_black_stones = int(spent_black_stones / tests)
        full_price = spent_items * stuff_price + spent_black_stones * black_stone_price
        print(f'{valkas_list} = {conv_nice_view(full_price)} silver. '
              f'{spent_items} items / {spent_black_stones} BS')
        return full_price, valkas_list.copy(), spent_items, spent_black_stones
    all_tests_result = {}
    fails = [10, 25, 40, 80, 100]
    for index in range(4):
        gen = permute_silver(fails, index)
        while True:
            try:
                one_valks_test = count_expenses(next(gen))
            except StopIteration:
                print('finished')
                break
            else:
                all_tests_result[one_valks_test[0]] = one_valks_test[1:]
        min_expenses = min(list(all_tests_result.keys()))
        fails = all_tests_result[min_expenses][0]
    report = []
    sort_test_result = list(all_tests_result.keys())
    sort_test_result.sort()
    for key in sort_test_result:
        string = f'{all_tests_result[key][0]} = {conv_nice_view(key)} silver. '
        string += f'{all_tests_result[key][1]} Items / {all_tests_result[key][2]} Black Stones'
        report.append(string)
    return report


def conv_nice_view(number):
    if number // 1000000000 > 0:
        number = str(round((number / 1000000000), 3))
        return (number + ' billions')
    elif number // 1000000 > 0:
        number = str(round((number / 1000000), 3))
        return (number + ' millions')
    else:
        return str(number)


def Green_Grade_Main_Weapon(begin_lev=0, end_lev=10, tests=1000, item_name='Green_Grade_Main_Weapon',
                            show_one_test=False, find_fails=False):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_stone_price = items_prices['Black_Stone_Weapon']
    con_black_stone_price = items_prices['Concentrated_Magical_Black_Stone']
    name_of_item = item_name.replace('_', ' ')

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    crons_amount = item_settings['crons_amount']
    item_grade = item_settings['item_grade']
    soft_cap_fails = item_settings['soft_cap_fails']
    best_failstacks = [0] * 20
    auction_price = item_settings['auction_price']
    use_the_same_item = item_settings['use_the_same_item']
    black_stone = item_settings['black_stone']
    con_black_stone = item_settings['con_black_stone']
    max_fails = item_settings['max_fails']

    if not find_fails:
        report = 'not ready'
    else:
        if end_lev >= 18:
            report = find_fails_with_naderr(begin_lev, end_lev, tests, base_persent,
                                            name_of_item, stuff_price,
                                            one_fail, black_stone_price)
        else:
            report = find_fails_whithout_naderr(begin_lev, end_lev, tests, base_persent,
                                                name_of_item, stuff_price,
                                                one_fail, black_stone_price, con_black_stone_price,
                                                max_fails)
    return report
