import time
import random
import math
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


def enhancement_LM_accessories(begin_lev, end_lev, tests, base_persent,
                               name_of_item, stuff_price, use_the_same_item,
                               auction_price, one_fail, black_gems, con_black_gems,
                               show_one_test):
    spent_items = 1
    if show_one_test == True:
        temp_begin_lev = begin_lev
        rolls = 0
        all_enh_items = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        string = ['*** FULL TEST ***', f'ENHANCEMENT: {name_of_item}',
                  f'from +{begin_lev} to +{end_lev}']
        while begin_lev != end_lev:
            additional_item = 0
            if rolls <= 1000:
                string.append('')
            rolls += 1
            enhancement_chance = base_persent[str(begin_lev + 1)]
            spent_items += 1
            if 1 <= random.randint(1, 10000) <= (base_persent[str(begin_lev + 1)]*100):
                begin_lev += 1
                all_enh_items[begin_lev] += 1
                if rolls <= 1000:
                    string.append(f'rolls: {rolls}, success!')
            else:
                additional_item = -1
                if rolls <= 1000:
                    string.append(f'rolls: {rolls}, failed.')
                    string.append(f'We lost item +{begin_lev}')
                spent_items += 1
                begin_lev = temp_begin_lev
            if rolls <= 1000:
                string.append(f"Current enhancement's level +{begin_lev}")
                string.append(f"Chance was {enhancement_chance} %")
                string.append('WE SPENT:')
                string.append(
                    f'{spent_items + additional_item} items ='
                    f' {conv_nice_view((spent_items + additional_item)* stuff_price)} silver')
        if rolls > 1000:
            string.append(f'And etc...We had {rolls} rolled total...')
        string.append('')
        string.append('<<<FULL REPORT>>>')
        string.append(f'Item: {name_of_item}')
        string.append(f'Item costs: {conv_nice_view(stuff_price)} silver')
        string.append(f'Sharpering from +{temp_begin_lev} to +{end_lev}')
        string.append(
            f'On auction house item +{end_lev} '
            f'costs {conv_nice_view(auction_price[str(end_lev)])} silver')
        string.append(f'ROLLED: {rolls}')
        string.append(
            'If you will spend 1 second for 1 click, you will do it:')
        string.append(f'{rolls} seconds = {int(rolls / 60)} minutes '
                      f'= {int(rolls / 3600)} hours = {int (rolls / 86400)} days.')
        temp_full_price = spent_items * stuff_price
        string.append(f'Spent {spent_items} items'
                      f' = {conv_nice_view(temp_full_price)} silver')
        string.append('Or you could get instead:')
        for key in all_enh_items:
            if all_enh_items[key] != 0 and key != end_lev:
                string.append(f'+{key} : {all_enh_items[key]} items')
        return string
    else:
        temp_begin_lev = begin_lev
        attempt = 0
        rolls = 0
        all_enh_items = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        temp_time = time.time()
        all_rolls = []
        all_expenses = []
        while attempt < tests:
            one_attempt_roll = 0
            one_attempt_item = 0
            attempt += 1
            begin_lev = temp_begin_lev
            while begin_lev != end_lev:
                one_attempt_roll += 1
                rolls += 1
                spent_items += 1
                one_attempt_item += 1
                if 1 <= random.randint(1, 10000) <= (base_persent[str(begin_lev + 1)]*100):
                    begin_lev += 1
                    all_enh_items[begin_lev] += 1
                else:
                    spent_items += 1
                    one_attempt_item += 1
                    begin_lev = temp_begin_lev
            all_expenses.append(one_attempt_item * stuff_price)
            if end_lev >= 4:
                temp_time = time.time() - temp_time
                print(
                    f'test: {attempt} / {tests}, counting time {round(temp_time, 2)} seconds')
                temp_time = time.time()
            all_rolls.append(one_attempt_roll)
        string = []
        string.append('')
        string.append('<<<FULL REPORT>>>')
        string.append(f'THE RESULT OF {tests} TESTS')
        string.append('')
        string.append(f'Item: {name_of_item}')
        string.append(
            f'The price for base item {conv_nice_view(stuff_price)} silver')
        string.append(
            f'The price from auction house for +{end_lev} '
            f': {conv_nice_view(auction_price[str(end_lev)])} silver')
        string.append(f'Sharpering from +{temp_begin_lev} to +{end_lev}')
        string.append('')
        string.append('FEATURES:')
        if type(one_fail) is str and one_fail == 'None':
            string.append("This item can't use Failstacks")
        if use_the_same_item:
            string.append(
                "This item uses the same kind of item for sharpening.")
            string.append("Doesn't use Black stones or Black gems.")
            string.append(
                "Doesn't use crone stones to save level. The maximum level can be +5")
        string.append('')
        string.append('EXPENSES:')
        string.append(f'We have obtained the following averages:')
        temp = int(rolls / tests)
        string.append(f'ROLLED: {temp}')
        string.append(
            'If you will spend 1 second for 1 click, you will do it:')
        string.append(f'{temp} seconds = {int(temp / 60)} minutes '
                      f'= {int(temp / 3600)} hours = {int (temp / 86400)} days.')
        temp_full_price = (spent_items / tests) * stuff_price
        string.append(f'Spent {int(spent_items / tests)} items'
                      f' = {conv_nice_view(temp_full_price)} silver')
        string.append('Or you could get instead:')
        for key in all_enh_items:
            if all_enh_items[key] != 0 and key != end_lev:
                string.append(
                    f'+{key} : {int(all_enh_items[key] / tests)} items')
        string.append(
            f'The minimum was {min(all_rolls)} rolled = {conv_nice_view(min(all_expenses))} silver')
        string.append(
            f'The maximum was {max(all_rolls)} rolled = {conv_nice_view(max(all_expenses))} silver')
        return string


def life_mastery_accessories(begin_lev=0, end_lev=3, tests=1000, item_name='Life_Mastery_Loggia_Ring',
                             show_one_test=False):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    name_of_item = item_name.replace('_', ' ')

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    crons_amount = item_settings['crons_amount']
    item_grade = item_settings['item_grade']
    black_gems = item_settings['black_gems']
    con_black_gems = item_settings['con_black_gems']
    auction_price = item_settings['auction_price']
    use_the_same_item = item_settings['use_the_same_item']

    report = enhancement_LM_accessories(begin_lev, end_lev, tests, base_persent,
                                        name_of_item, stuff_price, use_the_same_item,
                                        auction_price, one_fail, black_gems, con_black_gems,
                                        show_one_test)
    return report
