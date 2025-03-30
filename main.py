import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import FullScreenWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FullScreenWindow()
    sys.exit(app.exec_())