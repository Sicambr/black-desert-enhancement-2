import random
import json
from push_info import load_data, load_prices


def find_the_best_fails_collect(item_name, check_lev, tests=1000):
    items_prices = load_prices()
    stuff_price = items_prices[item_name]
    black_stone_price = items_prices['Black_Stone_Armor']

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    crons_amount = item_settings['crons_amount']
    item_grade = item_settings['item_grade']
    soft_cap_fails = item_settings['soft_cap_fails']
    auction_price = item_settings['auction_price']
    use_the_same_item = item_settings['use_the_same_item']

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item['Armor_(White_Blue_Yellow_Grade)'][str(check_lev)]

    report = []

    all_fails_we_got = {}
    attempt = 0
    dis_price = 100000
    while attempt < tests:
        attempt += 1
        begin_lev = check_lev
        fails = 0
        while begin_lev == check_lev:
            chance = ((one_fail[str(fails)])*100)
            if 1 <= random.randint(1, 10000) <= chance:
                if fails < 21:
                    report.append(
                        f'Success! rolled {chance/100}, fails was {fails}')
                else:
                    report.append(
                        f'!!!) Success! rolled {chance/100}, fails was {fails}')
                if fails not in all_fails_we_got:
                    all_fails_we_got[fails] = 1
                else:
                    all_fails_we_got[fails] += 1
                fails = 0
                begin_lev += 1
            else:
                fails += 1
    report.append('WE COULD HAVE:')
    for key in sorted(all_fails_we_got.keys()):
        report.append(f'{key} fails = {all_fails_we_got[key]}')
    return report
