import random
import json
from push_info import load_data, load_prices


def check_profit_from_100_enh(end_lev, tests, base_persent, memory_fragment_price,
                              name_of_item, stuff_price, auction_price, flawless_chaotic_blackstone,
                              one_fail, black_stone_price, flawless_chaotic_blackstone_price,
                              max_fails, best_failstacks, crons_amount, begin_lev, use_crone,):

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Fallen_Gods_Armor']
    crone_stone_price = 2000000
    stone_amount = {}
    for i in range(351):
        stone_amount[i] = 0
    stone_amount[5], stone_amount[10], stone_amount[15], stone_amount[20] = 5, 12, 21, 33
    stone_amount[25], stone_amount[30] = 53, 84
    fails = best_failstacks
    string = []
    tests = 1000
    safety_up = use_crone
    all_expenses = []
    all_enh_items = list()
    all_valks_used = dict()
    one_case_all_valks = dict()
    attempt = 0
    spent_flawless_blackstones = 0
    spent_black_stones = 0
    lost_durability = 0
    all_money = 0
    total_expenses = 0
    spent_cron_stones = 0
    rolls = 0
    string.append('')
    string.append(f'FULL REPORT FOR {tests} TESTS:')
    string.append(f'Item price = {conv_nice_view(stuff_price)} silver')
    string.append(
        f'Auction house price = {conv_nice_view(auction_price[str(end_lev)])} silver')
    string.append('')
    while attempt < tests:
        attempt += 1
        one_case_black_stones = 0
        all_enh_items.clear()
        one_case_all_valks.clear()
        one_case_flawless = 0
        one_case_durability = 0
        one_case_cron_stones = 0
        collected_fails = 0
        temp_level = begin_lev
        changed_grade = True
        current_fails = 0
        save_nadera_1 = 0
        save_nadera_2 = 0
        save_nadera_3 = 0
        save_nadera_4 = 0
        while temp_level < end_lev:
            rolls += 1
            if changed_grade:
                if temp_level == 1 and save_nadera_1 != 0:
                    all_enh_items.append(
                        f'(load N1 -> {save_nadera_1} F)')
                    current_fails = save_nadera_1
                    save_nadera_1 = 0
                elif temp_level == 2 and save_nadera_2 != 0:
                    current_fails = save_nadera_2
                    all_enh_items.append(
                        f'(load N2 -> {save_nadera_2} F)')
                    save_nadera_2 = 0
                elif temp_level == 3 and save_nadera_3 != 0:
                    current_fails = save_nadera_3
                    all_enh_items.append(
                        f'(load N3 -> {save_nadera_3} F)')
                    save_nadera_3 = 0
                elif temp_level == 4 and save_nadera_4 != 0:
                    current_fails = save_nadera_4
                    all_enh_items.append(
                        f'(load N4 -> {save_nadera_4} F)')
                    save_nadera_4 = 0
                else:
                    current_fails = fails[temp_level]
                    spent_black_stones += stone_amount[current_fails]
                    one_case_black_stones += stone_amount[current_fails]
                    if stone_amount[current_fails] > 0:
                        all_enh_items.append(
                            f'(use {stone_amount[current_fails]} st)')
                    elif stone_amount[current_fails] == 0:
                        all_enh_items.append(
                            f'(VALKS {current_fails})')
                        if current_fails not in one_case_all_valks:
                            one_case_all_valks[current_fails] = 1
                        else:
                            one_case_all_valks[current_fails] += 1
            else:
                current_fails = fails[temp_level] + collected_fails
            if current_fails > max_fails[str(temp_level + 1)]:
                current_fails = max_fails[str(temp_level + 1)]
            if current_fails >= 30:
                all_enh_items.append('(' + str(current_fails) +
                                     'F -> ' + str(temp_level + 1) + ')')
            chance = (
                (one_fail[str(temp_level + 1)][str(current_fails)])*100)
            if 1 <= random.randint(1, 10000) <= chance:
                changed_grade = True
                collected_fails = 0
                spent_flawless_blackstones += 1
                one_case_flawless += 1
                temp_level += 1
                if current_fails >= 30:
                    string.append(str(all_enh_items))
                    all_enh_items.clear()
                all_enh_items.append(temp_level)
            else:
                changed_grade = True
                spent_flawless_blackstones += 1
                one_case_flawless += 1
                if temp_level == 0:
                    changed_grade = False
                    collected_fails += 2
                elif temp_level == 1:
                    if safety_up:
                        spent_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        one_case_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        collected_fails += 3
                        changed_grade = False
                    else:
                        temp_level -= 1
                        save_nadera_1 = current_fails + 3
                elif temp_level == 2:
                    if safety_up:
                        spent_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        one_case_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        collected_fails += 4
                        changed_grade = False
                    else:
                        temp_level -= 1
                        save_nadera_2 = current_fails + 4
                elif temp_level == 3:
                    if safety_up:
                        spent_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        one_case_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        collected_fails += 5
                        changed_grade = False
                    else:
                        temp_level -= 1
                        save_nadera_3 = current_fails + 5
                elif temp_level == 4:
                    if safety_up:
                        spent_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        one_case_cron_stones += crons_amount[str(
                            temp_level + 1)]
                        collected_fails += 6
                        changed_grade = False
                    else:
                        temp_level -= 1
                        save_nadera_4 = current_fails + 6
                lost_durability += 30
                one_case_durability += 30
                if current_fails >= 30:
                    string.append(str(all_enh_items))
                    all_enh_items.clear()
                all_enh_items.append(temp_level)
        string.append(str(all_enh_items))
        one_case_worth = stuff_price
        one_case_worth += one_case_black_stones * black_stone_price
        one_case_worth += one_case_durability * memory_fragment_price
        one_case_worth += one_case_flawless * flawless_chaotic_blackstone_price
        one_case_worth += one_case_cron_stones * crone_stone_price
        for key, item in one_case_all_valks.items():
            if key not in all_valks_used:
                all_valks_used[key] = item
            else:
                all_valks_used[key] += item
        string.append('expenses:')
        string.append(
            f'  {one_case_black_stones} Black stones = '
            f'{conv_nice_view(one_case_black_stones * black_stone_price)} silver')
        string.append(
            f'{one_case_durability} memory fragments = '
            f'{conv_nice_view(one_case_durability * memory_fragment_price)} silver')
        string.append(
            f'{one_case_flawless} flawless chaotic black stones = '
            f'{conv_nice_view(one_case_flawless * flawless_chaotic_blackstone_price)} silver')
        for key, item in one_case_all_valks.items():
            string.append(f'+{key} valks = {item}')
        string.append(
            f'ALL EXPENSES = {conv_nice_view(one_case_worth)} silver')
        temp_money = ((auction_price[str(end_lev)]*0.85) - one_case_worth)
        if temp_money > 0:
            string.append(
                f'PROFIT = {conv_nice_view(temp_money)} silver')
        else:
            string.append(
                f'LOST = -{conv_nice_view(-1*temp_money)} silver')
        all_money += temp_money
        if all_money > 0:
            string.append(
                f'TOTAL BALANCE = {conv_nice_view(all_money)} silver')
        else:
            string.append(
                f'TOTAL BALANCE = -{conv_nice_view(-1*all_money)} silver')
        string.append('')
        all_expenses.append(one_case_worth)

    string.append(f'RESULT OF {tests} ENHANCEMENTS:')
    temp_worth = lost_durability * memory_fragment_price
    string.append(
        f'{lost_durability} memory fragments = '
        f'{conv_nice_view(temp_worth)} silver')
    temp_worth = spent_flawless_blackstones * flawless_chaotic_blackstone_price
    string.append(
        f'{spent_flawless_blackstones} flawless chaotic black stones = '
        f'{conv_nice_view(temp_worth)} silver')
    for key, item in all_valks_used.items():
        string.append(f'+{key} valks = {item}')
    if all_money > 0:
        string.append(
            f'TOTAL PROFIT = {conv_nice_view(all_money)} silver')
    else:
        string.append(
            f'TOTAL LOST = -{conv_nice_view(-1*all_money)} silver')
    string.append('')

    string.append('')

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


def Red_Fallen_Gods_Armor(valks=None, begin_lev=0, end_lev=5, tests=100, item_name='Fallen_Gods_Armor',
                          show_one_test=False, find_fails=False, use_crone=1):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_stone_price = items_prices['Black_Stone_Weapon']
    flawless_chaotic_blackstone_price = (items_prices['Sharp_Black_Crystal_Shard']
                                         + items_prices['Hard_Black_Crystal_Shard']
                                         + items_prices['Caphras_Stone'] * 10)
    memory_fragment_price = items_prices['Memory_Fragment']
    name_of_item = item_name.replace('_', ' ')

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    crons_amount = item_settings['crons_amount']
    flawless_chaotic_blackstone = item_settings['flawless_chaotic_blackstone']
    item_grade = item_settings['item_grade']
    best_failstacks = ['best_failstacks']
    auction_price = item_settings['auction_price']
    use_the_same_item = item_settings['use_the_same_item']
    max_fails = item_settings['max_fails']

    if not find_fails:
        report = check_profit_from_100_enh(end_lev, tests, base_persent, memory_fragment_price,
                                           name_of_item, stuff_price, auction_price, flawless_chaotic_blackstone,
                                           one_fail, black_stone_price, flawless_chaotic_blackstone_price,
                                           max_fails, valks, crons_amount, begin_lev, use_crone)
        # all_data = load_data()
        # all_data[item_name]['best_failstacks'] = new_best_fails
        # json.dump(all_data, fp=open('data.txt', 'w'), indent=4)
    return report
