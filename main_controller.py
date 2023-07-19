from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog


from main import Ui_MainWindow

import time

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.counter = 0

    def setup_control(self):
        # self.ui.radioButton.toggled.connect(self.onRadioButtonToggled)
        # self.ui.radioButton_2.toggled.connect(self.onRadioButtonToggled)
        # self.ui.radioButton_3.toggled.connect(self.onRadioButtonToggled)
        # self.ui.radioButton_4.toggled.connect(self.onRadioButtonToggled)
        # self.ui.radioButton_5.toggled.connect(self.onRadioButtonToggled)
        self.ui.pushButton.clicked.connect(self.onRadioButtonToggled)

    def onRadioButtonToggled(self):
        selected_option = None

        if self.ui.radioButton.isChecked():
            selected_option = "目前在模式1"
        elif self.ui.radioButton_2.isChecked():
            selected_option = "目前在模式2"
        elif self.ui.radioButton_3.isChecked():
            selected_option = "目前在模式3"
        elif self.ui.radioButton_4.isChecked():
            selected_option = "目前在模式4"
        elif self.ui.radioButton_5.isChecked():
            selected_option = "目前在模式5"

        self.ui.label.setText(f"{selected_option}")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
