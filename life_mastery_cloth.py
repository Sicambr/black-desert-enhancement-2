import json
import random
import math


def load_prices():
    items_prices = json.load(open('default_prices.txt'))
    return items_prices


def load_data():
    item_settings = json.load(open('data.txt'))
    return item_settings


def conv_nice_view(number):
    if number // 1000000000 > 0:
        number = str(round((number / 1000000000), 3))
        return (number + ' billions')
    elif number // 1000000 > 0:
        number = str(round((number / 1000000), 3))
        return (number + ' millions')
    else:
        return str(number)


def best_way_restore_dur(item_price, durability, item_grade, memory_fragment_price):
    memory_fr_restore = {'RED': 1, 'YELLOW': 1, 'BLUE': 2, 'GREEN': 5, 'WHITE': 10}
    dur_message = []
    dur_message.append(f'Price for one ITEM on auction house: {item_price} silver')
    dur_message.append(f'One memory fragment will restore {memory_fr_restore[item_grade]} points')
    dur_message.append(f'Worth for 1 durability point with item uses = {round((item_price / 10), 3)} silver')
    dur_message.append(f'Worth for 1 durability point with memore fragment uses '
                        f'= {round(memory_fragment_price / (memory_fr_restore[item_grade]), 3)} silver')
    temp_message = ''
    artisans_memory = 0
    if (item_price / 10) >= (memory_fragment_price / (memory_fr_restore[item_grade])):
        dur_message.append(f'Use {durability} MEMORY FRAGMENTS to restore durability!')
        worth = (memory_fragment_price / memory_fr_restore[item_grade]) * durability
        artisans_memory = math.ceil(durability / 5)
        temp_message = (f'And then use {math.ceil(durability / 5)} memory'
                        f' fragments = {conv_nice_view(worth / 5)} silver')
    else:
        dur_message.append(f'Use {math.ceil(durability / 10)} ITEMs to restore durability!')
        worth = (item_price / 10) * durability
        artisans_memory = math.ceil((durability / 10)/5)
        temp_message = (f'And then use {math.ceil((durability / 10)/5)} items'
                        f' = {conv_nice_view(worth / 5)} silver')
    dur_message.append(f'LOST {durability} points of DURABILITY = {conv_nice_view(worth)} silver')
    dur_message.append(f"Or you can use {artisans_memory} Artisan's Memory")
    dur_message.append(temp_message)
    return (artisans_memory, worth, dur_message)


def enhancement(begin_lev, end_lev, tests, base_persent, lost_durability, black_gems, con_black_gems,
                name_of_item, black_gem_price, con_black_gem_price, item_grade, 
                memory_fragment_price, stuff_price, show_one_test=False):
    spent_durability = 0
    spent_black_gems = 0
    spent_con_black_gems = 0
    temp_begin_lev = begin_lev
    if show_one_test == True:
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
        string.append(f'All price: {conv_nice_view(temp_full_price + worth)} silver')
        string.append(f"With {artisans_memory} Artisan's Memory: {conv_nice_view(temp_full_price + (worth / 5))} silver")
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

    item_settings = load_data()['Manos_Sailing_Life_Mastery_Clothes']
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    ceiling_persent = item_settings['ceiling_persent']
    crons_amount = item_settings['crons_amount']
    black_gems = item_settings['black_gems']
    con_black_gems = item_settings['con_black_gems']
    lost_durability = item_settings['lost_durability']
    item_grade = item_settings['item_grade']
    item_type = item_settings['item_type']

    report = enhancement(begin_lev, end_lev, tests, base_persent,
                         lost_durability, black_gems, con_black_gems,
                         name_of_item, black_gem_price, con_black_gem_price,
                         item_grade, memory_fragment_price, stuff_price, show_one_test)
    return report


# Manos_Life_Mastery_Clothes(show_one_test=True)
