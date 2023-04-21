import random
import json
from push_info import load_data, load_prices


def find_fails_whithout_naderr(begin_lev, tests, base_persent,
                               name_of_item, stuff_price,
                               one_fail, black_stone_price, con_black_stone_price,
                               max_fails, best_failstacks, end_lev):

    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        if name_of_item.replace(' ', '_') == 'Green_Grade_Main_Weapon':
            one_fail = item['WEAPON_(Green_Grade)']
        else:
            one_fail = item['RU_SERVER_WEAPON_(Green_Grade)']

    stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
    fails = [0, 0, 0, 0, 0, 0, 0, 10, 10, 15,
             15, 20, 30, 30, 30, 30, 30, 30, 30, 30]
    start_pos = 7
    finish_pos = end_lev - 1
    if begin_lev > 7:
        start_pos = begin_lev - 1
    report = []
    tests = 10000
    report.append(f'WE DID {tests} tests for each case:')
    first_case = True
    best_result = 0
    data_best_result = []
    best_check_fail = 0
    best_attempt_price = 0
    while True:
        for test_fails in range(0, 31, 5):
            fails[start_pos] = test_fails
            attempt = 0
            spent_black_stones = 0
            spent_con_black_stones = 0
            lost_durability = 0
            total_expenses = 0
            while attempt < tests:
                attempt += 1
                collected_fails = 0
                temp_level = begin_lev
                changed_grade = True
                current_fails = 0
                while temp_level < end_lev:
                    if changed_grade:
                        current_fails = fails[temp_level]
                        if temp_level >= 7:
                            spent_black_stones += stone_amount[current_fails]
                    else:
                        current_fails = fails[temp_level] + collected_fails
                    if current_fails > max_fails[str(temp_level + 1)]:
                        current_fails = max_fails[str(temp_level + 1)]
                    chance = (
                        (one_fail[str(temp_level + 1)][str(current_fails)])*100)
                    if 1 <= random.randint(1, 10000) <= chance:
                        changed_grade = True
                        collected_fails = 0
                        if temp_level <= 14:
                            spent_black_stones += 1
                        else:
                            spent_con_black_stones += 1
                        temp_level += 1
                    else:
                        changed_grade = False
                        if temp_level == 15:
                            collected_fails += 2
                            spent_con_black_stones += 1
                            lost_durability += 10
                        elif temp_level == 16:
                            collected_fails += 3
                            spent_con_black_stones += 1
                            lost_durability += 10
                        else:
                            lost_durability += 5
                            spent_black_stones += 1
                            collected_fails += 1
            spent_black_stones /= tests
            spent_con_black_stones /= tests
            spent_items = int((int(lost_durability / 10)) / tests)
            report.append(f'For case: {fails}')
            temp_expenses = int(spent_black_stones) * black_stone_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {int(spent_black_stones)} black stones = {conv_nice_view(temp_expenses)} silver')
            temp_expenses = spent_con_black_stones * con_black_stone_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {spent_con_black_stones} concentrated black stones = {conv_nice_view(temp_expenses)} silver')
            temp_expenses = spent_items * stuff_price
            total_expenses += temp_expenses
            report.append(
                f'Spent {spent_items} items = {conv_nice_view(temp_expenses)} silver')
            report.append(
                f'Total EXPENSES= {conv_nice_view(total_expenses)} silver')
            report.append('')
            if first_case == True:
                best_result = total_expenses
                first_case = False
            if total_expenses <= best_result:
                best_result = total_expenses
                data_best_result.clear()
                data_best_result.append(int(spent_black_stones))
                data_best_result.append(spent_con_black_stones)
                data_best_result.append(spent_items)
                data_best_result.append(total_expenses)
                data_best_result.append(fails.copy())
            if test_fails == 0:
                best_attempt_price = total_expenses
            if total_expenses <= best_attempt_price:
                best_attempt_price = total_expenses
                best_check_fail = test_fails
            print(f'Count position {start_pos}, with {test_fails} fails...')
        if (start_pos == finish_pos) and (fails[start_pos] == 30):
            report.append('')
            report.append('The best case:')
            report.append(f'Spent {data_best_result[0]} black stones')
            report.append(
                f'Spent {data_best_result[1]} concentrated black stones')
            report.append(f'Bought {data_best_result[2]} items')
            report.append(
                f'TOTAL EXPENSES = {conv_nice_view(data_best_result[3])} silver')
            report.append(
                f'Use next fails to get level from +{begin_lev} to +{end_lev}:')
            string = ''
            for number in range(1, 21, 1):
                string = '+' + str(number) + ' = ' + \
                    str(data_best_result[4][number - 1]) + ' fails'
                report.append(string)
            print('Succesfull!')
            break
        fails[start_pos] = best_check_fail
        start_pos += 1
    return report, data_best_result[4].copy(), data_best_result


def standart_enhancement_carrack(end_lev, tests, base_persent, best_failstacks,
                                 name_of_item, one_fail,
                                 max_fails, valks, begin_lev, use_crone, black_stone_price,
                                 stuff_price, eng_language):
    if one_fail == 'into_big_data_table.json':
        item = json.load(open('big_data_tables.json'))
        one_fail = item[name_of_item.replace(' ', '_')]
    stone_amount = {}
    for i in range(350):
        stone_amount[i] = 0
    stone_amount[5], stone_amount[10], stone_amount[15], stone_amount[20] = 5, 12, 21, 33
    stone_amount[25], stone_amount[30] = 53, 84
    # fails = best_failstacks
    fails = valks
    string = []
    tests = 10000
    safety_up = use_crone

    all_expenses = []
    all_enhanc_attempt = {0: 0, 1: 0, 2: 0, 3: 0,
                          4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    attempt = 0
    spent_memory = 0
    spent_sunset_black_stones = 0
    spent_black_stones = 0
    lost_durability = 0
    total_expenses = 0
    rolls = 0
    while attempt < tests:
        attempt += 1
        one_case_black_stones = 0
        one_case_sunset_bs = 0
        one_case_durability = 0
        collected_fails = 0
        temp_level = begin_lev
        current_fails = 0
        changed_grade = 1
        while temp_level < end_lev:
            rolls += 1
            if changed_grade:
                current_fails = fails[temp_level]
                spent_black_stones += stone_amount[current_fails]
                one_case_black_stones += stone_amount[current_fails]
            else:
                current_fails = fails[temp_level] + collected_fails
            if current_fails > max_fails[str(temp_level + 1)]:
                current_fails = max_fails[str(temp_level + 1)]
            chance = (
                (one_fail[str(temp_level + 1)][str(current_fails)])*100)
            if 1 <= random.randint(1, 10000) <= chance:
                changed_grade = True
                collected_fails = 0
                one_case_sunset_bs += 1
                temp_level += 1
                all_enhanc_attempt[temp_level] += 1
            else:
                all_enhanc_attempt[temp_level] += 1
                changed_grade = False
                collected_fails += 1
                one_case_sunset_bs += 1
                lost_durability += 10
                one_case_durability += 10
        one_case_worth = 0
        one_case_worth += one_case_black_stones * black_stone_price
        one_case_worth += int(one_case_durability / 2) * stuff_price
        spent_sunset_black_stones += one_case_sunset_bs
        all_expenses.append(one_case_worth)

    spent_black_stones /= tests
    spent_memory = int((int(lost_durability / 2)) / tests)
    spent_sunset_black_stones = int(spent_sunset_black_stones / tests)

    if eng_language:
        string.append('')
        string.append('<<<FULL REPORT>>>')
        string.append(f'THE RESULT OF {tests} TESTS')
        string.append('')
        string.append(f'Item: {name_of_item}')
        string.append(f'Sharpering from +{begin_lev} to +{end_lev}')
        string.append('')
        string.append('FEATURES:')
        string.append("This item has fail stacks. You may use"
                      " any way to increase them before you will sharp item.")
        string.append(
            "This item don't decrease level after +6 if you will failed.")
        string.append("This item don't use crone stones")
        string.append('')
        string.append('EXPENSES:')
        string.append(f'We have obtained the following averages:')
        temp = int(rolls / tests)
        string.append(f'ROLLED: {temp}')
        string.append(
            'If you will spend 1 second for 1 click, you will do it:')
        string.append(f'{temp} seconds = {int(temp / 60)} minutes '
                      f'= {int(temp / 3600)} hours = {int (temp / 86400)} days.')
        string.append(f'We used next faistacks pattern: {fails}')
        temp_expenses = int(spent_black_stones) * black_stone_price
        total_expenses += temp_expenses
        string.append(
            f'Spent {int(spent_black_stones)} black stones = {conv_nice_view(temp_expenses)} silver')
        string.append(
            f'Spent {spent_sunset_black_stones} sunset black stones = {spent_sunset_black_stones * 500} raven coins:')
        string.append(
            f'      inclide {spent_sunset_black_stones} solar black stones ({spent_sunset_black_stones * 200} raven coins)')
        string.append(
            f'      inclide {spent_sunset_black_stones} lunar black stones ({spent_sunset_black_stones * 300} raven coins)')
        string.append(
            f'      inclide {spent_sunset_black_stones * 10} starlight powder')
        temp_expenses = spent_memory * stuff_price
        total_expenses += temp_expenses
        string.append(
            f'Spent {spent_memory} Memory fragments = {conv_nice_view(temp_expenses)} silver')
        string.append(
            f'Total EXPENSES= {conv_nice_view(total_expenses)} silver')
        string.append('')
        string.append('USEFUL STATISTIC:')
        string.append('We staied on leveles, while did enhancement:')
        for key in all_enhanc_attempt:
            if all_enhanc_attempt[key] != 0 and key != end_lev:
                string.append(
                    f'+{key} : {int(all_enhanc_attempt[key] / tests)} times')
    else:
        string.append('')
        string.append('<<<ПОЛНЫЙ ОТЧЕТ>>>')
        string.append(f'РЕЗУЛЬТАТ {tests} ТЕСТОВ')
        string.append('')
        string.append(f'Предмет: {name_of_item}')
        string.append(f'Заточка с +{begin_lev} до +{end_lev}')
        string.append('')
        string.append('ОСОБЕННОСТИ:')
        string.append("Этот предмет использует систему накапливания фэйлов."
                      " Можете использовать советы валкса или любые другие фэйлы.")
        string.append(
            "Этот предмет не теряет уровень заточки при неудаче с +6 на +10.")
        string.append(
            "Этот предмет не использует камни крон для безопасной точки.")
        string.append('')
        string.append('ЗАТРАТЫ:')
        string.append(f'Мы получили следующие средние результаты по тестам:')
        temp = int(rolls / tests)
        string.append(f'ПОПЫТОК ЗАТОЧИТЬ: {temp}')
        string.append(
            'Если тратить 1 секунду на 1 клик мышкой, то уйдет времени:')
        string.append(f'{temp} секунд = {int(temp / 60)} минут '
                      f'= {int(temp / 3600)} часов = {int (temp / 86400)} дней.')
        string.append(f'Мы использовали модель начальных фэйлов: {fails}')
        temp_expenses = int(spent_black_stones) * black_stone_price
        total_expenses += temp_expenses
        string.append(
            f'Потрачено {int(spent_black_stones)} черный камней = {conv_nice_view(temp_expenses)} серебра')
        string.append(
            f'Потрачено {spent_sunset_black_stones} черных камней зари = {spent_sunset_black_stones * 500} монет ворон:')
        string.append(
            f'      включает {spent_sunset_black_stones} солнечных черных камней ({spent_sunset_black_stones * 200} монет ворон)')
        string.append(
            f'      включает {spent_sunset_black_stones} лунных черных камней ({spent_sunset_black_stones * 300} монет ворон)')
        string.append(
            f'      включает {spent_sunset_black_stones * 10} звездного порошка')
        temp_expenses = spent_memory * stuff_price
        total_expenses += temp_expenses
        string.append(
            f'Потрачено {spent_memory} обрывков воспоминаний = {conv_nice_view(temp_expenses)} серебра')
        string.append(
            f'ИТОГО ЗАТРАТ= {conv_nice_view(total_expenses)} серебра')
        string.append('')
        string.append('ПОЛЕЗНАЯ СТАТИСТИКА:')
        string.append(
            'При данной модели начальных фэйлов, мы делали попытки заточить на уровнях:')
        for key in all_enhanc_attempt:
            if all_enhanc_attempt[key] != 0 and key != end_lev:
                string.append(
                    f'+{key} : {int(all_enhanc_attempt[key] / tests)} раз')

    return string


def conv_nice_view(number):
    if number // 1000000000 > 0:
        number = str(round((number / 1000000000), 3))
        return (number + ' billions')
    elif number // 1000000 > 0:
        number = str(round((number / 1000000), 3))
        return (number + ' millions')
    else:
        return str(number)


def carrack_blue_parts(valks=None, begin_lev=0, end_lev=10, tests=1000, item_name='Carrack_Blue_Gear',
                       show_one_test=False, find_fails=False, use_crone=0):
    eng_language = 0
    items_prices = load_prices()
    black_stone_price = items_prices['Black_Stone_Weapon']
    stuff_price = items_prices['Memory_Fragment']
    name_of_item = item_name.replace('_', ' ')

    item_settings = load_data()[item_name]
    base_persent = item_settings['base_persent']
    one_fail = item_settings['one_fail']
    item_grade = item_settings['item_grade']
    soft_cap_fails = item_settings['soft_cap_fails']
    best_failstacks = item_settings['best_failstacks']
    use_the_same_item = item_settings['use_the_same_item']
    max_fails = item_settings['max_fails']

    if not find_fails:
        report = standart_enhancement_carrack(end_lev, tests, base_persent, best_failstacks,
                                              name_of_item, one_fail,
                                              max_fails, valks, begin_lev, use_crone, black_stone_price,
                                              stuff_price, eng_language)
    else:
        report, new_best_fails, saved_data = find_fails_whithout_naderr(begin_lev, tests, base_persent,
                                                                        name_of_item, sunset_black_stone, one_fail,
                                                                        max_fails, best_failstacks, end_lev)
        # all_data = load_data()
        # all_data[item_name]['best_failstacks'] = new_best_fails
        # json.dump(all_data, fp=open('data.txt', 'w'), indent=4)
    return report
