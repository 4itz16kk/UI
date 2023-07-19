from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog


from input import Ui_MainWindow

import time


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.counter = 0

    def setup_control(self):
        # TODO
        self.ui.button_line.clicked.connect(self.buttonClicked_line)
        self.ui.button_text.clicked.connect(self.buttonClicked_text)
        self.ui.button_plain.clicked.connect(self.buttonClicked_plain)
        self.ui.horizontalSlider.valueChanged.connect(self.getslidervalue)
        self.ui.button_go.clicked.connect(self.start_progress)
        self.ui.button_file.clicked.connect(self.open_file)
        self.ui.button_folder.clicked.connect(self.open_folder)
        self.ui.button_counter.clicked.connect(self.increment_counter)
        self.ui.radioButton_1.toggled.connect(self.onRadioButtonToggled)
        self.ui.radioButton_2.toggled.connect(self.onRadioButtonToggled)
        self.ui.radioButton_3.toggled.connect(self.onRadioButtonToggled)

    def buttonClicked_line(self):
        msg = self.ui.box_line.text()
        self.ui.label_line.setText(msg)

    def buttonClicked_text(self):
        msg = self.ui.box_text.toPlainText()
        self.ui.label_text.setText(msg)

    def buttonClicked_plain(self):
        msg = self.ui.box_plain.toPlainText()
        self.ui.label_plain.setText(msg)

    def getslidervalue(self):
        self.ui.value.setText(f"{self.ui.horizontalSlider.value()}")
        # print(self.ui.horizontalSlider.value())

    def start_progress(self):
        max_value = 100
        self.ui.progressBar.setMaximum(max_value)

        for i in range(max_value):
            time.sleep(0.1)
            self.ui.progressBar.setValue(i+1)

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(
            self, "Open file", "./")                 # start path
        print(filename, filetype)
        self.ui.file_path.setText(filename)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "Open folder", "./")
        print(folder_path)
        self.ui.folder_path.setText(folder_path)

    def increment_counter(self):
        self.counter += 1
        self.ui.counter_value.setText(str(self.counter))

    def onRadioButtonToggled(self):
        selected_option = None

        if self.ui.radioButton_1.isChecked():
            selected_option = "A"
        elif self.ui.radioButton_2.isChecked():
            selected_option = "B"
        elif self.ui.radioButton_3.isChecked():
            selected_option = "C"

        self.ui.label_radiobutt.setText(f"{selected_option}")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
