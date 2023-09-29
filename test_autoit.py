import random
import json
from push_info import load_data, load_prices


all_item_settings = json.load(open('big_data_tables.json'))
item_settings = all_item_settings['Armor_(White_Blue_Yellow_Grade)']
end_level = 15
all_fails = list()
graph_fails = dict()


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


difference = get_dif(end_level)
for i in range(10):
    one_upgrade(difference, end_level)
print(sum(all_fails)/10)
for key, value in graph_fails.items():
    if key > 15:
        print(key, value)
