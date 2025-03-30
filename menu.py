from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                           QLabel, QGroupBox, QButtonGroup, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Menu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.initUI()
        
    def initUI(self):
        # Layout principal
        main_layout = QVBoxLayout(self)
        
        # Título do menu
        title_label = QLabel("Menu de Configurações")
        title_label.setFont(QFont('Arial', 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Botão para configurações de ecrã
        self.screen_config_btn = QPushButton("Configurações de Ecrã")
        self.screen_config_btn.setFixedSize(200, 40)
        self.screen_config_btn.clicked.connect(self.toggle_screen_settings)
        main_layout.addWidget(self.screen_config_btn, 0, Qt.AlignCenter)
        
        # Painel de configurações de ecrã (inicialmente oculto)
        self.screen_settings_panel = QWidget()
        self.screen_settings_panel.setVisible(False)
        screen_panel_layout = QVBoxLayout(self.screen_settings_panel)
        
        # Botões de configurações de ecrã
        self.fullscreen_btn = QPushButton("Tela Cheia")
        self.fullscreen_btn.setFixedSize(180, 35)
        self.fullscreen_btn.clicked.connect(lambda: self.apply_screen_mode("fullscreen"))
        screen_panel_layout.addWidget(self.fullscreen_btn, 0, Qt.AlignCenter)
        
        self.maximized_btn = QPushButton("Janela Cheia")
        self.maximized_btn.setFixedSize(180, 35)
        self.maximized_btn.clicked.connect(lambda: self.apply_screen_mode("maximized"))
        screen_panel_layout.addWidget(self.maximized_btn, 0, Qt.AlignCenter)
        
        self.windowed_btn = QPushButton("Janela Normal")
        self.windowed_btn.setFixedSize(180, 35)
        self.windowed_btn.clicked.connect(lambda: self.apply_screen_mode("windowed"))
        screen_panel_layout.addWidget(self.windowed_btn, 0, Qt.AlignCenter)
        
        main_layout.addWidget(self.screen_settings_panel)
        
        # Espaçador para empurrar o botão de voltar para baixo
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        # Botão para voltar à interface principal
        back_btn = QPushButton("Voltar")
        back_btn.setFixedSize(100, 35)
        back_btn.clicked.connect(self.go_back)
        main_layout.addWidget(back_btn, 0, Qt.AlignCenter)
    
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
        # Redefinir todos os estilos primeiro
        stylesheet_normal = ""
        stylesheet_selected = "background-color: #e32f81; color: white;"
        
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