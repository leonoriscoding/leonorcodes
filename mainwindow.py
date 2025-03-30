import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
                            QWidget, QPushButton, QHBoxLayout, QLineEdit, QListWidget,
                            QToolBar, QAction, QSizePolicy, QStackedWidget)
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QFont, QIcon

class FullScreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_count = 0
        self.menu_interface = None
        self.initUI()
       
    def initUI(self):
        # Configurar a janela principal
        self.setWindowTitle('Aplicação em Tela Cheia Funcional')
        
        # Estilo geral da aplicação
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QToolBar {
                background-color: #333;
                border: none;
                spacing: 10px;
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
        
        # Criar uma barra de ferramentas no topo
        toolbar = QToolBar("Barra de Ferramentas")
        toolbar.setIconSize(QSize(24, 24))
        toolbar.setMovable(False)
        toolbar.setFixedHeight(50)  # Define a altura fixa da barra
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        
        # Primeiro espaçador para centralizar o botão de menu
        spacer1 = QWidget()
        spacer1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer1)
        
        # Adicionar botão de menu à barra de ferramentas (centralizado)
        self.menu_btn = QPushButton("Menu")
        self.menu_btn.setFont(QFont('Segoe UI', 12, QFont.Bold))
        self.menu_btn.setFixedSize(120, 40)
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
        toolbar.addWidget(self.menu_btn)
        
        # Segundo espaçador para centralizar o botão de menu
        spacer2 = QWidget()
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer2)
        
        # Criar um widget empilhado para alternar entre telas
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Criar o widget principal
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        
        # Adicionar um relógio digital
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignRight)
        self.time_label.setFont(QFont('Segoe UI', 32, QFont.Bold))
        self.time_label.setStyleSheet("color: #2c3e50;")
        self.main_layout.addWidget(self.time_label)
       
        # Configurar e iniciar o timer para atualizar o relógio
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Atualizar a cada segundo
        self.update_time()  # Atualizar imediatamente
       
        # Criar um gerenciador de tarefas simples
        tasks_layout = QHBoxLayout()
       
        # Lista de tarefas
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
        
        # Adicionar o widget principal ao widget empilhado
        self.stacked_widget.addWidget(self.main_widget)
        
        # Inicialmente, não temos um widget de menu, ele será criado sob demanda
        
        # Definir a janela para tela cheia
        self.showFullScreen()
    
    def show_menu(self):
        # Importação local para evitar referência circular
        from menu import Menu
        
        # Criar a interface de menu se ainda não existir
        if not self.menu_interface:
            self.menu_interface = Menu(self)
            self.stacked_widget.addWidget(self.menu_interface)
        
        # Mostrar a interface de menu
        self.stacked_widget.setCurrentWidget(self.menu_interface)
    
    def restore_main_interface(self):
        # Voltar para a interface principal
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
        # Permitir que o usuário saia do modo tela cheia pressionando ESC
        if event.key() == Qt.Key_Escape:
            if self.isFullScreen():
                self.showNormal()
       
        # Permitir ALT+F4 ou outros métodos padrão para fechar a aplicação
        super().keyPressEvent(event)
