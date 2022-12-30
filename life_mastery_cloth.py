# import json
import random
import math
from push_info import load_data, load_prices

# def load_prices():
#     items_prices = json.load(open('default_prices.txt'))
#     return items_prices


# def load_data():
#     item_settings = json.load(open('data.txt'))
#     return item_settings


def conv_nice_view(number):
    if number // 1000000000 > 0:
        number = str(round((number / 1000000000), 3))
        return (number + ' billions')
    elif number // 1000000 > 0:
        number = str(round((number / 1000000), 3))
        return (number + ' millions')
    else:
        return str(number)


def durability_price(item_price, item_grade, memory_fragment_price):
    memory_fr_restore = {'RED': 1, 'YELLOW': 1,
                         'BLUE': 2, 'GREEN': 5, 'WHITE': 10}
    if (item_price / 10) >= (memory_fragment_price / (memory_fr_restore[item_grade])):
        worth_one_point_dur = (memory_fragment_price /
                               (memory_fr_restore[item_grade]))
    else:
        worth_one_point_dur = item_price / 10
    return worth_one_point_dur


def best_way_restore_dur(item_price, durability, item_grade, memory_fragment_price):
    memory_fr_restore = {'RED': 1, 'YELLOW': 1,
                         'BLUE': 2, 'GREEN': 5, 'WHITE': 10}
    dur_message = []
    dur_message.append(
        f'Price for one ITEM on auction house: {item_price} silver')
    dur_message.append(
        f'One memory fragment will restore {memory_fr_restore[item_grade]} points')
    dur_message.append(
        f'Worth for 1 durability point with item uses = {round((item_price / 10), 3)} silver')
    dur_message.append(f'Worth for 1 durability point with memore fragment uses '
                       f'= {round(memory_fragment_price / (memory_fr_restore[item_grade]), 3)} silver')
    temp_message = ''
    artisans_memory = 0
    if (item_price / 10) >= (memory_fragment_price / (memory_fr_restore[item_grade])):
        dur_message.append(
            f'Use {durability} MEMORY FRAGMENTS to restore durability!')
        worth = (memory_fragment_price /
                 memory_fr_restore[item_grade]) * durability
        artisans_memory = math.ceil(durability / 5)
        temp_message = (f'And then use {math.ceil(durability / 5)} memory'
                        f' fragments = {conv_nice_view(worth / 5)} silver')
    else:
        dur_message.append(
            f'Use {math.ceil(durability / 10)} ITEMs to restore durability!')
        worth = (item_price / 10) * durability
        artisans_memory = math.ceil((durability / 10)/5)
        temp_message = (f'And then use {math.ceil((durability / 10)/5)} items'
                        f' = {conv_nice_view(worth / 5)} silver')
    dur_message.append(
        f'LOST {durability} points of DURABILITY = {conv_nice_view(worth)} silver')
    dur_message.append(f"Or you can use {artisans_memory} Artisan's Memory")
    dur_message.append(temp_message)
    return (artisans_memory, worth, dur_message)


def test_report(total_black_gems, total_con_black_gems, tests, black_gem_price, name_of_item,
                con_black_gem_price, total_durability, total_price, begin_lev, end_lev,
                price_dur_restore, item_price, memory_fragment_price, item_grade,
                auction_price, one_fail, crons_amount, total_rolls, full_tests_result):
    memory_fr_restore = {'RED': 1, 'YELLOW': 1,
                         'BLUE': 2, 'GREEN': 5, 'WHITE': 10}
    string = []
    string.append(f'<<< RESULT OF {tests} ENCHANTMENTS >>>')
    string.append(f'ITEM: {name_of_item}')
    string.append(f'grade: {item_grade}')
    string.append(f'item price: {conv_nice_view(item_price)} silver')
    string.append(f'From +{begin_lev} to +{end_lev}')
    string.append('')
    string.append('FEATURES:')
    if type(one_fail) is str and one_fail == 'None':
        string.append("This item can't use Failstacks")
    if type(crons_amount) is str and crons_amount == 'None':
        string.append(
            "This item can't use cron stones to save level after +17")
    string.append('')
    string.append('EXPENSES:')
    string.append('We got next average values: ')
    string.append(f'Rolls: {total_rolls}')
    temp_worth = total_black_gems * black_gem_price
    string.append(
        f'Spent {total_black_gems} black gems = {conv_nice_view(temp_worth)} silver')
    temp_worth = total_con_black_gems * con_black_gem_price
    string.append(f'Spent {total_con_black_gems} Concentrated'
                  f' black gems = {conv_nice_view(temp_worth)} silver')
    temp_worth = price_dur_restore * total_durability
    string.append(
        f'Lost {total_durability} durability points = {conv_nice_view(temp_worth)} silver')
    string.append(f'Full price = {conv_nice_view(total_price)} silver')
    temp_message = ''
    artisans_memory = 0
    if (item_price / 10) >= (memory_fragment_price / (memory_fr_restore[item_grade])):
        string.append(
            f'Use {total_durability} MEMORY FRAGMENTS to restore durability!')
        worth = (memory_fragment_price /
                 memory_fr_restore[item_grade]) * total_durability
        artisans_memory = math.ceil(total_durability / 5)
        temp_message = (f'And then use {math.ceil(total_durability / 5)} memory'
                        f' fragments = {conv_nice_view(worth / 5)} silver')
    else:
        string.append(
            f'Use {math.ceil(total_durability / 10)} ITEMs to restore durability!')
        worth = (item_price / 10) * total_durability
        artisans_memory = math.ceil((total_durability / 10)/5)
        temp_message = (f'And then use {math.ceil((total_durability / 10)/5)} items'
                        f' = {conv_nice_view(worth / 5)} silver')
    string.append('')
    string.append('SAVE MONEY:')
    string.append(f"Or you can use {artisans_memory} Artisan's Memory")
    string.append(temp_message)
    temp_worth = (total_black_gems * black_gem_price +
                  total_con_black_gems * con_black_gem_price +
                  price_dur_restore * (total_durability / 5))
    string.append(
        f'You will save {conv_nice_view(total_price - temp_worth)} silver')
    string.append(f'Then full price = {conv_nice_view(temp_worth)} silver')
    string.append('')
    string.append('SELL:')
    string.append(
        f'On auction house item +{end_lev} costs {conv_nice_view(auction_price[str(end_lev)])} silver')
    string.append(
        f'If you bought 1 item for {conv_nice_view(item_price)} silver')
    string.append(
        f'and spent for enhancement {conv_nice_view(total_price)} silver')
    string.append(
        f'and put on auction hous for {conv_nice_view(auction_price[str(end_lev)])} silver')
    string.append('You will get:')
    temp_worth = (auction_price[str(end_lev)] *
                  0.65 - total_price - item_price)
    string.append(
        f'Standart profit (65%)= {conv_nice_view(temp_worth)} silver')
    temp_worth = (auction_price[str(end_lev)] *
                  0.85 - total_price - item_price)
    string.append(
        f'Premium profit (85%) = {conv_nice_view(temp_worth)} silver')
    string.append('')
    string.append('ADDITIONAL INFORMATION:')
    zero_price_no_premium = auction_price[str(end_lev)]
    string.append(
        f'On auction house item +{end_lev} costs: {conv_nice_view(zero_price_no_premium)} silver')
    good_rolls = list(filter(lambda item: item <=
                             zero_price_no_premium, full_tests_result))
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
                            zero_price_no_premium, full_tests_result))
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


def enhancement(begin_lev, end_lev, tests, base_persent, lost_durability, black_gems, con_black_gems,
                name_of_item, black_gem_price, con_black_gem_price, item_grade,
                memory_fragment_price, stuff_price, auction_price, one_fail,
                crons_amount, show_one_test=False):
    spent_durability = 0
    spent_black_gems = 0
    spent_con_black_gems = 0
    if show_one_test == True:
        temp_begin_lev = begin_lev
        rolls = 0
        string = ['*** FULL TEST ***', f'ENHANCEMENT: {name_of_item}',
                  f'from +{begin_lev} to +{end_lev}']
        while begin_lev != end_lev:
            string.append('')
            rolls += 1
            spent_black_gems += black_gems[str(begin_lev + 1)]
            spent_con_black_gems += con_black_gems[str(begin_lev + 1)]
            enhancement_chance = base_persent[str(begin_lev + 1)]
            if 1 <= random.randint(1, 10000) <= (base_persent[str(begin_lev + 1)]*100):
                begin_lev += 1
                string.append(f'rolls: {rolls}, success!')
            else:
                spent_durability += lost_durability[str(begin_lev + 1)]
                string.append(f'rolls: {rolls}, failed.')
                if begin_lev >= 17:
                    begin_lev -= 1
            string.append(f"Current enhancement's level +{begin_lev}")
            string.append(f"Chance was {enhancement_chance} %")
            string.append('WE SPENT:')
            string.append(
                f'Black gems: {spent_black_gems}'
                f' = {black_gem_price * spent_black_gems} silver')
            string.append(
                f'Concentrated black gems: {spent_con_black_gems}'
                f' = {con_black_gem_price * spent_con_black_gems} silver')
            string.append(f'Lost {spent_durability} durability points')
        string.append('')
        string.append('<<<FULL REPORT>>>')
        string.append(f'Item: {name_of_item}')
        string.append(f'Sharpering from +{temp_begin_lev} to +{end_lev}')
        string.append(f'ROLLS: {rolls}')
        artisans_memory, worth, dur_message = best_way_restore_dur(stuff_price, spent_durability,
                                                                   item_grade, memory_fragment_price)
        string.extend(dur_message)
        string.append('SPENT:')
        temp_full_price = spent_black_gems * black_gem_price
        string.append(f'Spent {spent_black_gems} black gems'
                      f' = {conv_nice_view(spent_black_gems * black_gem_price)} silver')
        temp_full_price += spent_con_black_gems * con_black_gem_price
        string.append(f'Spent {spent_con_black_gems} concentrated black gems'
                      f' = {conv_nice_view(spent_con_black_gems * con_black_gem_price)} silver')
        string.append('TOTAL:')
        string.append(
            f'All price: {conv_nice_view(temp_full_price + worth)} silver')
        string.append(
            f"With {artisans_memory} Artisan's Memory: {conv_nice_view(temp_full_price + (worth / 5))} silver")
        return string

    else:
        full_tests_result = []
        total_gem = 0
        total_con_gem = 0
        total_dur = 0
        total_price = 0
        total_rolls = 0
        for i in range(tests):
            spent_durability = 0
            spent_black_gems = 0
            spent_con_black_gems = 0
            rolls = 0
            sharp_price = 0
            temp_begin_lev = begin_lev
            price_dur_restore = durability_price(
                stuff_price, item_grade, memory_fragment_price)
            while temp_begin_lev != end_lev:
                spent_black_gems += black_gems[str(temp_begin_lev + 1)]
                spent_con_black_gems += con_black_gems[str(temp_begin_lev + 1)]
                rolls += 1
                if 1 <= random.randint(1, 10000) <= (base_persent[str(temp_begin_lev + 1)]*100):
                    temp_begin_lev += 1
                else:
                    spent_durability += lost_durability[str(
                        temp_begin_lev + 1)]
                    if temp_begin_lev >= 17:
                        temp_begin_lev -= 1
            sharp_price += (spent_black_gems * black_gem_price) + \
                (spent_con_black_gems * con_black_gem_price) + \
                (spent_durability * price_dur_restore)
            total_gem += spent_black_gems
            total_con_gem += spent_con_black_gems
            total_dur += spent_durability
            total_price += sharp_price
            total_rolls += rolls
            full_tests_result.append(sharp_price)
        total_gem = math.ceil(total_gem / tests)
        total_con_gem = math.ceil(total_con_gem / tests)
        total_dur = math.ceil(total_dur / tests)
        total_price = math.ceil(total_price / tests)
        total_rolls = math.ceil(total_rolls / tests)
        string = test_report(total_gem, total_con_gem, tests, black_gem_price, name_of_item,
                             con_black_gem_price, total_dur, total_price, begin_lev, end_lev,
                             price_dur_restore, stuff_price, memory_fragment_price, item_grade,
                             auction_price, one_fail, crons_amount, total_rolls, full_tests_result)
        return string


def Life_Mastery_Clothes(begin_lev=0, end_lev=17, tests=1000, item_name='Manos_Sailing_Life_Mastery_Clothes',
                         show_one_test=False):
    items_prices = load_prices()
    black_gem_price = items_prices['Black_Gem']
    con_black_gem_price = items_prices['Concentrated_Black_Gem']
    stuff_price = items_prices[item_name]
    name_of_item = item_name.replace('_', ' ')
    memory_fragment_price = items_prices['Memory_Fragment']

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    ceiling_persent = item_settings['ceiling_persent']
    crons_amount = item_settings['crons_amount']
    black_gems = item_settings['black_gems']
    con_black_gems = item_settings['con_black_gems']
    lost_durability = item_settings['lost_durability']
    item_grade = item_settings['item_grade']
    item_type = item_settings['item_type']
    auction_price = item_settings['auction_price']

    report = enhancement(begin_lev, end_lev, tests, base_persent,
                         lost_durability, black_gems, con_black_gems,
                         name_of_item, black_gem_price, con_black_gem_price,
                         item_grade, memory_fragment_price, stuff_price,
                         auction_price, one_fail, crons_amount, show_one_test)
    return report
