import random
import json
from push_info import load_data, load_prices


all_item_settings = json.load(open('big_data_tables.json'))
item_settings = all_item_settings['Armor_(White_Blue_Yellow_Grade)']
start_level = 8

def get_dif(start_level):
    difference = (item_settings[str(start_level)]['1'] - 
                  item_settings[str(start_level)]['0']) * 100000
    return int(difference)

def one_upgrade(difference, start_level, fail_up = 1):
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
            print('ok')
            break
        else:
            fails += fail_up
            print(f'fails {fails}, chance {chance / 100000}')


difference = get_dif(start_level)
one_upgrade(difference, start_level)