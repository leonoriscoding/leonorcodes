import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import FullScreenWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Aplicar uma fonte global para toda a aplicação
    from PyQt5.QtGui import QFont
    app.setFont(QFont('Segoe UI', 11))
    
    window = FullScreenWindow()
    sys.exit(app.exec_())
