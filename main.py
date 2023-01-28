import sys
import life_mastery_cloth
import life_mastery_accessories
import how_collect_fails
import green_weapon
import yellow_weapon
from push_info import load_data
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtWidgets import QComboBox, QWidget, QLineEdit, QRadioButton
from PyQt5.QtGui import QFont


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

        self.switchers = QRadioButton()
        self.switchers.setChecked(0)

        self.begin_with = QLineEdit('0')
        self.end_with = QLineEdit('17')

        self.apply_button = QPushButton('Apply')
        self.find_failstacks = QPushButton('Find the best failstacks')

        self.advices_valks = QLineEdit('Advice of Valks')

        font = QFont("JetBrains Mono", 16)
        self.box_with_items.setFont(font)
        self.begin_with.setFont(font)
        self.end_with.setFont(font)
        self.apply_button.setFont(font)
        self.find_failstacks.setFont(font)
        self.advices_valks.setFont(font)
        self.apply_button.clicked.connect(self.get_full_report)
        self.find_failstacks.clicked.connect(self.find_best_fails)

        self.terminal = QTextEdit('')
        self.terminal.setFontPointSize(16)

        self.box_with_items.activated.connect(self.get_full_report)

        layout = QVBoxLayout()
        layout.addWidget(self.box_with_items)
        layout.addWidget(self.switchers)
        layout.addWidget(self.begin_with)
        layout.addWidget(self.end_with)
        layout.addWidget(self.apply_button)
        layout.addWidget(self.find_failstacks)
        layout.addWidget(self.advices_valks)
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
        check_for_one_test = self.switchers.isChecked()
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
                                                                 find_fails=False)
        else:
            test_report = 'NOT READY'
        for i in test_report:
            self.terminal.append(i)

    def find_best_fails(self):
        current_name = self.box_with_items.currentText().replace(' ', '_')
        begin_level = int(self.begin_with.text())
        end_level = int(self.end_with.text())
        repeat_tests = 1000
        check_for_one_test = self.switchers.isChecked()
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
                                                                 find_fails=True)
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
