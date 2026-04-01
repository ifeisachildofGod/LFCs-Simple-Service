

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
        
        # --------------------------------------------------------------------
        
        lo_widgets = BaseWidget()
        
        lo_widgets.addWidget(slsos_cbx := QCheckBox("Show live screen on startup"))
        lo_widgets.addWidget(asaglip_cbx := QCheckBox("Advanced Schedule after Go Live is pressed"))
        
        # --------------------------------------------------------------------
        
        sfo_widgets = BaseWidget()
        
        sfo_widgets.addWidget(asaglis_cbx := QCheckBox("Pack files in new schedule by default (recommended)"))
        
        # --------------------------------------------------------------------
        
        self.addWidget(title)
        self.addWidget(SeparatorLabel("Live Options"))
        self.addWidget(lo_widgets)
        self.addWidget(SeparatorLabel("Schedule File Options"))
        self.addWidget(sfo_widgets)
        self.addStretch()
