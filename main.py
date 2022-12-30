import sys
import life_mastery_cloth
from push_info import load_data
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QComboBox, QWidget, QLineEdit
from PyQt5.QtGui import QFont


all_items = load_data()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sharpering test for Black Desert")
        self.setMinimumSize(800, 600)

        button = QPushButton("Press Megit!")
        button.clicked.connect(self.the_button_was_clicked)

        self.box_with_items = QComboBox()
        for i in all_items.keys():
            self.box_with_items.addItem(i.replace('_', ' '))
        
        self.begin_with = QLineEdit('0')
        self.end_with = QLineEdit('17')

        self.apply_button = QPushButton('Apply')

        font = QFont("JetBrains Mono", 16)
        self.box_with_items.setFont(font)
        self.begin_with.setFont(font)
        self.end_with.setFont(font)
        self.apply_button.setFont(font)
        self.apply_button.clicked.connect(self.get_full_report)

        self.terminal = QTextEdit('')
        self.terminal.setFontPointSize(16)

        self.box_with_items.activated.connect(self.get_full_report)

        layout = QVBoxLayout()
        layout.addWidget(self.box_with_items)
        layout.addWidget(self.begin_with)
        layout.addWidget(self.end_with)
        layout.addWidget(self.apply_button)
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
        test_report = life_mastery_cloth.Life_Mastery_Clothes(item_name=current_name,
                                                              begin_lev=begin_level, end_lev=end_level, tests=1000, show_one_test=False)
        self.terminal.clear()
        for i in test_report:
            self.terminal.append(i)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
