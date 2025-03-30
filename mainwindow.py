import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
                            QWidget, QPushButton, QHBoxLayout, QLineEdit, QListWidget,
                            QToolBar, QAction, QSizePolicy, QStackedWidget)
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QFont, QIcon
from task import tarefa

class FullScreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_count = 0
        self.menu_interface = None
        self.initUI()
       
    def initUI(self):
        # Configurar a janela principal
        self.setWindowTitle('Aplicação em Tela Cheia Funcional')
        
        # Criar uma barra de ferramentas no topo
        toolbar = QToolBar("Barra de Ferramentas")
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        
        # Adicionar botão de menu à barra de ferramentas
        self.menu_btn = QPushButton("Menu")
        self.menu_btn.setFixedSize(80, 30)
        self.menu_btn.clicked.connect(self.show_menu)
        toolbar.addWidget(self.menu_btn)
        
        # Adicionar espaçador para alinhar botões à direita
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)
        
        # Botões no canto direito da barra de ferramentas
        self.toggle_btn = QPushButton("Sair da Tela Cheia")
        self.toggle_btn.setFixedSize(120, 30)
        self.toggle_btn.clicked.connect(self.toggle_fullscreen)
        toolbar.addWidget(self.toggle_btn)
        
        exit_btn = QPushButton("Sair")
        exit_btn.setFixedSize(60, 30)
        exit_btn.clicked.connect(self.close)
        toolbar.addWidget(exit_btn)
        
        # Criar um widget empilhado para alternar entre telas
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Criar o widget principal
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        
        # Adicionar um relógio digital
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignRight)
        self.time_label.setFont(QFont('Arial', 28, QFont.Bold))
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
            self.toggle_btn.setText("Sair da Tela Cheia")
        elif mode == "maximized":
            self.showMaximized()
            self.toggle_btn.setText("Entrar em Tela Cheia")
        elif mode == "windowed":
            self.showNormal()
            self.resize(800, 600)  # Tamanho padrão para o modo janela
            self.toggle_btn.setText("Entrar em Tela Cheia")
   
    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.toggle_btn.setText("Entrar em Tela Cheia")
        else:
            self.showFullScreen()
            self.toggle_btn.setText("Sair da Tela Cheia")
       
    def keyPressEvent(self, event):
        # Permitir que o usuário saia do modo tela cheia pressionando ESC
        if event.key() == Qt.Key_Escape:
            if self.isFullScreen():
                self.showNormal()
                self.toggle_btn.setText("Entrar em Tela Cheia")
       
        # Permitir ALT+F4 ou outros métodos padrão para fechar a aplicação
        super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FullScreenWindow()
    sys.exit(app.exec_())