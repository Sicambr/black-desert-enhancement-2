import random
import math
import json
from push_info import load_data, load_prices


def find_fails_whithout_naderr(begin_lev, end_lev, tests, base_persent,
                               name_of_item, stuff_price,
                               one_fail, black_stone_price, con_black_stone_price,
                               max_fails, best_failstacks):

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
    tests = 100
    report.append(f'WE DID {tests} tests for each case:')
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
            print(f'Count position {start_pos}, with {test_fails} fails...')
        if (start_pos == finish_pos) and (fails[start_pos] == 30):
            report.append('')
            report.append('The best case:')
            report.append(f'Spent {data_best_result[0]} black stones')
            report.append(
                f'Spent {data_best_result[1]} concentrated black stones')
            report.append(f'Bought {data_best_result[2]} items')
            report.append(
                f'TOTAL EXPENSES = {conv_nice_view(data_best_result[3])} silver')
            report.append(
                f'Use next fails to get level from +{begin_lev} to +{end_lev}:')
            string = ''
            for number in range(1, 21, 1):
                string = '+' + str(number) + ' = ' + \
                    str(data_best_result[4][number - 1]) + ' fails'
                report.append(string)
            print('Succesfull!')
            break
        fails[start_pos] = best_check_fail
        start_pos += 1
    return report, data_best_result[4].copy()


def find_fails_with_naderr(end_lev, tests, base_persent,
                           name_of_item, stuff_price,
                           one_fail, black_stone_price, con_black_stone_price,
                           max_fails, best_failstacks, crons_amount, begin_lev):

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['WEAPON_(Green_Grade)']
    crone_stone_price = 2000000
    stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84, 48: 0}
    fails = [0, 0, 0, 0, 0, 0, 0, 10, 10, 15,
             15, 20, 30, 30, 30, 30, 30, 30, 30, 48]
    start_pos = 7
    finish_pos = end_lev - 1
    if begin_lev > 7:
        start_pos = begin_lev - 1
    report = []
    tests = 1000
    report.append(f'WE DID {tests} tests for each case:')
    first_case = True
    best_result = 0
    data_best_result = []
    best_check_fail = 0
    best_attempt_price = 0
    safety_up = True
    while True:
        for test_fails in range(0, 31, 5):
            fails[start_pos] = test_fails
            attempt = 0
            spent_black_stones = 0
            spent_con_black_stones = 0
            lost_durability = 0
            total_expenses = 0
            spent_cron_stones = 0
            while attempt < tests:
                attempt += 1
                collected_fails = 0
                temp_level = begin_lev
                changed_grade = True
                current_fails = 0
                save_nadera_1 = 0
                save_nadera_2 = 0
                save_nadera_3 = 0
                # print(f'\nNEW CASE FOR {start_pos} pos, {test_fails} fails')
                while temp_level < end_lev:
                    # print(f'Current level = {temp_level}')
                    if changed_grade:
                        if temp_level == 17 and save_nadera_1 != 0:
                            # print(f'use {save_nadera_1} saved fails')
                            current_fails = save_nadera_1
                            save_nadera_1 = 0
                        elif temp_level == 18 and save_nadera_2 != 0:
                            # print(f'use {save_nadera_2} saved fails')
                            current_fails = save_nadera_2
                            save_nadera_2 = 0
                        elif temp_level == 19 and save_nadera_3 != 0:
                            # print(f'use {save_nadera_3} saved fails')
                            current_fails = save_nadera_3
                            save_nadera_3 = 0
                        else:
                            current_fails = fails[temp_level]
                            if temp_level >= 7:
                                spent_black_stones += stone_amount[current_fails]
                    else:
                        current_fails = fails[temp_level] + collected_fails
                    if current_fails > max_fails[str(temp_level + 1)]:
                        current_fails = max_fails[str(temp_level + 1)]
                    chance = (
                        (one_fail[str(temp_level + 1)][str(current_fails)])*100)
                    # print(f'fails = {current_fails}')
                    if 1 <= random.randint(1, 10000) <= chance:
                        changed_grade = True
                        collected_fails = 0
                        if temp_level <= 14:
                            spent_black_stones += 1
                        else:
                            spent_con_black_stones += 1
                        temp_level += 1
                        # print('success!')
                    else:
                        # print('FAILED!')
                        changed_grade = False
                        if temp_level == 15:
                            collected_fails += 2
                            spent_con_black_stones += 1
                            lost_durability += 10
                        elif temp_level > 15 and temp_level < 17:
                            collected_fails += 3
                            spent_con_black_stones += 1
                            lost_durability += 10
                        elif temp_level >= 17:
                            changed_grade = True
                            # print('level decreased.')
                            spent_con_black_stones += 1
                            if temp_level == 17:
                                save_nadera_1 = current_fails + 3
                                # print(f'will save {save_nadera_1} fails')
                            elif temp_level == 18:
                                if safety_up:
                                    spent_cron_stones += crons_amount[str(
                                        temp_level + 1)]
                                    temp_level += 1
                                else:
                                    save_nadera_2 = current_fails + 3
                                # print(f'will save {save_nadera_2} fails')
                            elif temp_level == 19:
                                if safety_up:
                                    spent_cron_stones += crons_amount[str(
                                        temp_level + 1)]
                                    temp_level += 1
                                else:
                                    save_nadera_3 = current_fails + 3
                                # print(f'will save {save_nadera_3} fails')
                            lost_durability += 10
                            temp_level -= 1
                        else:
                            lost_durability += 5
                            spent_black_stones += 1
                            collected_fails += 1
            spent_cron_stones = int(spent_cron_stones / tests)
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
            temp_expenses = spent_cron_stones * crone_stone_price
            report.append(
                f'Bought {spent_cron_stones} crone stones = {conv_nice_view(temp_expenses)} silver')
            total_expenses += temp_expenses
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
                data_best_result.append(spent_cron_stones)
                data_best_result.append(total_expenses)
                data_best_result.append(fails.copy())
            if test_fails == 0:
                best_attempt_price = total_expenses
            if total_expenses <= best_attempt_price:
                best_attempt_price = total_expenses
                best_check_fail = test_fails
            print(f'Count position {start_pos}, with {test_fails} fails...')
        if (start_pos == finish_pos) and (fails[start_pos] == 30):
            report.append('')
            report.append('The best case:')
            report.append(f'Spent {data_best_result[0]} black stones')
            report.append(
                f'Spent {data_best_result[1]} concentrated black stones')
            report.append(f'Bought {data_best_result[2]} items')
            report.append(f'Bought {data_best_result[3]} crone stones')
            report.append(
                f'TOTAL EXPENSES = {conv_nice_view(data_best_result[4])} silver')
            report.append(
                f'Use next fails to get level from +{begin_lev} to +{end_lev}:')
            string = ''
            for number in range(1, 21, 1):
                string = '+' + str(number) + ' = ' + \
                    str(data_best_result[5][number - 1]) + ' fails'
                report.append(string)
            print('Succesfull!')
            break
        fails[start_pos] = best_check_fail
        start_pos += 1
    return report, data_best_result[5].copy()


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
    best_failstacks = ['best_failstacks']
    auction_price = item_settings['auction_price']
    use_the_same_item = item_settings['use_the_same_item']
    black_stone = item_settings['black_stone']
    con_black_stone = item_settings['con_black_stone']
    max_fails = item_settings['max_fails']

    if not find_fails:
        report = 'not ready'
    else:
        if end_lev >= 18:
            report, new_best_fails = find_fails_with_naderr(end_lev, tests, base_persent,
                                                            name_of_item, stuff_price,
                                                            one_fail, black_stone_price, con_black_stone_price,
                                                            max_fails, best_failstacks, crons_amount, begin_lev=16)
        else:
            report, new_best_fails = find_fails_whithout_naderr(begin_lev, end_lev, tests, base_persent,
                                                                name_of_item, stuff_price,
                                                                one_fail, black_stone_price, con_black_stone_price,
                                                                max_fails, best_failstacks)
            # all_data = load_data()
            # all_data[item_name]['best_failstacks'] = new_best_fails
            # json.dump(all_data, fp=open('data.txt', 'w'), indent=4)
    return report
