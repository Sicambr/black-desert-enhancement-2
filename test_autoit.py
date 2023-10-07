import random
import json
from push_info import load_data, load_prices


def get_dif(start_level):
    start_level -= 1
    difference = (item_settings[str(start_level)]['1'] -
                  item_settings[str(start_level)]['0']) * 100000
    return int(difference)


def one_upgrade(difference, end_level, fail_up=1):
    start_level = end_level - 1
    fails = 0
    while True:
        number = random.randint(1, 10000000)
        if item_settings[str(start_level)].get(str(fails)):
            chance = item_settings[str(start_level)][str(fails)] * 100000
        else:
            chance += difference*fail_up
            if chance > 9000000:
                chance = 9000000
        if number <= chance:
            break
        else:
            fails += fail_up
    all_fails.append(fails)
    if fails not in graph_fails:
        graph_fails[fails] = 1
    else:
        graph_fails[fails] += 1


def collect_fails(difference, end_level, rich_fail, expenses, fails=0, fail_up=1):
    start_level = end_level - 1
    while True:
        number = random.randint(1, 10000000)
        if item_settings[str(start_level)].get(str(fails)):
            chance = item_settings[str(start_level)][str(fails)] * 100000
        else:
            chance += difference*fail_up
            if chance > 9000000:
                chance = 9000000
        if end_level >= 16:
            expenses['spent_con_bl_stones'] += 1
        else:
            expenses['spent_bl_stones'] += 1
        if number <= chance:
            expenses['item_up'] += 1
            break
        else:
            fails += fail_up
            stop_iteration = False
            if end_level >= 18:
                expenses['item_down'] += 1
                stop_iteration = True
            if fails >= rich_fail:
                expenses['got_need_fails'] += 1
                stop_iteration = True
            if stop_iteration:
                if end_level >= 16:
                    expenses['lost_dur'] += 10
                else:
                    expenses['lost_dur'] += 5
                break


def get_set_armor(difference, end_level, rich_fail, expenses, fails=0, fail_up=1):
    start_level = end_level - 1
    while True:
        number = random.randint(1, 10000000)
        if item_settings[str(start_level)].get(str(fails)):
            chance = item_settings[str(start_level)][str(fails)] * 100000
        else:
            chance += difference*fail_up
            if chance > 9000000:
                chance = 9000000
        if end_level >= 16:
            expenses['spent_con_bl_stones'] += 1
        else:
            expenses['spent_bl_stones'] += 1
        if number <= chance:
            expenses['item_up'] += 1
            break
        else:
            fails += fail_up
            stop_iteration = False
            if end_level >= 18:
                expenses['item_down'] += 1
                stop_iteration = True
            if fails >= rich_fail:
                expenses['got_need_fails'] += 1
                stop_iteration = True
            if stop_iteration:
                if end_level >= 16:
                    expenses['lost_dur'] += 10
                else:
                    expenses['lost_dur'] += 5
                break


# before +15 -> 1 fail, from 15 to I -> 2 fails, to II - > 3, to III - > 4, to IV - >5, to V - >6


give_fails_armor = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
                    13: 1, 14: 1, 15: 1, 16: 2, 17: 3, 18: 4, 19: 5, 20: 6}
all_item_settings = json.load(open('big_data_tables.json'))
# item_settings = all_item_settings['Armor_(White_Blue_Yellow_Grade)']
item_settings = all_item_settings["RU_SERVER_WEAPON_(Green_Grade)"]
end_level = 20
upgrade_fail = give_fails_armor.get(end_level)
all_fails = list()
graph_fails = dict()
test = 12
price_item = 446600
black_stone_price = 120000
con_black_stone_price = 1790000
expenses = {'item_up': 0, 'item_down': 0, 'got_need_fails': 0, 'lost_dur': 0,
            'spent_bl_stones': 0, 'spent_con_bl_stones': 0}
start_fails = 70
rich_fail = 76

difference = get_dif(end_level)

for i in range(test):
    get_set_armor(difference, end_level,
                  rich_fail, expenses,
                  start_fails, upgrade_fail)
print(f"we have {expenses['got_need_fails']} collected +{rich_fail} fails")
print(f"{expenses['item_up']} items +{end_level}")
print(f"{expenses['item_down']} items +{end_level-2}")
print(f"{expenses['lost_dur']} lost durability")
print(f"{expenses['spent_bl_stones']} black stones, {expenses['spent_con_bl_stones']} con black stones")

# for i in range(test):
# one_upgrade(difference, end_level)
# print(sum(all_fails)/test)
# print(all_fails)
# for j in range(15, max(graph_fails.keys())):
# for key, value in graph_fails.items():
# if key == j:
# print(key, value)
