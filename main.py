import sys
import life_mastery_cloth
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit


my_list = life_mastery_cloth.Manos_Life_Mastery_Clothes(
    begin_lev=0, end_lev=19, tests=1000, show_one_test=False)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sharpering test for Black Desert")
        self.setMinimumSize(800, 600)

        button = QPushButton("Press Megit!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        My_text = QTextEdit('')
        My_text.setFontPointSize(16)
        for i in my_list:
            My_text.append(i)

        # My_text.setText(my_list)

        self.setCentralWidget(My_text)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
