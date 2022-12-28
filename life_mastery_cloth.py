import json
import random


def load_prices():
    items_prices = json.load(open('default_prices.txt'))
    return items_prices


def load_data():
    item_settings = json.load(open('data.txt'))
    return item_settings


def enhancement(begin_lev, end_lev, tests, base_persent, lost_durability, black_gems, con_black_gems,
                name_of_item, black_gem_price, con_black_gem_price, show_one_test=False):
    spent_durability = 0
    spent_black_gems = 0
    spent_con_black_gems = 0
    if show_one_test == True:
        rolls = 0
        string = ['*** FULL TEST ***', f'ENHANCEMENT: {name_of_item}',
                  f'from {begin_lev} to +{end_lev}']
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
        return string

    else:
        while begin_lev != end_lev:
            spent_black_gems += black_gems[str(begin_lev + 1)]
            spent_con_black_gems += con_black_gems[str(begin_lev + 1)]
            if 1 <= random.randint(1, 10000) <= (base_persent[str(begin_lev + 1)]*100):
                begin_lev += 1

            else:
                spent_durability += lost_durability[str(begin_lev + 1)]


def Manos_Life_Mastery_Clothes(begin_lev=0, end_lev=17, tests=1000, show_one_test=False):
    items_prices = load_prices()
    black_gem_price = items_prices['Black_Gem']
    con_black_gem_price = items_prices['Concentrated_Black_Gem']
    stuff_price = items_prices['Manos_Sailing_Life_Mastery_Clothes']
    name_of_item = 'Sailing Life Mastery Clothes of Manos'
    memory_fragment_price = items_prices['Memory_Fragment']

    item_settings = load_data()['RED_CLOTH_Manos_LifeMastery']
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    ceiling_persent = item_settings['ceiling_persent']
    crons_amount = item_settings['crons_amount']
    black_gems = item_settings['black_gems']
    con_black_gems = item_settings['con_black_gems']
    lost_durability = item_settings['lost_durability']

    string = enhancement(begin_lev, end_lev, tests, base_persent,
                         lost_durability, black_gems, con_black_gems,
                         name_of_item, black_gem_price, con_black_gem_price,
                         show_one_test)
    return string


# Manos_Life_Mastery_Clothes(show_one_test=True)
