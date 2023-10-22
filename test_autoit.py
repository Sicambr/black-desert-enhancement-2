import random
import json
from push_info import load_data, load_prices


def count_sil(number):
    line = ''
    if number % 1000000000 > 1:
        line = str(round(number / 1000000000, 2)) + ' billions silver'
    else:
        line = str(round(number / 1000000000, 2)) + ' millions silver'
    return line


def get_dif(item_settings, end_level):
    difference = (item_settings[str(end_level)]['1'] -
                  item_settings[str(end_level)]['0']) * 100000
    # print('\ndif = ', difference/100000)
    return int(difference)


def create_file(file_name, report):
    with open(file_name, 'w', encoding='UTF-8') as file:
        file.writelines(report)


def one_upgrade(item_settings, difference, data, expenses, fail_up=1):
    while True:
        number = random.randint(1, 10000000)
        if item_settings[str(data['end_level'])].get(str(data['fails'])):
            data['chance'] = item_settings[str(
                data['end_level'])][str(data['fails'])] * 100000
        else:
            data['chance'] += difference*fail_up
            if data['chance'] > 9000000:
                data['chance'] = 9000000
        if data['end_level'] >= 16:
            expenses['spent_con_bl_stones'] += 1
        else:
            expenses['spent_bl_stones'] += 1
        if number <= data['chance']:
            expenses['item_up'] += 1
            data['fails'] = data['start_fails']
            data['chance'] = max(
                item_settings[str(data['end_level'])].values()) * 100000
            break
        else:
            data['fails'] += fail_up
            stop_iteration = False
            if data['end_level'] >= 18:
                expenses['item_down'] += 1
                stop_iteration = True
            if data['fails'] >= data['purpose_fail']:
                expenses['got_need_fails'] += 1
                stop_iteration = True
                data['fails'] = data['start_fails']
            if data['end_level'] >= 16:
                expenses['lost_dur'] += 10
            else:
                expenses['lost_dur'] += 5
            if stop_iteration:
                break


def get_set_armor(item_settings, difference, data, expenses, report, all_items,
                  all_fails, every_level_fails, saved_fails, fail_up=1):
    while True:
        expenses['rolls'] += 1
        number = random.randint(1, 10000000)
        if saved_fails[data['start_level']] != 0:
            data['fails'] = saved_fails[data['start_level']]
        else:

            data['fails'] = every_level_fails[data['start_level']]
        if item_settings[str(data['end_level'])].get(str(data['fails'])):
            data['chance'] = item_settings[str(
                data['end_level'])][str(data['fails'])] * 100000
        else:
            data['chance'] += difference*fail_up
            if data['chance'] > 9000000:
                data['chance'] = 9000000
        if data['end_level'] >= 16:
            expenses['spent_con_bl_stones'] += 1
        else:
            expenses['spent_bl_stones'] += 1
        if number <= data['chance']:
            expenses['item_up'] += 1
            all_items[data['end_level']] += 1
            all_items[data['start_level']] -= 1
            report.append(
                f"GOT ITEM +{data['end_level']} with {data['fails']} fails, chance = {data['chance']/100000}%\n")
            data['chance'] = max(
                item_settings[str(data['end_level'])].values()) * 100000
            if saved_fails[data['start_level']] != 0:
                saved_fails[data['start_level']] = 0
            else:
                all_fails[data['fails']] -= 1
            break
        else:
            data['fails'] += fail_up
            stop_iteration = False
            if saved_fails[data['start_level']] == 0:
                all_fails[data['start_fails']] -= 1
            if data['end_level'] >= 18:
                expenses['item_down'] += 1
                all_items[data['start_level']-1] += 1
                all_items[data['end_level']-1] -= 1
                report.append(f"more +{data['start_level']-1} items\n")
                stop_iteration = True
            saved_fails[data['start_level']] = data['fails']
            if data['fails'] >= data['purpose_fail']:
                saved_fails[data['start_level']] = 0
                data['purpose_fail'] = data['fails']
                every_level_fails[data['end_level']] = data['fails']
                expenses['got_need_fails'] += 1
                if data['fails'] not in all_fails:
                    all_fails[data['fails']] = 1
                else:
                    all_fails[data['fails']] += 1
                stop_iteration = True
                report.append(f"roll with {(data['fails']-fail_up)} fails, "
                              f"chance = {data['chance']/100000}% SUCCESS! (REACHED {data['fails']} fails)\n")
                report.append(f"ADD {data['fails']} FAILS to the STORE\n")
            else:
                report.append(f"roll with {(data['fails']-fail_up)} fails, "
                              f"chance = {data['chance']/100000}% MISSED (got {data['fails']})\n")
                saved_fails[data['start_level']] = data['fails']
            if data['end_level'] >= 16:
                expenses['lost_dur'] += 10
            else:
                expenses['lost_dur'] += 5
            if stop_iteration:
                break

# before +15 -> 1 fail, from 15 to I -> 2 fails, to II - > 3, to III - > 4, to IV - >5, to V - >6
# every_level_fails = {14: 0, 15: 10, 16: 23,
#                      17: 32, 18: 44, 19: 64, 20: 112}


def main_creator():
    # MAIN SETTINGS
    start_level = 16
    start_fail = 20
    every_level_fails = {14: 0, 15: 10, 16: start_fail,
                         17: 26, 18: 42, 19: 82, 20: 112}
    amount_of_100_fails = 10  # for item level +20
    all_items = {14: 0, 15: 0, 16: 100, 17: 0, 18: 0, 19: 0, 20: 0}
    all_fails = {start_fail: 200000}

    # COMMON SETTINGS
    all_item_settings = json.load(open('big_data_tables.json'))
    # item_settings = all_item_settings['Armor_(White_Blue_Yellow_Grade)']
    item_settings = all_item_settings["RU_SERVER_WEAPON_(Green_Grade)"]
    saved_fails = {16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
    full_expenses = list()
    price_item = 446600
    fragments_mem_price = 3000000
    price_level20_item = 2600000000
    # price_level20_item = 13000000000
    black_stone_price = 120000
    con_black_stone_price = 1790000  # weapon
    # con_black_stone_price = 1190000 # armor
    report = list()
    give_fails_armor = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
                        13: 1, 14: 1, 15: 1, 16: 2, 17: 3, 18: 4, 19: 5, 20: 6}
    expenses = {'item_up': 0, 'item_down': 0, 'got_need_fails': 0, 'lost_dur': 0,
                'spent_bl_stones': 0, 'spent_con_bl_stones': 0, 'rolls': 0}
    data = {'start_fails': 0, 'fails': 0, 'purpose_fail': 10,
            'end_level': 17, 'start_level': start_level, 'chance': 0}

    while True:
        report.append(f"+{data['start_level']} >> +{data['end_level']}\n")
        difference = get_dif(item_settings, data['end_level'])
        upgrade_fail = give_fails_armor.get(data['end_level'])
        data['start_fails'] = every_level_fails.get(data['start_level'])
        data['fails'] = every_level_fails.get(data['start_level'])
        data['purpose_fail'] = every_level_fails.get(data['end_level'])
        get_set_armor(item_settings, difference, data, expenses, report, all_items, all_fails,
                      every_level_fails, saved_fails, upgrade_fail)
        report.append(f"All items: {str(all_items)} \n")
        report.append(f"STORE: {str(all_fails)} \n")
        report.append(f"Hold fails: {str(saved_fails)} \n")
        try:
            while True:
                if (all_items[data['end_level']] > 0) and ((saved_fails[data['end_level']] != 0) or ((every_level_fails[data['end_level']] in all_fails) and (all_fails[every_level_fails[data['end_level']]] > 0))) and (data['end_level'] != 20):
                    data['start_level'] += 1
                    data['end_level'] += 1
                    report.append(f"LEVEL UP to {data['start_level']} level\n")
                elif (all_items[data['start_level']] <= 0) or (saved_fails[data['start_level']] == 0 and ((every_level_fails[data['start_level']] in all_fails) and (all_fails[every_level_fails[data['start_level']]] == 0))):
                    data['start_level'] -= 1
                    data['end_level'] -= 1
                    report.append(
                        f"LEVEL DOWN to {data['start_level']} level\n")
                else:
                    break
        except:
            print('we had Exception!!!')
            break
        report.append('\n')
        if all_fails.get(every_level_fails[20]) == amount_of_100_fails:
            break
    print('LOST DURABILITY: ')
    full_expenses.append((expenses['lost_dur'] / 10) * price_item)
    # full_expenses.append(expenses['lost_dur'] * fragments_mem_price)
    print(
        f"{expenses['lost_dur']} points = -{count_sil(full_expenses[0])} (1 item price = {price_item} silver)")
    print('USED:')
    full_expenses.append(black_stone_price * expenses['spent_bl_stones'])
    print(
        f"{expenses['spent_bl_stones']} black stones = -{count_sil(full_expenses[1])}")
    full_expenses.append(con_black_stone_price *
                         expenses['spent_con_bl_stones'])
    print(
        f"{expenses['spent_con_bl_stones']} con black stones = -{count_sil(full_expenses[2])}")
    print('SOLD +20 items:')
    full_expenses.append(price_level20_item * all_items[20] * 0.85)
    print(f"{all_items[20]} stuff = +{count_sil(full_expenses[3])}")
    full_expenses[3] = full_expenses[3] * -1
    print(f"TOTAL EXPENSES: -{count_sil(sum(full_expenses))}")
    print("FAIL'S MODEL:", every_level_fails)
    print('ITEMS:')
    print(all_items)
    print('SAVED FAILS:')
    print(saved_fails)
    print('FAILS:')
    print(all_fails)
    print(f"Rolled {expenses['rolls']} clicks")
    return report


def one_test(start_fail=0, purpose_fail=10, test=100, start_lev=16, end_lev=17):
    all_item_settings = json.load(open('big_data_tables.json'))
    item_settings = all_item_settings['Armor_(White_Blue_Yellow_Grade)']
    # item_settings = all_item_settings["RU_SERVER_WEAPON_(Green_Grade)"]
    report = list()
    give_fails_armor = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
                        13: 1, 14: 1, 15: 1, 16: 2, 17: 3, 18: 4, 19: 5, 20: 6}
    expenses = {'item_up': 0, 'item_down': 0, 'got_need_fails': 0, 'lost_dur': 0,
                'spent_bl_stones': 0, 'spent_con_bl_stones': 0, 'rolls': 0}
    data = {'start_fails': start_fail, 'fails': start_fail, 'purpose_fail': purpose_fail,
            'end_level': end_lev, 'start_level': start_lev, 'chance': 0}
    difference = get_dif(item_settings, data['end_level'])
    upgrade_fail = give_fails_armor.get(data['end_level'])
    for i in range(test):
        one_upgrade(item_settings, difference, data,
                    expenses, upgrade_fail)
    print('start >', data['start_fails'],
          'fails. End >', data['purpose_fail'], 'fails')
    print(
        f"we have {expenses['got_need_fails']} collected +{data['purpose_fail']} fails")
    print(f"{expenses['item_up']} items +{data['end_level']}")
    print(f"{expenses['item_down']} items +{data['end_level']-2}")
    print(f"{expenses['lost_dur']} lost durability")
    print(
        f"{expenses['spent_bl_stones']} black stones, {expenses['spent_con_bl_stones']} con black stones")
    return report


# report = one_test(start_fail=22, purpose_fail=42,
#                  test=10000, start_lev=17, end_lev=18)
report = main_creator()
# create_file('report.txt', report)
