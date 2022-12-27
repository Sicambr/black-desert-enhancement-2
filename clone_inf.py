import json


def add_default_price():
    all_items = json.load(open('default_prices.txt'))
    all_items['Black_Stone_Weapon'] = 160000
    all_items['Black_Stone_Armor'] = 160000
    json.dump(all_items, fp=open('default_prices.txt', 'w'), indent=4)


def add_item():
    item = json.load(open('data.txt'))
    base_persent = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 90, 7: 80, 8: 70, 9: 60,
                    10: 50, 11: 40, 12: 30, 13: 20, 14: 15, 15: 10, 16: 30, 17: 25,
                    18: 20, 19: 15, 20: 6}
    one_fail = 'None'
    ceiling_persent = 'None'
    crons_amount = 'None'
    black_gems = {1: 'BG_1', 2: 'BG_1', 3: 'BG_1', 4: 'BG_1', 5: 'BG_1', 6: 'BG_2',
                  7: 'BG_2', 8: 'BG_2', 9: 'BG_3', 10: 'BG_3', 11: 'BG_3', 12: 'BG_4',
                  13: 'BG_4', 14: 'BG_5', 15: 'BG_5', 16: 'GBG_1', 17: 'GBG_1',
                  18: 'GBG_1', 19: 'GBG_1', 20: 'GBG_1'}
    all_settings = {'base_persent': base_persent,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent,
                    'crons_amount': crons_amount, 'black_gems': black_gems}
    item['RED_CLOTH_Manos_LifeMastery'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


# add_default_price()
add_item()
