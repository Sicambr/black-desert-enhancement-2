import json
import random


def load_prices():
    items_prices = json.load(open('default_prices.txt'))
    return items_prices


def load_data():
    item_settings = json.load(open('data.txt'))
    return item_settings


def enhancement(begin_lev, end_lev, tests, base_persent, lost_durability, black_gems, con_black_gems):
    spent_durability = 0
    spent_black_gems = 0
    spent_con_black_gems = 0
    while begin_lev != end_lev:
        if 1 <= random.randint(1, 10000) <= (base_persent[str(begin_lev + 1)]*100):
            begin_lev += 1
            spent_black_gems += black_gems[str(begin_lev + 1)]
            spent_con_black_gems += con_black_gems[str(begin_lev + 1)]
        else:
            spent_durability += lost_durability[str(begin_lev + 1)]
            spent_black_gems += black_gems[str(begin_lev + 1)]
            spent_con_black_gems += con_black_gems[str(begin_lev + 1)]
    print(spent_durability, spent_black_gems, spent_con_black_gems)


def Manos_Life_Mastery_Clothes(begin_lev=0, end_lev=17, tests=1000):
    items_prices = load_prices()
    black_gem_price = items_prices['Black_Gem']
    con_black_gem_price = items_prices['Concentrated_Black_Gem']
    stuff_price = items_prices['Manos_Sailing_Life_Mastery_Clothes']
    memory_fragment_price = items_prices['Memory_Fragment']

    item_settings = load_data()['RED_CLOTH_Manos_LifeMastery']
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    ceiling_persent = item_settings['ceiling_persent']
    crons_amount = item_settings['crons_amount']
    black_gems = item_settings['black_gems']
    con_black_gems = item_settings['con_black_gems']
    lost_durability = item_settings['lost_durability']

    enhancement(begin_lev, end_lev, tests, base_persent,
                lost_durability, black_gems, con_black_gems)


Manos_Life_Mastery_Clothes(begin_lev=13)
