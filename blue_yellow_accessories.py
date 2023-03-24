import random
import math
from push_info import load_data, load_prices


def find_best_fails(begin_lev, end_lev, tests, base_persent,
                    name_of_item, stuff_price,
                    one_fail, black_stone_price):
    one_fail = unpack_one_fail(one_fail.copy(), base_persent)
    stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
    size = end_lev

    def count_expenses(valkas_list):
        tests = 100
        attempt = 0
        spent_items = 0
        spent_black_stones = 0
        nadera_level_1 = 2
        nadera_level_2 = 3
        while attempt < tests:
            attempt += 1
            temp_level = begin_lev
            collected_fails = 0
            increased_lev = True
            save_on_nedara_1 = 0
            save_on_nedara_2 = 0
            while temp_level != end_lev:
                # print(f'start {valkas_list}')
                spent_items += 1
                if temp_level == begin_lev:
                    spent_items += 1
                if (temp_level + 1 == nadera_level_1) and save_on_nedara_1 != 0:
                    fails = save_on_nedara_1
                    save_on_nedara_1 = 0
                    # print(f'use saved {fails} nadera')
                elif (temp_level + 1 == nadera_level_2) and save_on_nedara_2 != 0:
                    fails = save_on_nedara_2
                    save_on_nedara_2 = 0
                elif increased_lev:
                    fails = valkas_list[temp_level]
                    spent_black_stones += stone_amount[valkas_list[temp_level]]
                    # print(f'fails = {fails}')
                    # print(f'bought {stone_amount[valkas_list[temp_level]]} stones')
                else:
                    # print(f'alredy have {collected_fails} fails from past.')
                    fails = collected_fails
                chance = ((one_fail[str(temp_level + 1)][fails])*100)
                # print(f'we try to get {temp_level + 1}')
                # print(f'chance = {chance / 100} %')
                if 1 <= random.randint(1, 10000) <= chance:
                    increased_lev = True
                    temp_level += 1
                    # print('success!')
                else:
                    # print('failed :(')
                    increased_lev = False
                    collected_fails = fails + 1
                    if temp_level + 1 == nadera_level_1:
                        save_on_nedara_1 = collected_fails
                        # print(f'We SAVED {save_on_nedara_1} fails')
                        increased_lev = True
                        collected_fails = 0
                    elif temp_level + 1 == nadera_level_2:
                        save_on_nedara_2 = collected_fails
                        # print(f'We SAVED {save_on_nedara_1} fails')
                        increased_lev = True
                        collected_fails = 0
                    temp_level = begin_lev
                # print(f'total spent {spent_items} items\n')

        spent_items = int(spent_items / tests)
        spent_black_stones = int(spent_black_stones / tests)
        full_price = spent_items * stuff_price + spent_black_stones * black_stone_price
        print(f'{valkas_list} = {conv_nice_view(full_price)} silver. '
              f'{spent_items} items / {spent_black_stones} BS')
        return full_price, valkas_list.copy(), spent_items, spent_black_stones

    all_tests_result = {}
    gen = permute(size)
    while True:
        try:
            one_valks_test = count_expenses(next(gen))
        except StopIteration:
            print('finished')
            break
        else:
            all_tests_result[one_valks_test[0]] = one_valks_test[1:]
    report = []
    sort_test_result = list(all_tests_result.keys())
    sort_test_result.sort()
    for key in sort_test_result:
        string = f'{all_tests_result[key][0]} = {conv_nice_view(key)} silver. '
        string += f'{all_tests_result[key][1]} Items / {all_tests_result[key][2]} Black Stones'
        report.append(string)
    return report


def permute(size):
    failstacks = [0] * size
    index = 0
    while True:
        failstacks[index] += 5
        if failstacks[index] <= 30:
            yield failstacks
        else:
            pos = 0
            finish_all = False
            while True:
                if failstacks[pos] > 30 and pos == (size - 1):
                    finish_all = True
                    break
                elif failstacks[pos] > 30:
                    failstacks[pos] = 0
                    pos += 1
                    failstacks[pos] += 5
                else:
                    break
            if finish_all:
                break
            yield failstacks


def get_failstack_ceiling(one_fail):
    ceiling = []
    for key in one_fail:
        temp = one_fail[key]
        ceiling.append(max(list(temp.keys())))
    return ceiling.copy()


def find_silver_pen_fails(begin_lev, end_lev, tests, base_persent,
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


def permute_silver(failstacks, index=0):
    for number in range(0, 35, 5):
        failstacks.pop(index)
        failstacks.insert(index, number)
        yield failstacks


def unpack_one_fail(pack_one_fail, base_persent):
    one_fail = {}
    for level in pack_one_fail:
        temp = {}
        begin = 0
        begin_persent = base_persent[level]
        if len(pack_one_fail[level]) > 2:
            while True:
                temp[begin] = round(begin_persent, 3)
                begin += 1
                begin_persent += pack_one_fail[level][1]
                if begin_persent >= pack_one_fail[level][0]:
                    break
            begin_persent = pack_one_fail[level][0]
            while True:
                temp[begin] = round(begin_persent, 3)
                begin += 1
                begin_persent += pack_one_fail[level][3]
                if begin_persent >= pack_one_fail[level][2]:
                    temp[begin] = pack_one_fail[level][2]
                    break
        else:
            while True:
                temp[begin] = round(begin_persent, 3)
                begin += 1
                begin_persent += pack_one_fail[level][1]
                if begin_persent >= pack_one_fail[level][0]:
                    temp[begin] = pack_one_fail[level][0]
                    break
        make_keys = list(temp.keys())
        make_keys.sort()
        if abs(temp[make_keys[-1]] - temp[make_keys[-2]]) < 1*10e-15:
            temp.pop(make_keys[-1])
        one_fail[level] = temp
    return one_fail


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
    if good_rolls:
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
    if bad_rolls:
        string.append(
            f'The maximum costs were {conv_nice_view(max(bad_rolls))} silver')
    return string


def enhancement_silv_emb_clothes(begin_lev, end_lev, tests, base_persent,
                                 name_of_item, stuff_price, use_the_same_item,
                                 auction_price, one_fail, best_failstacks,
                                 soft_cap_fails, black_stone_price, show_one_test):
    spent_items = 1
    one_fail = unpack_one_fail(one_fail.copy(), base_persent)
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
        string = []
        rolls = 0
        valkas_list = best_failstacks
        all_enh_items = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        all_rolls = []
        all_expenses = []
        one_case = {}

        celiing_fail = get_failstack_ceiling(one_fail)
        stone_amount = {}
        for i in range(121):
            stone_amount[i] = 0
        stone_amount[5], stone_amount[10], stone_amount[15], stone_amount[20] = 5, 12, 21, 33
        stone_amount[25], stone_amount[30] = 53, 84
        advice_of_valks = {}
        attempt = 0
        spent_items = 0
        spent_black_stones = 0
        nadera_level_1, nadera_level_2, nadera_level_3, nadera_level_4 = 2, 3, 4, 5
        while attempt < tests:
            one_attempt_roll = 0
            one_attempt_item = 0
            one_attempt_black_stones = 0
            attempt += 1
            temp_level = begin_lev
            collected_fails = 0
            increased_lev = True
            save_on_nedara_1, save_on_nedara_2, save_on_nedara_3, save_on_nedara_4 = 0, 0, 0, 0
            while temp_level != end_lev:
                one_attempt_roll += 1
                one_attempt_item += 1
                if temp_level == begin_lev:
                    one_attempt_item += 1
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
                    one_attempt_black_stones += stone_amount[valkas_list[temp_level]]
                    if stone_amount[valkas_list[temp_level]] == 0 and temp_level != 0:
                        if valkas_list[temp_level] not in advice_of_valks.keys():
                            advice_of_valks[valkas_list[temp_level]] = 1
                        else:
                            advice_of_valks[valkas_list[temp_level]] += 1
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
                    if temp_level != 0:
                        all_enh_items[temp_level] += 1
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
            all_rolls.append(one_attempt_roll)
            rolls += one_attempt_roll
            temp_worth = one_attempt_item * stuff_price + \
                one_attempt_black_stones * black_stone_price
            all_expenses.append(temp_worth)
            spent_items += one_attempt_item
            spent_black_stones += one_attempt_black_stones
            one_case[temp_worth] = [one_attempt_roll,
                                    one_attempt_item, one_attempt_black_stones]
            if (end_lev - begin_lev == 5) and (attempt % 100) == 0:
                print(f'{attempt} from {tests} tests finished...')
        spent_items = int(spent_items / tests)
        spent_black_stones = int(spent_black_stones / tests)
        full_price = spent_items * stuff_price + spent_black_stones * black_stone_price
        for key in sorted(list(one_case.keys())):
            string.append(
                f'{conv_nice_view(key)} silver, {one_case[key][0]} rolls'
                f', {one_case[key][1]} items, {one_case[key][2]} black stones.')
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
        if type(one_fail) is str and one_fail == 'None':
            string.append("This item can't uses failstacks")
        else:
            string.append("This item has fail stacks. You may use"
                          " any way to increase them before you will sharp item.")
        if use_the_same_item:
            string.append(
                "This item uses the same kind of item for sharpening.")
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
        temp_string = ''
        for i in range(begin_lev, end_lev):
            temp_string += ('(+' + str(i + 1) + ':' +
                            str(valkas_list[i]) + '), ')
        string.append(f'We used next faistacks pattern: {temp_string}')
        temp_price = spent_items * stuff_price
        string.append(f'Spent {spent_items} items'
                      f' = {conv_nice_view(temp_price)} silver')
        temp_price = spent_black_stones * black_stone_price
        string.append(
            f'Spent {spent_black_stones} black stones = {conv_nice_view(temp_price)}')
        if advice_of_valks:
            for key in list(advice_of_valks.keys()):
                string.append(
                    f'Spent {math.ceil(advice_of_valks[key] / tests)} advices of valks +{key}')
        string.append(f'TOTAL EXPENSES = {conv_nice_view(full_price)} silver')
        string.append(
            f'You can buy item +{end_lev} on auction house '
            f': {conv_nice_view(auction_price[str(end_lev)])} silver')
        string.append('')
        string.append('Or you could get instead:')
        for key in all_enh_items:
            if all_enh_items[key] != 0 and key != end_lev:
                string.append(
                    f'+{key} : {int(all_enh_items[key] / tests)} items')
        string.append('')
        string.append('SELL:')
        string.append(
            f'On auction house item +{end_lev} costs {conv_nice_view(auction_price[str(end_lev)])} silver')
        string.append(
            f'If you will spent for enhancement {conv_nice_view(full_price)} silver')
        string.append(
            f'and put on auction hous for {conv_nice_view(auction_price[str(end_lev)])} silver')
        string.append('You will get:')
        temp_worth = (auction_price[str(end_lev)] *
                      0.65 - full_price)
        string.append(
            f'Standart profit (65%)= {conv_nice_view(temp_worth)} silver')
        temp_worth = (auction_price[str(end_lev)] *
                      0.85 - full_price)
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


def Silver_Embroidered_Clothes(adv_valks, begin_lev=0, end_lev=5, tests=1000, item_name='Silver_Embroidered_Sailors_Clothes',
                               show_one_test=False, find_fails=False):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_stone_price = items_prices['Black_Stone_Weapon']
    name_of_item = item_name.replace('_', ' ')

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    crons_amount = item_settings['crons_amount']
    item_grade = item_settings['item_grade']
    soft_cap_fails = item_settings['soft_cap_fails']
    best_failstacks = adv_valks
    auction_price = item_settings['auction_price']
    use_the_same_item = item_settings['use_the_same_item']

    if not find_fails:
        report = enhancement_silv_emb_clothes(begin_lev, end_lev, tests, base_persent,
                                              name_of_item, stuff_price, use_the_same_item,
                                              auction_price, one_fail, best_failstacks,
                                              soft_cap_fails, black_stone_price, show_one_test)
    else:
        if end_lev == 5:
            report = find_silver_pen_fails(begin_lev, end_lev, tests, base_persent,
                                           name_of_item, stuff_price,
                                           one_fail, black_stone_price)
        else:
            report = find_best_fails(begin_lev, end_lev, tests, base_persent,
                                     name_of_item, stuff_price,
                                     one_fail, black_stone_price)
    return report
