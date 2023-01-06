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
                               black_gem_price, con_black_gem_price,
                               show_one_test):
    spent_items = 0
    if show_one_test == True:
        temp_begin_lev = begin_lev
        rolls = 0
        spent_black_gems = 0
        spent_con_black_gems = 0
        all_enh_items = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        string = ['*** FULL TEST ***', f'ENHANCEMENT: {name_of_item}',
                  f'from +{begin_lev} to +{end_lev}']
        while begin_lev != end_lev:
            string.append('')
            rolls += 1
            if temp_begin_lev == begin_lev:
                spent_items += 1
            enhancement_chance = base_persent[str(begin_lev + 1)]
            spent_black_gems += black_gems[str(begin_lev + 1)]
            spent_con_black_gems += con_black_gems[str(begin_lev + 1)]
            if 1 <= random.randint(1, 10000) <= (base_persent[str(begin_lev + 1)]*100):
                begin_lev += 1
                all_enh_items[begin_lev] += 1
                string.append(f'rolls: {rolls}, success!')
            else:
                string.append(f'rolls: {rolls}, failed.')
                string.append(f'We lost item +{begin_lev}')
                begin_lev = temp_begin_lev
            string.append(f"Current enhancement's level +{begin_lev}")
            string.append(f"Chance was {enhancement_chance} %")
            string.append('WE SPENT:')
            string.append(
                f'{spent_items} items ='
                f' {conv_nice_view(spent_items * stuff_price)} silver')
            temp_worth = spent_black_gems * black_gem_price
            string.append(
                f'Black gems: {spent_black_gems} = {conv_nice_view(temp_worth)} silver')
            temp_worth = spent_con_black_gems * con_black_gem_price
            string.append(f'Concentrated_Black gems: {spent_con_black_gems} '
                          f'= {conv_nice_view(temp_worth)} silver')
        string.append('')
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
        string.append('')
        string.append('EXPENSES:')
        temp_full_price = spent_items * stuff_price
        string.append(f'Spent {spent_items} items'
                      f' = {conv_nice_view(temp_full_price)} silver')
        string.append('Or you could get instead:')
        for key in all_enh_items:
            if all_enh_items[key] != 0 and key != end_lev:
                string.append(f'+{key} : {all_enh_items[key]} items')
        temp_worth = spent_black_gems * black_gem_price
        temp_full_price += temp_worth
        string.append(
            f'Spent black gems: {spent_black_gems} = {conv_nice_view(temp_worth)} silver')
        temp_worth = spent_con_black_gems * con_black_gem_price
        temp_full_price += temp_worth
        string.append(f'Spent concentrated black gems: {spent_con_black_gems} '
                      f'= {conv_nice_view(temp_worth)} silver')
        additional_message = ''
        save_money = auction_price[str(end_lev)] - temp_full_price
        if save_money >= 0:
            additional_message = f' (saved {conv_nice_view(save_money)} silver)'
        else:
            additional_message = f' (lost -{conv_nice_view(abs(save_money))} silver)'
        string.append(
            f'Full price = {conv_nice_view(temp_full_price)} silver {additional_message}')
        return string
    else:
        temp_begin_lev = begin_lev
        attempt = 0
        rolls = 0
        all_enh_items = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        temp_time = time.time()
        all_rolls = []
        all_expenses = []
        spent_items = 0
        temp_full_price = 0
        spent_black_gems = 0
        spent_con_black_gems = 0
        while attempt < tests:
            one_attempt_roll = 0
            one_attempt_item = 0
            one_attempt_black_gems = 0
            one_attempt_con_black_gems = 0
            attempt += 1
            begin_lev = temp_begin_lev
            while begin_lev != end_lev:
                if begin_lev == temp_begin_lev:
                    spent_items += 1
                    one_attempt_item += 1
                one_attempt_roll += 1
                rolls += 1
                one_attempt_black_gems += black_gems[str(begin_lev + 1)]
                one_attempt_con_black_gems += con_black_gems[str(
                    begin_lev + 1)]
                if 1 <= random.randint(1, 10000) <= (base_persent[str(begin_lev + 1)]*100):
                    begin_lev += 1
                    all_enh_items[begin_lev] += 1
                else:
                    begin_lev = temp_begin_lev
            temp_one_attempt_worth = one_attempt_item * stuff_price
            temp_one_attempt_worth += one_attempt_black_gems * black_gem_price
            temp_one_attempt_worth += one_attempt_con_black_gems * con_black_gem_price
            all_expenses.append(temp_one_attempt_worth)
            temp_full_price += temp_one_attempt_worth
            spent_black_gems += one_attempt_black_gems
            spent_con_black_gems += one_attempt_con_black_gems
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
        string.append(f'Sharpering from +{temp_begin_lev} to +{end_lev}')
        string.append('')
        string.append('FEATURES:')
        if type(one_fail) is str and one_fail == 'None':
            string.append("This item can't use Failstacks")
        string.append('If you will fail rolled, your item will destroy')
        string.append(
            "Doesn't use crone stones to save level. The maximum level can be +5")
        for key in black_gems:
            if black_gems[key] != 0:
                string.append('This item uses black gems for sharpering')
                break
        for key in con_black_gems:
            if con_black_gems[key] != 0:
                string.append(
                    'This item uses concentrated black gems for sharpering')
                break
        string.append('')
        string.append('RESULTS:')
        string.append(f'We have obtained the following averages:')
        temp = int(rolls / tests)
        string.append(f'ROLLED: {temp}')
        string.append(
            'If you will spend 1 second for 1 click, you will do it:')
        string.append(f'{temp} seconds = {int(temp / 60)} minutes '
                      f'= {int(temp / 3600)} hours = {int (temp / 86400)} days.')
        string.append('')
        string.append('EXPENSES')
        temp_gems = int(spent_black_gems / tests)
        string.append(
            f'Spent {temp_gems} black gems = {conv_nice_view(temp_gems * black_gem_price)} silver')
        temp_gems = int(spent_con_black_gems / tests)
        string.append(f'Spent {temp_gems} concentrated black '
                      f'gems = {conv_nice_view(temp_gems * con_black_gem_price)} silver')
        string.append(f'Spent {int(spent_items / tests)} items'
                      f' = {conv_nice_view((spent_items / tests) * stuff_price)} silver')
        string.append('Or you could get instead:')
        for key in all_enh_items:
            if all_enh_items[key] != 0 and key != end_lev:
                string.append(
                    f'+{key} : {int(all_enh_items[key] / tests)} items')
        string.append(
            f'The minimum was {min(all_rolls)} rolled = {conv_nice_view(min(all_expenses))} silver')
        string.append(
            f'The maximum was {max(all_rolls)} rolled = {conv_nice_view(max(all_expenses))} silver')
        temp_full_price = (temp_full_price / tests)
        string.append(f'FULL PRICE = {conv_nice_view(temp_full_price)} silver')
        string.append('')
        string.append('SELL:')
        string.append(
            f'On auction house item +{end_lev} costs {conv_nice_view(auction_price[str(end_lev)])} silver')
        string.append(
            f'If you will spent for enhancement {conv_nice_view(temp_full_price)} silver')
        string.append(
            f'and put on auction hous for {conv_nice_view(auction_price[str(end_lev)])} silver')
        string.append('You will get:')
        temp_worth = (auction_price[str(end_lev)] *
                      0.65 - temp_full_price)
        string.append(
            f'Standart profit (65%)= {conv_nice_view(temp_worth)} silver')
        temp_worth = (auction_price[str(end_lev)] *
                      0.85 - temp_full_price)
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
        string.append(
            f'The maximum costs were {conv_nice_view(max(bad_rolls))} silver')

        return string


def life_mastery_accessories(begin_lev=0, end_lev=3, tests=1000, item_name='Life_Mastery_Loggia_Ring',
                             show_one_test=False):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_gem_price = items_prices['Black_Gem']
    con_black_gem_price = items_prices['Concentrated_Black_Gem']
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
                                        black_gem_price, con_black_gem_price,
                                        show_one_test)
    return report
