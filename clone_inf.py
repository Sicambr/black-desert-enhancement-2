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
    all_settings = {'base_persent': base_persent,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent,
                    'crons_amount': crons_amount, 'black_gems': black_gems,
                    'con_black_gems': con_black_gems, 'lost_durability': lost_durability}
    item['RED_CLOTH_Manos_LifeMastery'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


# add_default_price()
add_item()
