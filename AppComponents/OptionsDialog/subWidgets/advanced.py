

from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu, QCheckBox, QPushButton,
    QStackedWidget
)
from PyQt6.QtCore import Qt, pyqtSignal

from helper_widgets import *

from AppComponents.OptionsDialog._base_widgets import *


class Advanced(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        title = QLabel("Advanced")
        title.setStyleSheet(F"font-size: 25px;")
        
        self.addWidget(title)
        self.addWidget(SeparatorLabel("Live Options"))
        self.addWidget(SeparatorLabel("Schedule File Options"))
        self.addStretch()
