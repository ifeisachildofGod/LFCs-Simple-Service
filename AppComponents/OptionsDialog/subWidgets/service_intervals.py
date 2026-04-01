

from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu, QCheckBox, QPushButton,
    QStackedWidget
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from UIComponents.TabView import TabView_2
from UIComponents.SideBar import SideBar

from helper_widgets import *

from AppComponents.OptionsDialog._base_widgets import *


class ServiceIntervals(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        title = QLabel("Service Intervals")
        title.setStyleSheet(F"font-size: 25px;")
        
        self.addWidget(title)
        self.addWidget(SeparatorLabel("Service Start and Stop Times"))
        self.addStretch()
