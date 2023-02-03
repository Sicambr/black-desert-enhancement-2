import json


def load_prices():
    items_prices = json.load(open('default_prices.txt'))
    return items_prices


def load_data():
    item_settings = json.load(open('data.txt'))
    return item_settings


def add_default_price():
    all_items = json.load(open('default_prices.txt'))
    all_items['RU_Green_Grade_Krea_Longsword_Weapon'] = 765000
    json.dump(all_items, fp=open('default_prices.txt', 'w'), indent=4)


def add_item_manos():
    item = json.load(open('data.txt'))
    base_persent = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 90, 7: 80, 8: 70, 9: 60,
                    10: 50, 11: 40, 12: 30, 13: 20, 14: 15, 15: 10, 16: 30, 17: 25,
                    18: 20, 19: 15, 20: 6}
    one_fail = 'None'
    ceiling_persent = 'None'
    crons_amount = 'None'
    black_gems = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2,
                  7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 4,
                  13: 4, 14: 5, 15: 5, 16: 0, 17: 0,
                  18: 0, 19: 0, 20: 0}
    con_black_gems = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                      7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0,
                      13: 0, 14: 0, 15: 0, 16: 1, 17: 1,
                      18: 1, 19: 1, 20: 1}
    lost_durability = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 5, 7: 5, 8: 5, 9: 5,
                       10: 5, 11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 10, 17: 10,
                       18: 10, 19: 10, 20: 10}
    auction_price = {1: 174000000, 2: 174000000, 3: 174000000, 4: 174000000, 5: 174000000,
                     6: 199000000, 7: 199000000, 8: 199000000, 9: 199000000, 10: 199000000,
                     11: 199000000, 12: 199000000, 13: 199000000, 14: 210000000, 15: 595000000,
                     16: 855000000, 17: 990000000, 18: 1660000000, 19: 4980000000, 20: 56000000000}
    item_grade = 'RED'
    item_type = 'CLOTH_Life_Mastery'
    all_settings = {'base_persent': base_persent,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent,
                    'crons_amount': crons_amount, 'black_gems': black_gems,
                    'con_black_gems': con_black_gems, 'lost_durability': lost_durability,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type}
    item['Manos_Alchemy_Life_Mastery_Clothes'] = all_settings
    sort_keys = sorted(item.keys())
    new_item = {}
    for i in sort_keys:
        new_item[i] = item[i]
    json.dump(new_item, fp=open('data.txt', 'w'), indent=4)


def add_item_loggia():
    item = json.load(open('data.txt'))
    base_persent = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 90, 7: 80, 8: 70, 9: 60,
                    10: 50, 11: 45, 12: 40, 13: 35, 14: 30, 15: 20, 16: 50, 17: 40,
                    18: 30, 19: 20, 20: 10}
    one_fail = 'None'
    ceiling_persent = 'None'
    crons_amount = 'None'
    black_gems = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
                  7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
                  13: 1, 14: 1, 15: 1, 16: 0, 17: 0,
                  18: 0, 19: 0, 20: 0}
    con_black_gems = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                      7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0,
                      13: 0, 14: 0, 15: 0, 16: 1, 17: 1,
                      18: 1, 19: 1, 20: 1}
    lost_durability = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 5, 7: 5, 8: 5, 9: 5,
                       10: 5, 11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 10, 17: 10,
                       18: 10, 19: 10, 20: 10}
    auction_price = {1: 820000, 2: 820000, 3: 820000, 4: 820000, 5: 820000,
                     6: 5750000, 7: 5750000, 8: 5750000, 9: 5750000, 10: 10700000,
                     11: 10700000, 12: 10700000, 13: 18100000, 14: 18100000, 15: 18100000,
                     16: 45100000, 17: 61500000, 18: 135000000, 19: 381000000, 20: 1210000000}
    item_grade = 'GREEN'
    item_type = 'CLOTH_Life_Mastery'
    all_settings = {'base_persent': base_persent,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent,
                    'crons_amount': crons_amount, 'black_gems': black_gems,
                    'con_black_gems': con_black_gems, 'lost_durability': lost_durability,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type}
    item['Loggia_Cooking_Life_Mastery_Clothes'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


def add_item_geranoa():
    item = json.load(open('data.txt'))
    base_persent = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 90, 7: 80, 8: 70, 9: 60,
                    10: 50, 11: 45, 12: 40, 13: 35, 14: 30, 15: 20, 16: 35, 17: 30,
                    18: 25, 19: 20, 20: 8}
    one_fail = 'None'
    ceiling_persent = 'None'
    crons_amount = 'None'
    black_gems = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
                  7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
                  13: 1, 14: 1, 15: 1, 16: 0, 17: 0,
                  18: 0, 19: 0, 20: 0}
    con_black_gems = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                      7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0,
                      13: 0, 14: 0, 15: 0, 16: 1, 17: 1,
                      18: 1, 19: 1, 20: 1}
    lost_durability = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 5, 7: 5, 8: 5, 9: 5,
                       10: 5, 11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 10, 17: 10,
                       18: 10, 19: 10, 20: 10}
    auction_price = {1: 8200000, 2: 8200000, 3: 8200000, 4: 8200000, 5: 8200000,
                     6: 13200000, 7: 13200000, 8: 13200000, 9: 13200000, 10: 24600000,
                     11: 24600000, 12: 24600000, 13: 44200000, 14: 54500000, 15: 70000000,
                     16: 94000000, 17: 127000000, 18: 250000000, 19: 740000000, 20: 2790000000}
    item_grade = 'BLUE'
    item_type = 'CLOTH_Life_Mastery'
    all_settings = {'base_persent': base_persent,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent,
                    'crons_amount': crons_amount, 'black_gems': black_gems,
                    'con_black_gems': con_black_gems, 'lost_durability': lost_durability,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type}
    item['Geranoa_Alchemy_Life_Mastery_Clothes'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


def add_item_Silver_Embroidered_Clothes():
    item = json.load(open('data.txt'))
    base_persent = {1: 30, 2: 10, 3: 7.5, 4: 2.5, 5: 0.5}
    one_fail = {1: [72, 3, 90, 0.6], 2: [50, 1, 66, 0.2], 3: [40.5, 0.75, 51.9, 0.15],
                4: [30, 0.25, 30.5, 0.05], 5: [6.5, 0.05]}
    best_failstacks = [10, 20, 30, 30, 30]
    soft_cap_fails = {1: 14, 2: 40, 3: 44, 4: 110, 5: 120}
    ceiling_persent = 'None'
    crons_amount = 'None'
    use_the_same_item = True
    auction_price = {1: 4160000, 2: 15200000,
                     3: 146000000, 4: 1300000000, 5: 4890000000}
    item_grade = 'BLUE'
    item_type = 'CLOTH_Silver_Embroidered'
    all_settings = {'base_persent': base_persent, 'best_failstacks': best_failstacks,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent, 'soft_cap_fails': soft_cap_fails,
                    'crons_amount': crons_amount, 'use_the_same_item': use_the_same_item,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type}
    item['Silver_Embroidered_Sailors_Clothes'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


def add_item_life_mastery_accessories():
    item = json.load(open('data.txt'))
    base_persent = {1: 70, 2: 45, 3: 30, 4: 15, 5: 5}
    one_fail = 'None'
    ceiling_persent = 'None'
    crons_amount = 'None'
    use_the_same_item = None
    black_gems = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    con_black_gems = {1: 10, 2: 11, 3: 13, 4: 16, 5: 20}
    auction_price = {1: 166000000, 2: 750000000,
                     3: 2730000000, 4: 15700000000, 5: 140000000000}
    item_grade = 'RED'
    item_type = 'ACCESSORIES_Life_Mastery'
    all_settings = {'base_persent': base_persent, 'con_black_gems': con_black_gems,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent, 'black_gems': black_gems,
                    'crons_amount': crons_amount, 'use_the_same_item': use_the_same_item,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type}
    item['Accessories_Life_Mastery_Manos_Belt'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


def add_item_militia_longsword():
    item = json.load(open('data.txt'))
    base_persent = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 70, 7: 25.64, 8: 17.24, 9: 11.76, 10: 7.69,
                    11: 6.25, 12: 5, 13: 4, 14: 2.86, 15: 2, 16: 11.76, 17: 7.69, 18: 6.25, 19: 2, 20: 0.3}
    one_fail = 'into_big_data_table.json'
    best_failstacks = [0] * 20
    soft_cap_fails = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 15, 7: 54, 8: 88, 9: 120,
                      10: 120, 11: 120, 12: 120, 13: 120, 14: 120, 15: 120,
                      16: 50, 17: 82, 18: 102, 19: 120, 20: 120}
    ceiling_persent = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 90, 7: 90, 8: 90, 9: 87.02,
                       10: 76.59, 11: 72.25, 12: 65, 13: 52, 14: 37.18, 15: 26,
                       16: 87.02, 17: 76.59, 18: 72.25, 19: 26, 20: 3.9}
    crons_amount = 'None'
    use_the_same_item = False
    auction_price = 'None'
    item_grade = 'WHITE'
    item_type = 'ARMOR_White_Armor'
    all_settings = {'base_persent': base_persent, 'best_failstacks': best_failstacks,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent, 'soft_cap_fails': soft_cap_fails,
                    'crons_amount': crons_amount, 'use_the_same_item': use_the_same_item,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type}
    item['Collect_fails_stacks_with_reblath_helmet'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


def add_green_weapon():
    item = json.load(open('data.txt'))
    base_persent = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 70, 9: 40.82, 10: 28.58,
                    11: 20, 12: 13.34, 13: 8, 14: 7.5, 15: 6, 16: 11.76, 17: 7.69, 18: 6.25, 19: 2, 20: 0.3}
    one_fail = 'into_big_data_table.json'
    best_failstacks = [0] * 20
    max_fails = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 15,
                 9: 29, 10: 50, 11: 55, 12: 50, 13: 120, 14: 120, 15: 120,
                 16: 120, 17: 120, 18: 120, 19: 120, 20: 120}
    black_stone = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
                   7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
                   13: 1, 14: 1, 15: 1, 16: 0, 17: 0,
                   18: 0, 19: 0, 20: 0}
    con_black_stone = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                       7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0,
                       13: 0, 14: 0, 15: 0, 16: 1, 17: 1,
                       18: 1, 19: 1, 20: 1}
    soft_cap_fails = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 15, 9: 29,
                      10: 15, 11: 25, 12: 40, 13: 78, 14: 80, 15: 100,
                      16: 50, 17: 82, 18: 103, 19: 120, 20: 120}
    ceiling_persent = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 90, 9: 90,
                       10: 90, 11: 82, 12: 73.37, 13: 77.13, 14: 78.3, 15: 70,
                       16: 87.02, 17: 76.59, 18: 72.75, 19: 26, 20: 3.9}
    crons_amount = {18: 19, 19: 37, 20: 69}
    lost_durability = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 5, 7: 5, 8: 5, 9: 5,
                       10: 5, 11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 10, 17: 10,
                       18: 10, 19: 10, 20: 10}
    auction_price = {1: 51500, 2: 51500, 3: 51500, 4: 51500, 5: 51500,
                     6: 51500, 7: 51500, 8: 2680000, 9: 2680000, 10: 2680000,
                     11: 4160000, 12: 4160000, 13: 12600000, 14: 12600000, 15: 12600000,
                     16: 53000000, 17: 127000000, 18: 204000000, 19: 360000000, 20: 775000000}
    use_the_same_item = False
    item_grade = 'GREEN'
    item_type = 'WEAPON_Green_Weapon'
    all_settings = {'base_persent': base_persent, 'best_failstacks': best_failstacks,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent, 'soft_cap_fails': soft_cap_fails,
                    'crons_amount': crons_amount, 'use_the_same_item': use_the_same_item,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type,
                    'lost_durability': lost_durability, 'black_stone': black_stone,
                    'con_black_stone': con_black_stone, 'max_fails': max_fails}
    item['RU_Green_Grade_Krea_Longsword_Weapon'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


def add_yellow_weapon():
    item = json.load(open('data.txt'))
    base_persent = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 70, 9: 20.41, 10: 14.29,
                    11: 10, 12: 6.67, 13: 4, 14: 2.5, 15: 2, 16: 11.76, 17: 7.69, 18: 6.25, 19: 2, 20: 0.3}
    one_fail = 'into_big_data_table.json'
    best_failstacks = [0] * 20
    max_fails = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 15,
                 9: 71, 10: 109, 11: 120, 12: 120, 13: 120, 14: 120, 15: 120,
                 16: 120, 17: 120, 18: 120, 19: 120, 20: 250}
    black_stone = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
                   7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
                   13: 1, 14: 1, 15: 1, 16: 0, 17: 0,
                   18: 0, 19: 0, 20: 0}
    con_black_stone = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                       7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0,
                       13: 0, 14: 0, 15: 0, 16: 1, 17: 1,
                       18: 1, 19: 1, 20: 1}
    soft_cap_fails = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 15, 9: 71,
                      10: 109, 11: 120, 12: 120, 13: 120, 14: 120, 15: 120,
                      16: 50, 17: 82, 18: 102, 19: 120, 20: 120}
    ceiling_persent = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 90, 9: 90,
                       10: 90, 11: 82, 12: 73.37, 13: 52, 14: 32.5, 15: 26,
                       16: 87.02, 17: 76.59, 18: 72.25, 19: 26, 20: 3.9}
    crons_amount = {18: 34, 19: 127, 20: 549}
    lost_durability = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 5, 7: 5, 8: 5, 9: 5,
                       10: 5, 11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 10, 17: 10,
                       18: 10, 19: 10, 20: 10}
    auction_price = {1: 110000000, 2: 110000000, 3: 110000000, 4: 110000000, 5: 110000000,
                     6: 110000000, 7: 110000000, 8: 249000000, 9: 249000000, 10: 249000000,
                     11: 291000000, 12: 291000000, 13: 383000000, 14: 403000000, 15: 580000000,
                     16: 675000000, 17: 785000000, 18: 1100000000, 19: 2420000000, 20: 12400000000}
    use_the_same_item = False
    item_grade = 'RED'
    item_type = 'TOOLS_Life_Mastery_Manos'
    all_settings = {'base_persent': base_persent, 'best_failstacks': best_failstacks,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent, 'soft_cap_fails': soft_cap_fails,
                    'crons_amount': crons_amount, 'use_the_same_item': use_the_same_item,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type,
                    'lost_durability': lost_durability, 'black_stone': black_stone,
                    'con_black_stone': con_black_stone, 'max_fails': max_fails}
    item['Tools_Manos_Butcher_Knife'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


def convert_to_normal_database(file_way):
    first_conv = [line.strip()
                  for line in open(file_way)]
    normal_data_view = {}
    for i in range(1, 8):
        normal_data_view[str(i)] = {0: 100}
    current_level = ''
    number = 0
    for item in first_conv:
        if item.startswith('+'):
            normal_data_view[item[1:]] = {}
            current_level = item[1:]
            number = 0
        else:
            normal_data_view[current_level][number] = round(
                float(item[:-1].replace(',', '.')), 2)
            number += 1
    return normal_data_view


def add_item_to_big_data_tables():
    file_way = 'C:/Users/cnc/Desktop/111.txt'
    stuff = 'Weapons_(White_Blue_Yellow Grade)'
    table_fails_stacks = convert_to_normal_database(file_way)
    item = json.load(open('big_data_tables.json'))
    item[stuff] = table_fails_stacks
    json.dump(item, fp=open('big_data_tables.json', 'w'), indent=4)


# add_item_manos()
# add_item_loggia()
# add_item_geranoa()
# add_item_Silver_Embroidered_Clothes()
# add_item_life_mastery_accessories()
# add_item_militia_longsword()
# convert_to_normal_database()
# add_item_militia_longsword()

# add_item_to_big_data_tables()
# add_default_price()
# add_green_weapon()
# add_yellow_weapon()
