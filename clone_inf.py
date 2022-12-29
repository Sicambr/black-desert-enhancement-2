import json


def add_default_price():
    all_items = json.load(open('default_prices.txt'))
    all_items['Manos_Fishing_Life_Mastery_Clothes'] = 210000000
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
    auction_price = {1: 210000000, 2: 210000000, 3: 210000000, 4: 210000000, 5: 210000000,
                     6: 219000000, 7: 219000000, 8: 219000000, 9: 219000000, 10: 219000000,
                     11: 219000000, 12: 219000000, 13: 256000000, 14: 356000000, 15: 740000000,
                     16: 855000000, 17: 990000000, 18: 1660000000, 19: 4980000000, 20: 37600000000}
    item_grade = 'RED'
    item_type = 'CLOTH_Life_Mastery'
    all_settings = {'base_persent': base_persent,
                    'one_fail': one_fail, 'ceiling_persent': ceiling_persent,
                    'crons_amount': crons_amount, 'black_gems': black_gems,
                    'con_black_gems': con_black_gems, 'lost_durability': lost_durability,
                    'auction_price': auction_price, 'item_grade': item_grade, 'item_type': item_type}
    item['Manos_Fishing_Life_Mastery_Clothes'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


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
    item['Loggia_Processing_Life_Mastery_Clothes'] = all_settings
    json.dump(item, fp=open('data.txt', 'w'), indent=4)


add_default_price()
add_item_manos()
# add_item_loggia()
