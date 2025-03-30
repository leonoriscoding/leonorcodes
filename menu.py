from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                           QLabel, QGroupBox, QButtonGroup, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class Menu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.initUI()
        
    def initUI(self):
        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Título do menu
        title_label = QLabel("Menu de Configurações")
        title_label.setFont(QFont('Segoe UI', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Espaçador para dar espaço após o título
        main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
        # Botão para configurações de ecrã
        self.screen_config_btn = QPushButton("Configurações de Ecrã")
        self.screen_config_btn.setFont(QFont('Segoe UI', 14))
        self.screen_config_btn.setFixedSize(300, 60)
        self.screen_config_btn.setStyleSheet("""
            QPushButton {
                background-color: #e32f81;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #d42777;
            }
            QPushButton:pressed {
                background-color: #c5216d;
            }
        """)
        self.screen_config_btn.clicked.connect(self.toggle_screen_settings)
        main_layout.addWidget(self.screen_config_btn, 0, Qt.AlignCenter)
        
        # Painel de configurações de ecrã (inicialmente oculto)
        self.screen_settings_panel = QWidget()
        self.screen_settings_panel.setVisible(False)
        screen_panel_layout = QVBoxLayout(self.screen_settings_panel)
        screen_panel_layout.setSpacing(15)
        
        # Estilo base para os botões do painel
        button_style = """
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """
        
        # Botões de configurações de ecrã
        self.fullscreen_btn = QPushButton("Tela Cheia")
        self.fullscreen_btn.setFont(QFont('Segoe UI', 12))
        self.fullscreen_btn.setFixedSize(250, 50)
        self.fullscreen_btn.setStyleSheet(button_style)
        self.fullscreen_btn.clicked.connect(lambda: self.apply_screen_mode("fullscreen"))
        screen_panel_layout.addWidget(self.fullscreen_btn, 0, Qt.AlignCenter)
        
        self.maximized_btn = QPushButton("Janela Cheia")
        self.maximized_btn.setFont(QFont('Segoe UI', 12))
        self.maximized_btn.setFixedSize(250, 50)
        self.maximized_btn.setStyleSheet(button_style)
        self.maximized_btn.clicked.connect(lambda: self.apply_screen_mode("maximized"))
        screen_panel_layout.addWidget(self.maximized_btn, 0, Qt.AlignCenter)
        
        self.windowed_btn = QPushButton("Janela Pequena")
        self.windowed_btn.setFont(QFont('Segoe UI', 12))
        self.windowed_btn.setFixedSize(250, 50)
        self.windowed_btn.setStyleSheet(button_style)
        self.windowed_btn.clicked.connect(lambda: self.apply_screen_mode("windowed"))
        screen_panel_layout.addWidget(self.windowed_btn, 0, Qt.AlignCenter)
        
        main_layout.addWidget(self.screen_settings_panel)
        
        # Espaçador para empurrar o botão de voltar para baixo
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        # Botões de navegação inferiores
        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.setSpacing(20)
        
        # Botão para voltar à interface principal
        back_btn = QPushButton("Voltar")
        back_btn.setFont(QFont('Segoe UI', 12))
        back_btn.setFixedSize(150, 50)
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        back_btn.clicked.connect(self.go_back)
        bottom_buttons_layout.addWidget(back_btn, 0, Qt.AlignCenter)
        
        # Botão para sair da aplicação
        exit_btn = QPushButton("Sair")
        exit_btn.setFont(QFont('Segoe UI', 12))
        exit_btn.setFixedSize(150, 50)
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        exit_btn.clicked.connect(self.exit_application)
        bottom_buttons_layout.addWidget(exit_btn, 0, Qt.AlignCenter)
        
        main_layout.addLayout(bottom_buttons_layout)
    
    def toggle_screen_settings(self):
        # Alternar visibilidade do painel de configurações de ecrã
        is_visible = self.screen_settings_panel.isVisible()
        self.screen_settings_panel.setVisible(not is_visible)
        
        # Mudar o texto do botão
        if not is_visible:
            self.screen_config_btn.setText("Esconder Configurações")
        else:
            self.screen_config_btn.setText("Configurações de Ecrã")
    
    def apply_screen_mode(self, mode):
        # Aplicar o modo de ecrã diretamente
        self.parent_window.set_window_mode(mode)
        
        # Atualizar a aparência dos botões para destacar o selecionado
        self.update_button_styles(mode)
    
    def update_button_styles(self, selected_mode):
        # Estilo para botões normais
        stylesheet_normal = """
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """
        
        # Estilo para o botão selecionado
        stylesheet_selected = """
            QPushButton {
                background-color: #e32f81;
                color: white;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d42777;
            }
            QPushButton:pressed {
                background-color: #c5216d;
            }
        """
        
        self.fullscreen_btn.setStyleSheet(stylesheet_normal)
        self.maximized_btn.setStyleSheet(stylesheet_normal)
        self.windowed_btn.setStyleSheet(stylesheet_normal)
        
        # Destacar o botão selecionado
        if selected_mode == "fullscreen":
            self.fullscreen_btn.setStyleSheet(stylesheet_selected)
        elif selected_mode == "maximized":
            self.maximized_btn.setStyleSheet(stylesheet_selected)
        elif selected_mode == "windowed":
            self.windowed_btn.setStyleSheet(stylesheet_selected)
    
    def showEvent(self, event):
        # Ao mostrar o menu, atualizar os estilos dos botões conforme o estado atual
        if self.parent_window.isFullScreen():
            self.update_button_styles("fullscreen")
        elif self.parent_window.isMaximized():
            self.update_button_styles("maximized")
        else:
            self.update_button_styles("windowed")
        
        super().showEvent(event)
    
    def go_back(self):
        # Voltar para a interface principal
        self.parent_window.restore_main_interface()
    
    def exit_application(self):
        # Sair da aplicação
        self.parent_window.close()
