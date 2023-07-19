import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.label.setGeometry(100, 100, 2000, 300)
        self.label.setStyleSheet('font-size:300px;')

        self.time_label = QLabel(self)  # 新增时间标签
        self.time_label.setGeometry(100, 900, 2000, 300)  # 设置时间标签的位置和大小
        self.time_label.setStyleSheet('font-size:300px;')

        self.start_button = QPushButton('开始', self)
        self.start_button.setGeometry(100, 500, 800, 300)
        self.start_button.setStyleSheet('font-size:300px;')
        self.start_button.clicked.connect(self.start_counter)


        self.stop_button = QPushButton('停止', self)
        self.stop_button.setGeometry(1000, 500, 800, 300)
        self.stop_button.setStyleSheet('font-size:300px;')
        self.stop_button.clicked.connect(self.stop_counter)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_counter)

        self.time_timer = QTimer()  # 用于更新时间标签的计时器
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)  # 每秒更新一次时间标签

        self.counter = 0
        self.is_counter_running = False

    def start_counter(self):
        if not self.is_counter_running:
            self.timer.start(1000)  # 更新时间间隔（以毫秒为单位）
            self.is_counter_running = True

    def stop_counter(self):
        if self.is_counter_running:
            self.timer.stop()
            self.is_counter_running = False

    def update_counter(self):
        self.counter += 1
        display_text = str(self.counter)
        self.label.setText(display_text)

    def update_time(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss')
        self.label.setStyleSheet('font-size:300px;')
        self.time_label.setText(display_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    