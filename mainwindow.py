import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
                            QWidget, QPushButton, QHBoxLayout, QLineEdit, QListWidget,
                            QToolBar, QAction, QSizePolicy, QStackedWidget)
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QFont

class FullScreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_count = 0
        self.menu_interface = None
        self.initUI()
       
    def initUI(self):
        self.setWindowTitle('Aplicação em Tela Cheia Funcional')
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QToolBar {
                background-color: #333;
                border: none;
                padding: 5px;
            }
            QLabel {
                color: #333;
            }
            QListWidget {
                border-radius: 8px;
                padding: 5px;
                font-size: 14px;
                border: 1px solid #ddd;
                background-color: white;
            }
        """)
        
        self.toolbar = QToolBar("Barra de Ferramentas")
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)
        self.toolbar.setFixedHeight(70)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        
        toolbar_widget = QWidget()
        toolbar_layout = QHBoxLayout(toolbar_widget)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(0)
        
        left_section = QWidget()
        left_layout = QHBoxLayout(left_section)
        left_layout.setContentsMargins(10, 0, 10, 0)
        left_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        center_section = QWidget()
        center_layout = QHBoxLayout(center_section)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setAlignment(Qt.AlignCenter)
        center_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        self.menu_btn = QPushButton("Menu")
        self.menu_btn.setFont(QFont('Segoe UI', 30, QFont.Bold))
        self.menu_btn.setFixedSize(140, 60)
        self.menu_btn.setStyleSheet("""
            QPushButton {
                background-color: #e32f81;
                color: white;
                border-radius: 8px;
                padding: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d42777;
            }
            QPushButton:pressed {
                background-color: #c5216d;
            }
        """)
        self.menu_btn.clicked.connect(self.show_menu)
        center_layout.addWidget(self.menu_btn, 0, Qt.AlignCenter)
        
        right_section = QWidget()
        right_layout = QHBoxLayout(right_section)
        right_layout.setContentsMargins(10, 0, 20, 0)
        right_layout.setAlignment(Qt.AlignRight)
        right_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont('Segoe UI', 16, QFont.Bold))
        self.time_label.setStyleSheet("color: white;")
        self.time_label.setMinimumWidth(120)
        right_layout.addWidget(self.time_label, 0, Qt.AlignRight)
        
        toolbar_layout.addWidget(left_section)
        toolbar_layout.addWidget(center_section)
        toolbar_layout.addWidget(right_section)
        
        self.toolbar.addWidget(toolbar_widget)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
       
        tasks_layout = QHBoxLayout()
       
        self.task_list = QListWidget()
        self.task_list.setFont(QFont('Segoe UI', 14))
        self.task_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                background-color: white;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #eee;
            }
            QListWidget::item:selected {
                background-color: #4a86e8;
                color: white;
                border-radius: 5px;
            }
        """)
        tasks_layout.addWidget(self.task_list)
        
        self.main_layout.addLayout(tasks_layout)
        
        self.stacked_widget.addWidget(self.main_widget)
        
        self.showFullScreen()
       
    def show_menu(self):
        from menu import Menu
        
        if not self.menu_interface:
            self.menu_interface = Menu(self)
            self.stacked_widget.addWidget(self.menu_interface)
        
        self.stacked_widget.setCurrentWidget(self.menu_interface)
    
    def restore_main_interface(self):
        self.stacked_widget.setCurrentWidget(self.main_widget)
       
    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%d/%m/%Y")
        self.time_label.setText(f"{current_time}\n{current_date}")
        
    def set_window_mode(self, mode):
        if mode == "fullscreen":
            self.showFullScreen()
        elif mode == "maximized":
            self.showMaximized()
        elif mode == "windowed":
            self.showNormal()
            self.resize(800, 600)  # Tamanho padrão para o modo janela
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            if self.isFullScreen():
                self.showNormal()
        super().keyPressEvent(event)
