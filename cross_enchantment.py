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


def show_white_stuff_fails():
    item_name = 'Collect_fails_stacks_with_reblath_helmet'
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_stone_price = items_prices['Black_Stone_Armor']

    item_settings = load_data()[item_name]
    one_fail = item_settings['one_fail']

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Armor_(White_Blue_Yellow_Grade)']
        # one_fail = item['Weapons_(Black_Star)']

    stone_amount = dict()
    for i in range(121):
        stone_amount[i] = 0
    stone_amount[5], stone_amount[10], stone_amount[15], stone_amount[20] = 5, 12, 21, 33
    stone_amount[25], stone_amount[30] = 53, 84

    nadera = {num: 0 for num in range(1, 16, 1)}
    all_enh = dict()
    report = list()
    dis_price = 100000
    blacksmiths_secret_book = {20: 1000000, 30: 4000000, 40: 10000000}
    attempt = 0
    spent_con_black_stones = 0
    lost_durability = 0
    want_fails = 230

    tests = 64
    begin_lev = 19
    end_lev = 20

    got_18_back = 0
    got_fails = 0
    rolls = 0

    total_sum = 0

    while attempt < tests:

        one_case_black_stones = 0
        one_case_con_black_stones = 0
        one_case_durability = 0
        one_case_cron_stones = 0
        collected_fails = 100
        temp_level = begin_lev
        changed_grade = True
        current_fails = 0
        for num_nadera in nadera.keys():
            nadera[num_nadera] = 0

        while (temp_level < end_lev) and (attempt < tests):
            rolls += 1
            attempt += 1
            if collected_fails > 350:
                collected_fails = 350
            chance = (
                (one_fail[str(temp_level + 1)][str(collected_fails)])*100)
            if 1 <= random.randint(1, 10000) <= chance:
                changed_grade = True
                if collected_fails <= want_fails:
                    print(
                        f'lost {collected_fails} fails! chance = {chance / 100} %')
                    if collected_fails not in all_enh:
                        all_enh[collected_fails] = 1
                    else:
                        all_enh[collected_fails] += 1
                collected_fails = 0
                spent_con_black_stones += 1
                one_case_con_black_stones += 1
                temp_level += 1
            else:
                changed_grade = False
                if temp_level == 16:
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
                        collected_fails += 4
                        # nadera[1] = collected_fails + 4
                    elif temp_level == 18:
                        collected_fails += 5
                        # nadera[2] = collected_fails + 5
                        if collected_fails >= want_fails:
                            print(f'got {collected_fails} fails!')
                            got_fails += 1
                            temp_level = end_lev
                    elif temp_level == 19:
                        collected_fails += 6
                        print(
                            f'increased {collected_fails} fails. Chance = {chance / 100} %')
                        if collected_fails >= want_fails:
                            print(f'got {collected_fails} fails!')
                            print('try upgrade Manos:')
                            get_manos = False
                            for _ in range(6):
                                if 1 <= random.randint(1, 10000) <= 500:
                                    print('GOT MANOS RING IV!!')
                                    total_sum += 1
                                    get_manos = True
                                    break
                                else:
                                    print('Broked MANOS III')
                            got_fails += 1
                            temp_level = end_lev
                        # nadera[3] = collected_fails + 6
                    if total_sum < 6:
                        attempt = 0

                    lost_durability += 10
                    one_case_durability += 10
                    got_18_back += 1

    all_cases = 0
    num = 0
    for key, item in sorted(all_enh.items()):
        num += 1
        all_cases += item
        print(f'{num}) {key}: {item} ({all_cases})')

    print(f"We got back {got_18_back} stuff +18")
    print(f"We reach {want_fails} fails {got_fails} times")
    print(f'total sum = {total_sum}')
    print(f'{rolls - 64} rolls')


show_white_stuff_fails()
