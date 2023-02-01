import sys
import life_mastery_cloth
import life_mastery_accessories
import how_collect_fails
import green_weapon
import yellow_weapon
from push_info import load_data
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QComboBox, QWidget, QLineEdit, QRadioButton, QLabel, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


all_items = load_data()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sharpering test for Black Desert")
        self.setMinimumSize(900, 800)

        button = QPushButton("Press Megit!")
        button.clicked.connect(self.the_button_was_clicked)

        self.box_with_items = QComboBox()
        for i in all_items.keys():
            self.box_with_items.addItem(i.replace('_', ' '))

        self.check_method = QGroupBox('Check style:')
        self.check_click = QRadioButton('Click test:')
        self.check_click.setChecked(0)
        self.check_one_tests = QRadioButton('One test:')
        self.check_one_tests.setChecked(0)
        self.check_many_tests = QRadioButton('A lot of tests:')
        self.check_many_tests.setChecked(1)

        layout_with_method = QHBoxLayout()
        layout_with_method.addWidget(self.check_many_tests)
        layout_with_method.addWidget(self.check_one_tests)
        layout_with_method.addWidget(self.check_click)
        self.check_method.setLayout(layout_with_method)

        self.cron_stone_box = QGroupBox(
            'Use cron stone for levels: 18-19, 19-20:')
        self.switcher_cron_no = QRadioButton('No')
        self.space_label_2 = QLabel(' '*85)
        self.switcher_cron_yes = QRadioButton('Yes')
        self.switcher_cron_yes.setChecked(1)

        self.begin_with = QLineEdit('0')
        self.end_with = QLineEdit('17')

        self.apply_button = QPushButton('Apply')
        self.find_failstacks = QPushButton('Find the best failstacks')

        # int_string = list(range(0, 21, 1))
        # str_string = [('+ ' + str[number]) for number in int_string]

        # self.label_3 = QLabel(''.join(str_string))

        self.advices_valks = QLineEdit('Advice of Valks')

        font = QFont("JetBrains Mono", 16)
        self.box_with_items.setFont(font)
        self.space_label_2.setFont(font)
        self.check_method.setFont(font)
        # self.label_3.setFont(font)
        self.begin_with.setFont(font)
        self.cron_stone_box.setFont(font)
        self.end_with.setFont(font)
        self.apply_button.setFont(font)
        self.find_failstacks.setFont(font)
        self.advices_valks.setFont(font)
        self.apply_button.clicked.connect(self.get_full_report)
        self.find_failstacks.clicked.connect(self.find_best_fails)

        self.terminal = QTextEdit('')
        self.terminal.setFontPointSize(16)

        self.box_with_items.activated.connect(self.get_full_report)

        layout_with_cron = QHBoxLayout()
        layout_with_cron.addWidget(self.switcher_cron_yes)
        layout_with_cron.addWidget(self.switcher_cron_no)
        layout_with_cron.addWidget(self.space_label_2)
        self.cron_stone_box.setLayout(layout_with_cron)

        layout = QVBoxLayout()
        layout.addWidget(self.box_with_items)
        layout.addWidget(self.check_method)
        layout.addWidget(self.begin_with)
        layout.addWidget(self.end_with)
        layout.addWidget(self.cron_stone_box)
        layout.addWidget(self.apply_button)
        layout.addWidget(self.find_failstacks)
        layout.addWidget(self.advices_valks)
        # layout.addWidget(self.label_3)
        layout.addWidget(self.terminal)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print("Clicked!")

    def get_full_report(self):
        current_name = self.box_with_items.currentText().replace(' ', '_')
        begin_level = int(self.begin_with.text())
        end_level = int(self.end_with.text())
        repeat_tests = 1000
        check_for_one_test = self.check_one_tests.isChecked()
        check_for_crone = self.switcher_cron_yes.isChecked()
        self.terminal.clear()
        if 'Life_Mastery_Clothes' in current_name:
            if end_level <= 5:
                end_level = 6
                self.end_with.setText('6')
            test_report = life_mastery_cloth.Life_Mastery_Clothes(item_name=current_name,
                                                                  begin_lev=begin_level, end_lev=end_level,
                                                                  tests=repeat_tests, show_one_test=check_for_one_test)
        elif 'Silver_Embroidered' in current_name:
            if end_level > 5:
                end_level = 2
                self.end_with.setText('2')
            advices_of_valks = self.check_valks(current_name)
            test_report = life_mastery_cloth.Silver_Embroidered_Clothes(item_name=current_name, adv_valks=advices_of_valks,
                                                                        begin_lev=begin_level, end_lev=end_level,
                                                                        tests=repeat_tests, show_one_test=check_for_one_test)
        elif 'Accessories_Life_Mastery' in current_name:
            if end_level > 5:
                end_level = 2
                self.end_with.setText('2')
            test_report = life_mastery_accessories.life_mastery_accessories(item_name=current_name,
                                                                            begin_lev=begin_level, end_lev=end_level,
                                                                            tests=repeat_tests, show_one_test=check_for_one_test)

        elif 'Collect_fails_stacks' in current_name:
            if end_level <= 5:
                end_level = 6
                self.end_with.setText('6')
            test_report = how_collect_fails.find_the_best_fails_collect(item_name=current_name, check_lev=15,
                                                                        tests=1000)
        elif ('Green_Grade_Main_Weapon' in current_name) or ('RU_Green_Grade' in current_name):
            if end_level <= 7:
                end_level = 8
                self.end_with.setText('8')
            advices_of_valks = self.check_valks(current_name)
            test_report = green_weapon.Green_Grade_Main_Weapon(item_name=current_name, valks=advices_of_valks,
                                                               begin_lev=begin_level, end_lev=end_level,
                                                               tests=repeat_tests, show_one_test=check_for_one_test,
                                                               find_fails=False)
        elif ('Yellow_Grade_Kzarka' in current_name) or ('Tools_Manos' in current_name):
            if end_level <= 7:
                end_level = 8
                self.end_with.setText('8')
            advices_of_valks = self.check_valks(current_name)
            test_report = yellow_weapon.Yellow_Grade_Main_Weapon(item_name=current_name, valks=advices_of_valks,
                                                                 begin_lev=begin_level, end_lev=end_level,
                                                                 tests=repeat_tests, show_one_test=check_for_one_test,
                                                                 find_fails=False, use_crone=check_for_crone)
        else:
            test_report = 'NOT READY'
        for i in test_report:
            self.terminal.append(i)

    def find_best_fails(self):
        current_name = self.box_with_items.currentText().replace(' ', '_')
        begin_level = int(self.begin_with.text())
        end_level = int(self.end_with.text())
        repeat_tests = 1000
        check_for_one_test = self.check_one_tests.isChecked()
        check_for_crone = self.switcher_cron_yes.isChecked()
        self.terminal.clear()
        if 'Silver_Embroidered' in current_name:
            if end_level > 5:
                end_level = 2
                self.end_with.setText('2')
            test_report = life_mastery_cloth.Silver_Embroidered_Clothes(item_name=current_name,
                                                                        begin_lev=begin_level, end_lev=end_level,
                                                                        tests=repeat_tests, show_one_test=check_for_one_test,
                                                                        find_fails=True)
        elif ('Green_Grade_Main_Weapon' in current_name) or ('RU_Green_Grade' in current_name):
            if end_level <= 7:
                end_level = 8
                self.end_with.setText('8')
            test_report = green_weapon.Green_Grade_Main_Weapon(valks=None, item_name=current_name,
                                                               begin_lev=begin_level, end_lev=end_level,
                                                               tests=repeat_tests, show_one_test=check_for_one_test,
                                                               find_fails=True)
        elif ('Yellow_Grade_Kzarka' in current_name) or ('Tools_Manos' in current_name):
            if end_level <= 7:
                end_level = 8
                self.end_with.setText('8')
            test_report = yellow_weapon.Yellow_Grade_Main_Weapon(valks=None, item_name=current_name,
                                                                 begin_lev=begin_level, end_lev=end_level,
                                                                 tests=repeat_tests, show_one_test=check_for_one_test,
                                                                 find_fails=True, use_crone=check_for_crone)
        else:
            test_report = "NOT READY"

        for i in test_report:
            self.terminal.append(i)

    def check_valks(self, current_name):
        text = self.advices_valks.text()
        if not text.startswith('['):
            self.advices_valks.setText(
                str(all_items[current_name]['best_failstacks']))
        text = self.advices_valks.text()
        list_of_valks = []
        for advice in text.split():
            number = ''
            for digit in advice:
                if digit in '0123456789':
                    number += digit
            list_of_valks.append(int(number))
        return list_of_valks


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
