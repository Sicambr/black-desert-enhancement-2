import random
import json
from push_info import load_data, load_prices


def durability_price(item_price, item_grade, memory_fragment_price):
    memory_fr_restore = {'RED': 1, 'YELLOW': 1,
                         'BLUE': 2, 'GREEN': 5, 'WHITE': 10}
    memory_amount = 1
    durability_way = 'Item'
    if (item_price / 10) >= (memory_fragment_price / (memory_fr_restore[item_grade])):
        worth_one_point_dur = (memory_fragment_price /
                               (memory_fr_restore[item_grade]))
        durability_way = 'Memory_Fragment'
        memory_amount /= memory_fr_restore[item_grade]
    else:
        worth_one_point_dur = item_price / 10
    return worth_one_point_dur, durability_way, memory_amount


def find_fails_whithout_naderr(begin_lev, tests, base_persent, worth_one_point_dur,
                               name_of_item, stuff_price, durability_way, memory_amount,
                               one_fail, black_stone_price, con_black_stone_price,
                               max_fails, best_failstacks, end_lev):

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Weapons_(White_Blue_Yellow_Grade)']

    stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
    fails = [0, 0, 0, 0, 0, 0, 0, 10, 10, 15,
             15, 20, 30, 30, 30, 30, 30, 30, 30, 30]
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
    while True:
        for test_fails in range(0, 31, 5):
            fails[start_pos] = test_fails
            attempt = 0
            spent_black_stones = 0
            spent_con_black_stones = 0
            spent_memory_fragments = 0
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
            spent_durability = int(lost_durability / tests)
            report.append(f'For case: {fails}')
            temp_expenses = int(spent_black_stones) * black_stone_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {int(spent_black_stones)} black stones = {conv_nice_view(temp_expenses)} silver')
            temp_expenses = spent_con_black_stones * con_black_stone_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {spent_con_black_stones} concentrated black stones = {conv_nice_view(temp_expenses)} silver')
            if durability_way == 'Item':
                temp_expenses = spent_items * stuff_price
                total_expenses += temp_expenses
                report.append(
                    f'Spent {spent_items} items = {conv_nice_view(temp_expenses)} silver')
            else:
                temp_expenses = spent_durability * worth_one_point_dur
                total_expenses += temp_expenses
                spent_memory_fragments = spent_durability * memory_amount
                report.append(f'Spent {spent_items} items')
                report.append(f'Used {spent_memory_fragments} memory'
                              f' fragments = {conv_nice_view(temp_expenses)} silver')
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
                data_best_result.append(spent_memory_fragments)
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
            report.append(f'Used {data_best_result[5]} memory fragments')
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
    return report, data_best_result[4].copy(), data_best_result


def find_fails_with_naderr(end_lev, tests, base_persent, best_fails_less_16,
                           name_of_item, stuff_price, saved_data,
                           one_fail, black_stone_price, con_black_stone_price,
                           max_fails, best_failstacks, crons_amount,
                           worth_one_point_dur, durability_way, memory_amount,
                           begin_lev):

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Weapons_(White_Blue_Yellow_Grade)']
    crone_stone_price = 2000000
    stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84, 48: 0}
    fails = best_fails_less_16.copy()
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
            spent_memory_fragments = 0
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
                while temp_level < end_lev:
                    if changed_grade:
                        if temp_level == 17 and save_nadera_1 != 0:
                            current_fails = save_nadera_1
                            save_nadera_1 = 0
                        elif temp_level == 18 and save_nadera_2 != 0:
                            current_fails = save_nadera_2
                            save_nadera_2 = 0
                        elif temp_level == 19 and save_nadera_3 != 0:
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
                        elif temp_level >= 17:
                            changed_grade = True
                            spent_con_black_stones += 1
                            if temp_level == 17:
                                save_nadera_1 = current_fails + 4
                            elif temp_level == 18:
                                if safety_up:
                                    spent_cron_stones += crons_amount[str(
                                        temp_level + 1)]
                                    temp_level += 1
                                    collected_fails += 5
                                    changed_grade = False
                                else:
                                    save_nadera_2 = current_fails + 5
                            elif temp_level == 19:
                                if safety_up:
                                    spent_cron_stones += crons_amount[str(
                                        temp_level + 1)]
                                    temp_level += 1
                                    collected_fails += 6
                                    changed_grade = False
                                else:
                                    save_nadera_3 = current_fails + 6
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
            spent_durability = int(lost_durability / tests)
            temp_expenses = int(spent_black_stones) * black_stone_price
            total_expenses += temp_expenses
            temp_expenses = spent_con_black_stones * con_black_stone_price
            total_expenses += temp_expenses
            if durability_way == 'Item':
                temp_expenses = spent_items * stuff_price
                total_expenses += temp_expenses
            else:
                temp_expenses = spent_durability * worth_one_point_dur
                total_expenses += temp_expenses
                spent_memory_fragments = spent_durability * memory_amount
            temp_expenses = spent_cron_stones * crone_stone_price
            total_expenses += temp_expenses
            if first_case == True:
                best_result = total_expenses
                first_case = False
            if total_expenses <= best_result:
                best_result = total_expenses
                data_best_result.clear()
                data_best_result.append(
                    int(spent_black_stones) + saved_data[0])
                data_best_result.append(spent_con_black_stones + saved_data[1])
                data_best_result.append(spent_items + saved_data[2])
                data_best_result.append(spent_cron_stones)
                data_best_result.append(total_expenses + saved_data[3])
                data_best_result.append(fails.copy())
                data_best_result.append(spent_memory_fragments + saved_data[5])
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
            report.append(f'Used {data_best_result[6]} memory fragments')
            report.append(
                f'TOTAL EXPENSES = {conv_nice_view(data_best_result[4])} silver')
            report.append(
                f'Use next fails to get level from +0 to +{end_lev}:')
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


def standart_enhancement_yellow_weapon(end_lev, tests, base_persent,
                                       name_of_item, stuff_price, auction_price,
                                       one_fail, black_stone_price, con_black_stone_price,
                                       max_fails, best_failstacks, crons_amount, begin_lev):

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Weapons_(White_Blue_Yellow_Grade)']
    crone_stone_price = 2000000
    stone_amount = {}
    for i in range(121):
        stone_amount[i] = 0
    stone_amount[5], stone_amount[10], stone_amount[15], stone_amount[20] = 5, 12, 21, 33
    stone_amount[25], stone_amount[30] = 53, 84
    fails = best_failstacks
    string = []
    tests = 10000
    safety_up = True

    all_expenses = []
    all_enh_items = {17: 0, 18: 0, 19: 0, 20: 0}
    attempt = 0
    spent_black_stones = 0
    spent_con_black_stones = 0
    lost_durability = 0
    total_expenses = 0
    spent_cron_stones = 0
    rolls = 0
    while attempt < tests:
        attempt += 1
        one_case_black_stones = 0
        one_case_con_black_stones = 0
        one_case_durability = 0
        one_case_cron_stones = 0
        collected_fails = 0
        temp_level = begin_lev
        changed_grade = True
        current_fails = 0
        save_nadera_1 = 0
        save_nadera_2 = 0
        save_nadera_3 = 0
        while temp_level < end_lev:
            rolls += 1
            if changed_grade:
                if temp_level == 17 and save_nadera_1 != 0:
                    current_fails = save_nadera_1
                    save_nadera_1 = 0
                elif temp_level == 18 and save_nadera_2 != 0:
                    current_fails = save_nadera_2
                    save_nadera_2 = 0
                elif temp_level == 19 and save_nadera_3 != 0:
                    current_fails = save_nadera_3
                    save_nadera_3 = 0
                else:
                    current_fails = fails[temp_level]
                    if temp_level >= 7:
                        spent_black_stones += stone_amount[current_fails]
                        one_case_black_stones += stone_amount[current_fails]
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
                    one_case_black_stones += 1
                else:
                    spent_con_black_stones += 1
                    one_case_con_black_stones += 1
                temp_level += 1
                if temp_level in all_enh_items.keys():
                    all_enh_items[temp_level] += 1
            else:
                changed_grade = False
                if temp_level == 15:
                    collected_fails += 2
                    spent_con_black_stones += 1
                    one_case_con_black_stones += 1
                    lost_durability += 10
                    one_case_durability += 10
                elif temp_level == 16:
                    collected_fails += 3
                    spent_con_black_stones += 1
                    one_case_con_black_stones += 1
                    lost_durability += 10
                    one_case_durability += 10
                elif temp_level >= 17:
                    changed_grade = True
                    spent_con_black_stones += 1
                    one_case_con_black_stones += 1
                    if temp_level == 17:
                        save_nadera_1 = current_fails + 4
                    elif temp_level == 18:
                        if safety_up:
                            spent_cron_stones += crons_amount[str(
                                temp_level + 1)]
                            one_case_cron_stones += crons_amount[str(
                                temp_level + 1)]
                            temp_level += 1
                            collected_fails += 5
                            changed_grade = False
                        else:
                            save_nadera_2 = current_fails + 5
                    elif temp_level == 19:
                        if safety_up:
                            spent_cron_stones += crons_amount[str(
                                temp_level + 1)]
                            one_case_cron_stones += crons_amount[str(
                                temp_level + 1)]
                            temp_level += 1
                            collected_fails += 6
                            changed_grade = False
                        else:
                            save_nadera_3 = current_fails + 6
                    lost_durability += 10
                    one_case_durability += 10
                    temp_level -= 1
                else:
                    lost_durability += 5
                    one_case_durability += 5
                    spent_black_stones += 1
                    one_case_black_stones += 1
                    collected_fails += 1
        one_case_worth = 0
        one_case_worth += one_case_black_stones * black_stone_price
        one_case_worth += one_case_con_black_stones * con_black_stone_price
        one_case_worth += int(one_case_durability / 10) * stuff_price
        one_case_worth += one_case_cron_stones * crone_stone_price

        all_expenses.append(one_case_worth)

    spent_cron_stones = int(spent_cron_stones / tests)
    spent_black_stones /= tests
    spent_con_black_stones /= tests
    spent_items = int((int(lost_durability / 10)) / tests)

    string.append('')
    string.append('<<<FULL REPORT>>>')
    string.append(f'THE RESULT OF {tests} TESTS')
    string.append('')
    string.append(f'Item: {name_of_item}')
    string.append(
        f'The price for base item {conv_nice_view(stuff_price)} silver')
    string.append(f'Sharpering from +{begin_lev} to +{end_lev}')
    string.append('')
    string.append('FEATURES:')
    string.append("This item has fail stacks. You may use"
                  " any way to increase them before you will sharp item.")
    string.append("This item decrease level after +17 if you will failed.")
    string.append("You can use crone stones to save level after +17.")

    string.append('')
    string.append('CURRENT SETTINGS:')
    string.append('Used Nadera thread to save fails after +17 : YES')
    if safety_up:
        string.append('Used crone stones to keep level after +18 : YES')
    else:
        string.append('Used crone stones to keep level after +18 : NO')

    string.append('')
    string.append('EXPENSES:')
    string.append(f'We have obtained the following averages:')
    temp = int(rolls / tests)
    string.append(f'ROLLED: {temp}')
    string.append(
        'If you will spend 1 second for 1 click, you will do it:')
    string.append(f'{temp} seconds = {int(temp / 60)} minutes '
                  f'= {int(temp / 3600)} hours = {int (temp / 86400)} days.')
    string.append(f'We used next faistacks pattern: {fails}')
    temp_expenses = int(spent_black_stones) * black_stone_price
    total_expenses += temp_expenses
    string.append(
        f'Spent {int(spent_black_stones)} black stones = {conv_nice_view(temp_expenses)} silver')
    temp_expenses = spent_con_black_stones * con_black_stone_price
    total_expenses += temp_expenses
    string.append(
        f'Spent {spent_con_black_stones} concentrated black stones = {conv_nice_view(temp_expenses)} silver')
    temp_expenses = spent_items * stuff_price
    total_expenses += temp_expenses
    string.append(
        f'Spent {spent_items} items = {conv_nice_view(temp_expenses)} silver')
    temp_expenses = spent_cron_stones * crone_stone_price
    string.append(
        f'Bought {spent_cron_stones} crone stones = {conv_nice_view(temp_expenses)} silver')
    total_expenses += temp_expenses
    string.append(
        f'Total EXPENSES= {conv_nice_view(total_expenses)} silver')
    string.append('')
    string.append('We were on next levels, while did enhancement:')
    for key in all_enh_items:
        if all_enh_items[key] != 0 and key != end_lev:
            string.append(
                f'+{key} : {int(all_enh_items[key] / tests)} times')
    string.append('')
    string.append('SELL:')
    string.append(
        f'On auction house item +{end_lev} costs {conv_nice_view(auction_price[str(end_lev)])} silver')
    string.append(
        f'If you will spent for enhancement {conv_nice_view(total_expenses)} silver')
    string.append(
        f'and put on auction hous for {conv_nice_view(auction_price[str(end_lev)])} silver')
    string.append('You will get:')
    temp_worth = (auction_price[str(end_lev)] *
                  0.65 - total_expenses)
    string.append(
        f'Standart profit (65%)= {conv_nice_view(temp_worth)} silver')
    temp_worth = (auction_price[str(end_lev)] *
                  0.85 - total_expenses)
    string.append(
        f'Premium profit (85%) = {conv_nice_view(temp_worth)} silver')
    string.append('')
    string.append('ADDITIONAL INFORMATION:')
    zero_price_no_premium = auction_price[str(end_lev)]
    string.append(
        f'On auction house item +{end_lev} costs: {conv_nice_view(zero_price_no_premium)} silver')
    good_rolls = list(filter(lambda item: item <=
                             zero_price_no_premium, all_expenses))
    string.append('Good rolls:')
    string.append(
        f'All cases when our expenses were LESS than auction house prices:')
    string.append(f'We had: {len(good_rolls)} '
                  f'cases from {tests}. This is {round((len(good_rolls) / (tests/100)), 3)} %')
    good_rolls_2 = list(filter(lambda item: item <=
                               zero_price_no_premium * 0.8, good_rolls))
    string.append(f'20%) We spent less than {conv_nice_view(zero_price_no_premium * 0.8)} silver'
                  f' = {len(good_rolls_2)} cases. This is {round((len(good_rolls_2) / (tests/100)), 3)} %')
    good_rolls_3 = list(filter(lambda item: item <=
                               zero_price_no_premium * 0.5, good_rolls))
    string.append(f'50%) We spent less than {conv_nice_view(zero_price_no_premium * 0.5)} silver'
                  f' = {len(good_rolls_3)} cases. This is {round((len(good_rolls_3) / (tests/100)), 3)} %')
    if good_rolls:
        string.append(
            f'The minimum costs were {conv_nice_view(min(good_rolls))} silver')
    string.append('Bad rolls:')
    string.append(
        f'All cases when our expenses were MORE than auction house prices:')
    bad_rolls = list(filter(lambda item: item >
                            zero_price_no_premium, all_expenses))
    string.append(f'We had: {len(bad_rolls)} '
                  f'cases from {tests}. This is {round((len(bad_rolls) / (tests/100)), 3)} %')
    bad_rolls_2 = list(filter(lambda item: item >=
                              zero_price_no_premium * 1.5, bad_rolls))
    string.append(f'1.5x) We spent more than {conv_nice_view(zero_price_no_premium * 1.5)} silver'
                  f' = {len(bad_rolls_2)} cases. This is {round((len(bad_rolls_2) / (tests/100)), 3)} %')
    bad_rolls_3 = list(filter(lambda item: item >=
                              zero_price_no_premium * 2, bad_rolls))
    string.append(f'2x) We spent more than {conv_nice_view(zero_price_no_premium * 2)} silver'
                  f' = {len(bad_rolls_3)} cases. This is {round((len(bad_rolls_3) / (tests/100)), 3)} %')
    bad_rolls_4 = list(filter(lambda item: item >=
                              zero_price_no_premium * 3, bad_rolls))
    string.append(f'3x) We spent more than {conv_nice_view(zero_price_no_premium * 3)} silver'
                  f' = {len(bad_rolls_4)} cases. This is {round((len(bad_rolls_4) / (tests/100)), 3)} %')
    if bad_rolls:
        string.append(
            f'The maximum costs were {conv_nice_view(max(bad_rolls))} silver')

    return string


def conv_nice_view(number):
    if number // 1000000000 > 0:
        number = str(round((number / 1000000000), 3))
        return (number + ' billions')
    elif number // 1000000 > 0:
        number = str(round((number / 1000000), 3))
        return (number + ' millions')
    else:
        return str(number)


def Yellow_Grade_Main_Weapon(valks=None, begin_lev=0, end_lev=10, tests=1000, item_name='Yellow_Grade_Main_Weapon',
                             show_one_test=False, find_fails=False):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_stone_price = items_prices['Black_Stone_Weapon']
    con_black_stone_price = items_prices['Concentrated_Magical_Black_Stone']
    memory_fragment_price = items_prices['Memory_Fragment']
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

    worth_one_point_dur, durability_way, memory_amount = durability_price(
        stuff_price, item_grade, memory_fragment_price)

    if not find_fails:
        report = standart_enhancement_yellow_weapon(end_lev, tests, base_persent,
                                                    name_of_item, stuff_price, auction_price,
                                                    one_fail, black_stone_price, con_black_stone_price,
                                                    max_fails, valks, crons_amount, begin_lev)
    else:
        if end_lev >= 18:
            empty_report, best_fails_less_16, saved_data = find_fails_whithout_naderr(begin_lev, tests, base_persent, worth_one_point_dur,
                                                                                      name_of_item, stuff_price, durability_way, memory_amount,
                                                                                      one_fail, black_stone_price, con_black_stone_price,
                                                                                      max_fails, best_failstacks, end_lev=16)

            report, new_best_fails = find_fails_with_naderr(end_lev, tests, base_persent, best_fails_less_16,
                                                            name_of_item, stuff_price, saved_data,
                                                            one_fail, black_stone_price, con_black_stone_price,
                                                            max_fails, best_failstacks, crons_amount,
                                                            worth_one_point_dur, durability_way, memory_amount,
                                                            begin_lev=16)
        else:
            report, new_best_fails, saved_data = find_fails_whithout_naderr(begin_lev, tests, base_persent, worth_one_point_dur,
                                                                            name_of_item, stuff_price, durability_way, memory_amount,
                                                                            one_fail, black_stone_price, con_black_stone_price,
                                                                            max_fails, best_failstacks, end_lev)
            # all_data = load_data()
            # all_data[item_name]['best_failstacks'] = new_best_fails
            # json.dump(all_data, fp=open('data.txt', 'w'), indent=4)
    return report
