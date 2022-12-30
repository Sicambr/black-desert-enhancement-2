import sys
import life_mastery_cloth
from push_info import load_data
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QComboBox, QWidget


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

        self.terminal = QTextEdit('')
        self.terminal.setFontPointSize(16)

        self.box_with_items.activated.connect(self.get_full_report)

        layout = QVBoxLayout()
        layout.addWidget(self.box_with_items)
        layout.addWidget(self.terminal)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print("Clicked!")

    def get_full_report(self):
        current_name = self.box_with_items.currentText().replace(' ', '_')
        print(current_name)
        test_report = life_mastery_cloth.Life_Mastery_Clothes(item_name=current_name,
                                                              begin_lev=0, end_lev=18, tests=1000, show_one_test=False)
        self.terminal.clear()
        for i in test_report:
            self.terminal.append(i)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
