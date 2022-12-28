import sys
import life_mastery_cloth
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit


my_list = [
    item + '\n' for item in life_mastery_cloth.Manos_Life_Mastery_Clothes(show_one_test=True)]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setMinimumSize(600, 400)

        button = QPushButton("Press Megit!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        My_text = QTextEdit('')
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
